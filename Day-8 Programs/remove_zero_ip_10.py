import re


def remove_zero(ip):
    string = re.sub('\.[0]*', '.', ip)
    return string


ip_address = "216.08.094.196"
print(remove_zero(ip_address))
