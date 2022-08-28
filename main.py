import urllib.request
from flask import Flask, jsonify, request
from bs4 import BeautifulSoup



app = Flask(__name__)
#Convert the currency from rate to to rate
@app.route('/<fromRate>/<toRate>', methods = ['GET'])
def convertRate(fromRate,toRate):
    file_name = "{}_{}.html".format(fromRate,toRate)
    convert_tag = "{}-{}".format(fromRate,toRate)
    request_url ="https://www.google.com/finance/quote/"+convert_tag

    urllib.request.urlretrieve(request_url, "conversion.html")

    with open('conversion.html') as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    elements = soup.find_all("div", {"class": "YMlKec fxKbKc"})

    #for element in elements:
    if len(elements)==0:
        return 0

    rate = elements[0].text
    return jsonify({"data":rate})


if __name__ == '__main__':
    app.run(debug = True,host="0.0.0.0",port=3030)