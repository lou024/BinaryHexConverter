
def DecimalToBinaryRec(num, out):
    if num >= 1:
        out+=DecimalToBinaryRec(num//2,out)
        out+=str(num%2)
    return out
    
def DecimalToBinary(num):
    out = DecimalToBinaryRec(num,"")
    print(out)
    
def DecimalToHexRec(num, out):
    if num < 0:
        out+="0"
    elif num <= 1:
        out+=str(num)
    else:
        out+=DecimalToHexRec(num//16, out)
        x =(num%16)
        if (x < 10):
            out+=str(x)
        if (x == 10):
            out+="A"
        if (x == 11):
            out+="B"
        if (x == 12):
            out+="C"
        if (x == 13):
            out+="D"
        if (x == 14):
            out+="E"
        if (x == 15):
            out+="F"
    return out


def DecimalToHex(num):
    out = DecimalToHexRec(num,"")
    print(out[1:])

    
def run():
    num = input("enter a positive integer:")
    if num == "q":
        return
    print("%d in binary: " % int(num))
    DecimalToBinary(int(num))
    print("\n%d in hex: " % int(num))
    DecimalToHex(int(num))
    print("\n")
    run()
    
run()
