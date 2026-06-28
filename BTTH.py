from fastapi import FastAPI, HTTPException, status

app = FastAPI()

courses = [
    {
        "id": 1,
        "code": "PY101",
        "name": "Python Basic",
        "level": "beginner",
        "price": 1500000
    },
    {
        "id": 2,
        "code": "FA101",
        "name": "FastAPI Basic",
        "level": "beginner",
        "price": 2000000
    },
    {
        "id": 3,
        "code": "JS101",
        "name": "JavaScript Advanced",
        "level": "intermediate",
        "price": 2500000
    }
]

@app.get("/health")
def check_health():
    return {"message": "API is running"}

@app.get("/courses")
def get_all_courses():
    return courses

@app.get("/courses/{course_id}")
def get_course_detail(course_id: int):
    if course_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID khóa học phải là số nguyên dương lớn hơn 0"
        )
    
    for course in courses:
        if course["id"] == course_id:
            return course
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Không tìm thấy khóa học với ID {course_id}"
    )