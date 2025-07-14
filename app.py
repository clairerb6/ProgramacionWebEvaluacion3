from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from database import init_db
from ejercicio1.routes import ej1
from ejercicio2.routes import ej2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'D0zHXu02yu00vFBOnDx'
csrf = CSRFProtect(app)
init_db()

# Registro del Blueprint
app.register_blueprint(ej1)
app.register_blueprint(ej2)

@app.route('/')
def inicio():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
