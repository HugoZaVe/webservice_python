from app import app
from flaskext.mysql import MYSQL

mysql = MYSQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'cultura'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

