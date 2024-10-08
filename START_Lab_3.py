
def lab3Question1(number, cutoff):
    # Take in two arguments - a number and a 'cutoff' (another number)
    # Return True if the number is less than the cutoff, False otherwise
    # Also, print a statement of "[Number] is less than [cutoff]" or "[Number] is not less than [cutoff]"
    # Where the [Number] and [cutoff] are the actual numbers passed in
    
    if number >= cutoff:
        return False
    if number <cutoff:
        return True
    else:
        return False
   
number = input('Enter frst number:  ')
print(number)
cutoff = input('Enter second number: ')
print(cutoff)
if lab3Question1(number, cutoff)== True:   
    print(number, " is less than ", cutoff)
else:
    print(number, " is not less than ", cutoff) 


def lab3Question2(decimal_number):
    # Take in an argument of a float (decimal) number.
    # Return "zero" if the number is 0, "positive" if the number is positive, and "negative" if the number is negative
    # Return "invalid" if the input is not a float

    
    if decimal_number == 0:
        return( "zero")
    elif decimal_number > 0:
        return( "positive")
    elif decimal_number < 0:
         return( "negative")
    else:
        if decimal_number != float():
         return ("invalid")

decimal_number = float(input("Enter a number:  "))
print(decimal_number) 
print(lab3Question2(decimal_number))  
      

def lab3Question3(year):
    # Take in a number that represents a year
    # Return "21st century" if the year is between 2001 and 2100,
    # "20th century" if the year is between 1901 and 2000,
    # "19th century" if the year is between 1801 and 1900, 
    # "ancient" if the year is older
    # "invalid" if the input is not an acceptable year number. 
        
    if year in range(2001, 2100):
        print("21st century")
    elif year in range(1901, 2000):
        print("20st century")
    elif year in range(1801, 1900):
        print("19th century") 
    elif year < 1800:
        print("19th century")  
    else:
        print( "invalid") 

year = int(input('Enter a year:  '))
print(lab3Question3(year))         

def lab3Question4(number_1, number_2, number_3):
    # Take in three numbers as arguments
    # Return the largest of the three numbers
    # Return None if the inputs are not 3 numbers
        
    if number_1 is int and number_2 is int and number_3 is int:  
       return max(number_1, number_2, number_3)
    else:
        return None
           
number_1 = input('Enter the first number:  ')
number_2 = input('Enter the second number:  ')
number_3 = input('Enter the third number:  ')  
    
print (lab3Question4(number_1, number_2, number_3)) 


def lab3Question5(temperature, scale_used):
    # Take in a temperature and the scale that the temperature is in - either "C" for Celsius or "F" for Fahrenheit (capitalized)
    # Return "Liquid" if water is in liquid state at that temperature
    # Return "Solid" if water is in solid state at that temperature
    # Return "Gas" if water is in gas state at that temperature
    # Return "Invalid" if the temperature or scale are invalid
    #
    if scale_used == "C":
        if temperature >= 0 and temperature <100:
         return ("Liquid")
        elif temperature >=100:
            return ("Gas")
        elif temperature<0:
            return ("Solid")
        else:
            return ("Invalid")
    else:
        if temperature >= 32 and temperature <212:
         return ("Liquid")
        elif temperature >=212:
            return ("Gas")
        elif temperature<32:
            return ("Solid")
        else:
            return ("Invalid")
    
scale_used = input("Enter 'C' for Celsius or 'F' for Fahrenheit (capitalized):  ")
print(scale_used)   
temperature = int(input("Enter the degrees :"  ))  
print(temperature)
print(lab3Question5(temperature, scale_used))   


