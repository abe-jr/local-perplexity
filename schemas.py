from pydantic import BaseModel
from typing import List




class QueryResult(BaseModel):
    title: str = None
    url: str = None
    resume: str = None

class QueryResponse(BaseModel):
    user_input: str = None
    final_respose: str = None
    queries: List[str] = []
