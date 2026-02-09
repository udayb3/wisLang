#include<stdio.h>
#include<cuda.h>

#define N 2048
#define BLOCK_SIZE 1024

__global__ void mykernel( int *A, int *B, int *C)
{
    int id= threadIdx.x + blockIdx.x * blockDim.x;
    if ( id<N ) {
        C[id]= A[id] + B[id];
    }
}

int main() {
  // creating variables
  int *A, *B, *C, *dA, *dB, *dC;

  // allocating space for variables
  A= (int *)malloc( N*sizeof(int) );
  B= (int *)malloc( N*sizeof(int) );
  C= (int *)malloc( N*sizeof(int) );

  cudaMalloc ( (void**)&dA, N*sizeof(int) );
  cudaMalloc ( (void**)&dB, N*sizeof(int) );
  cudaMalloc ( (void**)&dC, N*sizeof(int) );

  // initializing and allocating space
  for ( int i=0;i<N;i++ ) {
      A[i]= 1; B[i]= 2;
  }

  // copying data from cpu to gpu
  cudaMemcpy( dA, A, N*sizeof(int), cudaMemcpyHostToDevice );
  cudaMemcpy( dB, B, N*sizeof(int), cudaMemcpyHostToDevice );

  int p= N/BLOCK_SIZE;
  mykernel<<< p+1 , BLOCK_SIZE >>>( dA, dB, dC);   cudaDeviceSynchronize();

  cudaMemcpy( C, dC, N*sizeof(int), cudaMemcpyDeviceToHost );

  for ( int i=0;i<N;i++ ) {
      printf("%d ", C[i]);
  }
  return 0;
}