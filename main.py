from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
import json
import datetime as dt

from fastapi.responses import JSONResponse

app = FastAPI()


class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType


class Timestamp(BaseModel):
    id: int
    timestamp: int


dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]


@app.get('/')
def root():
    # ваш код здесь
    return 'Добро пожаловать!'


@app.get('/dog/{pk}')
def get_dog_by_id(pk: int):
    res = dogs_db.get(pk)
    return JSONResponse(res.__dict__)


@app.post('/post')
def post_timestamp():
    new_timestamp = dt.datetime.now()
    new_TS = Timestamp(id=post_db[-1].id + 1, timestamp = int(round(new_timestamp.timestamp())))
    post_db.append(new_TS)
    return JSONResponse(post_db[-1].__dict__)

@app.get('/dog')
def get_dog(dog_kind: DogType):
  dogs_db_filtered =  {key: {"name": val.name, "pk": val.pk, "kind": val.kind.value} for key, val in dogs_db.items() if val.kind == dog_kind}
  return JSONResponse(dogs_db_filtered)

@app.post('/dog')
def post_new_dog(JSONstr:str):
  new_dogs = json.loads(JSONstr)
  for elem in new_dogs.items():
    if dogs_db.get(int(elem[0]), False) == False:
      dogs_db[int(elem[0])] = Dog(name=elem[1]['name'], pk=elem[1]['pk'], kind=elem[1]['kind'])
      return JSONResponse(new_dogs)
    else:
      return f'Error: dog with id {int(elem[0])} already exists.'