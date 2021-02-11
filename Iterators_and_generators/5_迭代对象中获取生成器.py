# 用生成器代替迭代器
class Fibonacci():
    def __init__(self, all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        while self.current_num <= self.all_num:
            yield self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1

if __name__ == "__main__":
    fibo = Fibonacci(10)
    for num in fibo:
        print(num)