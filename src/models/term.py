from src.extensions import db


class Subject(db.Model):
    __tablename__ = "subject"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    course_link = db.Column(db.String)
    internship_link = db.Column(db.String)

    term = db.relationship("Term", back_populates="subject")
    term_id = db.Column(db.ForeignKey("term.id"))

class Term(db.Model):
    __tablename__ = "term"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    example = db.Column(db.String)
    photo = db.Column(db.String)

    subject = db.relationship("Subject", back_populates="term")