price = int(input("Enter the original price:"))
slab_rate= float(input("Enter the slab rate percent:"))
x= (slab_rate * price)/100
Net_price= x+price
print("GST price = ", end='')
print(Net_price, end='')