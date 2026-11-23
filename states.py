import os

# 1st way to create a state (most common approach)

from typing import TypedDict

class State(TypedDict):
    topic : str
    summary : str
    score : int
    
    
# 2nd way pydantic approach 
# it is good at data validation and type checking at runtime

from pydantic import BaseModel, field_validator

class State2(BaseModel):
    topic : str
    summary : str = ''
    score : int
    
    @field_validator
    def score_positive(cls,v):
        if v < 0:
            raise ValueError('score must be positive')
        
        
# 3rd way Python dataclasses (v.low usage)

from dataclasses import dataclass, field

@dataclass
class State3:
    topic : str = ''
    summary : str = ''
    messages : list = field(default_factory=list)
    
    
#4th way using langgraph

from langgraph.graph import MessagesState

class State4(MessagesState):
    topic : str
    summary : str
    score : int
    