import MySQLdb
import simplejson as json
import sys




def connect():
    connection = MySQLdb.Connection(host='localhost', user='netshoes', passwd='BEAAAATIIIIT', db='meninobonito', charset='utf8')
    return connection

def get_data(table, value):
    if table == 'dados_gerais_bairro':
        return get_dados_gerais_bairro(value)
    elif table == 'qedu':
        return get_qedu(value)
    elif table == 'ponto_interesse':
        return get_ponto_interesse(value)
    
def get_dados_gerais_bairro(bairro):
    #try:
        # Load the connection
        query = "SELECT * FROM dados_gerais_bairro WHERE UPPER(bairro) = '%s'" % bairro
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(query)
        query_result = [ dict(line) for line in [zip([str(column[0]) for column in cursor.description], row) for row in cursor.fetchall()] ]
        return json.dumps(query_result, ensure_ascii=False, use_decimal=True)        
    #except Exception, e:
        print "Error [%r]" % (e)
        sys.exit(1)
    #finally:
        #if cursor:
        #    cursor.close()

def get_area_contaminada(bairro):
    try:
        # Load the connection
        query = "SELECT * FROM area_contaminada WHERE UPPER(bairro) = '%s'  LIMIT 15" % bairro
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
        query = "SELECT * FROM cartorios WHERE UPPER(bairro) = '%s'  LIMIT 15" % bairro
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
        query = "SELECT * FROM linha_onibus WHERE UPPER(municipio) = '%s'  LIMIT 15" % municipio
        print query
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
        query = "SELECT * FROM ponto_interesse WHERE UPPER(bairro) = '%s' LIMIT 15" % bairro
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
        query = "SELECT * FROM sistema_viario WHERE UPPER(bairro_esq) = '%s' OR UPPER(bairro_dir) = '%'  LIMIT 15" % bairro
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
            
            
            
def get_qedu(escola):
    import mechanize
    import cookielib
    
    # Browser
    br = mechanize.Browser()
    
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.114 Safari/537.36')]
    br.addheaders = [('X-Requested-With', 'XMLHttpRequest')]
    br.addheaders = [('Accept', 'application/json, text/javascript, */*; q=0.01')]
    
    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    
    br.open('http://www.qedu.org.br/')
    br.addheaders = [('Referer', 'http://www.qedu.org.br/')]
    br.open('http://www.qedu.org.br/api/search/?text=' + escola)
    

    return(br.response().read())


get_data('dados_gerais_bairro', 'PARADA INGLESA')
