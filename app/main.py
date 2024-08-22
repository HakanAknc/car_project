from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas  # Mutlak import kullanımı
from app.database import SessionLocal, engine

# Veritabanı tablolarını oluştur
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/cars/", response_model=schemas.Car)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    return crud.create_car(db=db, car=car)

@app.get("/cars/", response_model=list[schemas.Car])
def read_cars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_cars(db, skip=skip, limit=limit)

@app.get("/cars/{car_id}", response_model=schemas.Car)
def read_car(car_id: int, db: Session = Depends(get_db)):
    db_car = crud.get_car(db, car_id=car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

@app.delete("/cars/{car_id}")
def delete_car(car_id: int, db: Session = Depends(get_db)):
    crud.delete_car(db=db, car_id=car_id)
    return {"message": "Car deleted successfully"}

@app.put("/cars/{car_id}", response_model=schemas.Car)
def update_car(car_id: int, car: schemas.CarUpdate, db: Session = Depends(get_db)):
    crud.update_car(db=db, car_id=car_id, car=car)
    updated_car = crud.get_car(db=db, car_id=car_id)
    if updated_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return updated_car
