from tkinter import  *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
root = Tk()
root.title("Hệ thống quản lý sinh viên")
root.geometry("600x800")
#kết nối tới db
conn = sqlite3.connect('student_book.db')
c = conn.cursor()
# #Tạo bảng để lưu trữ
# c.execute('''
#     CREATE TABLE student(
#          id INTEGER PRIMARY KEY AUTOINCREMENT,
#          firstName text,
#          lastName text,
#          classes text,
#          yearAdmission integer,
#          averagePoint float
#          )
# '''
# )
def them():
    # Kết nối và lấy dữ liệu
    conn = sqlite3.connect('student_book.db')
    c = conn.cursor()
    # Lấy dữ liệu đã nhập
    id_value = id.get()
    firstName_value = firstName.get()
    lastName_value = lastName.get()
    classes_value = classes.get()
    yearAdmission_value = yearAdmission.get()
    averagePoint_value = averagePoint.get()
    # Thực hiện câu lệnh để thêm
    c.execute('''
        INSERT INTO student (id, firstName, lastName, classes, yearAdmission, averagePoint)
        VALUES (:id, :name, :last_name, :classes, :yearAdmission, :averagePoint)
    ''', {
        'id': id_value,
        'name': firstName_value,
        'last_name': lastName_value,
        'classes': classes_value,
        'yearAdmission': yearAdmission_value,
        'averagePoint': averagePoint_value,
    })
    conn.commit()
    conn.close()
    # Reset form
    id_value.delete(0, END)
    firstName_value.delete(0, END)
    lastName_value.delete(0, END)
    classes_value.delete(0, END)
    yearAdmission_value.delete(0, END)
    averagePoint_value.delete(0, END)

    # Hien thi lai du lieu
    truy_van()

def xoa():
    # Kết nối và lấy dữ liệu
    conn = sqlite3.connect('student_book.db')
    c = conn.cursor()
    c.execute('''DELETE FROM
                        student 
                      WHERE id=:id''',
              {'id':delete_box.get()})
    delete_box.delete(0, END)
    conn.commit()
    conn.close()
    # Hiên thi thong bao
    messagebox.showinfo("Thông báo", "Đã xóa!")
    # Hiển thị lại dữ liệu
    truy_van()


def truy_van():
    # Xóa đi các dữ liệu trong TreeView
    for row in tree.get_children():
        tree.delete(row)

    # Kết nối và lấy dữ liệu
    conn = sqlite3.connect('student_book.db')
    c = conn.cursor()
    c.execute("SELECT * FROM student")
    records = c.fetchall()

    # Hien thi du lieu
    for r in records:
        tree.insert("", END, values=(r[0], r[1], r[2]))

    # Ngat ket noi
    conn.close()
def chinh_sua():
    global editor
    editor = Tk()
    editor.title('Cập nhật bản ghi')
    editor.geometry("400x200")

    conn = sqlite3.connect('student_book.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM addresses WHERE id=:id", {'id':record_id})
    records = c.fetchall()

    global f_id_editor, f_name_editor, l_name_editor, class_editor, yearAdmission_editor, averagePoint_editor

    f_id_editor = Entry(editor, width=30)
    f_id_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=1, column=1, padx=20)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=2, column=1)
    class_editor = Entry(editor, width=30)
    class_editor.grid(row=3, column=1)
    yearAdmission_editor = Entry(editor, width=30)
    yearAdmission_editor.grid(row=4, column=1)
    averagePoint_editor = Entry(editor, width=30)
    averagePoint_editor.grid(row=5, column=1)

    f_id_label = Label(editor, text="Mã số sinh viên")
    f_id_label.grid(row=0, column=0, pady=(10, 0))
    f_name_label = Label(editor, text="Họ")
    f_name_label.grid(row=1, column=0)
    l_name_label = Label(editor, text="Tên")
    l_name_label.grid(row=2, column=0)
    class_label = Label(editor, text="Lớp")
    class_label.grid(row=3, column=0)
    yearAdmission_label = Label(editor, text="Năm nhập học")
    yearAdmission_label.grid(row=4, column=0)
    averagePoint_label = Label(editor, text="Điểm trung bình")
    averagePoint_label.grid(row=5, column=0)


    for record in records:
        f_id_editor.insert(0, record[0])
        f_name_editor.insert(0, record[1])
        l_name_editor.insert(0, record[2])
        class_editor.insert(0, record[3])
        yearAdmission_editor.insert(0, record[4])
        averagePoint_editor.insert(0, record[5])

    edit_btn = Button(editor, text="Lưu bản ghi", command=cap_nhat)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)
