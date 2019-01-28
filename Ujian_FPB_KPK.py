import math
def findKPK(a,b):
    tampung=a*b
    hasil=tampung/findFPB(a,b)
    return int(hasil)
            
def findFPB(a,b):
    while True:
        sisa = a%b
        if sisa==0:
            break
        a,b = b, sisa
    return b

try:
    input1=int(input("Ketik Angka Pertama: "))
    input2=int(input("Ketik Angka Kedua: "))
    print("FPB dari ",input1," dan ",input2," = ",findFPB(input1,input2))
    print("KPK dari ",input1," dan ",input2," = ",findKPK(input1,input2))
except:
    print("Input Salah")