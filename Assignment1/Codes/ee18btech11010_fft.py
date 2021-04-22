import numpy as np
import matplotlib.pyplot as plt

N=8
#input signal
x=[1,2,3,4,2,1]
n=len(x)

#zero-padding of x for fitting the length requirements of fft algorithm)
if n<N:
    x_pad = x
    for i in range(N-n):
        x_pad.append(0)

#impuse response signal-h(n)
h=np.zeros(N)
h[0]=1
h[1]=(-1/2)*h[0]
h[2]=1-(1/2)*h[1]
for i in range(3,N):
    h[i]=(-1/2)*h[i-1]

# 8-point FFT algo
def FFT(x):
    n=len(x)
    if n==2:
        return np.hstack((x[0]+x[1],x[0]-x[1])) #2-point dft
    Xe = FFT(x[0::2]) # Even indexing of n of x(n)
    Xo = FFT(x[1::2]) # odd indexing of n of x(n)
    
    F=np.zeros((n//2,n//2), dtype=np.complex64)
    for i in range(n//2):
        F[i,i]=np.exp(-1j*2*np.pi*i/n)
    
    Xa = Xe + F@Xo # for n : [0,n/2-1]
    Xb = Xe - F@Xo # for n : [n/2,n]
    return np.hstack((Xa,Xb))


#FFT
X=FFT(x_pad)
H=FFT(h)

#plots

n =np.linspace(0,N-1,N)
plt.stem(n,x,use_line_collection='True')
plt.title('x[n]'); plt.xlabel('n'); plt.ylabel('Magnitude')
plt.grid()
plt.show()

plt.stem(n,h,use_line_collection='True')
plt.title('h[n]'); plt.xlabel('n'); plt.ylabel('Magnitude')
plt.grid()
plt.show()

plt.stem(n,abs(X),use_line_collection='True')
plt.title('$\mid X[k]\mid $') ; plt.xlabel('k') ; plt.ylabel('Amplitude')
plt.grid()
plt.show()

plt.stem(n,np.angle(X,deg=True),use_line_collection='True')
plt.title(r'$ \angle{X[k]}$'); plt.xlabel('k'); plt.ylabel('phase in degrees')
plt.grid()
plt.show()

plt.stem(n,abs(H),use_line_collection='True')
plt.title('$\mid H[k] \mid $'); plt.xlabel('k'); plt.ylabel('amplitude')
plt.grid()
plt.show()

plt.stem(n,np.angle(H,deg=True),use_line_collection='True')
plt.title(r'$\angle{H[k]}$'); plt.xlabel('k'); plt.ylabel('phase in degrees')
plt.grid()
plt.show()
