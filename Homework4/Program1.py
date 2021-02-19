def temp_converter(Tf):
    Tc = (5/9)*(Tf-32)
    return Tc

Tf = float(input('Enter temperature in Fahrenheit :')) 
print(temp_converter(Tf)) 