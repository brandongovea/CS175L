def main():
    controlLoop()

def convertToKelvin(Fahrenheit):
    #Take in the fahrenheit temp as an argument
    #Convert Fahrenheit to Kelvin
    Kelvin = (Fahrenheit - 32) * 5 / 9 + 273.15
    
    #return Kelvin
    return Kelvin

    pass

def convertToCentigrade(Fahrenheit):
    #Take in the fahrenheit temp as an argument
    #Convert Fahrenheit to Centigrade
    Centigrade = (Fahrenheit - 32) * 5 / 9
    
    #return Centigrade
    return Centigrade

    pass

def doConversion():
    #getFahrenheit(), get back Fahrenheit
    Fahrenheit = getFahrenheit()
    
    #convertToKelvin(), send Fahrenheit get back Kelvin
    Kelvin = convertToKelvin(Fahrenheit)

    #ConvertToCentigrade, sends Fahrenheit gets back Centigrade
    Centigrade = convertToCentigrade(Fahrenheit)
    
    #prints for example: 'Fahrenheit: xx Kelvin xx Centigrade: xx'
    print(f'Fahrenheit: {Fahrenheit} Kelvin: {Kelvin} Centigrade: {Centigrade}')
          
    pass

def repeat():
    #Inputs How many conversions would you like to do this time?
    conversion_amount = int(input("How many conversions would you like to do this time? "))
    
    #for x in range how many
        #doConversion()
    for x in range(conversion_amount):
        doConversion()

    pass

def controlLoop():
    #Inputs 'Do you want to do some conversions(Yes or No)?'
    conversion = input("Do you want to do some conversions (Yes or No) ")
    
    #if 'yes' repeat()
    if conversion == 'Yes':
        repeat()
        
    pass

def getFahrenheit():
    #Inputs 'Enter Fahrenheit temperature (must be -50 to 130):'
    Fahrenheit = int(input("Enter Fahrenheit temperature (must be -50 to 130): "))

    
    #(validation loop)'Please re-enter'
    while Fahrenheit < -50 or Fahrenheit > 130:
        print("Invalid Fahrenheit temperature! Must be -50 to 130")
        Fahrenheit = int(input("Enter Fahrenheit temperature (must be -50 to 130): "))

    
    #return Fahrenheit
    return Fahrenheit


# This code will call the 'main' function if the entire program was run.
if __name__ == '__main__':
    main()
