import math

def ValidateInput(input_number, source_base):
    #Checks base and assigns valid digits depending on said base
    if (source_base == "2"):
        validDigits = ("0", "1", ".", "x")
    
    elif (source_base == "10"):
        try:
            float(input_number)

        except(ValueError):
            return False
        
        return True
            
    
    elif (source_base == "16"):
        validDigits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", ".", "x")
    
    #this is to handle invalid base input, can be modified as error will not notify the user of this specific case
    else:
        return False
    
    #goes through each digit to verify, returns True or False depending on validity
    for digit in input_number:
        if (digit not in validDigits):
            return False
    return True



def to_binary(input_number, source_base, target_base):
    try:
        input_number = float(input_number) #Convert to integer and if successful then we continue 
        result_list = [] #Empty list to store the values of the result but will be backwrds
        comp1 = [] #First compliments empty list
        result = "" #Empty string to store the final result in the correct order
        bin_replacement = {'1': '0', '0':'1','1.0':'0','0.0':'1'} # Dictionary to change binary values for the 1st compliment
        negative = False #Variable to check if we have a negative number initialized to false
        
        #Checks if the number is negative
        if(input_number < 0):
            negative = True
            input_number = input_number * -1
        

        while(input_number != 0): 
            rem = input_number%2 # Getting the remanider and storing it in rem
            result_list.append(str(rem)) # Storing the remainder as a string in the result list
            input_number = math.floor(input_number/2) #Dividing the number by 2 and flooring it to ensure there are no decimals 


        result_list = result_list[::-1] # Reversing the order of the list


        if(negative == True): #if we have a negative number
            for num in result_list:
                num = bin_replacement[num] #Going through each element and swaping the 0 with 1 and 1 wiht 0 for the first compliment 
                comp1.append(num)

            max_index = len(comp1)-1 #finding the max index number of the list

            while(max_index >= 0): #Startting from the max index which is the element on the far right and checking if it is a 0 if so then we swap to 1n and break the loop else we contiunue till we find one

                if(comp1[max_index]== "0"):
                    comp1[max_index] = "1"
                    break

                max_index -= 1 # Decreasing so we can move through the elements from right to left

            
            result = "1" #negative numbers always start with 1
            for num in comp1:
                result += num #Joining into a string 


            return result #The result is returned 
            

        else:
            for num in result_list:
                result += num #Iterating over the correct order list and storing the result as a single string in result 

            return result #The result is returned 


    except(ValueError):
        hex_to_binary_replacement = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001',
                                        'A': '1010', 'B': '1011', 'C': '1100','D':'1101','E':'1110','F':'1111'} #Dictionary to map the hex values to their corresponding binary values
        hex_list = list(input_number) # Turning the users input into a list
        result = "" #Empty string to store the result 

        for hex in hex_list: #iterating over the list 
            hex = hex_to_binary_replacement[hex] #For each value in the users list it is mapped to its binary value 
            result += hex # the mapped value is joined into a string
        
        return result #The result is returned 
    
    


