import MySQLdb
import simplejson as json
import sys




def connect():
    connection = MySQLdb.Connection(host='localhost', user='netshoes', passwd='BEAAAATIIIIT', db='meninobonito')
    return connection

def get_data(table, value):
    if table == 'dados_gerais_bairro':
        return get_dados_gerais_bairro(value)
    
def get_dados_gerais_bairro(bairro):
    try:
        # Load the connection
        query = "SELECT * FROM dados_gerais_bairro WHERE UPPER(bairro) = '%s'" % bairro
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(query)
        query_result = [ dict(line) for line in [zip([str(column[0]) for column in cursor.description], row) for row in cursor.fetchall()] ]
        return json.dumps(query_result, ensure_ascii=False, use_decimal=True)        
    except Exception, e:
        print "Error [%r]" % (e)
        sys.exit(1)
    finally:
        if cursor:
            cursor.close()

def get_area_contaminada(bairro):
    try:
        # Load the connection
        query = "SELECT * FROM area_contaminada WHERE UPPER(bairro) = '%s'" % bairro
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(query)
        query_result = [ dict(line) for line in [zip([str(column[0]) for column in cursor.description], row) for row in cursor.fetchall()] ]
        return json.dumps(query_result, ensure_ascii=False, use_decimal=True)        
    except Exception, e:
        print "Error [%r]" % (e)
        sys.exit(1)
    finally:
        if cursor:
            cursor.close()

def get_cartorios(bairro):
    try:
        # Load the connection
        query = "SELECT * FROM cartorios WHERE UPPER(bairro) = '%s'" % bairro
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(query)
        query_result = [ dict(line) for line in [zip([str(column[0]) for column in cursor.description], row) for row in cursor.fetchall()] ]
        return json.dumps(query_result, ensure_ascii=False, use_decimal=True)        
    except Exception, e:
        print "Error [%r]" % (e)
        sys.exit(1)
    finally:
        if cursor:
            cursor.close()

def get_linha_onibus(municipio):
    try:
        # Load the connection
        query = "SELECT * FROM linha_onibus WHERE UPPER(municipio) = '%s'" % municipio
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(query)
        query_result = [ dict(line) for line in [zip([str(column[0]) for column in cursor.description], row) for row in cursor.fetchall()] ]
        return json.dumps(query_result, ensure_ascii=False, use_decimal=True)        
    except Exception, e:
        print "Error [%r]" % (e)
        sys.exit(1)
    finally:
        if cursor:
            cursor.close()

def get_ponto_interesse(bairro):
    try:
        # Load the connection
        query = "SELECT * FROM ponto_interesse WHERE UPPER(bairro) = '%s'" % bairro
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(query)
        query_result = [ dict(line) for line in [zip([str(column[0]) for column in cursor.description], row) for row in cursor.fetchall()] ]
        return json.dumps(query_result, ensure_ascii=False, use_decimal=True)        
    except Exception, e:
        print "Error [%r]" % (e)
        sys.exit(1)
    finally:
        if cursor:
            cursor.close()

def get_sistema_viario(bairro):
    try:
        # Load the connection
        query = "SELECT * FROM sistema_viario WHERE UPPER(bairro_esq) = '%s' OR UPPER(bairro_dir) = '%'" % bairro
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(query)
        query_result = [ dict(line) for line in [zip([str(column[0]) for column in cursor.description], row) for row in cursor.fetchall()] ]
        return json.dumps(query_result, ensure_ascii=False, use_decimal=True)        
    except Exception, e:
        print "Error [%r]" % (e)
        sys.exit(1)
    finally:
        if cursor:
            cursor.close()

get_data('dados_gerais_bairro', 'PARADA INGLESA')