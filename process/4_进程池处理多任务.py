# 用进程池来处理多文件copy任务

import os, multiprocessing


def copy_file(queue, file_name, old_folder, new_folder):
    # with open(os.path.join(old_folder, file_name), "rb") as fp:
    #     content = fp.read()
    
    # with open(os.path.join(new_folder, file_name), "wb") as fp:
    #     fp.write(content)

    # 复制大文件内存不够时用下面的方式
    f_read = open(os.path.join(old_folder, file_name), "rb")
    f_write = open(os.path.join(new_folder, file_name), "wb")
    while True:
        content = f_read.read(1024)
        if content:
            f_write.write(content)
        else:
            break
    f_read.close()
    f_write.close()

    # copy完后发送已经copy的文件名
    queue.put(file_name)

def main(old_folder, new_folder):
    if not new_folder:
        new_folder = old_folder + "[复件]"
    try:
        os.mkdir(new_folder)
    except:
        pass

    file_names = os.listdir(old_folder)
    
    # 进程池
    po = multiprocessing.Pool(5)

    # 创建队列，用于进程池之间通讯
    queue = multiprocessing.Manager().Queue()

    for file_name in file_names:
        po.apply_async(copy_file, (queue, file_name, old_folder, new_folder))

    po.close()
    # po.join()

    all_count = len(file_names)
    copy_ok_num = 0
    # 显示进度条
    while True:
        file_name = queue.get()
        copy_ok_num += 1
        copy_rate = copy_ok_num * 100 / all_count
        print("\r%.2f...(%s)" % (copy_rate, file_name) + " " * 50, end="") # \r 回到行首
        if copy_rate>= 100:
            break
    print()


if __name__ == "__main__":
    old_folder = "test"
    new_folder = ""
    main(old_folder, new_folder)