

def calcper(price1,price2):
    x = abs(price1-price2)
    y = (x/price1)
    answer = (y*100)
    return answer
while True:
    price1 = input("Price 1?: ")
    price2 = input("Price 2?: ")
    try:
        float(price2)
    except:
        print("Prices must be valid floats!")
    try:
        float(price1)
    except:
        print("Prices must be valid floats!")
    price1 = float(price1)
    price2 = float(price2)
    print(calcper(price1,price2))