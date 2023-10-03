from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, FloatField
from wtforms.validators import DataRequired
from forms import RateMovieForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)

## site issue logging into The Movie Database 
# def get_movie_image(movie_title):
#     api_key = 'your_tmdb_api_key'  # Replace with your TMDb API key
#     base_url = 'https://api.themoviedb.org/3/search/movie'

#     params = {
#         'api_key': api_key,
#         'query': movie_title,
#         'language': 'en-US',
#         'page': 1,
#         'include_adult': 'false',
#     }

#     response = requests.get(base_url, params=params)
#     data = response.json()

# Define the Movie model
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.Text)
    rating = db.Column(db.Float)  # Assuming ratings are decimal numbers
    ranking = db.Column(db.Integer)
    review = db.Column(db.Text)
    img_url = db.Column(db.String(255))  # Adjust the length as needed

# Define the WTForm for adding a movie
class MovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    year = IntegerField('Year')
    description = TextAreaField('Description')
    rating = FloatField('Rating') 
    ranking = IntegerField('Ranking')
    review = TextAreaField('Review')
    img_url = StringField('Image URL')



# Routes
@app.route('/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    form = MovieForm()

    if form.validate_on_submit():
        with app.app_context():
            new_movie = Movie(
                title=form.title.data,
                year=form.year.data,
                description=form.description.data,
                rating=form.rating.data,
                ranking=form.ranking.data,
                review=form.review.data,
                img_url=form.img_url.data
            )
            db.session.add(new_movie)
            db.session.commit()
            flash('Movie added successfully!', 'success')
            return redirect(url_for('index'))

    return render_template('add_movie.html', form=form)


@app.route('/edit_movie/<int:movie_id>', methods=['GET', 'POST'])
def edit_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    form = RateMovieForm()

    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        flash('Movie updated successfully!', 'success')
        return redirect(url_for('index'))

    # Pre-fill the form with the existing movie data
    form.rating.data = movie.rating
    form.review.data = movie.review

    return render_template('edit.html', form=form, movie=movie)


@app.route('/delete_movie/<int:movie_id>', methods=['GET', 'POST'])
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('Movie deleted successfully!', 'success')
    return redirect(url_for('index'))

# Ensure the application context is pushed before running the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
