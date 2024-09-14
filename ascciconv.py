

# Python3 program to convert ASCII
# string to Hexadecimal format string
 
# function to convert ASCII to HEX
def ASCIItoHEX(ascii):
 
    # Initialize final String
    hexa = ""
 
    # Make a loop to iterate through
    # every character of ascii string
    for i in range(len(ascii)):
 
        # take a char from
        # position i of string
        ch = ascii[i]
 
        # cast char to integer and
        # find its ascii value
        in1 = ord(ch)
   
        # change this ascii value
        # integer to hexadecimal value
        part = hex(in1).lstrip("0x").rstrip("L")
 
        # add this hexadecimal value
        # to final string.
        hexa += part
 
    # return the final string hex
    return hexa
   
# Driver Function
if __name__ == '__main__':
 
    # print the Hex String
    print(ASCIItoHEX("wgjgg"))
