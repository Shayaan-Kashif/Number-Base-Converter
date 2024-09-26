import math

def ValidateInput(input_number, source_base):
    #Checks base and assigns valid digits depending on said base
    if (source_base == 2):
        validDigits = ("0", "1" , ".")
    
    elif (source_base == 10):
        try:
            float(input_number)

        except(ValueError):
            return False
        
        return True
            
    
    elif (source_base == 16):
        validDigits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", ".")
    
    #this is to handle invalid base input, can be modified as error will not notify the user of this specific case
    else:
        return False
    
    #goes through each digit to verify, returns True or False depending on validity
    for digit in input_number:
        if (digit not in validDigits):
            return False
    return True

def convert_number(input_number,source_base,target_base):
    result = [] #for int
    result_decimal = [] #for decimal


#since python has approximation with floating points, i will need to make binary as string value which should be the default of an input, note make decimal cast to float
    if source_base == 10:
        temp = float(input_number)
        input_number = temp
        input_number/=1 #make sure that it has decimal, whethir it be a whole number or not: ex 5 will become 5.0
        whole_number = math.modf(input_number)
        input_number = int(whole_number[1])
        decimal_number = (whole_number[0])
    
    else:
        whole_number = str(input_number).split(".")
        input_number = str(whole_number[0])
        if len(whole_number) == 1:
            decimal_number = "0" 
        else:
            decimal_number = str(whole_number[1])
        
        
    
    
    
    
    
    
    
   

    

    if source_base == 10 and target_base == 2: #decimal to binary

        if int(input_number)<2:
            result.append(input_number)
        while(int(int(input_number)/2) != 0):
            result.append(input_number%2)
            input_number = int(input_number/2)
            if(int(input_number/2) == 0):
                result.append(input_number%2)

        #fraction

       

        counter = 0
        while(decimal_number!=0.0) and (counter < 5):
            
            decimal_number = decimal_number*2
            carry = int(decimal_number)
            result_decimal.append(carry)

            decimal_number = decimal_number - carry
            counter+=1
            
        
        



            
            



            
        
        result.reverse()


       
        integer_part =""
        if len(result) == 0:
            integer_part = "0."

        result.append(".")

        for digit in result:
            integer_part+=str(digit)
        
        decimal_part = ""
        if len(result_decimal) == 0:
            decimal_part = "0"
        
        for digit in result_decimal:
            decimal_part+= str(digit)
        
        whole_number = integer_part+decimal_part

        
        


        
        return whole_number 
    
    elif source_base == 10 and target_base == 16: #decimal to hex
        if input_number < 16:
            result.append(input_number)
        
        while(int(input_number/16) != 0):
            result.append(input_number%16)
            input_number = int(input_number/16)
            if(int(input_number/16) == 0):
                result.append(input_number%16)
        

            
        result.reverse()

        
        

        alpha = {10:"A", 11:"B", 12:"C", 13:"D",14:"E", 15:"F"}

        for i in range(0,len(result)):
            if result[i]>9:
                result[i] = alpha[result[i]]


        #fraction
        

       

        counter = 0
        while(decimal_number!=0.0) and (counter < 5):
            
            decimal_number = decimal_number*16
            carry = int(decimal_number)
            result_decimal.append(carry)

            decimal_number = decimal_number - carry
            counter+=1
        

        for i in range(0,len(result_decimal)):
            if result_decimal[i] > 9:
                result_decimal[i] = alpha[result_decimal[i]]



        
        integer_part = ""
        decimal_part = ""

        if len(result) == 0:
            integer_part = "0."
        else:
            result.append(".")
            for digit in result:
                integer_part+= str(digit)
            
        if len(result_decimal) == 0:
            decimal_part = "0"
        else:
            for digit in result_decimal:
                decimal_part += str(digit)

        
            
        whole_number = integer_part + decimal_part

        
        



    
        
        
            
        

        
        return whole_number
    

    
    elif source_base == 2 and target_base == 10: # binary to decimal
        num = []
        for digit in input_number:
            num.append(int(digit))
        
        num.reverse()
        sum = 0

        for i in range(0,len(num)):
            sum+= (num[i])*2**i
        

        #for fraction
        sum_fraction = 0

        

        num_fraction = []
        for digit in decimal_number:
            num_fraction.append(int(digit))
        
        
        
        for i in range(0,len(num_fraction)):
            sum_fraction+= (num_fraction[i])*2**(-(i+1))

        





        
        return sum+ sum_fraction
    
    elif source_base == 16 and target_base == 10: #hex to decimal
        num = []
        alpha_reverse = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
        for digit in str(input_number):
            try:
                number = int(digit)
                num.append(number)
            except Exception as e:
                num.append(alpha_reverse[digit])
            
        num.reverse()

        sum = 0; 

        for i in range(0,len(num)):
            sum+= int(num[i])*16**i
        
        #for fraction
        num = []
        

        for digit in decimal_number:
            try: 
                number = int(digit)
                num.append(number)

            except Exception as e:
                num.append(alpha_reverse[digit])
        
        sum_decimal = 0
            
        for i in range(0,len(num)):
            sum_decimal += (int(num[i]))*16**(-(i+1))

        




        
        return sum+sum_decimal
    
    elif source_base == 16 and target_base == 2: #hex to binary--------------------------------------------------------------------------------------------------


        #first from hex to decimal
        num = []
        alpha_reverse = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
        for digit in str(input_number):
            try:
                number = int(digit)
                num.append(number)
            except Exception as e:
                num.append(alpha_reverse[digit])
            
        num.reverse()

        sum = 0 

        for i in range(0,len(num)):
            sum+= int(num[i])*16**i
        
        input_number = sum
        
        #then decimal to binary, all of which is code from previous else statements
        result = []

        if input_number<2:
            result.append(input_number)
        while(int(input_number/2) != 0):
            result.append(input_number%2)
            input_number = int(input_number/2)
            if(int(input_number/2) == 0):
                result.append(input_number%2)
            
        
        result.reverse()


        #fraction
        num = []
        for digit in decimal_number:
            try:
                number = int(digit)
                num.append(number)
            except Exception as e:
                num.append(alpha_reverse[digit])
        
        sum_decimal=0

        for i in range(0,len(num)):
            sum_decimal += (int(num[i]))*16**(-(i+1))

        decimal_number = sum_decimal
        result_decimal = []
        counter = 0
    
        while(decimal_number!=0.0) and (counter < 5):
            
            decimal_number = decimal_number*2
            carry = int(decimal_number)
            result_decimal.append(carry)

            decimal_number = decimal_number - carry
            counter+=1
        


        integer_part = ""
        decimal_part = ""

        if len(result) == 0:
            integer_part = "0."
        else:
            result.append(".")
            for digit in result:
                integer_part+= str(digit)
            
        if len(result_decimal) == 0:
            decimal_part = "0"
        else:
            for digit in result_decimal:
                decimal_part += str(digit)

        
            
        whole_number = integer_part + decimal_part

        



        return whole_number
    

    elif source_base == 2 and target_base == 16: #binary to hex-----------------------------------------------------------------------------------------------------
        #first binary to decimal
        num = []
        for digit in (input_number):
            num.append(int(digit))
        
        num.reverse()
        sum = 0
       

        for i in range(0,len(num)):
            sum+= (num[i])*2**i
        
        input_number = sum
        

        #then decimal to hex
        if input_number < 16:
            result.append(input_number)
        
        while(int(input_number/16) != 0):
            result.append(input_number%16)
            input_number = int(input_number/16)
            if(int(input_number/16) == 0):
                result.append(input_number%16)
        

            
        result.reverse()

        
        

        alpha = {10:"A", 11:"B", 12:"C", 13:"D",14:"E", 15:"F"}

        for i in range(0,len(result)):
            if result[i]>9:
                result[i] = alpha[result[i]]
        


        #fraction
        num = []
        sum_fraction = 0
        

             
        for digit in decimal_number:
            num.append(int(digit))
        
        
        for i in range(0,len(num)):
            sum_fraction+= (num[i])*2**(-(i+1))
        
        counter = 0
        decimal_number = sum_fraction
        result_decimal = []

        while(decimal_number!=0.0) and (counter < 5):
            
            decimal_number = decimal_number*16
            carry = int(decimal_number)
            result_decimal.append(carry)

            decimal_number = decimal_number - carry
            counter+=1
        
        for i in range(0,len(result_decimal)):
            if result_decimal[i] >9:
                result_decimal[i] = alpha[result_decimal[i]]
        

        integer_part = ""
        decimal_part = ""

        if len(result) == 0:
            integer_part = "0."
        else:
            result.append(".")
            for digit in result:
                integer_part+= str(digit)
            
        if len(result_decimal) == 0:
            decimal_part = "0"
        else:
            for digit in result_decimal:
                decimal_part += str(digit)

        
            
        whole_number = integer_part + decimal_part


        


        

        
        return whole_number









            








            
        









    
    
    



