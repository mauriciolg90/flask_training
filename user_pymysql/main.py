from app import app
from db_config import mysql

import pymysql
from flask import jsonify
from flask import request
from werkzeug import generate_password_hash, check_password_hash

@app.route('/users', methods=['GET'])
def users():
    try:
        conn = mysql.connect()
        # DictCursor to fetch rows as a data dictionary
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        # Object with appropriate content-type header
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/user/<int:id>', methods=['GET'])
def user(id):
    try:
        conn = mysql.connect()
        # DictCursor to fetch rows as a data dictionary
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM users WHERE id=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/update/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _name = request.json['name']
        _email = request.json['email']
        _password = request.json['password']
        # Validate the received values
        if _name and _email and _password:
            # Do not save password as a plain text
            _hashed_password = generate_password_hash(_password)
            query = "UPDATE users SET name=%s, email=%s, password=%s WHERE id=%s"
            data = (_name, _email, _hashed_password, id,)
            cursor.execute(query, data)
            conn.commit()
            # Object with appropriate content-type header
            resp = jsonify('User updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/add', methods=['POST'])
def add_user():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _name = request.json['name']
        _email = request.json['email']
        _password = request.json['password']
        # Validate the received values
        if _name and _email and _password:
            # Do not save password as a plain text
            _hashed_password = generate_password_hash(_password)
            query = "INSERT INTO users(name, email, password) VALUES(%s, %s, %s)"
            data = (_name, _email, _hashed_password,)
            cursor.execute(query, data)
            conn.commit()
            # Object with appropriate content-type header
            resp = jsonify('User added successfully!')
            resp.status_code = 201
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id=%s", id)
        conn.commit()
        # Object with appropriate content-type header
        resp = jsonify('User deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
        
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    # Object with appropriate content-type header
    resp = jsonify(message)
    resp.status_code = 404
    return resp

if __name__ == "__main__":
    app.run(debug=True)