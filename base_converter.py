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
    pass #Needs to be coded



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
        print(converted_num)

    else:
        print("\nThe input",input_number,"was not a valid input for base",source_base+".","Please enter a valid number.\n")


    print("Do you wish to contuinue with other numbers? ")
    print("Enter (Y) to contiue")
    print("Enter (N to quit)")
    print("Hello")

    wish_to_continue = input("Your Choice: ")

    if(wish_to_continue == "Y"):
        pass #do nothing as the continue_choice variable is already set to true

    else:
        continue_choice = False


print("Quitting calculator... Thank you!!!")




 



