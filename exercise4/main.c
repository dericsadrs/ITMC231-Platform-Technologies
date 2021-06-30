/*Filename and Description,
Author's Name, Course and Year, San Andres Deric C
Honor Code which states the following: I have not given nor received any unathorized help in completing this
exercise. I am also well aware of the policies stipulated in the AdNU student handbook.

*/

//library
#include <stdio.h>

//main
int main() {
    

    //variable declarations
    int loop, val1, val2, add, sub, mul, quo, rem ;

    // input for loop
    scanf("%d",&loop);
    
    // loop for testcases
    for (int iterator = 1; iterator < loop+1; iterator++)
    {
    // input 
    scanf( "%d%d", &val1, &val2 );

      /* Adds the val1  and val2  and store result into register %eax */
    __asm__ ( "addl %%ebx, %%eax;" : "=a" (add) : "a" (val1) , "b" (val2) );
     /* Subtract val1 from val2 and store result into register %eax */
    __asm__ ( "subl %%ebx, %%eax;" : "=a" (sub) : "a" (val1) , "b" (val2) );
     /* Multiply val1 and val2 and store result into register %eax */
    __asm__ ( "imull %%ebx, %%eax;" : "=a" (mul) : "a" (val1) , "b" (val2) );

    __asm__ ( "movl $0x0, %%edx;"
               "idivl %%ebx;" : "=a" (quo), "=d" (rem) : "g" (val1), "g" (val2) );

    printf( "CASE %d:\n", iterator);
    printf( "%d + %d = %d\n", val1, val2, add );
    printf( "%d - %d = %d\n", val1, val2, sub );
    printf( "%d * %d = %d\n", val1, val2, mul );
    printf( "%d / %d = %d\n", val1, val2, quo );
    printf( "%d %% %d = %d\n", val1, val2, rem );

    }

    return 0 ;
}