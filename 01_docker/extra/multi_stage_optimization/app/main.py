from datetime import datetime
from typing import List
from uuid import uuid4
from fastapi import FastAPI, Depends

from database import Session, BikeRides

app = FastAPI()

conn = None


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.get("/", status_code=200)
async def root(db: Session = Depends(get_db)) -> List[BikeRides]:
    rows = (
        db
            .query(BikeRides)
            .order_by(BikeRides.created.desc())
            .all()
    )
    return rows


@app.get("/rent/", status_code=201)
async def insert_rental(name: str, location: str, db: Session = Depends(get_db)) -> BikeRides:
    db_user = BikeRides(uuid=str(uuid4()), name=name, location=location, created=datetime.now())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/healthz", status_code=200)
async def healthz():
    return "healthy!"
