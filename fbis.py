import time

def fbis(num):
    result=[0,1]
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

