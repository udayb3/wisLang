%%cuda
#include<stdio.h>
#include <sys/time.h>

__global__ void computeZ ( int *X, int *Y, int *Z, int a, int N ) {
    int i =  threadIdx.x;
    if (i < N) {
        Z[i] = X[i] + Y[i];
    }
}

int main() {
    int k = 2048;
    int a = 4;

    time_t t0, t1;

    int *sX = new int[k*k];
    int *sY = new int[k*k];
    int *sZ = new int[k*k];
    int *X = new int[k*k];
    int *Y = new int[k*k];
    int *Z = new int[k*k];

    // Initialize X and Y with some values (example)
    for (int i = 0; i < k*k; ++i) {
        X[i] = 1;  Y[i] = 2; sX[i]= 1; sY[i]= 2;
    }

    clock_t start = clock();

    for ( int i=0;i<k;i++ ) {
        for ( int j=0; j< k;j++ ) {
            sZ[i*k+j]= sX[i*k+j] + sY[i*k+j]; 
        }
    }

    clock_t end = clock();
    double time_seq = (end - start)/(double)CLOCKS_PER_SEC;


    // Allocate memory for arrays X, Y, Z on the device
    int *d_X, *d_Y, *d_Z;
    cudaMalloc((void**)&d_X,k* k * sizeof(int));
    cudaMalloc((void**)&d_Y, k*k * sizeof(int));
    cudaMalloc((void**)&d_Z, k*k * sizeof(int));

    // Copy data from host to device
    cudaMemcpy(d_X, X, k*k * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(d_Y, Y, k*k* sizeof(int), cudaMemcpyHostToDevice);

    
    int THREAD_BLOCK_NO   =  4096 ;
    int THREADS_PER_BLOCK =  1024 ;

    start = clock();

    // Launch the kernel
    computeZ<<<1,k*k >>>(d_X, d_Y, d_Z, a, k*k);

    end = clock();
    double time_par = (end - start)/(double)CLOCKS_PER_SEC;
    
    // Copy the result array Z back to host
    cudaMemcpy(Z, d_Z, k*k * sizeof(int), cudaMemcpyDeviceToHost);

    printf("Number of thread block: %d , Threads per Block: %d \n\n Sequential Execution time: %lf, Cuda Kernel Speed up time: %lf", THREAD_BLOCK_NO, THREADS_PER_BLOCK, time_seq, time_par);
    
    // Free device memory
    cudaFree(d_X);
    cudaFree(d_Y);
    cudaFree(d_Z);

    // Free host memory
    free(X);
    free(Y);

    return 0;
}