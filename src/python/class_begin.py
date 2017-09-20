# -*- coding:utf-8 -*- 
#!/usr/bin/python

class Parent:
    parentAttr = 100
    def __init__(self):
        print ('调用父类构造函数')
    
    def parentMethod(self):
        print ('调用父类方法')
    
    def setAttr(self, attr):
        Parent.parentAttr = attr
    
    def getAttr(self):
        print ('父类属性：',Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        # 关于显示调用父类构造方法 可参考 https://segmentfault.com/q/1010000000622999
        # Parent.__init__(self)             #更直观
        # super(Child,self).__init__()      #一次初始化所有父类

        print ('调用子类构造函数')

    def childMethod(self):
        print ('调用子类方法')

    def __del__(self):
        print(self.__class__.__name__, 'destoryed')


c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

del c