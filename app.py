from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:dominion@localhost/kfc'

else:
    app.debug = False
    app.debug['SQLALCHEMY_DATABASE_URI'] = ''

db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key = True)
    customer = db.Column(db.String(200), unique = True)
    worker = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, worker, rating, comments):
        self.customer = customer
        self.worker = worker
        self.rating = rating
        self.comments = comments



app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form["customer"]
        worker = request.form["worker"]
        rating = request.form["rating"]
        comments = request.form["comments"]
        # print(customer, worker, rating, comments)
        if customer == '' or worker == '' or rating == '' or comments =='':
            return render_template('index.html', message = "Please enter the required fields.")
        return render_template('success.html')





if __name__ == '__main__':
    app.debug = True
    app.run()
