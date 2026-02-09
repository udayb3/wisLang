#include<stdio.h>
#include<cuda.h>

__global__ void mykernel()
{
    int a= blockIdx.x, b= threadIdx.x;
    printf("Hello from block: %d, thread: %d\n", a, b);
}

int main() {
    mykernel<<< 2,2 >>>();
    cudaDeviceSynchronize();
    return 0;
}