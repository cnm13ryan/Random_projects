
//
//  printBinary.cpp
//  C03
//
//  Created by Chan Nok Man on 18/2/2021.
//

//: C03:printBinary.cpp
#include <iostream>

void printBinary( const unsigned char val){
    for(int i = 7; i >= 0; i--){
        if( val & (1<< i)) {std::cout << "1";}
        else {std::cout << "0";}
    }
}///:~
