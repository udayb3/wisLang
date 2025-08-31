#include<stdio.h>
#include<cuda.h>

#define N 3
#define BLOCK_SIZE 1024

__global__ void mykernel( int *A, int *B, int *C)
{
    int id= blockIdx.x * BLOCK_SIZE + threadIdx.x;
    if ( id<N*N ) {
      int x= id/N, y= id%N;
      int sum=0;
      for ( int i=0;i<N;i++ ) {
        sum+= A[ x *N + i  ] * B[ i*N + y ];
      }
      C[id]= sum;
    }
}

int main() {
  // creating variables
  int *A, *B, *C, *dA, *dB, *dC;

  // allocating space for variables
  A= (int *)malloc( N*N*sizeof(int) );
  B= (int *)malloc( N*N*sizeof(int) );
  C= (int *)malloc( N*N*sizeof(int) );

  cudaMalloc ( (void**)&dA, N*N*sizeof(int) );
  cudaMalloc ( (void**)&dB, N*N*sizeof(int) );
  cudaMalloc ( (void**)&dC, N*N*sizeof(int) );

  // initializing and allocating space
  for ( int i=0;i<N*N;i++ ) {
      A[i]= 1; B[i]= 2;
  }

  // copying data from cpu to gpu
  cudaMemcpy( dA, A, N*N*sizeof(int), cudaMemcpyHostToDevice );
  cudaMemcpy( dB, B, N*N*sizeof(int), cudaMemcpyHostToDevice );

  int p= N/BLOCK_SIZE;
  mykernel<<< p+1 , BLOCK_SIZE >>>( dA, dB, dC);   cudaDeviceSynchronize();

  cudaMemcpy( C, dC, N*N*sizeof(int), cudaMemcpyDeviceToHost );

  for ( int i=0;i<N;i++ ) {
    for ( int j=0;j<N;j++ ) {
      printf("%d ", C[i*N + j]);
    }
    printf("\n");
  }
  return 0;
}