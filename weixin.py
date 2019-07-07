import csv
import time
import pdfkit
import requests
from multiprocessing.pool import ThreadPool

def process(item):
    url = str(item[2])
    name = item[1] + item[0] + '.pdf'
    response = requests.get(url)
    print(response.status_code)
    html = response.text
    html = html.replace('data-src', 'src')

    try:
        pdfkit.from_string(html, name)
    except:
        pass
    
with open("weixin.csv","r",encoding="gbk") as f:
    f_csv=csv.reader(f)
    next(f_csv)
    pool = ThreadPool(processes=20)
    pool.map(process, (i for i in f_csv))
    pool.close() 






























