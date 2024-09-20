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
        try:
            input_number = float(input_number) #Convert to integer and if successful then we continue 
            result_list = [] #Empty list to store the values of the result but will be backwrds
            comp1 = [] #First compliments empty list
            result = "" #Empty string to store the final result in the correct order
            bin_replacement = {'1': '0', '0':'1','1.0':'0','0.0':'1'} # Dictionary to change binary values for the 1st compliment
            negative = False #Variable to check if we have a negative number initialized to false
           

            if(input_number < 0):
                negative = True
                input_number = input_number * -1
            

            while(input_number != 0): 
                rem = input_number%2 # Getting the remanider and storing it in rem
                result_list.append(str(rem)) # Storing the remainder as a string in the result list
                input_number = math.floor(input_number/2) #Dividing the number by 2 and flooring it to ensure there are no decimals 

    
            result_list = result_list[::-1] # Reversing the order of the list
            print("bin value",result_list)

            if(negative == True): #if we have a negative number
                for num in result_list:
                    num = bin_replacement[num] #Going through each element and swaping the 0 with 1 and 1 wiht 0 for the first compliment 
                    comp1.append(num)
                print("1st compliment",comp1)
                max_index = len(comp1)-1 #finding the max index number of the list

                while(max_index >= 0): #Startting from the max index which is the element on the far right and checking if it is a 0 if so then we swap to 1n and break the loop else we contiunue till we find one
                    print("in loop",max_index)
                    if(comp1[max_index]== "0"):
                        comp1[max_index] = "1"
                        break

                    max_index -= 1 # Decreasing so we can move through the elements from right to left
                print("second comp",comp1)
                
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
    

    if(target_base == "16"):
        input_number_backup = input_number
        input_number = list(input_number)
        length_of_list = len(input_number)
        num_of_one = input_number.count('1')
        num_of_zero = input_number.count('0')
        result = ""
        binary_to_hex_replacement = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', 
                                     '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
        

        if(source_base == "2"):
            #code for binary 
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
                    input_number.insert(0,0)
                    zero_add -= 1

            elif(length_of_list % 4 == 2):
                zero_add = 2
                while(zero_add != 0):
                    input_number.insert(0,0)
                    zero_add -= 1

            else:# if the remainder is 3
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
        
            return result


        else:
            input_number = input_number_backup
            input_number = float(input_number) #Convert to integer and if successful then we continue 
            result_list = [] #Empty list to store the values of the result but will be backwrds
            result = "" #Empty string to store the final result in the correct order
            deci_replacement = {'10.0':'A', "11.0":'B','12.0':'C','13.0':'D','14.0':'E','15.0':'F'} # Dictionary to map decimal values to hex


            while(input_number != 0): 
                rem = input_number%16 # Getting the remanider and storing it in rem
                result_list.append(str(rem)) # Storing the remainder as a string in the result list
                input_number = math.floor(input_number/16) #Dividing the number by 2 and flooring it to ensure there are no decimals 

            result_list = result_list[::-1]


            for num in result_list:
                if(num in deci_replacement):
                    num = deci_replacement[num]
                else:
                    num = str(int(float(num)))
                
                result += num
            
            return result



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




 



