//  FloatingAsBinary.cpp
//  {L} printBinary
//  {T} 3.14159
//  Created by Chan Nok Man on 12/3/2021.
//

/*
 The bits inside of floats and doubles are divided into three regions:
 1) the exponent
 2) the mantissa
 3) the sign bit
 */
#include "printBinary.h"
#include <cstdlib>
#include <iostream>
using namespace std;

int main(int argc, char* argv[]) {
    // This checks the value of argc
    // which is two, if there is a single argument
    // 1 if there is no arguments,
    // since the first element of argv
    if(argc != 2) {
        cout << "Must provide a number " << endl;
        exit (-1);
    }
    
    // This grabs the argument from the command line
    // and convert the chars into a double using atof, atoi, atol
    double d = atof(argv[1]);
    // The double is then treated as an array of bytes
    // by taking the address and casting it to an unsigned char*
    unsigned char* cp = reinterpret_cast<unsigned char*> (&d);
    // Then the bytes are passed into printBinary() to display
    for(int i = sizeof(double); i > 0; i -= 2){
        printBinary(cp[i-1]);
        printBinary(cp[i]);
    }
}
/*
clang: error: linker command failed with exit code 1 (use -v to see invocation)
/*
