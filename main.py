from flask import Flask, render_template, request
from urllib import urlopen, urlencode
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        # return request.form["zipcode"]
        zipcode = request.form["zipcode"]
        zipcode = zipcode + "," + "fr"
        # call to the API
        token = "3bc388b5c6a331e7958629902889974f"
        parameters = urlencode({"zip": zipcode, "APPID": token})
        hostname = " http://api.openweathermap.org/data/2.5/weather"
        url = hostname + "?" + parameters
        print url
        api_response = urlopen(url)
        data = json.loads(api_response.read())
        print data
        temp = data["main"]["temp"]
        return str(temp)



    return render_template("ask_weather.html") 



if __name__ == "__main__":
    app.run(debug=True)
