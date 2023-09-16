from flask import Flask,render_template
import random,datetime,requests

app = Flask(__name__)

agify_endpoint = "https://api.agify.io?"
gendrize_endpont = "https://api.genderize.io?"
@app.route('/')
def home():
    random_number = random.randint(1,9)
    current_year = datetime.datetime.now().year
    return render_template("index.html",numb=random_number,year= current_year)

@app.route('/guess/<name>')
def using_api(name):
    age_url = f"https://api.agify.io/?name={name}"
    age_response = requests.get(age_url)
    age = age_response.json()["age"]
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender = gender_response.json()["gender"]
    return render_template("guess.html",name=name,age=age,gender= gender)

if __name__ == "__main__":
    app.run(debug=True)