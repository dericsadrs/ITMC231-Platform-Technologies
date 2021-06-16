//Author's Name, San Andres Deric 
//Course and Year, and BS- IT 2ND
//Honor Code which states the following: I have not given nor received any
// unathorized help in completing this exercise. I am also well aware of the policies
//stipulated in the AdNU student handbook.
// Filename        : main.c
// Description     : This program tests the implementation of the function 
//                   to approximate the value of PI.
//
//                   Input is read from STDIN and consists of multiple lines. 
//                   The first line contains the number of test cases, T. 
//                   This is then followed by T lines containing a positive integer n.
//
//                   Output is displayed in STDOUT. The output for each case 
//                   begin with the word CASE followed by a single space, 
//                   the case number starting from 1, a colon (:), and a single space,
//                   and finally, the approximate value of PI up to fifteen (15) decimal places.

#include <stdio.h>

#include "approx.h"

int main(int argc, char *argv[]){
    int testCase = 0; // testCases
    long double numberOfTerms,valueOfTerms,; //t for the number of terms; n for the value of terms
    long double rem; 

    scanf("%Lf", &numberOfTerms);
        

    for (int iterator=0; iterator<numberOfTerms; iterator=iterator+1) {
        testCase=testCase+1;
        scanf("%Lf",&valueOfTerms);
        long double outcome=approx_pi(valueOfTerms);

        rem = 4 * outcome;
        printf("CASE %d: ",testCase);
        printf("%0.15Lf \n", rem);


    }
    return 0;
    
}
