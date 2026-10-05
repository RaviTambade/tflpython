from dataclasses import dataclass

@dataclass
class Policy:
    id:int
    name:str
    description:str
    maturity:str
    premium:float