from sqlalchemy.orm import Session
from app import models, schemas  # Mutlak import kullanımı

def create_car(db: Session, car: schemas.CarCreate):
    db_car = models.Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def get_cars(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Car).offset(skip).limit(limit).all()

def get_car(db: Session, car_id: int):
    return db.query(models.Car).filter(models.Car.id == car_id).first()

def delete_car(db: Session, car_id: int):
    db.query(models.Car).filter(models.Car.id == car_id).delete()
    db.commit()

def update_car(db: Session, car_id: int, car: schemas.CarUpdate):
    db.query(models.Car).filter(models.Car.id == car_id).update(car.dict())
    db.commit()
