from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# ------- Define models:
class StoreLocation(Base):
    __tablename__ = "store_locations"
    __table_args__ = {"schema": "sbp"}
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, nullable=False)
    name = Column(String, nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)

class CityPopulation(Base):
    __tablename__ = "city_population"
    __table_args__ = {"schema": "sbp"}
    city = Column(String, primary_key=True, index=True)
    total = Column(String, nullable=False)
    age_0_5 = Column(Float, nullable=False)
    age_6_18 = Column(Float, nullable=False)
    age_19_45 = Column(Float, nullable=False)
    age_46_55 = Column(Float, nullable=False)
    age_56_64 = Column(Float, nullable=False)
    age_65 = Column(Float, nullable=False)

class CityTransportation(Base):
    __tablename__ = "city_transportation"
    __table_args__ = {"schema": "sbp"}
    stationid = Column(Integer, primary_key=True, index=True)
    city = Column(String, nullable=False)
    stationoperatortypename = Column(String, nullable=False)
    stationtypename = Column(String, nullable=False)
    lat = Column(Float, nullable=False)
    long = Column(Float, nullable=False)

class CityShoppingCenter(Base):
    __tablename__ = "shopping_center"
    __table_args__ = {"schema": "sbp"}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    remarks = Column(String, nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)

class FutureBusiness(Base):
    __tablename__ = "future_business"
    __table_args__ = {"schema": "sbp"}
    id = Column(Integer, primary_key=True, index=True)
    plandisgn = Column(String, nullable=False)
    shape_area = Column(Float, nullable=False)
    internet = Column(String, nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)

class CityArnona(Base):
    __tablename__ = "arnona"
    __table_args__ = {"schema": "sbp"}
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

# ------- Define models response:
class StoreLocationResponse(BaseModel):
    id: int
    city: str
    name: str
    lat: float
    lon: float

    class Config:
        from_attributes = True

class CityPopulationResponse(BaseModel):
    city: str
    total: int
    age_0_5: int
    age_6_18: int
    age_19_45: int
    age_46_55: int
    age_56_64: int
    age_65: int

    class Config:
        from_attributes = True

class CityTransportationResponse(BaseModel):
    city: str
    stationtypename: str
    lat: float
    long: float

    class Config:
        from_attributes = True

class CityShoppingCenterResponse(BaseModel):
    id: int
    name: str
    remarks: str
    lat: float
    lon: float

    class Config:
        from_attributes = True

class FutureBusinessResponse(BaseModel):
    id: int
    plandisgn: str
    shape_area: float
    internet: str
    lat: float
    lon: float

    class Config:
        from_attributes = True

class CityArnonaResponse(BaseModel):
    id: int
    city: str
    year: int
    price: float

    class Config:
        from_attributes = True

# ------- application:
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint to fetch store locations by city
@app.get("/store-locations/{city}", response_model=list[StoreLocationResponse])
def get_store_locations(city: str):
    db = SessionLocal()
    locations = db.query(StoreLocation).filter(StoreLocation.city == city).all()
    db.close()
    if not locations:
        raise HTTPException(status_code=404, detail="No locations found for this city")
    return locations

# Endpoint to fetch population by city
@app.get("/city-population/{city}", response_model=list[CityPopulationResponse])
def get_city_population(city: str):
    db = SessionLocal()
    population = db.query(CityPopulation).filter(CityPopulation.city == city).all()
    db.close()
    if not population:
        raise HTTPException(status_code=404, detail="No locations found for this city")
    return population

# Endpoint to fetch city transportations
@app.get("/city-transportation/{city}/{stationoperatortypename}", response_model=list[CityTransportationResponse])
def get_city_transportation(city: str, stationoperatortypename: str):
    db = SessionLocal()
    operators = db.query(CityTransportation).filter(
        CityTransportation.city == city,
        CityTransportation.stationoperatortypename == stationoperatortypename
    ).all()
    db.close()
    if not operators:
        raise HTTPException(status_code=404, detail="No station operators found for this city and type")
    return operators

# Endpoint to fetch shopping centers
@app.get("/city-shopping-center/", response_model=list[CityShoppingCenterResponse])
def get_shopping_center():
    db = SessionLocal()
    population = db.query(CityShoppingCenter).all()
    db.close()
    if not population:
        raise HTTPException(status_code=404, detail="No shopping center found.")
    return population

# Endpoint to fetch future business
@app.get("/future-business/", response_model=list[FutureBusinessResponse])
def get_future_business():
    db = SessionLocal()
    population = db.query(FutureBusiness).all()
    db.close()
    if not population:
        raise HTTPException(status_code=404, detail="No future business found.")
    return population

@app.get("/city-arnona/{city}", response_model=list[CityArnonaResponse])
def get_city_arnona(city: str):
    db = SessionLocal()
    operators = db.query(CityArnona).filter(
        CityArnona.city == city
    ).all()
    db.close()
    if not operators:
        raise HTTPException(status_code=404, detail="No Arnona prices found for this city and type")
    return operators

