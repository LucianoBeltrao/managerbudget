from flask import Flask, render_template
app = Flask(__name__)

print(__name__)

@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/contatos')
def contatos():
    return render_template("contatos.html")


@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/tables')
def tables():
    return render_template("tables.html")

@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/forgot_password')
def forgot_password():
    return render_template("forgot-password.html")

@app.route('/utilitiesanimation')
def utilitiesanimation():
    return render_template("utilities-animation.html")


@app.route('/charts')
def charts():
    return render_template('charts.html')


@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template('usuarios.html', nome_usuario=nome_usuario)



if __name__ == '__main__':
    app.run(debug=True)



