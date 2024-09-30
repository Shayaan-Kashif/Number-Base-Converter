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
    if (source_base == "10"):
        input_number_list = list(input_number) #keeps a list of the number in case of fractional
        input_number = int(float(input_number)) #Convert to integer and if successful then we continue 
        result_list = [] #Empty list to store the values of the result but will be backwrds
        comp1 = [] #First compliments empty list
        result = "" #Empty string to store the final result in the correct order
        bin_replacement = {'1': '0', '0':'1','1.0':'0','0.0':'1'} # Dictionary to change binary values for the 1st compliment
        negative = False #Variable to check if we have a negative number initialized to false
        fractional_check = input_number_list.count(".") #checks for a dot which will trigger a fraction operation
        fractional_binary = ""

        if(fractional_check == 1):
            #gets the location of the dot and keeps only fractional part
            dot_index = input_number_list.index(".")
            fractional_part = input_number_list[dot_index :]
            fractional_part = float("0" + "".join(fractional_part))
            counter = 0 #counts only up to 5 as it is the requested accuracy
            fractional_binary = ""
            while (True):
                complete_new_fraction = fractional_part * 2 #gets a new number, whole part will be added to fractional_binary string and fractional part goes back into loop
                fractional_binary += str(int(complete_new_fraction))
                complete_new_fraction_list = list(str(complete_new_fraction)) #cast to a list for manipulation
                complete_new_fraction_list[0] = "0" #makes sure first digit is a 0
                fractional_part = float("".join(complete_new_fraction_list))
                counter += 1
                if (counter > 4 or fractional_part == 0):
                    break
        
        #Checks if the number is negative
        if(input_number < 0):
            negative = True
            input_number = input_number * -1
        

        while(True): 
            rem = input_number%2 # Getting the remanider and storing it in rem
            result_list.append(str(rem)) # Storing the remainder as a string in the result list
            input_number = math.floor(input_number/2) #Dividing the number by 2 and flooring it to ensure there are no decimals 
            if (input_number == 0):
                break


        result_list = result_list[::-1] # Reversing the order of the list


        if(negative == True): #if we have a negative number
            result = "" #stores final result of calculations

            if (len(result_list) < 8): #makes the current number 8 bits for 2's compliment
                while(len(result_list) != 8):
                    result_list.insert(0, "0")
            elif (len(result_list) < 16): #makes the number 16 bit if bigger than 8 bits for 2's compliment.
                while(len(result_list) != 16): 
                    result_list.insert(0, "0")
            else: #if bigger, 2's compliment will be of integer size in + 1
                result = "1" #negative numbers always start with 1, when bigger then 16, just add 1

            result_list = result_list + list(fractional_binary) #adds fracional part to be added if applicable
            for num in result_list:
                num = bin_replacement[num] #Going through each element and swaping the 0 with 1 and 1 wiht 0 for the first compliment 
                comp1.append(num)

            max_index = len(comp1)-1 #finding the max index number of the list


            while(max_index >= 0): #Startting from the max index which is the element on the far right and checking if it is a 0 if so then we swap to 1n and break the loop else we contiunue till we find one

                if(comp1[max_index]== "1"):
                    comp1[max_index] = "0"
                    
                elif(comp1[max_index]=="0"):
                    comp1[max_index] = "1"
                    break

                max_index -= 1 # Decreasing so we can move through the elements from right to left

            
            if (fractional_binary != ""):
                dot_index = len(comp1) - len(fractional_binary)
                comp1.insert(dot_index, ".")

            for num in comp1:
                result += num #Joining into a string 
            return result  #The result is returned 

            
        #If the number is positive
        else:
            for num in result_list:
                result += num #Iterating over the correct order list and storing the result as a single string in result 
            if (fractional_binary !=""):
                return result + "." + fractional_binary #The result is returned
            else:
                return result 
              


    else:
        hex_to_binary_replacement = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001',
                                        'A': '1010', 'B': '1011', 'C': '1100','D':'1101','E':'1110','F':'1111', '.':'.'} #Dictionary to map the hex values to their corresponding binary values
        hex_list = list(input_number) # Turning the users input into a list
        result = "" #Empty string to store the result 

        for hex in hex_list: #iterating over the list 
            hex = hex_to_binary_replacement[hex] #For each value in the users list it is mapped to its binary value 
            result += hex # the mapped value is joined into a string
        
        return result #The binary result is returned  
    
    


