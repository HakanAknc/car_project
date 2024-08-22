from pydantic import BaseModel

class CarBase(BaseModel):
    marka: str
    seri: str
    renk: str
    yil: int
    yakit: str
    durum: str
    kilometre: int
    motor_gucu: int

class CarCreate(CarBase):
    pass  # Yeni bir araba kaydı oluşturmak için kullanılır.

class CarUpdate(CarBase):
    pass  # Mevcut bir araba kaydını güncellemek için kullanılır.

class Car(CarBase):
    id: int

    class Config:
        orm_mode = True  # SQLAlchemy modelleriyle uyumlu hale getirir.
