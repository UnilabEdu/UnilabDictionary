from src.extensions import db


class Subject(db.Model):
    __tabelname__ = "subject"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    course_link = db.Column(db.String)
    internship_link = db.Column(db.String)

    term = db.relationship("ParentWord", secondary="Term", back_populates="Subject")


class ParentWord(db.Model):
    __tablename__ = "parent_word"

    id = db.Column(db.Integer, primary_key=True)
    word_geo = db.Column(db.String)
    word_eng = db.Column(db.String)

    term = db.relationship("Subject", secondary="Term", back_populates="parent_word")


class Term(db.Model):
    __tabelname__ = "term"
    id = db.Column(db.Integer, primary_key=True)

    description = db.Column(db.String)
    example = db.Column(db.String)
    photo = db.Column(db.LargeBinary)

    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"))
    parent_word_id = db.Column(db.Integer, db.ForeignKey("parent_word.id"))

# Subject
#     id
#     name
#     course_link
#     internship_link
#
#     Term
#     subject_id - foreignKey
#     subject - ze
#     parent_word_id - foreignKey
#     word - ze
#     word_geo
#     word_eng
#     description
#     example
#     photo
#
# გადაიტანე ყველა თემფლეითი main-ში
# ბლუპრინტები გააერთიანე
# ადმინ პანელის ტერმინები შექმენი
