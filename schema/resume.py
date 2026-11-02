from pydantic import BaseModel


class Improve(BaseModel):
    instructions: str

class Tailor(BaseModel):
    job_description:str

class AtsScore(BaseModel):
    job_description: str