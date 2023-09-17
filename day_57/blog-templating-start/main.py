from flask import Flask,render_template
import requests


app = Flask(__name__)

api = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(api)
data = response.json()

@app.route('/')
def index():
    return render_template('index.html',all_data= data)


@app.route('/post/<int:id>')
def get_post(id):
    global data
    return render_template('post.html',data=data[id-1])


if __name__ == "__main__":
    app.run(debug=True)