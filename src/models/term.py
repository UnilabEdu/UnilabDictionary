from src.extensions import db


class Subject(db.Model):
    __tablename__ = "subject"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    course_link = db.Column(db.String)
    internship_link = db.Column(db.String)

    terms = db.relationship("Term", back_populates="subject")


    def __repr__(self):
        return f"{self.name}"


class Term(db.Model):
    __tablename__ = "terms"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    eng_word = db.Column(db.String)
    geo_word = db.Column(db.String)

    subject_id = db.Column(db.ForeignKey("subject.id"))
    subject = db.relationship("Subject", back_populates="terms")

    parent_word_id = db.Column(db.Integer, db.ForeignKey("terms.id"))
    parent_word_rel = db.relationship("Term", remote_side="Term.id", backref="parent_word")

    def __repr__(self):
        return f"{self.geo_word}"