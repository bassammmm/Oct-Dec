def dec_oct(decimal):
    octal=[]
    if decimal<8:
        print("Octal Equivalent:",decimal)
    else:
        while decimal!=0:
            octal.append(str(decimal%8))
            decimal//=8
        octal.reverse()
        print("Octal Equivalent:","".join(octal))

def oct_dec(octal):
    decimal=[]
    octal_lst=list(octal)
    octal_lst.reverse()
    sum=0
    if int(octal)<8:
        print("Octal Equivalent:",decimal)
    elif int(octal)<10 and int(octal)>7:
        print("Invalid octal number!")
    else:
        for val in range(len(octal_lst)):
            sum+=(8**val) * (int(octal_lst[val]))
        print(sum)
            

decimal=int(input("Please enter a Decimal number to convert to Octal:"))
dec_oct(decimal)
octal = input("Please enter an Octal value to convert to Decimal:")
oct_dec(octal)
