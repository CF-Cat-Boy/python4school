gstrate = float(1.1)
while True:
    gstrate = input("VAT Rate?: ")
    gstprice = input("Price Including VAT?: ")
    try:
        float(gstprice)
    except:
        print("Price must be a valid float!")
    try:
        float(gstrate)
    except:
        print("VAT Rate must be a valid float!")
    gstrate = float(gstrate)
    gstprice = float(gstprice)
    gst = gstprice/(gstrate*10)
    price = gstprice-gst
    print(f"========================\nVAR Including: {gstprice}\nVAT Excluding: {price}\nVAT: {gst}\n========================\n")