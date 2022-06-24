
with open("href.txt",'r') as f:
    reader = f.read()
    print(reader)

with open("newhref.txt",'w') as nf:
    write = nf.write(reader)

