class CSV:#定义一个类
    def __init__(self,path,is_postfix=True,is_head=True):#设定属性
        self.is_postfix=is_postfix#设置后缀名变量
        self.is_head=is_head#设置头部变量
        self.path=path#设置路径

    def is_csv(self):#正在判断是否为CSV文件的函数
        if self.is_postfix:#判断属性
            print("正在判断是否为CSV文件 ===")
            import os.path#引入模块
            name=os.path.splitext(self.path)[1]#获取文件后缀名
            if name==".csv":#判断文件后缀名是否为csv
                return True#返回正确
            else:
                return False#返回错误
        else:
            return True#如给的属性是正确就返回正确


    def get_head(self):#判断头部的函数
        if self.is_head:#判断属性
            print("正在判断是否包含默认的头 部 ===")
            default_head = ["Namtee","Age","No"]#给出标准头部的定义
            csvfile=open(self.path,'r').read()#打开并阅读文件
            content = csvfile.split()#使字符串列表化
            head  = content[0]#获取头部
            print(head)#打印出头部
            if len(head and default_head) > 0:#判断是否为csv文件的头部
                return (True,content)#是就返回正确，并返回列表化的文件内容
            else:
                return (False)
        else:
            return False#否则返回错

    def read(self):#判断并打印文件的函数
        if self.is_csv():#判断是否为csv文件
            print("正在处理CSV文件 ===")
            content = self.get_head()#调用函数，函数会返回元组，里面有判断结果和列表化的文件内容
            if content[0]:#调用文件的判断结果
                for c in content[1]:#如果是true，就循环出列表中的文件内容
                    print(c)
            else:
                print("只能处理带头部文件")
        else:
            print("只能处理.csv后缀文件")

csv=CSV("C:/Users/ASUS/python_csv_class/demo.csv")#实例化类
csv.read()#调用函数
