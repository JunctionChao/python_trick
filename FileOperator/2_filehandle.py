# 流式读取大文件

"""
读取文件有一种“标准做法”：首先使用 withopen(fine_name) 上下文管理器的方式获得一个文件对象，
然后使用 for 循环迭代它，逐行获取文件里的内容
"""
# 读取文件中字符9的个数
def count_nine(fname):
    count = 0
    with open(fname) as fp:
        for line in fp: # 迭代文件对象时，内容一行一行返回
            count += line.count('9')
    return count

"""
上述方法的缺点是：如果被读取的文件里，根本就没有任何换行符，所有字符都在一行，内容巨大。
当代码执行到 for line in file 时，line 将会变成一个非常巨大的字符串对象，消耗掉非常可观的内存
"""
# 使用read方法分块读取
# 调用 file.read(chunk_size) 会直接返回从当前位置往后读取 chunk_size 大小的文件内容，不必等待任何换行符出现
def count_nine_v2(fname):
    count = 0
    block_size = 1024 * 8 # 8kb
    with open(fname) as fp:
        while True:
            chunk = fp.read(block_size)
            if not chunk:
                break
            count += chunk.count('9')
    return count

"""利用生成器解耦代码

认真分析一下 count_nine_v2 函数，会发现在循环体内部存在着两个独立的逻辑：
数据生成（read 调用与 chunk 判断） 与 数据消费。而这两个独立逻辑被耦合在了一起。
为了提升复用能力，我们可以定义一个新的 chunked_file_reader 生成器函数，由它来负责所有与“数据生成”相关的逻辑。
这样 count_nine_v3 里面的主循环就只需要负责计数即可
"""
def chunked_file_reader(fp, block_size=1024*8):
    while True:
        chunk = fp.read(block_size)
        if not chunk:
            break
        yield chunk

def count_nine_v3(fname):
    count = 0
    with open(fname) as fp:
        for chunk in chunked_file_reader(fp):
            count += chunk.count('9')
    return count

"""还可以进一步优化

进行到这一步，代码似乎已经没有优化的空间了，但其实不然。iter(iterable) 是一个用来构造迭代器的内建函数，但它还有一个更少人知道的用法。当我们使用 iter(callable,sentinel) 的方式调用它时，会返回一个特殊的对象，迭代它将不断产生可调用对象 callable 的调用结果，直到结果为 setinel 时，迭代终止
"""
def chunked_file_reader_v2(fp, block_size=1024*8):
    # 首先使用 partial(fp.read, block_size) 构造一个新的无需参数的函数
    # 循环将不断返回 fp.read(block_size) 调用结果，直到其为 '' 时终止
    for chunk in iter(partial(fp.read, block_size), ''):
        yield chunk


"""设计接受文件对象的函数

让我们换一个需求。现在，我想要统计每个文件里出现了多少个英文元音字母（aeiou）。只要对之前的代码稍作调整，很快就可以写出新函数 count_vowels
"""
def count_vowels(filename):
    vowels_letters = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    with open(filename, 'r') as fp:
        for line in fp:
            for char in line:
                if char.lower() in vowels_letters:
                    count += 1
    return count

print(count_vowels('filename.txt'))

"""
为了保证程序的正确性，我需要为它写一些单元测试。但当我准备写测试时，却发现这件事情非常麻烦，主要问题点如下：
函数接收文件路径作为参数，所以我们需要传递一个实际存在的文件
为了准备测试用例，我要么提供几个样板文件，要么写一些临时文件
而文件是否能被正常打开、读取，也成了我们需要测试的边界情况

如果，你发现你的函数难以编写单元测试，那通常意味着你应该改进它的设计。上面的函数应该如何改进呢？
答案是：让函数依赖“文件对象”而不是文件路径。
"""
# 修改后为
def count_vowels_v2(fp):
    vowels_letters = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for line in fp:
        for char in line:
            if char.lower() in vowels_letters:
                count += 1
    return count

# 修改函数后，打开文件的职责移交给了上层函数调用者
with open('filename.txt') as fp:
    print(count_vowels_v2(fp))

"""
这个改动带来的主要变化，在于它提升了函数的适用面。因为 Python 是“鸭子类型”的，虽然函数需要接受文件对象，但其实我们可以把任何实现了文件协议的 “类文件对象（file-like object）” 传入 count_vowels_v2 函数中。

而 Python 中有着非常多“类文件对象”。比如 io 模块内的 StringIO 对象就是其中之一。它是一种基于内存的特殊对象，拥有和文件对象几乎一致的接口设计。

利用 StringIO，我们可以非常方便的为函数编写单元测试
"""
import pytest
from io import StringIO

@pytest.mark.parametrize(
    "content,vowels_count", [
        # 使用pytest提供的参数化测试工具，定义测试参数列表
        # (文件内容, 期待结果)
        ('', 0),
        ('Hello word!', 3),
        ('some things', 3),
        ('你好, 陌生人', 0),
    ]
)

def test_count_vowels_v2(content, vowels_count):
    # 利用 StringIO 构造类文件对象
    file = StringIO(content)
    assert count_vowels_v2(file) == vowels_count

"""
而让编写单元测试变得更简单，并非修改函数依赖后的唯一好处。
除了 StringIO 外，subprocess 模块调用系统命令时用来存储标准输出的 PIPE 对象，也是一种“类文件对象”。
这意味着我们可以直接把某个命令的输出传递给 count_vowels_v2 函数来计算元音字母数
"""
import subprocess
# 统计 /tmp 下面所有一级子文件名有多少元音字母
p = subprocess.Popen(['ls', '/tmp'], stdout=subprocess.PIPE, encoding='utf-8')
# p.stdout 是一个流式类文件对戏，可以直接传入函数
print(count_vowels_v2(p.stdout))

"""
将函数参数修改为“文件对象”，最大的好处是提高了函数的 适用面 和 可组合性。
通过依赖更为抽象的“类文件对象”而非文件路径，给函数的使用方式开启了更多可能，StringIO、PIPE 以及任何其他满足协议的对象都可以成为函数的客户。

不过，这样的改造并非毫无缺点，它也会给调用方带来一些不便。
假如调用方就是想要使用文件路径，那么就必须得自行处理文件的打开操作
"""

"""如何编写兼容二者的函数

有没有办法即拥有“接受文件对象”的灵活性，又能让传递文件路径的调用方更方便？答案是：有，而且标准库中就有这样的例子。
打开标准库里的 xml.etree.ElementTree 模块，翻开里面的 ElementTree.parse 方法。你会发现这个方法即可以使用文件对象调用，也接受字符串的文件路径。而它实现这一点的手法也非常简单易懂
使用这种基于“鸭子类型”的灵活检测方式
"""
def parse(self, source, parser=None):
    """ source 是一个文件名或类文件对象，parser是一个可选的解析参数
    """
    close_source = False
    # 通过判断source是否有 read 属性来判断它是否是 类文件对象
    # 如果不是类文件对象，则用open函数打开并在函数末尾关闭它
    if not hasattr(source, "read"):
        source = open(source, "rb")
        close_source = True

# 改进后的count_vowels_v3
def count_vowels_v3(source):
    vowels_letters = {'a', 'e', 'i', 'o', 'u'}
    close_source = False
    if not hasattr(source, "read"):
        fp = open(source, "r")
        close_source = True

    count = 0
    for line in fp:
        for char in line:
            if char.lower() in vowels_letters:
                count += 1

    if close_source:
        fp.close()
    
    return count