 # 有两个人(Human):
#     1.
#       姓名: 张三
#       年龄: 35
#     2.
#       姓名: 李四
#       年龄: 8
#     行为:
#       1. 教别人学东西 teach
#       2. 赚钱 works
#       3. 借钱 borrow
#     事情:
#       张三 教 李四 学 python
#       李四 教 张三 学 跳皮筋
#       张三 上班赚了 1000 元钱
#       李四 向 张三 借了 200 元钱
#       打印张三的信息: 35岁 的 张三 有钱 800元, 它学会跳皮筋
#       打印李四的信息: 8岁 的 李四 有钱 200元, 它学会python
class Human:
    def __init__(self,name,age,skill):
        self.name=name
        self.age=age
        self.skill=skill
    def teach(self,other,skill):
        self.skill=skill
        print(self.name,'教',other.name,'学',self.skill)
    def work(self,money):
        self.money=1000
        print(self.name,'上班赚了',self.money,'元钱')
    def borrow(self,jie,other):
        self.jie=200
        print(self.name,'向',other.name,'借了',self.jie,'元钱')
    def fun(self,)
zs=Human('张三',35,'python')
ls=Human('李四',8,'跳皮筋')

zs.teach(ls,'python')
ls.teach(zs,'跳皮筋')

zs.work(1000)
ls.borrow(200,zs)


