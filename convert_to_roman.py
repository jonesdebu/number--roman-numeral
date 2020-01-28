#Donovan Jones 1/27/2020
# jonesde@bu.edu

#first create a tuple to hold the roman numerals
roman_tuple = [
    ("M", 1000), ("CM", 900), ("D", 500),
    ("CD", 400), ("C", 100), ("XC", 90),
    ("L", 50), ("XL", 40), ("X", 10),
    ("IX", 9), ("V", 5), ("IV", 4),
    ("I", 1)
]

#Basically the function will use divmod to get the quotient
#and remainder of the input divided by the largets base value
#in the tuple:

#Ex: 3549 >= 1000 so 1000 is the largest base value
#   3549/1000 : quotient = 3, remainder = 549
#   or: divmod(3549,1000) = (3,549)

#The quotient is 3 so the M numeral will be appended 3 times

#This sequence continuies until it has iterated through every value in the 
#roman numeral tuple
def to_roman(input):
    #create an array to hold the calculated numerals
    #and append new discovered numerals to the array
    if input < 0:
        print("Input must be greater than 0 absolute value will be used")
        input = abs(input)

    if input == 0:
        print("0 entered will be incremented to 1")
        input = 1

    roman_numerals=[]

    for numeral, val in roman_tuple:
        while val <= input:
            (quotient, remainder) = divmod(input, val)
            input = remainder
            roman_numerals.append(numeral * quotient)

        #   Here numeral is a roman numeral text value such as "M"
        #   number is the respective value of the roman numeral
        #   and quotient is the number of times the numeral will appear
        #   and lastly remainder is the new input number to divmod in order
        #   to find the next numeral
        #   Alternative implementation is to check if the remainder is 0

    return ''.join(roman_numerals)
