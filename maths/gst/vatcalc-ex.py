while True:
    gstrate = input("VAT Rate?: ")
    price = input("Price Excluding VAT?: ")
    try:
        float(price)
    except:
        print("Price must be a valid float!")
    try:
        float(gstrate)
    except:
        print("VAT Rate must be a valid float!")
    price = float(price)
    gstrate = float(gstrate)
    gstprice = gstrate*price
    gst = price*(gstrate-1)
    print(f"========================\nVAT Including: {gstprice}\nVAT Excluding: {price}\nVAT: {gst}\n========================\n")