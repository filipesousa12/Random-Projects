from numdifftools import Hessian,Gradient
import numpy as np
import matplotlib.pyplot as plt
import time 
from math import pi


#def f(x):
    #return (x[0]**2+x[1]-11)**2+(x[0]+x[1]**2-7)**2

def f(x):
		return 100*(x[1]-x[0]**2)**2+(1-x[0])**2

def NEWTON(mu,c2,f,ro,x0):

    xk=np.array(x0)
    n=0
    w=[]
    fun = []
    xs=[xk]
    e=10
    gra = 10
    grad = []
    g=Gradient(f)
    h=Hessian(f)
    t0 = time.time()

    while(e>10**(-10) and gra > 10**(-10)):

        h_inv= np.linalg.inv(h(xk))
        p=-np.matmul(h_inv,g(xk))
        
        a = 1
        while( f(xk+a*p) > f(xk)-mu*a*np.matmul(g(xk),p)):   #and np.matmul(g(xk+a*p),p)<c2*np.matmul(g(xk),p)):
            a = a*ro
    
        xv = xk    
        xk = xk+a*p
        n += 1
        fun.append(f(xk))
        xs.append(xk)
        e = np.linalg.norm(xk-xv)
        gra = np.linalg.norm(g(xk))
        grad.append(gra)
        w.append(e)
        

    t = time.time() - t0

    print(f"A solução ótima é {round(f(xk),3)} atingida no ponto {np.round(xk,3)} em {n} iterações com um tempo de {round(t,2)}s.")



x0=[10,10]

#x3 = [-40,40]


   

y1 = NEWTON(0.00001,0.0001, f, 0.5, x0)
y2 = NEWTON(0.00001,0.0001, f, 1/4, x0)
y3 = NEWTON(0.00001,0.0001, f, 1/8, x0)
#y4 = NEWTON(0.00001, 0.0001,f, 0.5, x0)



x1 = range(0,len(y1))
x2 = range(0,len(y2))
x3 = range(0,len(y3))
#x4 = range(0,len(y4))







plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
#plt.plot(x4,y4)
plt.xlabel("Nº iterações")
plt.ylabel("f(x)")
plt.legend(['ro=1/2','ro=1/4','ro=1/8'])
plt.show()









