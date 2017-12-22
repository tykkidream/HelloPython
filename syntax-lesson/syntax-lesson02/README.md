syntax-lesson02说明
========================

本 lesson 内容为 《Python编程从入门到实践》 第12、13、14章内容。



语法知识
=====================

1
-----

子类中调用父类的构造函数，兼容 python2.7 和 python3.0 的调用方法。

[`bullet.py`](bullet.py) 文件：

~~~python
class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
~~~