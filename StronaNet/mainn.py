from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///przepisy.db'
db = SQLAlchemy(app)


class Przepis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(100), nullable=False)
    tresc = db.Column(db.Text, nullable=False)
    skladniki = db.Column(db.String(200), nullable=True)


def dodaj_przepis(nazwa_przepisu, tresc_przepisu, skladniki_przepisu=None):
    if skladniki_przepisu is not None:
        skladniki_lista = skladniki_przepisu.split(",")
        skladniki_string = ", ".join(skladniki_lista)
    else:
        skladniki_string = None

    nowy_przepis = Przepis(nazwa=nazwa_przepisu, tresc=tresc_przepisu, skladniki=skladniki_string)
    db.session.add(nowy_przepis)
    db.session.commit()


def wyszukaj_przepis(szukana_fraza):
    przepisy_po_nazwie = Przepis.query.filter(Przepis.nazwa.like(f"%{szukana_fraza}%")).all()
    przepisy_po_skladniku = Przepis.query.filter(Przepis.skladniki.like(f"%{szukana_fraza}%")).all()
    return list(set(przepisy_po_nazwie + przepisy_po_skladniku))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nazwa_przepisu = request.form['nazwa']
        tresc_przepisu = request.form['tresc']
        skladniki_przepisu = request.form['skladniki']  # Dodajemy pobieranie składników
        dodaj_przepis(nazwa_przepisu, tresc_przepisu, skladniki_przepisu)

    if request.method == 'GET' and 'search' in request.args:
        szukana_nazwa = request.args['search']
        przepisy = wyszukaj_przepis(szukana_nazwa)
    else:
        przepisy = Przepis.query.all()

    return render_template('index.html', przepisy=przepisy)


@app.route('/przepis/<int:przepis_id>')
def wyswietl_przepis(przepis_id):
    przepis = Przepis.query.get_or_404(przepis_id)
    return render_template('przepis.html', przepis=przepis)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
