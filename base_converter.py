def ValidateInput(input_number, source_base):
    pass #Needs to be coded 

def convert_number(input_number,source_base,target_base):
    pass #Needs to be coded lol just testing




print("Number Base Converter")
print("\nThis progam will easily convert betwwen Deicmal, Binary and Hexadecimal numbers.")
print("\nPlease enter the following inputs: ")


continue_choice = True


while(continue_choice != False):

    input_number = input("\nThe number to convert: ")
    source_base = input("\ni.e, the base to convert from: ")
    target_base = input("\ni,e, the base to convert to: ")

    Validated = ValidateInput(input_number, source_base) #Will return true or false depending on if the input is validated

    if(Validated == True):
        converted_num = convert_number(input_number,source_base,target_base)
        print(converted_num)

    else:
        print("The input",input_number,"was not a valid input for base",source_base+".","Please enter a valid number.")


    print("Do you wish to contuinue with other numbers? ")
    print("Enter (Y) to contiue")
    print("Enter (N to quit)")

    wish_to_continue = input("Your Choice: ")

    if(wish_to_continue == "Y"):
        pass #do nothing as the continue_choice variable is already set to true

    else:
        continue_choice = False


print("Quitting calculator... Thank you!!!")




 



