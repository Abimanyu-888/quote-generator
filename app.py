import requests

from flask import Flask,render_template,url_for,request
app=Flask(__name__,template_folder="template")

@app.route('/',methods=["POST","GET"])
def mike_checking():
    return render_template("first.html")

@app.route('/quotes',methods=["POST"])
def quotes():
    if 'amount' in request.form.keys():
        amount=request.form['amount']
        quotes=requests.get(f'https://dummyjson.com/quotes/random/{amount}')
        return render_template("display-quote.html",data=quotes.json())

if __name__=='__main__':
    app.run(host="127.0.0.1",port=5556,debug=True)