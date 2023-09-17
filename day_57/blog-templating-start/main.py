from flask import Flask,render_template
import requests


app = Flask(__name__)

api = "https://api.npoint.io/c790b4d5cab58020d391"


@app.route('/')
def index():
    response = requests.get(api)
    data = response.json()
    return render_template('index.html',datas= data)


@app.route('/post/<int:id>')
def get_post(id):
    response = requests.get(api)
    data = response.json()[id-1]
    return render_template('post.html',data=data)


if __name__ == "__main__":
    app.run(debug=True)