def remove_zero_ip(ip_add):
    new_ip_add = ".".join([str(int(i)) for i in ip_add.split(".")])
    return new_ip_add


print(remove_zero_ip("255.024.01.01"))
