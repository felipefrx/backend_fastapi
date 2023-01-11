from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.infra.sql_alchemy.config.database import get_db, create_db
from src.schemas.schemas import User
from src.infra.sql_alchemy.repositories.user import RepositoryUser


create_db()


app = FastAPI()


@app.get('/user')
def read_user():
    pass

@app.post('/user')
def create_user(user: User, db: Session = Depends(get_db) ):
    user_create = RepositoryUser().create(user)
    pass