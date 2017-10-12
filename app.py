from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from flask import Flask
from flask import Flask, render_template
from flask import request
from flask import make_response

import json
import os
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp',methods=['POST'])
def showSignUp():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))
    
    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "pyweb":
        return {}
    result = req.get("result")
    #parameters = result.get("parameters")
    #ctry = parameters.get("geo-country")
    
    render_template('signup.html')
    
   # cost = {'Europe':100, 'North America':200, 'South America':300, 'Asia':400, 'Africa':500}

    speech = ctry + " is done " 
    #speech = ctry + "is in " + "Asia" + " continent"
    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-continent-find"
    }

   # return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

