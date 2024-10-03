from flask import Flask, Blueprint, render_template, redirect, url_for,request

usuario_route = Blueprint('usuarios', __name__)

@usuario_route.route('/cadastrar', methods = ['GET', 'POST'])
def cadastrar():
    if request.method == 'GEt':
        return url_for('iniciar')