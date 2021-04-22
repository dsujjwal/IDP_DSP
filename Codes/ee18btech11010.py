import numpy as np
import matplotlib.pyplot as plt

N=6
x=np.array([1,2,3,4,2,1])

#h[n]
h=np.zeros(N)
h[0]=1
h[1]=(-1/2)*h[0]
h[2]=1-(1/2)*h[1]
for i in range(3,N):
    h[i]=(-1/2)*h[i-1]

#DFT function using matrix multiplication
def DFT_matrix(N):
    n,k=np.meshgrid(np.arange(N),np.arange(N))
    
    
    W=np.exp(-1j*2*np.pi*n*k/N)
    return W


X=DFT_matrix(N)@x    #DFT of x
H=DFT_matrix(N)@h    #DFT of h

#plots
n=np.linspace(0,N-1,N)

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
plt.title(r'$ \angle{X[k]}$'); plt.xlabel('k'); plt.ylabel('Phase in Degrees')
plt.grid()
plt.show()

plt.stem(n,abs(H),use_line_collection='True')
plt.title('$\mid H[k] \mid $'); plt.xlabel('k'); plt.ylabel('Amplitude')
plt.grid()
plt.show()

plt.stem(n,np.angle(H,deg=True),use_line_collection='True')
plt.title(r'$\angle{H[k]}$'); plt.xlabel('k'); plt.ylabel('Phase in Degrees')
plt.grid()
plt.show()
