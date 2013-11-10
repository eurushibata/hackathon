#!/usr/bin/env python

from bottle import route, run, template, get, debug
from backend.get_data import get_data

debug(True)

# this will be the dictionary returned by the ajax call.
# Bottle convert this in a json compatibile string.

items = {1: 'first item', 2: 'second item'}

# a simple json test main page
@route('/')
def jsontest():
        return template('json')

@route('/vw_dado_geral')
def get_vw_dado_geral():
        return (get_data('VW_DADO_GERAL', 'PARADA INGLESA'))

run(host='127.0.0.1', port=8081)
