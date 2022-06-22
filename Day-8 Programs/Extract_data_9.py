import re


def extract_quotes(data):
    quotes_data = re.findall(r'"([^"]*)"', data)
    return quotes_data


with open('sample.txt', 'r') as file_1:
    data_1 = file_1.read()
print(extract_quotes(data_1))
