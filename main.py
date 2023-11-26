from datetime import datetime

from fastapi import FastAPI, Depends, status
import models
from database import engine, SessionLocal
from pydantic import BaseModel
from sqlalchemy.orm import Session
from seedScripts import merge_temp_score_types_to_actual, merge_temp_users_to_actual

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class ScoreBase(BaseModel):
    userId: int
    score: int


def init_db():
    db = SessionLocal()
    try:
        merge_temp_score_types_to_actual(db)
        merge_temp_users_to_actual(db)
    finally:
        db.close()

def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

db_dependency = Depends(get_db)
app.add_event_handler("startup", init_db)


@app.get("/")
async def root():
    return {"message": "Quordle Api"}


@app.post("/scores", status_code=status.HTTP_201_CREATED)
async def insert_score(req: ScoreBase, db: Session = db_dependency):
    db_score = models.Score(
        userId=req.userId,
        scoreDate=datetime.now(),
        score=req.score,
    )
    db.add(db_score)
    db.commit()
    return {"message": "Score added successfully"}

@app.get("/scores", status_code=status.HTTP_200_OK)
async def get_all_scores(db: Session = db_dependency):
    db_scores = db.query(models.Score).all()
    return db_scores

@app.get("/scores/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_scores(user_id: int, db: Session = db_dependency):
    scores = db.query(models.Score).filter(models.Score.userId == user_id).all()
    return scores
