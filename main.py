from flask import Flask, render_template, redirect, abort, request, Blueprint, jsonify
import requests
import os
from sqlalchemy import func, and_, or_, not_
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flask_secret_key'


@app.route('/index')
@app.route('/')
def index():
    list1 = open('db/points.txt').readlines()
    for i in range(len(list1)):
        list1[i] = [float(i) for i in list1[i].split(',')]
    print(list1)
    return render_template('main.html', title='Главная', list1=list1)


@app.route('/kolomna')
def kolomna():
    list1 = open('db/points.txt').readlines()
    for i in range(len(list1)):
        list1[i] = [float(i) for i in list1[i].split(',')]
    print(list1)
    return render_template('kolomna.html', title='Главная', list1=list1)


@app.route('/krasnogorsk')
def krasnogorsk():
    list1 = open('db/points.txt').readlines()
    for i in range(len(list1)):
        list1[i] = [float(i) for i in list1[i].split(',')]
    print(list1)
    return render_template('krasnogorsk.html', title='Главная', list1=list1)


@app.route('/kolomna/<int:id>')
def sights_kolomn(id):
    data = []
    list1 = open('db/sights.txt', encoding='utf-8').readlines()
    for i in range(len(list1)):
        list1[i] = [i for i in list1[i].split(';')]
        print(list1[i])
        if id == int(list1[i][0]):
            data = list1[i]
    return render_template('sights.html', title=data[1], data=data)

@app.route('/krasnogorsk/<int:id>')
def sights_krasn(id):
    data = []
    list1 = open('db/sights1.txt', encoding='utf-8').readlines()
    for i in range(len(list1)):
        list1[i] = [i for i in list1[i].split(';')]
        print(list1[i])
        if id == int(list1[i][0]):
            data = list1[i]
    return render_template('sights.html', title=data[1], data=data)

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
