from sqlalchemy.orm import Session
import models

def get_recommendations(user_id: int, db: Session):
    user_books = db.query(models.ReadingHistory.book_id).filter(models.ReadingHistory.user_id == user_id).all()
    user_books = {b[0] for b in user_books}

    similar_users = db.query(models.ReadingHistory.user_id).filter(models.ReadingHistory.book_id.in_(user_books)).distinct().all()
    similar_users = {u[0] for u in similar_users}

    recommended_books = db.query(models.ReadingHistory.book_id).filter(models.ReadingHistory.user_id.in_(similar_users)).distinct().all()
    recommended_books = [b[0] for b in recommended_books if b[0] not in user_books]

    return db.query(models.Book).filter(models.Book.id.in_(recommended_books)).all()
