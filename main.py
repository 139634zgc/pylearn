from fbis import fb


def seq():
    a = [1,2,3,4,5,6,3,7,8,9,990,12,3,232,42]
    b = len(a)
    c = max(a)
    d = sorted(a)
    e = reversed(a)
    print(a)
    print(b)
    print(c)
    print(d)
    print(list(e))


def str():
    a = "qwertyuioplkjhgfdsazxcvbnm"
    a1 = a.center(10)
    a2 = a.capitalize()
    a3 = a.isdigit()
    a4 = a.upper()
    b = "hello world hah ah hha hha hha hah ha a a"
    c = b.split()
    print(c)
# 元组
def tup():
    tuple1 = (1,4,3,5,2)
    tuple1 = tuple1 + tuple1
    print(tuple1)
    a =tuple1.count(5)
    print(a)
    print(4 in tuple1)

def set1():
    mylist = ['1','a']
    sam = set(mylist)
    print(sam)
def dic():
    dict1 = {'language':'english', 'title':'py book', 'pages':'900'}
    print(dict1)
    dict1['pages'] = '800'
    print(dict1)
    print(dict1.keys())

def whi():
    mylist = ["evf","qqq","rrr","yyyy"]
    while len(mylist)>0:
        print("pop:" , mylist.pop())

if __name__ == '__main__':

    # str()
    # tup()
    fb()
    # dic()
    whi()
