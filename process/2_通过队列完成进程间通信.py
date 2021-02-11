import multiprocessing


def enter_queue(q):
    data = [1, 2, 3, 4]
    # 往队列中写入数据
    for temp in data:
        q.put(temp)

    print("---数据放入队列完毕---")


def export_queue(q):
    transform_data = []
    # 从队列中获取数据处理
    while not q.empty():
        data = q.get()
        data += 1
        transform_data.append(data)

    print("转换后的数据：", transform_data)

def main():
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=enter_queue, args=(q,))
    p2 = multiprocessing.Process(target=export_queue, args=(q,))

    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
