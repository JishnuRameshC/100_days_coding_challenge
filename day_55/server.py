from flask import Flask
import random

random_number =  random.randint(1,10)
print(random_number)

app = Flask(__name__)


@app.route('/')
def home():
    return "<center><h1>heigher or lower</h1>\
        <img src='https://media.giphy.com/media/fDUOY00YvlhvtvJIVm/giphy.gif' weigth= 400></center>"


@app.route('/<int:number>')
def guess_number(number):
    if number == random_number:
        return "<center><img src='https://media.giphy.com/media/3oEjHY2dCdoXcTsHDi/giphy.gif' width=600>\
            <h1>you win</h1></center"
    elif number > random_number:
        return "<center><img src='https://media.giphy.com/media/DVSpPORBAgDwiXCjzf/giphy.gif' width=500>\
            <h1> try lower</h1></center"
    else:
        return "<center><img src='https://media.giphy.com/media/l2JhAgiGSvMordxQs/giphy.gif' width=500>\
            <h1> try higer</h1></center"
        
        
if __name__ == '__main__':
    app.run(debug=True)
