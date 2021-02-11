def fibonacci(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num <= all_num:
        yield a
        a, b = b, a + b
        current_num += 1
    return "finished"

if __name__ == "__main__":
    genfi = fibonacci(10)
    # for num in genfi:
    #     print(num)

    while True:
        try:
            ret = next(genfi)
            print(ret)
        except Exception as e:
            print(e.value) # 通过异常来捕获生成器的返回值
            break