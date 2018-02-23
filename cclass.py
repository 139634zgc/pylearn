class Myclass(object):
    message = "hello, developer"

    def show(self):
        print(self.message)
    # 构造函数，可以多种

    def __init__(self, name="unset", color="green"):
        self.name = name
        self.color = color
        print("constructor is", name, ",,", color)

    # del 析构函数被自动调用 销毁对象
    def __del__(self):
        print("{0} has been deleted".format(self.name))