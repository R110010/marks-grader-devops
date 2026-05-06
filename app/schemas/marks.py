from typing import Annotated
from pydantic import BaseModel, Field

MarkType = Annotated[int, Field(ge=0, le=100)]

class MarksInput(BaseModel):
    name: str
    student_class: str
    subject_marks: dict[str, MarkType]