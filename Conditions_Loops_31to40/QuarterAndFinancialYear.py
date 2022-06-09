months=['january','february','march','april','may','june','july','august','september','october','november','december']
for i in range(len(months)):
    if months[i] in ['january','february','march']:
        print(months[i]+'2022 - Q1 FY 2021-2022')
    elif months[i] in ['april','may','june']:
        print(months[i]+'2022 - Q2 FY 2022-2023')
    elif months[i] in ['july','august','september']:
        print(months[i]+'2022 - Q3 FY 2022-2023')
    elif months[i] in ['october','november','december']:
        print(months[i]+'2022 - Q4 FY 2022-2023')
    else:
        print("not in list") 