#!/usr/bin/env python

from bottle import route, run, template, get, debug
from bottle import response
from backend.get_data import get_data

debug(True)

# this will be the dictionary returned by the ajax call.
# Bottle convert this in a json compatibile string.

items = {1: 'first item', 2: 'second item'}

# a simple json test main page
@route('/')
def jsontest():
        return template('json')

@route('/search/area_contaminada/<bairro>')
def get_area_contaminada(bairro):
        bairro = bairro.replace('%20',' ')
        return (get_data('area_contaminada', bairro.upper()))

@route('/search/cartorios/<bairro>')
def get_cartorios(bairro):
        bairro = bairro.replace('%20',' ')
        return (get_data('cartorios', bairro.upper()))
    
@route('/search/dados_gerais_bairro/<bairro>')
def get_dados_gerais_bairro(bairro):
        response.content_type = 'application/json'
        response.add_header('Access-Control-Allow-Origin', '*')
        bairro = bairro.replace('%20',' ')
        print bairro
        return (get_data('dados_gerais_bairro', bairro.upper()))
    
@route('/search/linha_onibus/<municipio>')
def get_linha_onibus(municipio):
        municipio = municipio.replace('%20',' ')
        return (get_data('linha_onibus', municipio.upper()))
    
@route('/search/ponto_interesse/<bairro>')
def get_ponto_interesse(bairro):
        bairro = bairro.replace('%20',' ')
        return (get_data('ponto_interesse', bairro.upper()))
    
@route('/search/sistema_viario/<bairro>')
def get_sistema_viario(bairro):
        bairro = bairro.replace('%20',' ')
        return (get_data('sistema_viario', bairro.upper()))
    
@route('/search/qedu/<escola>')
def get_qedu(escola):
    return (get_data('qedu', escola))   

    
run(host='0.0.0.0', port=8081)