from database import db

class Student(db.Model):
    name = db.Column("name", db.String(200))
    StudentID = db.Column("StudentID", db.Integer, primary_key=True)

class Clubs(db.Model):
        name = db.Column("name", db.String(200))
        ClubID = db.Column("ClubID", db.Integer, primary_key=True)
        Size = db.Column("Size", db.Integer)
        Activity = db.Column("Activity", db.Integer)
        Communication = db.Column("Communication", db.VARCHAR)

        def __init__(self, name, ClubID, Size, Activity, Communication):
            self.name = name
            self.ClubID = ClubID
            self.Size = Size
            self.Activity = Activity
            self.Communication = Communication
