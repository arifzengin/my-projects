from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', number1 = 2000, number2 = 4000)



if __name__ == '__main__':
    app.run(debug=True)