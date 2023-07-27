from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landingPage():
    return render_template('landingPage.html')


@app.route('/home')
def homePage():
    return render_template('homePage.html')

if __name__ == '__main__':
    app.run(debug=True)