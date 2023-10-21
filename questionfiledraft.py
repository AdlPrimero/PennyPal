deposit = int(input("How much are you looking to deposit?"))
term = input("Are you looking to save long term?")
use = int(input("How many months will you not use your money?"))
risk = (input("Are you ok with your money being at risk?"))
house =(input("Are you saving to buy your first house?"))
age =(input("Are you applying for someone under 18?"))

if term=="y":
    if age=="y":
        print("Junior ISA")
    elif house=="y":
        print("Lifetime ISA")
    elif risk=="y":
        print("Stocks and Shares ISA")
    else:
        print("Cash ISA")

else:
    if use<1:
        print("Instant saver")
    elif use<9:
        print("Notice saver")
    else:
        print("Fixed term saver")