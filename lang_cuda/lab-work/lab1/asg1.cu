#include<stdio.h>

__global__ void computeZ ( int *X, int *Y, int *Z, int a, int N ) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < N) {
        Z[i] = a * X[i] + Y[i];
    }
}

int main() {
    int N = 1024;
    int a = 4;

    int *X = new int[N];
    int *Y = new int[N];
    int *Z = new int[N];

    // Initialize X and Y with some values (example)
    for (int i = 0; i < N; ++i) {
        X[i] = i;  Y[i] = i * 2;
    }

    // Allocate memory for arrays X, Y, Z on the device
    int *d_X, *d_Y, *d_Z;
    cudaMalloc((void**)&d_X, N * sizeof(int));
    cudaMalloc((void**)&d_Y, N * sizeof(int));
    cudaMalloc((void**)&d_Z, N * sizeof(int));

    // Copy data from host to device
    cudaMemcpy(d_X, X, N * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(d_Y, Y, N * sizeof(int), cudaMemcpyHostToDevice);

    // Define block size and grid size
    int blockSize = 256;  // Number of threads per block
    int gridSize = (N + blockSize - 1) / blockSize;  // Number of blocks

    // Launch the kernel
    computeZ<<<gridSize, blockSize>>>(d_X, d_Y, d_Z, a, N);
    
    // Copy the result array Z back to host
    cudaMemcpy(Z, d_Z, N * sizeof(int), cudaMemcpyDeviceToHost);

    //  Optionally, print the result
    for (int i = 0; i < N; ++i) {
       printf("%d", Z[i]);
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

