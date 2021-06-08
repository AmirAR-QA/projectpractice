from application import app

db.drop_all()
db.create_all()

db.session.commit()