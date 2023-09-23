from flask import Flask,render_template,request
import smtplib
from secret import my_email,my_password
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login',methods=['post'])
def home():
    name = request.form["name"]
    phoneno = request.form["phoneno"]
    email = request.form["email"]
    message = request.form["message"]
    # sending mail
    connecting = smtplib.SMTP("smtp.gmail.com", 587)
    connecting.starttls()
    connecting.login(user=my_email,password=my_password)
    connecting.sendmail(from_addr=my_email,to_addrs=email,msg=f"from:{name}\n {phoneno}\n\n{message}")
    connecting.close()
    print(f"succes name ={name} \n {phoneno} \n {email} \n {message} ")
    return f"<h1> Succesfuly send your message"


if __name__ == "__main__":
    app.run()