from sql_alchemy import Session
from src.schemas import schemas
from src.infra.sql_alchemy.models import models

class RepositoryUser():
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: schemas.user):
        db_user = models.user(id=user.id, name=user.name, email=user.email, telephone=user.telephone)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
        
    def read(self):
        users = self.db.query(models.user).all()
        return users

    def update(self):
        pass

    def delete(self):
        pass