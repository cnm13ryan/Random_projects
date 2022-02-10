#!/usr/bin/env python
# coding: utf-8

# The below section is on the outlet stream of the heat exchanger
# which uses Antoine's equation and coefficients to calculate the vapour pressure given known values of pressure and temperature. The vapour pressure calculated can then be applied to the multi component version of Raoult's Law to determine the composition of individual species in the outlet stream.

# For this purpose, a class "Chem_Species" is created to store the data and functions to compute the partial vapour pressures and the individual composition of species in binary phases.
# 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt



# In[2]:


class Chem_Species(object):
    
    def __init__(self, name='no name', P_satur=lambda T: null):
        self.name = name;
        self.P_satur = P_satur;
    
    # Compute the saturation pressure given the known temperature of 20 degrees Celsius
    def P_satur(self, T):
        raise Exception('P_satur() has not been defined for ' + self.name);
        
    
# Antoine coefficient referenced from Yaw's handbook 
act_Pp =  Chem_Species('Acetone',  lambda T: 10**(7.31414 - 1315.67/(T + 240.479)));
w_Pp   =  Chem_Species('Water',  lambda T: 10**(8.05573 - 1723.64/(T + 233.076)));
ipa_Pp =  Chem_Species('IPA',  lambda T: 10**(7.83056 - 1483.3/(T + 217.413)));


# In[3]:


T_sys = 20; # degree Celsius
P_sys = 1200; # mm Hg


S4_act_Pp = act_Pp.P_satur(T_sys); # Expected: 183.3057966039555
# name1 = act_Pp.name
print(S4_act_Pp);

S4_w_Pp = w_Pp.P_satur(T_sys); # Expected: 17.578005499499085
print(S4_w_Pp);

S4_ipa_Pp = ipa_Pp.P_satur(T_sys); # Expected: 38.2646426454334
print(S4_ipa_Pp);


# In[4]:


# Create a list of Vapour Pressure 
vp_S4 = [S4_act_Pp, S4_w_Pp, S4_ipa_Pp];
print(vp_S4)


# In[5]:


# Function to calculate the pressure ratio
def pressure_ratio(list_Pp, P_sys=1200):
    Pr_i = [];
    i = 0;
    while i < len(list_Pp):
        result = list_Pp[i] / P_sys;
        Pr_i.append(result);
        i += 1;
    return Pr_i;


# In[6]:


# Create a list of Composition of Species
composition_S4_i = [0.376, 0.206, 0.0417];

Pp_i = pressure_ratio(vp_S4)
print(Pp_i);


# In[7]:


def calcuate_composition(list_com, list_Pr):
    
    X_i = [];
    Y_i = [];
    i = 0;
    while i < len(list_com):
        x_result = list_com[i] / (1 + list_Pr[i]);
        y_result = list_com[i] - x_result;
        X_i.append(round(x_result, 5));
        Y_i.append(round(y_result, 5));
        i += 1;
    return X_i, Y_i;


# In[16]:


X_S4, Y_S4 = calcuate_composition(composition_S4_i, Pp_i  )


# In[17]:


print(f" X_S4 \tX_act \tX_w \tX_ipa\n\t{X_S4} \n\n Y_S4 \tY_act \tY_w \tY_ipa\n\t{Y_S4} ")


# In[18]:


hydrogen_composition = 1 - composition_S4_i[0] - composition_S4_i[1] - composition_S4_i[2]


# In[19]:


print(f"\nY_S4_Hydrogen is: {hydrogen_composition}");


# In[20]:

# For purposes of checking
hydrogen_composition1 = 1 - X_S4[0] - X_S4[1] - X_S4[2] - Y_S4[0] - Y_S4[1] - Y_S4[2]
check = hydrogen_composition - hydrogen_composition1;
if check != 0:
    print("Error in Calculation");



