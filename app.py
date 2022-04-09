from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
from io import BytesIO
import base64
from bs4 import BeautifulSoup 
import requests
plt.style.use('seaborn')

#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

#insert the scrapping here
url_get = requests.get('https://www.coingecko.com/en/coins/ethereum/historical_data/usd?start_date=2020-01-01&end_date=2021-06-30#panel')
soup = BeautifulSoup(url_get.content,"html.parser")

#find your right key here
table = soup.find('table', attrs = {'table table-striped text-sm text-lg-normal'})
row = table.find_all('th', attrs = {'font-semibold text-center'})

row_length = len(row)

temp = [] #initiating a list 

j = 1

for i in range(0, row_length):
#insert the scrapping process here
    #get period
    period = table.find_all('th', attrs = {'font-semibold text-center'})[i].text
    period = period.strip()
    
    #get volume
    volume = table.find_all('td', attrs = {'text-center'})[j].text
    volume = volume.strip()
    j += 4

    temp.append((period,volume))

temp = temp[::-1]

#change into dataframe
df = pd.DataFrame(temp, columns = ('period','volume'))

#insert data wrangling here
df['period'] = df['period'].astype('datetime64')
df = df.set_index('period')
df['volume'] = df['volume'].str.replace("$","")
df['volume'] = df['volume'].str.replace(",","")
df['volume'] = df['volume'].astype('int64')

#end of data wranggling 

@app.route("/")
def index(): 
	
	card_data = f'{int(df["volume"].mean())}' #be careful with the " and ' 

	# generate plot
	ax = df.plot(figsize = (20,9), rot = 45) 
	ax.legend(['Volume in U.S. Dollars'])
	loc = mdates.MonthLocator(interval=1)
	ax.xaxis.set_major_locator(loc)
	fmt = mdates.DateFormatter('%b-%d-%Y')
	ax.xaxis.set_major_formatter(fmt)
	ax.get_yaxis().set_major_formatter(
    	ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

	# Rendering plot
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result = str(figdata_png)[2:-1]

	# render to html
	return render_template('index.html',
		card_data = card_data, 
		plot_result=plot_result
		)


if __name__ == "__main__": 
    app.run(debug=True)