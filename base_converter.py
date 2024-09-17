import math

def ValidateInput(input_number, source_base):
    #Checks base and assigns valid digits depending on said base
    if (source_base == "2"):
        validDigits = ("0", "1")
    
    elif (source_base == "10"):
        try:
            float(input_number)

        except(ValueError):
            return False
        
        return True
            
    
    elif (source_base == "16"):
        validDigits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F")
    
    #this is to handle invalid base input, can be modified as error will not notify the user of this specific case
    else:
        return False
    
    #goes through each digit to verify, returns True or False depending on validity
    for digit in input_number:
        if (digit not in validDigits):
            return False
    return True

def convert_number(input_number,source_base,target_base):
    if(target_base == "2"):
        pass

    
    if(target_base == "10"): #If the user wants to convert to decimal 
        num_list = list(input_number) #Split the user input into a list
        iteration = len(num_list) - 1 # This is the power the source base will be raised to 
        hex_replacement = {'A': 10, 'B': 11, 'C': 12,'D':13,'E':14,'F':15} # DIctionary to map hex values
        result = 0 # Variable to store result

        for num in num_list:
            if(num in hex_replacement):
                num = hex_replacement[num] # If the character being iterated over is a hex letter it is mapped to its number value

            result += float(num) * math.pow(int(source_base), iteration) # Converstion from binary to decimal or Hex to decimal
            iteration -= 1 #Subtracting by one as the code is solving it from left to right

        return result 
    

    if(target_base == "16"):
        pass



print("Number Base Converter")
print("\n This progam will easily convert betwwen Deicmal, Binary and Hexadecimal numbers.")
print("\n Please enter the following inputs: ")


continue_choice = True


while(continue_choice != False):

    input_number = input("\nThe number to convert: ")
    source_base = input("\ni.e, the base to convert from: ")
    target_base = input("\ni,e, the base to convert to: ")

    Validated = ValidateInput(input_number, source_base) #Will return true or false depending on if the input is validated

    if(Validated == True):
        print("\nInput Number Was Validated\n")
        converted_num = convert_number(input_number,source_base,target_base)
        print("\nThe result is:",converted_num)

    else:
        print("\nThe input",input_number,"was not a valid input for base",source_base+".","Please enter a valid number.\n")


    print("\nDo you wish to contuinue with other numbers? ")
    print("Enter (Y) to contiue")
    print("Enter (N to quit)")


    wish_to_continue = input("\nYour Choice: ")

    if(wish_to_continue == "Y"):
        pass #do nothing as the continue_choice variable is already set to true

    else:
        continue_choice = False


print("\nQuitting calculator... Thank you!!!\n")




 



