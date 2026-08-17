---
## What is CUDA
Compute Unified Device Architecture is  

### Generally, there are some conventions:
1. Device  ->  GPU
2. Host    ->  CPU

### The following flow is used generally:
1. Copy input data from cpu to memory.
2. Load gpu kernel and execute, data can be cached on chip too.
3. copy the results from the gpu.

### The Device code is generally put in a kernel like below one: 
```cuda
__global__ void myKernel(int *a, int *b, int *c, int N) {
    // code is put here
}

int main() {
    Serial code is put here 
}
```
- In the above code, /_/_global/_/_ shows that the method runs on Device.
- Device methods are processed by **Nvidia compiler** and Host methods are processed by **cpu**.

### Call to Device Code 
```cuda
mykernel<<< 1, 5 >>>();
```
- Above is called a **kernel launch**.
- Items inside the **<<< >>>** are known as **kernel execution configuration**.

### Memory handling APIs
```cuda
int A[10]; int *dA;

cudaMalloc( (void**)&dA , n*sizeof(int)  );
cudaMemcpy( A, dA , n*n, cudaDeviceToHost );

free(A); cudaFree(dA);
```
- Above there methods which do the task of allocating, copying and freeing of memory in gpu and cpu respectively.

### Concepts of Blocks and Threads
```cuda
mykernel<<< # of blocks , # of threads per block  >>>();
```
- it can be seen above as how the number of threads and blocks can be used.
- There is a limit as to how many threads can be there in a block. For safety, assume it to be 1024.
- Using a combination of threads and blocks give us the advantage of:
  - **Scalability**: # of threads is limited
  - **Communication**: Concept of shared memory

### Concept of Shared Memory
- This is shared by all the threads within a block. It's access time is less.
- Declaration is done as below:
  ```cuda
  __global__ myKernel() {
    __shared__ int x;
    for ( int i=0; i<8;i++ ) {
      x= i;
    }
  }
  ```
- A good example in this is the concept of Stencils
  ```cuda
  __global__ void stencil(int *in, int *out ) {
    __shared__ t1[ 2*RADIUS+ blockDim.x ];
    int genind= threadId.x + blockId.x * blockDim.x;
    int shind= threadId.x + RADIUS;

    t1[ shaind ]= input[genind];
    if ( threadId.x < RADIUS ) {
      t1[ shind-RADIUS ]= in[ genind - RADIUS ];
      t1[ shind + blockDim.x ]= in[genind + blockDim.x];
    \}

    __syncthreads();

    int res=0;
    for ( int i=-RADIUS;i<=RADIUS;i++ ) {
      res += t1[ i + shind ];
    }
    out[genind]= res;
  \}
  ```
- In the above code, the use of `__syncthreads` is to act as a barrier for all the threads in a particular block.
  
### Concept of Cooperative Groups
- This is a flexible model for synchronization and comm. within a group of threads.
- The concept of sharing in thread block can further be scaled to sharing in thread group.

### Different Architectures
- There are different architectures for the GPU's such Kepler, Maxwell, Pascal, Volta and more.

### Execution Model
- Threads are executed by Scalar Processor.
- Thread blocks are executed by Multi-processor.
- A kernel is generally launched as a grid of thread blocks.
- A thread block further consists of Warp

### Launch Configuration
- The latency in the case of GPU's is hidden inside the SM's.