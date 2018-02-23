import time


        
def fbis(num):
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result


def fb():
    result = fbis(10)
    fobj = open('D:\\pyl\\res.txt', 'w+')
    for i, num in enumerate(result):
        print("第 {0} 是 ：{1}" .format(i, num))
        fobj.write("{0}    " .format(num))
        time.sleep(1)


# 交换运算符
# reslist[i], reslist[j] = reslist[j], reslist[i]
# range（）函数不包含上界
def sort():
    reslist = [4, 6, 32, 2, 1, 6, 7, 8, 34, 5, 1]
    length = len(reslist)
    for i in range(0, length):
        for j in range(i + 1, length):
            if reslist[i] > reslist[j]:
                reslist[i], reslist[j] = reslist[j], reslist[i]
    print(length)
    print("finished")
    print(reslist)


# 返回参数，可返回多个
# 可带默认值
# 函数名当作参数
# lambda 匿名函数

def sum(x, y):
    return x + y


def total(x, y, z):
    return sum(x, y) + z, sum(x, y)


# 变长参数 *
def show_message(message, *name):
    for name in name:
        print(message, ",", name)