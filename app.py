from flask import Flask, render_template, url_for,request, redirect, jsonify, json
import COVID19Py
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
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
        return render_template('index.html', data=data, len = len(data), paises=paises)

#@app.route('/get_data')
# def get_data():
#  labels = paises
#  data = data
#  return flask.jsonify({'payload':json.dumps({'data':data, 'labels':labels})})
        
     
if __name__ == "__main__": 
        app.run(debug=True)