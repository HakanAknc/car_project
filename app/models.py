from sqlalchemy import Column, Integer, String
from app.database import Base  # Mutlak import kullanıyoruz

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    marka = Column(String, index=True)
    seri = Column(String, index=True)
    renk = Column(String)
    yil = Column(Integer)
    yakit = Column(String)
    durum = Column(String)
    kilometre = Column(Integer)
    motor_gucu = Column(Integer)

