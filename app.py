from flask import Flask, render_template, request
import requests
app = Flask("my_app")

def send_email(senders_emai_addressl,senders_name):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox9bec1d3584a44bcdbd6039001706cc67.mailgun.org/messages",
        auth=("api", "e6fffe3a767781dfdb962946a862d0c8-de7062c6-df31c160"),
        data={"from": "Christine Ho <postmaster@sandbox9bec1d3584a44bcdbd6039001706cc67.mailgun.org>",
              "to": "senders_email_address",
              "subject": "Thank you for subscribing!",
              "text": "Congratulations!  You have subscribed!"})
# You can see a record of this email in your logs: https://app.mailgun.com/app/logs

@app.route("/")
def say_hello():
    return render_template("index.html")

@app.route("/News.html")
def News():
    return render_template("News.html")

@app.route("/Weathers.html")
def Weathers():
    return render_template("Weathers.html")

@app.route("/TV.html")
def TV():
    return render_template("TV.html")

@app.route("/subscription", methods = {"POST"})
def subscribe():
    data = request.values
    send_email(data['email'], data['name'])
    return render_template("subscription.html", form_data = data)

app.run(debug = True)
