 
#include <stdio.h>
 
int main(){
 
   unsigned int EAX, EBX, ECX, EDX;
   EAX = 0x0;
 
   asm("movl %0, %%eax" : : "r"(EAX));  /* Copy the value of EAX variable 
                                           into the %eax register */
   asm("cpuid");                        /* Call the CPUID instruction */
   asm("movl %%ebx, %0":"=r" (EBX));    /* Copy the contents of the %ebx register  
                                           into the EBX variable */
   asm("movl %%ecx, %0":"=r" (ECX));    /* Copy the contents of the %ecx register
                                           into the ECX variable */
   asm("movl %%edx, %0":"=r" (EDX));    /* Copy the contents of the %edx register 
                                           into EDX variable */
 
   unsigned int vendor_id[] = {EBX, EDX, ECX};  /* Store EBX:EDX:ECX in contiguous
                                                   memory locations */
  
   printf("%s", &vendor_id);            /* Treat vendor_id as a byte/char array and 
                                           print the result */
   
   return 0;
}
