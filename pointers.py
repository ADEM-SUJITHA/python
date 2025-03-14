# Importing ctypes module 
import ctypes as ct 
  
# creating a ctypes float variable 
float_value = ct.c_float(15.25) 
  
# creating a ctypes double variable 
double_value = ct.c_double(85.69845) 
  
# printing what float_value and double_value variable holds 
print(float_value,double_value) 
  
# printing the values stored inside float_value and double_value variable 
print(float_value.value,double_value.value)