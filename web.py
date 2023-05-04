from bottle import route, run, template
from bib import metrosParaCentimetros

@route('/ex1/<metros:float>')
def route_ex1(metros):
    cm = metrosParaCentimetros(metros)
    return template('<h1>{{cm}}</h1>', cm=cm)

run(host='localhost', port=8080)