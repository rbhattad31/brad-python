m =['january','february','march','april','may','june','july','august','september','october','november','december']
for i in range(len(m)):
    if m[i] in ['january','february','march']:
        print(m[i]+' Q1 FY 2021-2022')
    elif m[i] in ['april','may','june']:
        print(m[i]+' Q2 FY 2022-2023')
    elif m[i] in ['july','august','september']:
        print(m[i]+' Q3 FY 2022-2023')
    elif m[i] in ['october','november','december']:
        print(m[i]+' Q4 FY 2022-2023')
    else:
        print("not in list")