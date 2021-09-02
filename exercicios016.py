from math import trunc
x = float(input("Digite o numero aqui:"))
k = x*(10**11)
y = (trunc(x))*(10**11)
print("O numero que você digitou foi {},"
      " e a sua parte inteira é {}!"
      " E a sua parte decimal é {}!" .format(x, trunc(x), (k-y)*(1/(10**11))))
