fraction = "sorry, too complicated to do this part"
while True:
    number = input("Number?: ")
    if number.endswith("%"):
        number = number.removesuffix("%")
        number = float(number)
        number = (number/100)
    elif len(number.split(sep=".")) == 2:
        number = float(number)
    elif len(number.split(sep="/")) == 2:
        fraction = number
        listt = number.split(sep="/")
        number = float(listt[0])/float(listt[1])
    elif number.isdecimal():
        number = float(number)
    percent = number*100
    decimal = number

    print(f"========================\nPercentage: {percent}%\nDecimal: {decimal}\nFraction: {fraction}\n========================\n")
    fraction = "sorry, too complicated to do this part"
