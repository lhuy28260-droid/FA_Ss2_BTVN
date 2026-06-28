from fastapi import FastAPI

app = FastAPI(title="Hệ thống Quản lý Sách - API Routing")


# 1. Xem danh sách sách
@app.get("/books")
def get_all_books():
    return {
        "message": "Lấy danh sách sách thành công",
        "data": [
            {"id": 1, "title": "Python Basic", "quantity": 12},
            {"id": 2, "title": "FastAPI Beginner", "quantity": 3}
        ]
    }

# 2. Xem chi tiết sách
@app.get("/books/detail")
def get_book_detail():
    return {
        "message": "Lấy chi tiết sách thành công",
        "data": {"id": 1, "title": "Python Basic", "quantity": 12}
    }

# 3. Thêm sách mới
@app.post("/books/create")
def create_new_book():
    return {
        "message": "Thêm mới sách thành công",
        "data": {"id": 3, "title": "New Book Mock", "quantity": 1}
    }

# 4. Cập nhật thông tin sách
@app.put("/books/update")
def update_existing_book():
    return {
        "message": "Cập nhật thông tin sách thành công",
        "data": {"id": 1, "title": "Python Basic (Updated)", "quantity": 15}
    }

# 5. Xóa sách
@app.delete("/books/delete")
def delete_existing_book():
    return {
        "message": "Xóa sách thành công",
        "deleted_id": 2
    }

# 6. Xem thống kê sách
@app.get("/books/dashboard/stats")
def get_books_statistics():
    return {
        "message": "Lấy dữ liệu thống kê hệ thống thành công",
        "statistics": {
            "total_books": 2,
            "low_stock_count": 1,
            "out_of_stock_count": 0
        }
    }


@app.get("/books/newest")
def get_newest_books():
    return {
        "message": "Lấy danh sách sách mới cập nhật thành công",
        "data": [
            {"id": 8, "title": "AI and Machine Learning 2026", "quantity": 5}
        ]
    }

# 8. Xem danh sách sách bán chạy (Popular)
@app.get("/books/popular")
def get_popular_books():
    return {
        "message": "Lấy danh sách sách được mượn/mua nhiều nhất thành công",
        "data": [
            {"id": 3, "title": "Clean Code", "quantity": 5, "views": 1250}
        ]
    }