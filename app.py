from flask import Flask, render_template, request
import http.client
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']

    conn = http.client.HTTPSConnection("gpts4u.p.rapidapi.com")

    payload = [
        {
            "role": "user",
            "content": user_input + " step by step"
        }
    ]

    headers = {
        'content-type': "application/json",
        'X-RapidAPI-Key': "c60b16a458msh962d7cc6d083353p1ce7d8jsn94a738161a5c",
        'X-RapidAPI-Host': "gpts4u.p.rapidapi.com"
    }

    conn.request("POST", "/chatbase", json.dumps(payload), headers)

    res = conn.getresponse()
    data = res.read()

    return render_template('index.html', user_input=user_input.replace("\n","<br>"), response=data.decode("utf-8").replace("\n","<br>"))

if __name__ == '__main__':
    app.run(debug=True)
