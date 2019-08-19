from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_DB'] = 'flask_test'
app.config['MYSQL_DATABASE_USER'] = 'mauri'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PASSWORD']= '280490mg'
mysql.init_app(app)