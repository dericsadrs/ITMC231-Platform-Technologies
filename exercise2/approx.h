//Author's Name, San Andres Derid 
//Course and Year, 2ND BS-IT 
//Honor Code which states the following: I have not given nor received any
//unathorized help in completing this exercise. I am also well aware of the policies
//stipulated in the AdNU student handbook.
// Filename        : approx.h
// Description     : This header file contains the definition of the function to approximate the value of PI.

#ifndef APPROX_H
#define APPROX_H

long double approx_pi(int n){    
    long double outcome = 0; 
    long double var1,denominator;

    for(int iterator=1; iterator <= n; iterator=iterator+1) { // loop
        denominator=(2*(iterator))-1; 
        if(iterator%2==1) { // to chec if the number is divisible to 1
            var1= 1* (1.0/denominator);
        }
        else {

            var1= 1* (-1.0/denominator);
        }
    outcome = outcome +var1;
    }
    return outcome;
}

#endif // APPROX_H
