from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db, require_teacher, get_current_user
from app.models.student import Student
from app.models.subject import Subject
from app.models.marks import Marks
from app.models.grade import Grade
from app.schemas.marks import MarksInput
from app.services.grading import calculate_grade

router = APIRouter(prefix="/grades", tags=["grades"])


@router.post("/")
def add_marks(
    data: MarksInput,
    db: Session = Depends(get_db),
    user: dict = Depends(require_teacher)
):
    # create student
    student = Student(name=data.name, student_class=data.student_class)
    db.add(student)
    db.commit()
    db.refresh(student)

    marks_list = []

    for subject_name, marks_value in data.subject_marks.items():
        subject = db.query(Subject).filter(Subject.name == subject_name).first()

        if not subject:
            subject = Subject(name=subject_name)
            db.add(subject)
            db.commit()
            db.refresh(subject)

        mark = Marks(
            student_id=student.id,
            subject_id=subject.id,
            marks=marks_value
        )
        db.add(mark)
        marks_list.append(marks_value)

    avg, grade_value = calculate_grade(marks_list)

    grade = Grade(
        student_id=student.id,
        average=avg,
        grade=grade_value
    )
    db.add(grade)

    db.commit()

    return {"message": "Marks added", "grade": grade_value}

@router.get("/")
def get_grades(
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    results = db.query(Student, Grade).join(Grade).all()

    return [
        {
            "name": s.name,
            "class": s.student_class,
            "average": g.average,
            "grade": g.grade
        }
        for s, g in results
    ]