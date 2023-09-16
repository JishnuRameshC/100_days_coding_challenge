from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1>'\
        '<p>hello  ddnjdjdndj dsjkaniundsnfaskndjkfsnjksdfnjkfd</p>'\
            '<img src="https://media.giphy.com/media/Jf2fskuTRv7fDS27gg/giphy.gif"  width=200>'
            
def makebold(function):
    def wrapper_function(*args, **kwargs):
        return "<b>" + function() + "</b>"
    return wrapper_function

def makebold(function):
    def wrapper_function(*args, **kwargs):
        return "<b>" + function() + "</b>"
    return wrapper_function

def makebold(function):
    def wrapper_function(*args, **kwargs):
        return "<b>" + function() + "</b>"
    return wrapper_function

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/bye')
@make_emphasis
@make_underlined
@makebold
def bye():
    return "<h1>bye</h1>"

@app.route('/user/<name>/<int:num>')
def greet(name,num):
    return f"hello {name} and {num}"


if __name__ == "__main__":
    app.run(debug=True)