def cap_nhat():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    record_id = f_id_editor.get()

    c.execute("""UPDATE addresses SET
           first_name = :first,
           last_name = :last,
           address = :address,
           city = :city,
           state = :state,
           zipcode = :zipcode
           WHERE id = :id""",
              {
                  'id': record_id,
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'class': class_editor.get(),
                  'yearAdmission': yearAdmission_editor.get(),
                  'averagerPoint': averagePoint_editor.get()
              })

    conn.commit()
    conn.close()
    editor.destroy()

    # Cập nhật lại danh sách bản ghi sau khi chỉnh sửa
    truy_van()
# Khung cho các ô nhập liệu
input_frame = Frame(root)
input_frame.pack(pady=10)

# Các ô nhập liệu cho cửa sổ chính
id = Entry(input_frame, width=30)
id.grid(row=0, column=1, padx=20, pady=(10, 0))
firstName = Entry(input_frame, width=30)
firstName.grid(row=1, column=1)
lastName = Entry(input_frame, width=30)
lastName.grid(row=2, column=1)
classes = Entry(input_frame, width=30)
classes.grid(row=3, column=1)
yearAdmission = Entry(input_frame, width=30)
yearAdmission.grid(row=4, column=1)
averagePoint = Entry(input_frame, width=30)
averagePoint.grid(row=5, column=1)

# Các nhãn
f_id_label = Label(input_frame, text="Mã số sinh viên")
f_id_label.grid(row=0, column=0, pady=(10, 0))
f_name_label = Label(input_frame, text="Họ")
f_name_label.grid(row=1, column=0)
l_name_label = Label(input_frame, text="Tên")
l_name_label.grid(row=2, column=0)
classes_label = Label(input_frame, text="Lớp")
classes_label.grid(row=3, column=0)
yearAdmission_label = Label(input_frame, text="Năm nhập học")
yearAdmission_label.grid(row=4, column=0)
averagePoint_label = Label(input_frame, text="Điểm trung bình")
averagePoint_label.grid(row=5, column=0)

# Khung cho các nút chức năng
button_frame = Frame(root)
button_frame.pack(pady=10)

# Các nút chức năng
submit_btn = Button(button_frame, text="Thêm thông tin sinh viên", command=them)
submit_btn.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
query_btn = Button(button_frame, text="Hiển thị thông tin sinh viên", command=truy_van)
query_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
delete_box_label = Label(button_frame, text="Chọn Mã số sinh viên")
delete_box_label.grid(row=2, column=0, pady=5)
delete_box = Entry(button_frame, width=30)
delete_box.grid(row=2, column=1, pady=5)
delete_btn = Button(button_frame, text="Xóa thông tin sinh viên", command=xoa)
delete_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=136)
edit_btn = Button(button_frame, text="Chỉnh sửa thông tin sinh viên", command=chinh_sua)
edit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

# Khung cho Treeview
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Treeview để hiển thị bản ghi
columns = ("ID", "Họ", "Tên")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=15)
for column in columns:
    tree.column(column, anchor=CENTER) # This will center text in rows
    tree.heading(column, text=column)
tree.pack()

# Định nghĩa tiêu đề cho các cột
for col in columns:
    tree.heading(col, text=col)

# Gọi hàm truy vấn để hiển thị bản ghi khi khởi động
truy_van()

root.mainloop()