from app import app
from flask import render_template, request


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/present', methods = ['POST','GET'])
def present():
    if request.method == 'POST':
        attdeees = request.form['name']
        # start date
        sd = request.form['date1']
        # end date
        ed = request.form['date2']

        # then, get their email and name
        # TODO: funtions
        



    return render_template('presnt.html')


@app.route('/notice')
def notice():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)