from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData
from sqlalchemy.orm import Session
from models import User, ScoreType

def create_temp_users(session: Session):
    users = [
        User(id=1, user="Joe"),
        User(id=2, user="Erin"),
        User(id=3, user="Paul"),
        User(id=4, user="Allie"),
        User(id=5, user="Abby"),
    ]
    session.execute(User.__table__.insert().values(users))

def create_temp_score_types(session: Session):
    score_types = [
        ScoreType(id=1, type="5 Guesses Left"),
        ScoreType(id=2, type="4 Guesses Left"),
        ScoreType(id=3, type="3 Guesses Left"),
        ScoreType(id=4, type="2 Guesses Left"),
        ScoreType(id=5, type="1 Guesses Left"),
        ScoreType(id=6, type="0 Guesses Left"),
        ScoreType(id=7, type="3/4"),
        ScoreType(id=8, type="2/4"),
        ScoreType(id=9, type="1/4"),
        ScoreType(id=10, type="0/4"),
    ]
    session.execute(ScoreType.__table__.insert().values(score_types))

def merge_temp_users_to_actual(session: Session):
    # Check if values in the temporary table differ from the actual table
    temp_users = session.query(User).all()
    for temp_user in temp_users:
        actual_user = session.query(User).filter(User.id == temp_user.id).first()
        if actual_user is None or actual_user.user != temp_user.user:
            session.merge(temp_user)

def merge_temp_score_types_to_actual(session: Session):
    # Check if values in the temporary table differ from the actual table
    temp_score_types = session.query(ScoreType).all()
    for temp_score_type in temp_score_types:
        actual_score_type = session.query(ScoreType).filter(ScoreType.id == temp_score_type.id).first()
        if actual_score_type is None or actual_score_type.type != temp_score_type.type:
            session.merge(temp_score_type)