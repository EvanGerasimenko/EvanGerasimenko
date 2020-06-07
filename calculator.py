#debilniy calculator v.2
from colorama import init
from colorama import Fore, Back, Style
init()

while True:

    print ( Fore.BLACK )
    print ( Back.WHITE )

    what = input ("what we gonna do? (+, -):" )

    print ( Back.CYAN )

    a = float(input ("input first number: "))
    b = float(input ("input second number: "))

    print ( Back.GREEN)   

    if what == "+":
	    c = a + b
	    print ("result: " + str(c))
    elif what == "-":
	    c = a - b 
	    print ("result: " + str(c))
    else:
	    print ("incorrect operation")

