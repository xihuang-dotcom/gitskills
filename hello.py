# 定义一个计算斐波那契数列的函数
def fibonacci(n):
    # 处理输入合法性
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    # 初始化前两项
    result = [0, 1]
    # 循环生成后续项
    for i in range(2, n):
        result.append(result[-1] + result[-2])
    return result

# 测试函数
if __name__ == "__main__":
    print(fibonacci(10))
