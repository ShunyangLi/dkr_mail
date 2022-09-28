from app import app
from flask import render_template, request
from utils.presenter_handling import handle_presenter, handle_upload

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/present', methods = ['POST','GET'])
def present():
    if request.method == 'POST':
        # get the current and next week's presenter
        ca = request.form['people1']
        na = request.form['people2']

        ca = ca.split(",")
        na = na.split(",")

        # start date and next week date
        sd = request.form['date1']
        nd = request.form['date2']

        # then, get their email and name
        data = handle_presenter(ca, na, sd, nd)

        if data is not None:
            return render_template('presenter.html', re = True, message = data)

    return render_template('presnt.html')


@app.route('/notice')
def notice():
    handle_upload()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)