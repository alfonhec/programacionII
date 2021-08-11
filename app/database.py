from flask_sqlalchemy import sqlalchemy
db= sqlalchemy()
class User(db.Model):
    _tablename_='users'
    id=db.column(db.integer, primary_key = True)
    name=db.column(db.string(80), nullable = False)
    lastname=db.column(db.string(80), nullable = False)
    username=db.column(db.string(80), unique = True, nullable = False)4
    email=db.column(db.string(120), nullable =False)
    password=db.column(db.string(250), nullable =False)
    is_admin=db.column(db.boolean, default = False)
    cellphone=db.column(db.string(100), nullable = False)
    avatar=db.column(db.string(250), nullable = True)
    

