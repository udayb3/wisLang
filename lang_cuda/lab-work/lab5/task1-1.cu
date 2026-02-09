#include<stdio.h>
#include<cuda.h>
#include<math.h>

#define N 8
#define VALUE 2
#define BLOCK_SIZE 1024


__global__ void reduce1(int *g_idata, int *g_odata, int val) {
 
  extern __shared__ int sdata[];
 
  unsigned int i = blockIdx.x*blockDim.x + threadIdx.x;
 
  if ( i< val ){
    
    // each thread loads one element from global to shared mem
    unsigned int tid = threadIdx.x;
    sdata[tid] = g_idata[i];
    __syncthreads();
    
    // do reduction in shared mem
    for (unsigned int s=1; s < blockDim.x; s *= 2) {
      if (tid % (2*s) == 0 && tid+s<val) {
        sdata[tid] += sdata[tid + s];
      }
      __syncthreads();
    }
    
    // write result for this block to global mem
    if (tid == 0) g_odata[blockIdx.x] = sdata[0];
  }
}

int main()
{
  int *inp, *out, *d_inp, *d_out;
  double t1= pow(2,N);
  int val= (int)t1;
  
  inp= new int[ val ];
  out= new int[ val ];
  
  for ( int i=0;i<val;i++ ){
    inp[i]= VALUE;
  }

  cudaMalloc( &d_inp, val*sizeof(int)  );
  cudaMalloc( &d_out, val*sizeof(int) );

  cudaMemcpy( d_inp, inp, val*sizeof(int), cudaMemcpyHostToDevice);
  
  int N_BLOCKS= val/BLOCK_SIZE;
  
  reduce1<<<N_BLOCKS+1,BLOCK_SIZE >>>( d_inp, d_out,val ); cudaDeviceSynchronize();
  
  cudaMemcpy( out, d_out, val*sizeof(int), cudaMemcpyDeviceToHost);

  printf("Result: %d\n", out[0]);
  return 0;
}
