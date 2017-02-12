#!/usr/bin/env python3

from flask import Flask, request, render_template
import komunikace

app = Flask('nastenka', template_folder='sablony')


@app.route('/')
def zobrazit_formular():
    return render_template('formular.html')


@app.route('/zpracuj', methods=['POST'])
def zpracuj_formular():
    # načteme příspěvek z odeslaného formuláře
    prispevek = request.form['prispevek']

    komunikace.odesli_na_server(prispevek)

    # vrátíme potvrzení
    return render_template('potvrzeni.html')


if __name__ == '__main__':
    app.run(debug=True)
