// -----------------------------------------------------------
// basic_ops.c: Demonstrates basic C operations
//
// Command to compile:
// gcc -c basic_ops.c
//
// Command to build executable file:
// gcc -o main basic_ops.o -lm
//
// This is a handout for ITMC231 (Platform Technologies)
// Intercession, S/Y 2020-2021
//
// (c) Glenn G. Fabia, 2021
// -----------------------------------------------------------
#include <stdio.h>
#include <math.h>
int main(int argc, char *argv[]) {
// Variable Declaration/Initialization
int x = 2, y = 3;
double pi = 3.1415926;
int arr[] = {2,1,4};
int *p = arr;
// Arithmetic Operations, Formatted Output
printf("%d %% %d == %d\n", x, y, x % y);
printf("%d / %d == %d\n", x, y, x / y);
printf("pi == %0.3f\n", pi);
printf("pi* pow(%d, 2) == %0.3f\n", y, pi*pow(y, 2));
printf("(x) ? 7 : 8 == %d\n", (x) ? 7 : 8);
printf("(int) pi == %d\n", (int) pi);
printf("sizeof(int) == %d\n", sizeof(int));
printf("sizeof(arr) == %d\n", sizeof(arr));
printf("*p == %d\n", *p);
printf("*p + 1 == %d\n", *p+1);
printf("*(p + 1) == %d\n", *(p+1));
return 0;
}