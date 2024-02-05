from flask import url_for

from src.extensions import db


class Subject(db.Model):
    __tablename__ = "subjects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    course_link = db.Column(db.String)
    internship_link = db.Column(db.String)

    terms = db.relationship("Term", secondary="subjects_terms", back_populates="subject")

    def __repr__(self):
        return f"{self.name}"


class TermToSubject(db.Model):
    __tablename__ = "subjects_terms"

    id = db.Column(db.Integer, primary_key=True)
    subjects_id = db.Column(db.Integer, db.ForeignKey("subjects.id"))
    terms_id = db.Column(db.Integer, db.ForeignKey("terms.id"))


class Term(db.Model):
    __tablename__ = "terms"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    example = db.Column(db.String)
    eng_word = db.Column(db.String)
    geo_word = db.Column(db.String)
    img = db.Column(db.String)

    subject = db.relationship("Subject", secondary="subjects_terms", back_populates="terms")

    parent_word_id = db.Column(db.Integer, db.ForeignKey("terms.id"))
    parent_word_rel = db.relationship("Term", remote_side="Term.id", backref="parent_word")

    def __repr__(self):
        return f"{self.geo_word}"

    def get_image(self):
        if self.img:
            return url_for('static', filename='uploads/' + self.img)
        return url_for('static', filename='img/unknown.png')
