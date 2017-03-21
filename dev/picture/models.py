from datetime import datetime 
from pictureViewer import db



class Data(db.Model):

    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.varchar(50), index=True, unique=False)
	image= db.Column(db.BLOB)

    

    def __init__(self, notes):

        self.notes = notes



    def __repr__(self):

        return '<Data %r>' % self.notes