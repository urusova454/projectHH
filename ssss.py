from pydantic import BaseModel
from typing import Optional

class Breed(BaseModel):
    name: str
    estimation: int

class Cats(BaseModel):
    name: str
    breed: Optional[Breed]

tom = Cats(name = "Tom", breed = Breed(name = "Tom", estimation = 5))
values = {"name":"Tom","breed":{"name":"Siam","estimation":5}}
tom1 = Cats(**values)
print(tom1.get)
