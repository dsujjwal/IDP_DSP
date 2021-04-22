
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
//define M_PI 3.1415926535

typedef struct
{
	double real;
	double imag;
} complex;

void FFT(complex *X, int n)
{
	if (n <= 1) /* Trivial case */
		return;

	complex *eve_X = (complex *)malloc(n / 2 * sizeof(complex));
	complex *odd_X = (complex *)malloc(n / 2 * sizeof(complex));

	for (int i = 0; i < n / 2; i++)
	{
		eve_X[i] = X[2 * i];
		odd_X[i] = X[2 * i + 1];
	}

	FFT(eve_X, n / 2);
	FFT(odd_X, n / 2);

	for (int i = 0; i < n / 2; i++)
	{
		complex temp;

		double cos_val = cos(2 * M_PI * i / n);
		double sin_val = sin(2 * M_PI * i / n);

		temp.real = cos_val * odd_X[i].real + sin_val * odd_X[i].imag;
		X[i].real = eve_X[i].real + temp.real;
		X[i + n / 2].real = eve_X[i].real - temp.real;

		temp.imag = cos_val * odd_X[i].imag - sin_val * odd_X[i].real;
		X[i].imag = eve_X[i].imag + temp.imag;
		X[i + n / 2].imag = eve_X[i].imag - temp.imag;
	}

	free(eve_X);
	free(odd_X);
}





int main()
{
	int N = 8;
	int x[] = {1,2,3,4,2,1};

	//zero-padding of x(n)
	int n=sizeof(x)/sizeof(int);
	int x_pad[N];
    for(int i=0;i<N;i++){
        if (i<n){
            x_pad[i]=x[i];
        }
        else{
            x_pad[i]=0;
        }
    }

	complex *X = (complex *) malloc(N * sizeof(complex));

	for(int i = 0; i < N; i++)
	{
		X[i].real = x_pad[i];
		X[i].imag = 0;
	}
	FFT(X,N);

	//Displaying X(k)
	printf("X(k)= (X{Re} , X{Img})\n");
	for(int i = 0; i < N; i++){
		printf("X(%d)= (%.5lf, %.5lf)\n",i, X[i].real, X[i].imag);
}
}



