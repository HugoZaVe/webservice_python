import pymysql
from app import app
from dbconfig import mysql
from flask import jsonify
from flask import flash, request

#add Editorial
@app.route('/add', methods=['POST'])
def add_editorial():
    try:
        _json = request.json
        _editorial = _json['editorial']
        _passwd = _json['passwd']

        sqlQuery = "INSERT INTO web_service(editorial, passwd) VALUES(%s, %s)"
        data = (_editorial, _passwd)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sqlQuery, data)
        conn.commit()
        res = jsonify('Editorial agregada correctamente')
        res.status_code = 200
        return res

    except Exception as e:
        print(e)
    finally: 
        cursor.close()
        conn.close()        

@app.errorhandler(404)
def not_found(error=None):
	    message = {
	        'status': 404,
	        'message': 'There is no record: ' + request.url,
	    }
	    res = jsonify(message)
	    res.status_code = 404
 
	    return res
			
if __name__ == "__main__":
    app.run()	