def convert_number(input_number,source_base,target_base):

    #If the user wishes to convert from either decimal or hex to binary 
    if(target_base == "2"):
        result = to_binary(input_number,source_base,target_base) #calling the to binary funtion to convert the number to binary
        return result #returning the result 


    if(target_base == "10"): #If the user wants to convert to decimal 
        num_list = list(input_number) #Split the user input into a list
        iteration = len(num_list) - 1 # This is the power the source base will be raised to 
        hex_replacement = {'A': 10, 'B': 11, 'C': 12,'D':13,'E':14,'F':15} # Dictionary to map hex values
        result = 0 # Variable to store result

        for num in num_list:
            if(num in hex_replacement):
                num = hex_replacement[num] # If the character being iterated over is a hex letter it is mapped to its number value

            result += float(num) * math.pow(int(source_base), iteration) # Converstion from binary to decimal or Hex to decimal
            iteration -= 1 #Subtracting by one as the code is solving it from left to right

        return result #The result is returned 
    
    #If the user wishes to convert to hex
    if(target_base == "16"):
        input_number_backup = input_number #Sorting the users input into a backup variable to preserve the original input for later use
        input_number = list(input_number) #tunring the input into a list 
        length_of_list = len(input_number) # Finding the length of the list as it will be used later
        adjusted_source_base = False #This varaible will be used to route to the binary if statment 
        result = ""
        binary_to_hex_replacement = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', 
                                     '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
        
        if(input_number[0]=="-"): #Checking if the first character is a "-" which means the input is negative 
            input_number = input_number_backup #getting the original users input and re assigning to input_value
            input_number = to_binary(input_number, source_base, 2) #seding the negaive number to be converted to binary. THis will return the second compliment
            input_number = list(input_number) #TUnrnign the result into a list 
            length_of_list = len(input_number) #finding the new length of the list
            adjusted_source_base = True # Setting the adjusted base to true since the users original source base was 10
        
        #If the users source base is 2 or if the adjusted base is true the following code will execute 
        if(source_base == "2" or adjusted_source_base == True):

            """
            The code below checks to see if the binary numb er can be broken down into groups of 4 bits. 
            If it cannot then it will find the remainder. The remandier value will be 0 if it can be broken down into 
            bits of 4. And it will be either 1,2 or 3 if the binary number cannot be broken into 4 bits. if the remandier is 1
            that means 2 numbers either 00 or 11 have to be added to the start of the list in order to ensure it can be broken into 
            4 bits. Two 00 are added if the number is positive and two 11 are added if it is negative.
            """
            if(length_of_list % 4== 0):
                count = 0
                placeholder = ""
                for num in input_number: #Loop where the conversion will take place
                    placeholder += num

                    if(count == 3):
                        result += binary_to_hex_replacement[placeholder]
                        placeholder = ""
                        count = -1

                    count += 1
                
                return result

            elif(length_of_list % 4 == 1):
                zero_add = 3
                while(zero_add != 0):
                    if(adjusted_source_base == True):
                        input_number.insert(0,1)
                    else:
                        input_number.insert(0,0)

                    zero_add -= 1

            elif(length_of_list % 4 == 2):
                zero_add = 2
                while(zero_add != 0):
                    if(adjusted_source_base == True):
                        input_number.insert(0,1)
                        
                    else:
                        input_number.insert(0,0)
                    
                    zero_add -= 1

            else:# if the remainder is 3
                if(adjusted_source_base == True):
                    input_number.insert(0,1)
                else:
                    input_number.insert(0,0)


            count = 0
            placeholder = ""
            for num in input_number: #Loop where the conversion will take place
                placeholder += str(num)

                if(count == 3):
                    result += binary_to_hex_replacement[placeholder]
                    placeholder = ""
                    count = -1

                count += 1
        
            return result #Returning the result


        else: #Handles conversions of base 10 to base 16
            input_number = input_number_backup #Recalling the backup number 
            input_number = float(input_number) #Convert to integer and if successful then we continue 
            result_list = [] #Empty list to store the values of the result but will be backwrds
            result = "" #Empty string to store the final result in the correct order
            deci_replacement = {'10.0':'A', "11.0":'B','12.0':'C','13.0':'D','14.0':'E','15.0':'F'} # Dictionary to map decimal values to hex


            while(input_number != 0): 
                rem = input_number%16 # Getting the remanider and storing it in rem
                result_list.append(str(rem)) # Storing the remainder as a string in the result list
                input_number = math.floor(input_number/16) #Dividing the number by 2 and flooring it to ensure there are no decimals 

            result_list = result_list[::-1] #Reversing the list


            for num in result_list:
                #Iterating overt the list to check if the current element is in the dictionary and if it is then we swap the value of the varaible to the value for the key
                if(num in deci_replacement):
                    num = deci_replacement[num]
                else:
                    num = str(int(float(num))) #num is multi casted. It is first casted to float then into int and then into string
                
                result += num # Adding the string value of num into the result 
            
            return result #Returning the result 



print("Number Base Converter")
print("\nThis progam will easily convert betwwen Deicmal, Binary and Hexadecimal numbers.")
print("\nPlease enter the following inputs: ")


continue_choice = True



while(continue_choice != False):

    choice_left = ["2","10","16"]

    input_number = input("\nPlease enter the number to convert: ")
    source_base = input("\nPlease enter the base to convert from: ")

    while(source_base != "2" and source_base !="10" and source_base != "16"):
        print("We do not support converting from that base.")
        source_base = input("\nPlease enter the base to convert from: ")

    target_base = input("\nPlease enter the base to convert to: ")

   
    
    index = choice_left.index(source_base)

    choice_left.pop(index)

    while(target_base not in choice_left):
        while(target_base == source_base):
            print("You cannot convert between same bases As there is no change from the input number.")
            print("You can pick between:",choice_left[0],"or",choice_left[1])

            target_base = input("\nPlease enter the base to convert to: ")


        if(target_base != source_base and target_base not in choice_left):
            print("target and source not equal")
            print("We do not convert to that base.")
            print("Your choices avalible are:",choice_left[0],"and",choice_left[1])
            
            target_base = input("\nPlease enter the base to convert to: ")

    Validated = ValidateInput(input_number, source_base) #Will return true or false depending on if the input is validated

    while(Validated == False):
        print("\nThe input",input_number,"was not a valid input for base",source_base+".","Please enter a valid number.\n")
        input_number = input("\nPlease enter the number to convert: ")
        Validated = ValidateInput(input_number, source_base) #Will return true or false depending on if the input is validated
       


    print("\nInput Number Was Validated\n")
    converted_num = convert_number(input_number,source_base,target_base)
    print("\nThe result is:",converted_num)

    print("\nDo you wish to contuinue with other numbers? ")
    print("Enter (Y) to contiue")
    print("Enter (N to quit)")


    wish_to_continue = input("\nYour Choice: ")

    while(wish_to_continue != "Y" and wish_to_continue != "y" and wish_to_continue != "N" and wish_to_continue != "n"):
        print("\nYou entered an invalid choice. Please try again.")
        print("\n\nDo you wish to contuinue with other numbers? ")
        print("Enter (Y) to contiue")
        print("Enter (N to quit)")

        wish_to_continue = input("Your Choice: ")


       
    if(wish_to_continue == "Y" or wish_to_continue == "y"):
        pass #do nothing as the continue_choice variable is already set to true

    else:
        continue_choice = False

   


print("\nQuitting calculator... Thank you!!!\n")




 



