from fastapi import FastAPI

app = FastAPI()

# Danh sách sinh viên gốc
students = ["An", "Binh", "Cuong"]

# (2) SỬA LỖI: 
# - Đổi endpoint sang chuẩn RESTful: dùng danh từ số nhiều '/students' thay vì '/getStudents'
@app.get("/students")
def get_students():
    # - Đảm bảo trả về JSON array đúng chuẩn bằng cách return trực tiếp list Python
    # - Không sử dụng string concat (cộng chuỗi) để trả dữ liệu
    return students