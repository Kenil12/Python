# Codded by  Kenil Chovatiya



# defingin the function for Fahrenheit to Celsius
def conv_to_celsius(f):
    cel = 5*(f-32)/9 # formula for conversion
    cel = round(cel) # rounding it to nearest integer
    return cel
    
def main():
    temrature = input("Enter the temrature in Fahrenheit: ")
    temp = int(temrature) 
    celsius = conv_to_celsius(temp) # calling function for conversion
    print(temp," Fahrenheit = ", celsius," Celsius") # printing the final output

if __name__ == "__main__":
    main() # calling main function