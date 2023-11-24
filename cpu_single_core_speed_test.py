import time
import sys
import gmpy2
from gmpy2 import mpz
import datetime
from time import strftime

size=6
global n
n=str(5)
for i in range(size):
    n=n+'0'
n=int(n)
path_now = str(sys.path[0]).replace('\\','/')+'/piCalRes.txt'
# 使用 Chudnovsky 公式和 binary splitting 算法计算圆周率小数点后 n 位
# 使用 gmpy2.mpz 加速
def piCal(digits):
    digits *= 2
    def binsplit(a, b):
        if b - a == 1:
            if a == 0:
                Pab = Qab = 1
            else:
                Pab = (6*a-5) * (2*a-1) * (6*a-1)
                Qab = 640320**3//24 * a**3
            Tab = (13591409 + 545140134 * a) * Pab
            if a & 1:
                Tab = -Tab
            return mpz(Pab), mpz(Qab), mpz(Tab)
        else:
            m = (a + b) // 2
            Pam, Qam, Tam = binsplit(a, m)
            Pmb, Qmb, Tmb = binsplit(m, b)
            Pab = Pam * Pmb
            Qab = Qam * Qmb
            Tab = Qmb * Tam + Pam * Tmb
            return Pab, Qab, Tab
    # Chudnovsky 公式每计算一项，正确位数会增加 14 位，
    # 所以要计算 digits//14 + 1 项
    terms = digits // 14 + 1
    P, Q, T = binsplit(0, terms)
    return Q * 426880 * gmpy2.sqrt(10005 * mpz(10)**digits) // T


def cal():
    global n
    x=piCal(n)
    return x

n=5000000

ts = time.time()
print('start......')
x=piCal(n)
now=datetime.datetime.now()
strTime=str(now.strftime("%Y-%m-%d %H:%M:%S"))
file=open(path_now,'w+')
te = time.time()-ts
te="%.2f"%te
t2=float(te)
rank="%.2f"%(10000/t2)
mes='pi cal '+str(n)+' length time use:\n'+str(te)+'s\ntest date: '+strTime+'\ncpu score: '+str(rank)+'\ne.g: zen2 3.6GHz single core (LPddr4 3200) score: 1600'
file.write(mes)
file.close()
print(mes)
print('completed!')
sys.exit()
