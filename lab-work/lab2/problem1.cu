#include<stdio.h>

__global__ void computeZ ( int *X, int *Y, int *Z, int a, int N ) {
    int i =  threadIdx.x;
    if (i < N) {
        Z[i] = X[i] + Y[i];
    }
}

int main() {
    int k = 32;
    int a = 4;

    int *X = new int[k*k];
    int *Y = new int[k*k];
    int *Z = new int[k*k];

    // Initialize X and Y with some values (example)
    for (int i = 0; i < k*k; ++i) {
        X[i] = 1;  Y[i] = 2;
    }

    // Allocate memory for arrays X, Y, Z on the device
    int *d_X, *d_Y, *d_Z;
    cudaMalloc((void**)&d_X,k* k * sizeof(int));
    cudaMalloc((void**)&d_Y, k*k * sizeof(int));
    cudaMalloc((void**)&d_Z, k*k * sizeof(int));

    // Copy data from host to device
    cudaMemcpy(d_X, X, k*k * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(d_Y, Y, k*k* sizeof(int), cudaMemcpyHostToDevice);


    // Launch the kernel
    computeZ<<<1,k*k >>>(d_X, d_Y, d_Z, a, k*k);
    
    // Copy the result array Z back to host
    cudaMemcpy(Z, d_Z, k*k * sizeof(int), cudaMemcpyDeviceToHost);

    //  Optionally, print the result
    for (int i = 0; i < k; ++i) {
	for ( int j=0; j<k;j++ ) {
       	   printf("%d ", Z[i*k+j]);
	}
       printf("\n");
    }

    // Free device memory
    cudaFree(d_X);
    cudaFree(d_Y);
    cudaFree(d_Z);

    // Free host memory
    free(X);
    free(Y);

    return 0;
}

