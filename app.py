from flask import Flask, render_template, url_for,request, redirect, jsonify, json
import COVID19Py
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)
@app.route('/')
def home():
        url = "https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen&mid=%2Fm%2F027rn"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        data = []
        paises=[]
       
        table = soup.find('table', class_='pH8O4c')
        table_body = table.find('tbody')
        rows= table_body.find_all('tr')
    #    country = table.find("div", { "class" : "pcAJd" })

        for row in rows:
                
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele])
                nombre = row.find_all("div", { "class" : "pcAJd" })
                nombre = [ele.text.strip() for ele in nombre]
                paises.append([ele for ele in nombre if ele])
        return render_template('home.html', data=data, len = len(data), paises=paises)

        
@app.route('/ultimas')
def noticias():
        url = "https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen&mid=%2Fm%2F027rn"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        weblinks = soup.find_all('article')
        pagelinks = []
        linkeable = []
        
        base_url = 'https://news.google.com/'
        
        
        for item in weblinks:
                de = []
                product_name = item.find("a", {"class":"VDXfz"}) 
                product_link = 'https://news.google.com/' + str(product_name.get('href'))
                product_name = product_name.text.replace('\n', "").strip() 
                linkeable.append(product_link)

        for link in weblinks:    
                url = link.find_all('h4')
                text =[ele.text.strip() for ele in url]
                enlace = link.find_all('a', {"class" : "hXwDdf"})
                final = [ele.text.strip() for ele in enlace]    
                pagelinks.append(text)


        return render_template("ultimas.html", pagelinks=pagelinks, len=len(pagelinks), linkeable=linkeable, lendk=len(linkeable), de=de)


if __name__ == "__main__": 
        app.run(port=5000, debug=True, threaded=True)