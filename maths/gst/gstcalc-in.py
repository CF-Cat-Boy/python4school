gstrate = float(1.1)
while True:
    gstprice = input("Price Including GST?: ")
    try:
        float(gstprice)
    except:
        print("Prices must be valid floats!")
    gstprice = float(gstprice)
    gst = gstprice/(gstrate*10)
    price = gstprice-gst
    print(f"========================\nGST Including: {gstprice}\nGST Excluding: {price}\nGST: {gst}\n========================\n")