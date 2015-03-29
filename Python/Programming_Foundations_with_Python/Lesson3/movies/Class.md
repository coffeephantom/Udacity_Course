
>原文地址:http://www2.lib.uchicago.edu/keith/courses/python/class/5/

#类定义语法

在python中类由类定义创建，有着相关的命名空间，支持属性查询，并且可以被调用。

    class name[(expr[,expr]*)]:
        suite
类定义是一个可执行声明，所以可以用在任何可以进行可执行声明的地方。当执行这个声明的时候,每个expr都会按照类进行计算,然后在新建的本地命名空间执行suite:设想suite中的声明会和这个命名空间绑定,这些声明通常是一些赋值和函数。而执行suite以后,name即为外部（调用的）命名空间中的新建类,并且类定义新建的命名空间和类对象是有联系的。

#类预定义属性
类有5个预定义属性
<table>
    <tr>
        <td>属性</td>
        <td>类型</td>
        <td>读／写</td>
        <td>描述</td>
    </tr>
    <tr>
        <td>__dict__</td>
        <td>词典</td>
        <td>R/W</td>
        <td>类命名空间</td>
    </tr>
    <tr>
        <td>__name__</td>
        <td>字符串</td>
        <td>R/O</td>
        <td>类名称</td>
    </tr>
    <tr>
        <td>__bases__</td>
        <td>类的元组</td>
        <td>R/O</td>
        <td>所继承的类</td>
    </tr>
    <tr>
        <td>__doc__</td>
        <td>字符串或者为None</td>
        <td>R/W</td>
        <td>类文档字符串</td>
    </tr>
    <tr>
        <td>__module__</td>
        <td>字符串</td>
        <td>R/W</td>
        <td>用以定义类的模块名</td>
    </tr>
</table>

#作为纪录和结构的类
类的最简单的用法就是笛卡尔类型,就像Pascal中的纪录或者说C中的结构
    
    class foo:
        a, b, c = 0, "bar", (1,2)

##类的实例化
调用类对象实现了类的实例化:

    i=foo()
        pirnt i.a,i.b,i.c

在上述例子中,i是类foo的一个实例,a,b,c可以通过赋值进行修改：
    
    i.a=12
        i.new="yikes"

注意在新建类时没有定义的新参数，可以通过赋值创建，非常简单。确实，在进行交互性工作的时候，空类非常好用。
    
    class foo: pass
        foo.a = 1
        foo.b = 2

##实例属性
实例有两个预定义属性
<table>
    <tr>
        <td>属性</td>
        <td>类型</td>
        <td>读／写</td>
        <td>描述</td>
    </tr>
    <tr>
        <td>__dict__</td>
        <td>词典</td>
        <td>读／写</td>
        <td>实例命名空间</td>
    </tr>
    <tr>
        <td>__class__</td>
        <td>类</td>
        <td>读／写</td>
        <td>实例所对应的类</td>
    </tr>
</table>

##类属性 vs 实例属性
理解类属性与实例属性的区别是十分重要的,因为类属性也可以通过实例进行访问。
在类中定义的属性, 但凡是在类中定义的，还是之后通过对类属性参数进行赋值的，都称为类属性。
它们保存在类的命名空间。（即类的__dict__当中）

在实例中通过赋值定义的属性称为实例属性，即使存在与类属性重名的，也是存储在实例的命名空间。通过实例赋值,会使得实例属性覆盖类属性:

    class foo:
        a = 1
        i = foo()
        foo.a => 1
        i.a => 1
        i.a = "inst"
        foo.a => 1
        i.a => "inst"

可以通过实例属性改变类属性，不过你需要让python显示命名空间。

    foo.a => 1
        i.__class__.__dict__[a] = "class"
        foo.a => "class"
        i.a => "inst"
当你用点操作符指向实例的属性时,Python首先查看实例命名空间,如果该属性没有找到,它会查看类命名空间。以下是用python语言描述的实例属性查找算法:

    def instlookup(inst,name):
        #simplfied algorithm
        if inst.__dict__.has_key(name):
            return inst.__dict__[name]
        else:
            return inst.__class__.__dict__[name]

注意如果在实例和类中均没有找到这个属性，那么这个函数会报AttributiveError的错误,就像python那样。

