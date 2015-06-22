from pip._vendor.distlib.compat import raw_input


if __name__ == "__main__":
    while True:
        dig = raw_input("Select the digits (max 100) of Pi you want to find >> ")
        if dig > 0 and dig <= 100:
            break
    
    print "%.df" % (dig, math.pi)