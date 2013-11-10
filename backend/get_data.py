import MySQLdb
import simplejson as json
import sys




def connect():
    connection = MySQLdb.Connection(host='localhost', user='happybday', passwd='lulz', db='happybday')
    return connection

def get_data(table, value):
    if table == 'VW_DADO_GERAL':
        return get_VW_DADO_GERAL(value)
    
def get_VW_DADO_GERAL(value):    
    
    try:
        # Load the connection
        query = "SELECT * FROM VW_DADO_GERAL WHERE NOME_ZONA_ = '%s'" % value
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(query)
        query_result = [ dict(line) for line in [zip([str(column[0]) for column in cursor.description], row) for row in cursor.fetchall()] ]
        print json.dumps(query_result, ensure_ascii=False, use_decimal=True)
        print
    except Exception, e:
        print "Error [%r]" % (e)
        sys.exit(1)
    finally:
        if cursor:
            cursor.close()
            
            
#def get_summarization(table):
    
            
get_data('VW_DADO_GERAL', 'PARADA INGLESA')