#在内容定义函数：方法
假设我们有笛卡尔坐标：

    cpt=(3,4)

然后有一个计算其到原点距离的函数：
    
    def distanceToOrigin(p):
        from math import floor,sqrt
        return floor(sqrt(p[0]**2+p[1]**2)

现在在我们的程序当中，我们对点进行操作时，只需要调用：
    
    print distanceToOrigin(cpt)

假设我们要定义一种新的坐标，叫做曼哈顿坐标：
    
    mpt=(3,4)

它使用另一种距离计算函数，我们马上希望重新命名我们第一个函数：

    CartesianDistanceToOrigin = distanceToOrigin

然后我们可以定义曼哈顿版本的：
    
    def ManhattanDistanceToOrigin(p):
        return abs(p[0]) + abs(p[1])

这显示了一个命名空间的问题:我们需要将笛卡尔和曼哈顿函数存储在不同的命名空间。我们可以利用python的模块来完成这一点：(cartesian.distanceToOrigin, manhattan.distanceToOrigin)，但是我们又遇到了另外一个问题：我们怎么知道哪个点属于哪个坐标呢？我们需要在元组当中加一个标签进行区分。

    CARTESIAN, MANHATTAN = 0, 1
    cpt = (CARTESIAN, 3, 4)
    mpt = (MANHATTAN, 3, 4)

(当然, 因为我们对象的属性是根据位置定义的,我们现在需要重写我们的距离函数，但是这并不是我们正在考虑的问题……) 并且, 糟糕的是, 我们需要在每次使用这段代码的地方增加标签判断代码:

    if pt[0] == CARTESIAN:
        print cartesian.distanceToOrigin(pt)
    elif pt[0] == MANHATTAN:
        print manhattan.distanceToOrigin(pt)
    else:
        raise TypeError, pt
    
为了解决这个问题， 我们可以写一个通用函数，这样就能保持条件位于一个地方, 但是我们仍然存在每新增一个新类型点就要更新这个条件的问题更新。如果新类型发生了改动，但是通用函数没有发生改动，这就会产生问题。(你会对针对新类型点的］作出改动，但是你也许并不了解外部每个需要更新条件的点操作通用函数。）解决方法是把函数和其操作各种类型的对象联系在一起T。这种函数叫做对象的方法。:

    cpt = (3,4, lambda p: floor(sqrt(p[0]**2 + p[1]**2)))
    
现在为了计算pt点到原点的距离, 我们不需要其他条件了: 每个点都知道如何去计算它自己的距离: pt[2](pt).

    print cpt[2](cpt)
    
即使对象执行它的函数, 我们也用不着条件或者是类型信息 (至少不是为了这个原因。) 并且针对新类型点的改动，也不需要去改动其他通用函数。

    mpt = (3,4, lambda p: p[0] + p[1])
    print mpt[2](mpt)
    
这是面向对象编程的基本概念.

上述例子最大的问题之一是使用了元组及其代表位置的下标。显然使用词典会更好:

    cpt = {
        "x": 3,
        "y": 4,
        "distanceToOrigin": lambda p: floor(sqrt(p["x"]**2 + p["y"]**2))
        }
        print cpt["distanceToOrigin"](cpt)
    
但是词典并不产生任何模板工具: 使用词典,对于我们定义的每一点，我们需要复制到distanceToOrigin定义当中. 我们需要的是类似Pascal或者是C中结构的东西，而Python则可以使用类:

    class cartesian:
        x, y = 0, 0
        def distanceToOrigin(p):
        return floor(sqrt(p.x**2 + p.y**2))
    cpt = cartesian()
    cpt.x, cpt.y = 3,4
    # WARNING: the following is not correct Python code...
    print cpt.distanceToOrigin(cpt)
    
这看起来好多了, 但是总是都要向对象本身传递它的方法有些烦人，尤其因为对象是主要的，并且有可能有着复杂的表达式。比如：

    x[y].distanceToOrigin(x[y])
    
这很容易出错，而且有可能很低效(因为重计算的关系) ，因为它总是需要把复杂的对象表达式赋值给本地变量，所以python给出了一个十分好用的语法来帮助我们完成这个工作：如果你在一个类中定义了一个函数，它假设这个函数是这个类的方法，所以当它被调用的时候，Python会在后台首先把实例作为第一个参数传递给它，所以调用distanceToOrigin方法的正确途径十分简单:

    print cpt.distanceToOrigin()
    
##Self

在python当中把方法的第一个参数命名为self是一个传统, 比如:

    class cartesian:
        def distanceToOrigin(self):
        return floor(sqrt(self.x**2 + self.y**2))
    
这种命名方式并不是强制的, 但是如果你使用其他命名方式的话，在别的python编程者看起来会很奇怪。

##自定义对象

Python allows you to customize your objects by defining some methods with special names:

__init__ Method

      def __init__(self, parameters):
          suite
    
The parameters are as for ordinary functions, and support all the variants: positional, default, keyword, etc. When a class has an __init__ method, you pass parameters to the class when instantiating it, and the __init__ method will be called with these parameters. Usually the method will set various instance variables via self.

      class cartesian:
          def __init__(self, x=0, y=0):
              self.x, self.y = x, y
    
__del__ Method

      def __del__(self):
          suite
    
A __del__ method is called when an object is deleted, which is when the garbage collector decides that their are no more references to an object. Note that this is not necessarily when the object is explicitly deleted with the del statement. The __del__ method takes exactly one parameter, self. Due to a weirdness in the current C implementation of Python, exceptions are ignored in __del__ methods: instead, an error will be printed to standard error.

__repr__ Method

      def __repr__(self):
          suite
    
A __repr__ method takes exactly one parameter, self, and must return a string. This string is intended to be a representation of the object, suitable for display to the programmer, for instance when working in the interactive interpreter. __repr__ will be called anytime the builtin repr function is applied to an object; this function is also called when the backquote operator is used.

__str__ Method

      def __str__(self):
          suite
    
The __str__ method is exactly like __repr__ except that it is called when the builtin str function is applied to an object; this function is also called for the %s escape of the % operator. In general, the string returned by __str__ is meant for the user of an application to see, while the string returned by __repr__ is meant for the programmer to see, as in debugging and development: but there are no hard and fast rules about this. You're best off just thinking, __str__ for %s, __repr__ for backquotes.

Inheritance

Using classes to define objects provides a templating facility: class attributes and methods need only be defined once, and you can then instantiate any number of objects, all sharing the same methods.

But we could benefit from more sharing opportunities. Lots of times classes of related objects differ only slightly from one another. Consider the full definitions of our two classes of points:

      class cartesian:
          def __init__(self, x=0, y=0):
              self.x, self.y = x, y
          def distanceToOrigin(self):
          return floor(sqrt(self.x**2 + self.y**2))
      class manhattan:
          def __init__(self, x=0, y=0):
              self.x, self.y = x, y
          def distanceToOrigin(self):
          return self.x + self.y
    
Both of these classes share the same __init__ method, yet we have to code it twice. We can solve this problem by abstracting the common method into a new, more generic class called point:

      class point:
          def __init__(self, x=0, y=0):
              self.x, self.y = x, y
    
Now we can redefine cartesian and manhattan and specify that they inherit from point:

      class cartesian(point):
          def distanceToOrigin(self):
          return floor(sqrt(self.x**2 + self.y**2))
      class manhattan(point):
          def distanceToOrigin(self):
          return self.x + self.y
    
We can define all behavior common to all types of points in the point class, and then define any number of subclasses of point which inherit from it. We could go farther and define subclasses of cartesian or manhattan if that were appropriate.

In some object-oriented languages (e.g., Java), point would be an abstract class: in other words, a class that's used only to inherit from, and not itself directly instantiated. Python doesn't make this distinction: if you want to instantiate point, go right ahead!

Let's look at the class definitition syntax again:

      class name[(expr[,expr]*)]:
          suite
    
As mentioned earlier, each expr, if given, must evaluate to a class, and now we know why: these are called the base classes, and are the classes that the new class inherits from. If multiple base classes are given, the new class inherits from all of them: this is called multiple inheritance. See the next section for an explanation of how attribute reference works in the presence of multiple inheritance.

Attribute Reference in Detail

Now we can explain class and instance attribute reference in detail.

When looking up an attribute via a class object C, Python first searches the class's name space (C.__dict__); if it doesn't find the attribute, it then recursively searches the class's base classes, left to right and depth first.

When looking up an attribute via an instance object i, Python first searches the instance's name space (i.__dict__); if it doesn't find the attribute, it then searches the instance's class (i.__class__) as described in the previous paragraph.

Here are the complete algorithms for class attribute lookup and instance attribute lookup. These functions each return a 2-tuple whose first element is a truth value indicating the success of the lookup, and whose second element is the value of the attribute, if the lookup was successful, or None if not:

    def classlookup(C, name):
        if C.__dict__.has_key(name):
        return (1, C.__dict__[name])
        else:
        for b in C.__bases__:
            success, value = classlookup(b, name)
            if success:
            return (1, value)
            else:
            pass
        else:
            return (0, None)

    def instlookup(I, name):
        if I.__dict__.has_key(name):
        return (1, I.__dict__[name])
        else:
        return classlookup(I.__class__, name)
    
Protection

Some B&D-oriented languages prevent access to the attributes of a class or instance, the idea being that if the author of the class didn't define a method to manipulate an attribute, then the user of the instance has no right to examine or change it. As you might have already guessed, Python doesn't take this approach. Attribute reference syntax can be used to access most instance and class attributes, and __dict__ attributes give the entire show away. The assumption is that you know what you're doing, and if you want to shoot yourself in the foot, that's your affair.

That said, Python does support name mangling: if a method or other attribute name starts with two leading underscores (e.g., __secret), Python magically changes the name so that references to this attribute made in the usual way will fail:

      class foo:
          def __secret(self): pass
      foo.__secret => AttributeError: __secret
    
This protection is purely advisory, however: if we examine the class name space we can see what Python is up to:

      foo.__dict__ => {'_foo__secret': <function __secret at fc328>, '__module__': '__main__', '__doc__': None}
    
The method name has been changed, or mangled, into _foo__secret: i.e., prefixed with underscore and the class name. Since this is documented behavior, you can use this name, either going through the __dict__ directly, or just via attribute reference (foo._foo__secret), to access the attribute.

Polymorphism

Another important attribute of an object-oriented programming language is polymorphism: the ability to use the same syntax for objects of different types. (Strictly speaking, this is ad-hoc polymorphism.) For example, in Python, the square bracket operator is used to perform indexing of various sequence types (list[3], dict["foo"]); polymorphism allows us to define our own types, as classes, that emulate builtin Python types like sequences and which therefore can use e.g. square brackets for indexing.

Customizing Attribute Reference

We'll start by showing how to override the behavior of the dot operator, which does attribute reference in classes and instances. By customizing attribute reference, an object can perform an arbitrary action whenever one of its attributes is referenced, such as type checking.

__getattr__ Method

      def __getattr__(self, name):
    
This method, if defined, is called when attribute lookup fails. For example, consider the following:

      class foo:
          a = 0
          def __getattr__(self, name):
              return "%s: DEFAULT" % name
      i = foo()
      i.b = 1
    
Since the attribute a is a class attribute of instance i, and the attribute b is an instance attribute of i, the __getattr__ method isn't called when either of these are accessed:

      i.a, i.b => 0, 1
    
But if we try to access an undefined attribute, say c, __getattr__ is called, with the attribute name as a parameter:

      i.c => "c: DEFAULT"
    
Note that __getattr__ won't be called if attribute lookup succeeds via inheritance.

The __getattr__ method should either return a value (of any type) or raise an AttributeError exception.

__setattr__ Method

      def __setattr__(self, name, value):
    
__setattr__ is called whenever an attribute assignment is attempted, regardless of whether or not the attribute is already bound in the instance or class. This happens instead of the normal mechanism of storing the value in the instance dictionary. This method can be used, for example, to perform type checking on a value before assigning it.

The __setattr__ method should not try to assign a value to an attribute in the usual way, i.e., self.name = value, as this will result in an infinite number of recursive calls to __setattr__; instead, the instance dictionary should be used directly:

      def __setattr__(self, name, value):
          self.__dict__[name] = value
    
__delattr__ Method

      def __delattr__(self, name):
    
This method is called when an attribute is deleted via the del statement.