print("Number Base Converter")
print("\n This progam will easily convert betwwen Deicmal, Binary and Hexadecimal numbers.")
print("\n Please enter the following inputs: ")




keepGoing = True

while(keepGoing):

    invalidInput = True
    while(invalidInput):
        source = input("The source base (i.e., the base to convert from 10, 2 or 16): ")
        if source != "10" and source != "2" and source != "16":
            print("Invalid input, please try again")
        else:
            invalidInput = False
            source_base = int(source)
    
    invalidInput = True
    while(invalidInput):
        target = input("The target base (i.e., the base to convert to ): ")
        if target != "10" and target!= "2" and target!= "16":
            print("Invalid input, please try again")
        else:
            invalidInput = False
            target_base = int(target)
        
    invalidInput = True
    while(invalidInput):
        number = input("The number to convert: ")
        if(ValidateInput(number, source_base)):
            invalidInput = False
        
        else:
            print("Invalid input, it has to be the base of " , source_base, ". Please try again")
    
    output = convert_number(number,source_base,target_base)

    print("The result of converting the number: ", number, " from the base ", source_base , " to base ", target_base, " is: \n" , output)

    invalidInput = True
    while(invalidInput):
        WantToStay = input("Do you wish to continue with other numbers? \nEnter (Y) to continue \nEnter (N) to quit\n")
        if WantToStay!= "Y" and WantToStay!= "N":
            print("invalid input, please try again")
        
        else:
            invalidInput = False
            if WantToStay == "N":
                keepGoing = False
                print("Quitting calculator ... Thank you!")








    

    

        
            






