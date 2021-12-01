from math import *

k = 1
alpha = (sqrt(5)-1)/2 #0.618
eps = 0.0001
a = 0.0
b = 1.0

def f(x):
    y = exp(-x) + x**2
    return y

x1 = a + (1-alpha)*(b-a)
x2 = a + alpha*(b-a)
while(b-a>eps):
    if f(x1)>f(x2):  #如果f(x1)>f(x2)，则在区间(x1,b)内搜索
        a = x1
        x1 = x2
        x2 = a + alpha*(b-a)
    elif f(x1)<f(x2):  #如果f(x1)<f(x2),则在区间(a,x2)内搜索
        b = x2
        x2 = x1
        x1 = b - alpha*(b-a)
    else:  #如果f(x1)=f(x2)，则在区间(x1,x2)内搜索
        a = x1
        b = x2
        x1 = b - alpha*(b-a)
        x2 = a + alpha*(b-a)
    print("第"+str(k)+"次迭代结果为:", [a,b])
    k = k + 1
    


