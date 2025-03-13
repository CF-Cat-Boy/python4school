gstrate = float(1.1)
while True:
    price = input("Price Excluding GST?: ")
    try:
        float(price)
    except:
        print("Prices must be valid floats!")
    price = float(price)
    gstprice = gstrate*price
    gst = price*(gstrate-1)
    print(f"========================\nGST Including: {gstprice}\nGST Excluding: {price}\nGST: {gst}\n========================\n")