import json

KG_Articles = '''
{
"Articles": [
    {
        "Article_ID": "KA 10282",
        "Display_Name": "Trouble Enrolling in ADP Portal",
        "Primary_FAQ": "What do I do when there is trouble enrolling in ADP portal?",
        "Article_URL": "https://storageaccountrpabeaf.blob.core.windows.net/testpdf/Trouble%20Enrolling%20in%20ADP%20Portal.pdf",
        "Role": ""
    },
    {
        "Article_ID": "KA 10488",
        "Display_Name": "Accessing and Navigating Kronos",
        "Primary_FAQ": "What is the process for accessing and navigating kronos?",
        "Article_URL": "https://storageaccountrpabeaf.blob.core.windows.net/testpdf/Accessing%20and%20Navigating%20Kronos.pdf",
        "Role": ""
    }
]
}
'''
data = json.loads(KG_Articles)
print(data)
for url in data['Articles']:
    print(url)
    print(url['Article_ID'])
    del url['Role']
    new_string = json.dumps(data, indent=2)
    print(new_string)

with open('states_titlecase.json') as f:
    data2 = json.load(f)
for state in data2['states']:
    # print(state)
    del state['abbreviation']
    print(state)
with open('new_states.json', 'w') as nf:
    json.dump(data2, nf,indent=2)
from urllib.request import urlopen
with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()
    data3 = json.loads(source)
    print(json.dumps(data3, indent=2))



