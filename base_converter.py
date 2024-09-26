import math

def ValidateInput(input_number, source_base):
    # Checks base and assigns valid digits depending on said base
    if (source_base == "2"):
        validDigits = ("0", "1")

        if input_number.count('.') > 1:
            return False
    
    elif (source_base == "10"):
        try:
            float(input_number)
        except(ValueError):
            return False
        
        if input_number.count('.') > 1:
            return False
        return True
            
    elif (source_base == "16"):
        validDigits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F")
    
        # Check for multiple decimal points
        if input_number.count('.') > 1:
            return False
    else:
        return False
    
    # Goes through each digit to verify, returns True or False depending on validity
    for digit in input_number:
        if (digit not in validDigits and digit != '.'):
            return False
    return True

def decimal_to_binary_with_fraction(decimal_number):
    # Separate the integer and fractional parts
    integer_part = int(decimal_number)
    fractional_part = decimal_number - integer_part

    # Convert the integer part to binary
    binary_integer_part = bin(integer_part).replace('0b', '')

    # Convert the fractional part to binary
    binary_fractional_part = []
    while fractional_part > 0:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional_part.append(str(bit))
        fractional_part -= bit
        if len(binary_fractional_part) > 10:  # Limit the precision
            break

    # Combine both parts
    binary_result = binary_integer_part + '.' + ''.join(binary_fractional_part) if binary_fractional_part else binary_integer_part
    return binary_result

def decimal_to_binary_with_two_complement(decimal_number):
    # Separate the integer and fractional parts
    integer_part = int(decimal_number)
    fractional_part = decimal_number - integer_part

    if integer_part >= 0:
        return decimal_to_binary_with_fraction(decimal_number)
    else:
        bits = 8  # Define the number of bits you want to use (e.g., 8 bits for two's complement)
        # Apply two's complement only to the integer part
        two_complement_integer = bin((1 << bits) + integer_part).replace('0b', '')

        # Convert the fractional part to binary (no two's complement needed for fractional part)
        if fractional_part != 0:
            binary_fractional_part = decimal_to_binary_with_fraction(fractional_part)
            if '.' in binary_fractional_part:
                binary_fractional_part = binary_fractional_part.split('.')[1]  # Get only the fractional part
                return two_complement_integer + '.' + binary_fractional_part
            else:
                return two_complement_integer  # No fractional part
        return two_complement_integer

def binary_to_decimal_with_two_complement(binary_number):
    if binary_number[0] == '1':  # If MSB is 1, it's a negative number
        bits = len(binary_number)
        return int(binary_number, 2) - (1 << bits)
    else:
        return int(binary_number, 2)

def decimal_to_hex_with_fraction(decimal_number):
    integer_part = int(decimal_number)
    fractional_part = decimal_number - integer_part

    # Convert integer part to hex
    hex_integer_part = hex(integer_part).replace('0x', '').upper()

    # Convert fractional part to hex
    hex_fractional_part = []
    while fractional_part > 0:
        fractional_part *= 16
        digit = int(fractional_part)
        hex_fractional_part.append(hex(digit).replace('0x', '').upper())
        fractional_part -= digit
        if len(hex_fractional_part) > 10:  # Limit the precision
            break

    hex_result = hex_integer_part + '.' + ''.join(hex_fractional_part) if hex_fractional_part else hex_integer_part
    return hex_result

def decimal_to_hex_with_two_complement(decimal_number):
    if decimal_number >= 0:
        return decimal_to_hex_with_fraction(decimal_number)
    else:
        bits = 16  # Define the number of bits for two's complement (e.g., 16 bits)
        # Convert to binary and then to hexadecimal
        two_complement = (1 << bits) + int(decimal_number)
        return hex(two_complement).replace('0x', '').upper()

def hex_to_decimal_with_fraction(hex_number):
    if '.' in hex_number:
        integer_part, fractional_part = hex_number.split('.')
    else:
        integer_part = hex_number
        fractional_part = '0'

    # Convert integer part to decimal
    decimal_integer_part = int(integer_part, 16)

    # Convert fractional part to decimal
    decimal_fractional_part = 0
    for i, digit in enumerate(fractional_part):
        decimal_fractional_part += int(digit, 16) * (16 ** -(i + 1))

    return decimal_integer_part + decimal_fractional_part

def convert_number(input_number, source_base, target_base):
    if target_base == "2":  # Conversion to binary
        if source_base == "10":
            return decimal_to_binary_with_two_complement(float(input_number))
        elif source_base == "16":
            decimal_value = int(input_number, 16)
            return decimal_to_binary_with_two_complement(decimal_value)
        else:
            return input_number  # Already binary

    elif target_base == "10":  # Conversion to decimal
        if source_base == "2":
            return binary_to_decimal_with_two_complement(input_number)
        elif source_base == "16":
            return hex_to_decimal_with_fraction(input_number)

    elif target_base == "16":  # Conversion to hexadecimal
        if source_base == "10":
            return decimal_to_hex_with_two_complement(float(input_number))
        elif source_base == "2":
            binary_to_decimal = binary_to_decimal_with_two_complement(input_number)
            return decimal_to_hex_with_two_complement(binary_to_decimal)

    return "Conversion not supported."

def main():
    print("Number Base Converter")
    print("\nThis program will convert between Decimal, Binary, and Hexadecimal numbers.")
    print("\nPlease enter the following inputs:")

    continue_choice = True

    while continue_choice:
        choice_left = ["2", "10", "16"]

        input_number = input("\nPlease enter the number to convert: ")
        source_base = input("\nPlease enter the base to convert from (2 for binary, 10 for decimal, 16 for hexadecimal): ")

        while source_base not in choice_left:
            print("We do not support converting from that base.")
            source_base = input("\nPlease enter a valid base to convert from: ")

        target_base = input("\nPlease enter the base to convert to (2 for binary, 10 for decimal, 16 for hexadecimal): ")

        # Don't remove the source base; just check if the target base is valid and not the same as the source base
        while target_base == source_base or target_base not in choice_left:
            if target_base == source_base:
                print("\nYou cannot convert from base", source_base, "to base", source_base, ". Please select a different base.")
            else:
                print("We do not support converting to that base.")
            
            print(f"\nYou can pick between: {', '.join(choice_left)}")
            target_base = input("\nPlease enter the base to convert to: ")

        validated = ValidateInput(input_number, source_base)

        while not validated:
            print(f"\nThe input {input_number} was not valid for base {source_base}. Please enter a valid number.")
            input_number = input("\nPlease enter the number to convert: ")
            validated = ValidateInput(input_number, source_base)

        print("\nInput Number Was Validated.")
        converted_num = convert_number(input_number, source_base, target_base)
        print(f"\nThe result is: {converted_num}")

        print("\nDo you wish to continue with other numbers?")
        print("Enter (Y) to continue.")
        print("Enter (N) to quit.")

        wish_to_continue = input("\nYour Choice: ").lower()

        while wish_to_continue not in ['y', 'n']:
            print("\nYou entered an invalid choice. Please try again.")
            wish_to_continue = input("\nYour Choice (Y/N): ").lower()

        continue_choice = wish_to_continue == 'y'

    print("\nQuitting calculator... Thank you!!!\n")


# Run the main program
main()
