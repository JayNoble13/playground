from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/play')
def play():
    return render_template("index.html", num=3, color="skyblue")

@app.route('/play/<int:num>')
def num(num):
    return render_template("index.html", num=num, color= "skyblue")

@app.route('/play/<int:num>/<string:color>')
def pluscolor(num, color):
    return render_template("index.html", num=num, color=color)

@app.route('/success')
def success():
    return"Success"


if __name__=="__main__":
    app.run(debug=True)
