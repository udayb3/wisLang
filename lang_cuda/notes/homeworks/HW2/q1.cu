#include <stdio.h>

using namespace std;

#define N1 30
#define N2 30
#define RADIUS 7
#define BLOCK_SIZE 1024

__global__ void stencil1D(int *input, int *output) {
  __shared__ int t1[2*RADIUS + BLOCK_SIZE];
  int genind= threadIdx.x + blockIdx.x * blockDim.x;

  if ( genind<N1 ) {
    int shaind= threadIdx.x + RADIUS;

    t1[ shaind ]= input[genind];
    if ( threadIdx.x < RADIUS) {
      t1[ shaind-RADIUS ]= input[ genind- RADIUS];
      t1[ shaind+RADIUS ]= input[ genind + BLOCK_SIZE];
    }
    __syncthreads();

    int res=0;
    for ( int i=-RADIUS;i<= RADIUS; i++ ) {
      res+= t1[ i+ shaind ];
    }
    output[genind]= res;
  }
}

int main(){

  int *input, *output, *d_input, *d_output;
  input = new int[N1];  output = new int[N2];
  for (int i = 0; i < N1; i++){
    input[i] = 5;
  }

  // Allocate device memory and copy input data over to GPU
  cudaMalloc(&d_input, N1*sizeof(int));
  cudaMalloc(&d_output, N2*sizeof(int));

  cudaMemcpy(d_input, input, N1*sizeof(int), cudaMemcpyHostToDevice);

  int tot= N1/BLOCK_SIZE;
  stencil1D<<< tot+1, BLOCK_SIZE>>>( d_input, d_output );
  cudaDeviceSynchronize();

  cudaMemcpy(output, d_output, N1*sizeof(int), cudaMemcpyDeviceToHost );
  for ( int i=0;i<N1;i++ ) {
    if ( i>RADIUS && i<N1-RADIUS) printf("%d ", output[i]);
  }
  return 0;
}
  