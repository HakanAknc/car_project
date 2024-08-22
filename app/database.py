import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL bağlantı bilgileri
DATABASE_NAME = ""
USER_NAME = ""
PASSWORD = ""
HOST_IP = ""
HOST_PORT = ""

# Varsayılan veritabanına bağlan
default_connection = psycopg2.connect(
    database="postgres",
    user=USER_NAME,
    password=PASSWORD,
    host=HOST_IP,
    port=HOST_PORT
)

default_connection.autocommit = True
cursor = default_connection.cursor()

# Veritabanının var olup olmadığını kontrol et
cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{DATABASE_NAME}'")
exists = cursor.fetchone()

# Veritabanı yoksa oluştur
if not exists:
    cursor.execute(f"CREATE DATABASE {DATABASE_NAME}")
    print(f"Veritabanı '{DATABASE_NAME}' başarıyla oluşturuldu.")
else:
    print(f"Veritabanı '{DATABASE_NAME}' zaten mevcut.")

# Varsayılan bağlantıyı kapat
cursor.close()
default_connection.close()

# SQLAlchemy bağlantı ayarları
