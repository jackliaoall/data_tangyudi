#使用 exec() 函数动态赋值
for i in range(5):
    exec('var{} = {}'.format(i, i))
print(var0, var1, var2, var3 ,var4)

#利用命名空间动态赋值
names = locals()
for i in range(5):
    names['n' + str(i) ] = i
print(n0, n1, n2, n3, n4)

#在类中使用动态变量
class Test_class(object):
    def __init__(self):
        names = self.__dict__
        for i in range(5):
            names['n' + str(i)] = i
t = Test_class()
print(t.n0, t.n1, t.n2, t.n3, t.n4)