price = int(input())
slab_rate= float(input())
cal= (slab_rate * price)/100
Net_price= cal+price
print("GST price = ", end='')
print(Net_price, end='')