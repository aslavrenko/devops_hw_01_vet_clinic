from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
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

# ваш код здесь
def my_filtering_function(pair):
    wanted_key = dog_kind
    key, value = pair
    if value.kind == wanted_key:
        return True  # filter pair out of the dictionary
    else:
        return False  # keep pair in the filtered dictionary


# grades = {'John': 7.8, 'Mary': 9.0, 'Matt': 8.6, 'Michael': 9.5}

#@app.get('/dog')
#def get_dogs(dk: string):
#    # ваш код здесь
#    dog_kind = dk
#    filtered_dog = dict(filter(my_filtering_function, dogs_db.items()))
#    return JSONResponse(content=filtered_dog)

@app.get('/dog/{pk}')
def get_dog_by_id(pk: int):
    res = dogs_db.get(pk)
    return res
