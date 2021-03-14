# 使用pathlib更方便处理文件
import pathlib, os

# 将文件夹中.txt文件修改为.csv

# 使用os方式
def unify_ext_with_os_path(dirpath):
    for filename in os.listdir(dirpath):
        basename, ext = os.path.splitext(filename)
        if ext == ".txt":
            abs_filepath = os.path.join(path, filename)
            os.rename(abs_filepath, os.path.join(dirpath, f"{basename}.csv"))

# 使用pathlib模块
from pathlib import Path

"""
使用 Path(path) 将字符串路径转换为 Path 对象
调用 .glob('*.txt') 对路径下所有内容进行模式匹配并以生成器方式返回，结果仍然是 Path 对象
使用 .with_suffix('.csv') 直接获取使用新后缀名的文件全路径
"""
def unify_ext_with_pathlib(dirpath):
    for fpath in Path(dirpath).glob("*.txt"):
        fpath.rename(fpath.with_suffix(".csv"))