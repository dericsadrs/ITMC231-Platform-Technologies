/*# Author's Name San Andres Deric 
# Course and Year, 2ND BS-IT 
# Honor Code which states the following: I have not given nor received any
# unathorized help in completing this exercise. I am also well aware of the policies
# stipulated in the AdNU student handbook.
# Filename        : approx.py
# Description     : 
*/
#include <stdio.h>
 int a[4];
void stringBrand(int eax);
int main()
{
    for(int iterator = 0; iterator < 4; ++iterator)
    {
    stringBrand(iterator);
    }
}

void stringBrand(int eax)
{
    if(eax == 1) __asm__("mov $0x80000002, %eax\n"); 

    else if (eax == 2) __asm__("mov $0x80000003, %eax\n"); 

    else if (eax == 3)  __asm__("mov $0x80000004, %eax\n");
        
    asm("cpuid" : "=a" (a[0]), "=b" (a[1]), "=c" (a[2]), "=d"(a[3]));
    printf("%s", &a[0]);
}
