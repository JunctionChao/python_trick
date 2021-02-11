# 生成器的调用方可以使用 .send(...) 方法发送数据，
# 发送的数据会成为生成器函数中 yield 表达式的值。因此，生成器可以作为协程使用

from collections import namedtuple
Result = namedtuple('Result', 'count average')

def averager():
    total = 0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)


if __name__ == "__main__":
    coro_avg = averager()
    next(coro_avg)

    coro_avg.send(10)
    coro_avg.send(30)
    try:
        coro_avg.send(None)
    except StopIteration as exc:
        result = exc.value
    print(result)