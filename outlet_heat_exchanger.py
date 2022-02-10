#!/usr/bin/env python
# coding: utf-8

# The below section is on the outlet stream of the heat exchanger
# which uses Antoine's equation and coefficients to calculate the vapour pressure given known values of pressure and temperature. The vapour pressure calculated can then be applied to the multi component version of Raoult's Law to determine the composition of individual species in the outlet stream.

# For this purpose, a class "Chem_Species" is created to store the data and functions to compute the partial vapour pressures and the individual composition of species in binary phases.
# 

import numpy as np
import matplotlib.pyplot as plt


class Chem_Species(object):
    
    def __init__(self, name='no name', P_satur=lambda T: null):
        self.name = name;
        self.P_satur = P_satur;
   
    def P_satur(self, T):
        """Compute the saturation pressure given the known temperature """
        raise Exception('P_satur() has not been defined for ' + self.name);
        

 
def pressure_ratio(list_Pp, P_sys=1200):
    """Function to calculate the pressure ratio"""
    
    Pr_i = [];
    i = 0;
    while i < len(list_Pp):
        result = list_Pp[i] / P_sys;
        Pr_i.append(result);
        i += 1;
    return Pr_i;

def cal_phase_com(list_com, list_Pr):
    """ Function to calculate the composition of the species in their respective phases"""
    
    X_i, Y_i = [], [];
    i = 0;
    while i < len(list_com):
        x_result = list_com[i] / (1 + list_Pr[i]);
        y_result = list_com[i] - x_result;
        X_i.append(round(x_result, 5));
        Y_i.append(round(y_result, 5));
        i += 1;
    return X_i, Y_i;


def compute_partial_P(Tsys=20):
    """Return the partial pressure of the compund
    
    >>> compute_partial_P(20)
    (183.3057966039555, 17.578005499499085, 38.2646426454334)
    """
    # Antoine coefficient referenced from Yaw's handbook 
    act_fn =  Chem_Species('Acetone',  lambda T: 10**(7.31414 - 1315.67/(T + 240.479)));
    w_fn   =  Chem_Species('Water',  lambda T: 10**(8.05573 - 1723.64/(T + 233.076)));
    ipa_fn =  Chem_Species('IPA',  lambda T: 10**(7.83056 - 1483.3/(T + 217.413)));
    
    # Partial Pressure of Acetone, Water, IPA
    act_Pp = act_fn.P_satur(Tsys);  # Expected: 183.3057966039555
    w_Pp = w_fn.P_satur(Tsys);      # Expected: 17.578005499499085
    ipa_Pp = ipa_fn.P_satur(Tsys);  # Expected: 38.2646426454334
    return act_Pp, w_Pp, ipa_Pp;

def sum_list(list1):
    """Return the summation of all the elements in the list
    >>> sum_list(range(1,100))
    4950
    """
    tot = sum(list1);
    return tot;

# Create a list of Composition of Species ['Acetone', 'Water', 'IPA']
com_S4_i = [0.376, 0.206, 0.0417];


# Calculate the composition of the species in binary phases
X_4i, Y_4i = cal_phase_com(com_S4_i, 
                           pressure_ratio(
                               compute_partial_P(20)));

# Verify the composition of hydrogen
Y_H2 = 1 - sum_list(Y_4i) - sum_list(X_4i);
# display(Y_H2);

# Append the hydrogen composition to the list Y_4i
Y_4i.append(round(Y_H2,5))

# Print the output of the compositions
print(f" X_4i \tX_act \tX_w \tX_ipa\n\t{X_4i} \n\n Y_4i \tY_act \tY_w \tY_ipa \tY_H2\n\t{Y_4i} ");

# Verify if all the compositions of individual species add up to one
sum(X_4i+Y_4i);