def convert_number(input_number,source_base,target_base):

    #If the user wishes to convert from either decimal or hex to binary 
    if(target_base == "2"):
        result = to_binary(input_number,source_base,target_base) #calling the to binary funtion to convert the number to binary
        return result #returning the result 


    if(target_base == "10"): #If the user wants to convert to decimal 
        num_list = list(input_number) #Split the user input into a list
        fractional_check = num_list.count(".")
        iteration = len(num_list) - 1 # This is the power the source base will be raised to 
        hex_replacement = {'A': 10, 'B': 11, 'C': 12,'D':13,'E':14,'F':15} # Dictionary to map hex values
        result1 = 0 # Variable to store result
        result2 = 0
      

        if(fractional_check == 1):
            dot_index = num_list.index(".")

            whole_num = num_list[:dot_index] #To store the whole number if a floating point is entered
            fractional_num = num_list[(dot_index + 1):] #To store the fractional part if a floating point is entered

            iteration = len(whole_num)-1

            for num in whole_num:
                if(num in hex_replacement):
                    num = hex_replacement[num] # If the character being iterated over is a hex letter it is mapped to its number value

                result1 += float(num) * math.pow(int(source_base), iteration) # Converstion from binary to decimal or Hex to decimal
                iteration -= 1 #Subtracting by one as the code is solving it from left to right

            result1 = str(result1)

            result1 = result1[:len(result1)-2]


            iteration = -1
            for num in fractional_num:
                if(num in hex_replacement):
                    num = hex_replacement[num] # If the character being iterated over is a hex letter it is mapped to its number value

                result2 += float(num) * math.pow(int(source_base), iteration) # Converstion from binary to decimal or Hex to decimal
                iteration -= 1 #Subtracting by one as the code is solving it from left to right

            result2 = str(result2)
            result2 = result2[2:]

            result = result1+"."+result2

            return result
        
        #If input num is not a floating-point number
        else:
            result = 0
            for num in num_list:
                if(num in hex_replacement):
                    num = hex_replacement[num] # If the character being iterated over is a hex letter it is mapped to its number value
            
                result += int(float(num) * math.pow(int(source_base), iteration)) # Converstion from binary to decimal or Hex to decimal
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
        fractional_check = input_number.count(".")
        fractional_hex = "" #sets blank as a placeholder incase no fractional is given

        if(input_number_backup == "0"):
            return("0")

        if(input_number[0]=="-"): #Checking if the first character is a "-" which means the input is negative 
            input_number = input_number_backup #getting the original users input and re assigning to input_value
            input_number = to_binary(input_number, source_base, 2) #seding the negaive number to be converted to binary. THis will return the second compliment
            input_number = list(input_number) #TUnrnign the result into a list 
            length_of_list = len(input_number) #finding the new length of the list
            adjusted_source_base = True # Setting the adjusted base to true since the users original source base was 10
        
        if (fractional_check == 1): #checks if the number contains a decimal point
            input_number_binary = input_number #makes a backup of the original number
            dot_index = input_number.index(".") #get index of dot to split number
            input_number_backup = "".join(input_number[:dot_index]) #get the whole part without fraction for the decimal part of the program to manage
            length_of_list = len(input_number[:dot_index])  #gets new length since we removed the fractional part
            input_number = input_number[:dot_index] #new list without dot or fractional part for the binary part to manage

            if (source_base == "10" and adjusted_source_base == False): #if source base is 10, convert to binary to make managing easier
                input_number_binary = to_binary("".join(input_number_binary), source_base, 2)
            input_number_binary = list(input_number_binary) #turns string back into list
            dot_index = input_number_binary.index(".") #gets new dot index of binary number
            fractional_part = input_number_binary[(dot_index + 1) :] #get the fractional part
            length_of_fractional_part = len(fractional_part) #length of fractional part for padding
            placeholder = ""
            zero_add = 0

            if (length_of_fractional_part % 4 == 1): #add zeros depending on modulo, explanation in paragraph below
                zero_add = 3
            elif (length_of_fractional_part % 4 == 2):
                zero_add = 2
            elif (length_of_fractional_part % 4 == 3):
                zero_add = 1


            while(zero_add != 0): #adds required zeros to split into proper hex
                    fractional_part.append("0")
                    zero_add -= 1

            count = 0
            for num in fractional_part: #groups 4 bits together and then converts them to binary
                placeholder += num
                count += 1
                if (count == 4):
                    fractional_hex += binary_to_hex_replacement[placeholder]
                    count = 0
                    placeholder = ""
        
        #If the users source base is 2 or if the adjusted base is true the following code will execute 
        if(source_base == "2" or adjusted_source_base == True):
            """
            The code below checks to see if the binary number can be broken down into groups of 4 bits. 
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
                if(fractional_check == 0):
                    return result
                else:
                    return result + "." + fractional_hex

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

            if (fractional_hex != ""):
                return result + "." + fractional_hex #Returning the result
            else:
                return result

            


        else: #Handles conversions of base 10 to base 16
            input_number = input_number_backup #Recalling the backup number 
            input_number = int(input_number) #Convert to integer and if successful then we continue 
            result_list = [] #Empty list to store the values of the result but will be backwrds
            result = "" #Empty string to store the final result in the correct order
            deci_replacement = {'10':'A', "11":'B','12':'C','13':'D','14':'E','15':'F'} # Dictionary to map decimal values to hex


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
            
            if (fractional_hex != ""):
                return result + "." + fractional_hex #Returning the result
            else:
                return result   



print("\n----Number Base Converter---")
print("\nThis progam will easily convert between Deicmal, Binary and Hexadecimal numbers.")
print("\nInstructions:\n1. Enter the number you'd like to convert\n2. Enter the base you would like to convert from\n3. Enter the base you want to convert to\n4. You can exit anytime by entering the command \"-Exit\" or by entering \"N\" after a conversion")
print("\n\nPlease enter the following inputs: ")


continue_choice = True
exit_choice = False



while(continue_choice != False or exit_choice == True):

    choice_left = ["2","10","16"]

    input_number = input("\nPlease enter the number to convert: ")

    input_test = list(input_number)

    while(input_test.count(" ") == len(input_test)):
        print("\nYou cannot convert nothing. Please enter a number to convert.")
        input_number = input("\nPlease enter the number to convert: ")
        input_test = list(input_number)

    if(input_number == "-Exit"):
        exit_choice == True
        break

    source_base = input("\nPlease enter the base to convert from: ")

    if(source_base == "-Exit"):
        exit_choice == True
        break

    while(source_base != "2" and source_base !="10" and source_base != "16"):
        print("We do not support converting from that base.")
        source_base = input("\nPlease enter the base to convert from: ")

    
    Validated = ValidateInput(input_number, source_base) #Will return true or false depending on if the input is validated

    while(Validated == False or input_number == " -Exit"):
        print("\nThe input",input_number,"was not a valid input for base",source_base+".","Please enter a valid number.\n")
        input_number = input("\nPlease enter another valid number to convert to: ")

        if(input_number == "-Exit"):
            exit_choice == True
            break

        Validated = ValidateInput(input_number, source_base) #Will return true or false depending on if the input is validated
       
    if(input_number == "-Exit"):
        exit_choice == True
        break

    target_base = input("\nPlease enter the base to convert to: ")
    if(target_base == "-Exit"):
        exit_choice == True
        break

   
    
    index = choice_left.index(source_base)

    choice_left.pop(index)

    while(target_base not in choice_left):
        while(target_base == source_base):
            print("You cannot convert between same bases As there is no change from the input number.")
            print("You can pick between:",choice_left[0],"or",choice_left[1])

            target_base = input("\nPlease enter the base to convert to: ")
            if(target_base == "-Exit"):
                exit_choice == True
                break



        if(target_base != source_base and target_base not in choice_left):
            print("target and source not equal")
            print("We do not convert to that base.")
            print("Your choices avalible are:",choice_left[0],"and",choice_left[1])
            
            target_base = input("\nPlease enter the base to convert to: ")
            if(target_base == "-Exit"):
                exit_choice == True
                break



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
        print("Enter (N) to quit")

        wish_to_continue = input("Your Choice: ")


       
    if(wish_to_continue == "Y" or wish_to_continue == "y"):
        pass #do nothing as the continue_choice variable is already set to true

    else:
        continue_choice = False

   


print("\nQuitting calculator... Thank you!!!\n")




 



