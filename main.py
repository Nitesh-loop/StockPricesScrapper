import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; '
           'Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
           'Chrome/84.0.4147.105 Safari/537.36'}

urls = [
    'https://www.investing.com/equities/nike',
    'https://www.investing.com/equities/coca-cola-co',
    'https://www.investing.com/equities/microsoft-corp',
    'https://www.investing.com/equities/3m-co',
    'https://www.investing.com/equities/american-express',
    'https://www.investing.com/equities/amgen-inc',
    'https://www.investing.com/equities/apple-computer-inc',
    'https://www.investing.com/equities/boeing-co',
    'https://www.investing.com/equities/cisco-sys-inc',
    'https://www.investing.com/equities/goldman-sachs-group',
    'https://www.investing.com/equities/ibm',
    'https://www.investing.com/equities/intel-corp',
    'https://www.investing.com/equities/jp-morgan-chase',
    'https://www.investing.com/equities/mcdonalds',
    'https://www.investing.com/equities/salesforce-com',
    'https://www.investing.com/equities/verizon-communications',
    'https://www.investing.com/equities/visa-inc',
    'https://www.investing.com/equities/wal-mart-stores',
    'https://www.investing.com/equities/disney',
]

all_data = []
for url in urls:
    page = requests.get(url, headers=headers)
    try:
        soup = BeautifulSoup(page.text, 'html.parser')
        company = soup.find('h1', {'class': 'mb-2.5 text-left text-xl font-bold leading-7 text-[#232526] md:mb-2 md:text-3xl md:leading-8 rtl:soft-ltr'}).text
        # price = soup.find('div', {'class': 'text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]'}).find_all('span')[0].text
        change = soup.find('div', {'class': 'instrument-price-change'}).find_all('span')[2].text
        all_data.append([company, change])
    except AttributeError:
        print("Change the Element id")

# Create DataFrame directly from the list
column_names = ["Company", "Change"]
df = pd.DataFrame(all_data, columns=column_names)

# Save to Excel
df.to_excel('stocks.xlsx', index=False)
