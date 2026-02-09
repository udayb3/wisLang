#include<stdio.h>
#include<cuda.h>

__global__ void myKernel( int *M, int *V, int *R, int n ) {
  int id= threadId.x, sum=0;
  for ( int i=0;i<n;i++ ) {
    sum+= M[ id*n+i  ] * V[ i ];
  }
  R[id]= sum;
}

int main() {
  int n= 16;
  int *M= new int[n*n], *V= new int[n*1], *R= new int[n*1], *dM, *dV, *dR;
  for ( int i=0;i<n*n;i++ ) {
      M[i]= i+1;
  }
  for ( int i=0;i<n;i++ ) {
    V[i]= i+1;
  }
  
  cudaMalloc( (void**)&dM, n*n*sizeof(int) );
  cudaMalloc( (void**)&dV, n*sizeof(int) );

  cudaMemcpy( dM, M, n*n*sizeof(int), cudaMemcpyHostToDevice );
  cudaMemcpy( dV, V, n*sizeof(int), cudaMemcpyHostToDevice );
  cudaMemcpy( dR, R, n*sizeof(int), cudaMemcpyHostToDevice );

  myKernel<<<1, n>>>( dM, dV, dR , n );
  
  cudaMemcpy(  R, dR, n*1*sizeof(int), cudaMemcpyDeviceToHost );
  for (int i=0;i<n;i++ ){
    printf("%d ", R[i]);
  }
  
  return 0;
}
