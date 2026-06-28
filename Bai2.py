from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "An"},
    {"id": 2, "name": "Binh"},
    {"id": 3, "name": "Cuong"}
]

# SỬA LỖI:
# - Endpoint đúng chuẩn RESTful số nhiều: "/students"
# - Tên hàm rõ nghĩa, dễ hiểu: get_all_students
@app.get("/students")
def get_all_students():
    # - API trả về toàn bộ danh sách sinh viên (không lấy index [0])
    return students