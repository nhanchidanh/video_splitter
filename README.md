# Video Frame Extractor

Một ứng dụng GUI đơn giản để tách khung hình từ video thành các file ảnh PNG.

## ✨ Tính năng

- 🎬 Hỗ trợ nhiều định dạng video (MP4, AVI, MOV, MKV)
- ⚡ Giao diện đồ họa thân thiện với CustomTkinter
- 🕒 Tùy chỉnh khoảng thời gian tách khung hình (giây)
- 📊 Thanh tiến trình theo dõi quá trình xử lý
- 🖼️ Xuất ảnh PNG chất lượng cao
- 🎯 Đặt tên file tự động với thứ tự (frame_000001.png, frame_000002.png...)

## 🛠️ Yêu cầu hệ thống

- Python 3.7 trở lên
- Windows/macOS/Linux

## 📦 Cài đặt

## 🗜️ Đóng gói ứng dụng thành file .exe (Windows)

Bạn có thể đóng gói ứng dụng thành file thực thi (.exe) để dễ dàng chia sẻ mà không cần cài Python.

### Các bước thực hiện:

1. Kích hoạt môi trường ảo:
   ```powershell
   .venv\Scripts\activate
   ```
2. Cài đặt PyInstaller:
   ```powershell
   pip install pyinstaller
   ```
3. Đóng gói ứng dụng:

   ```powershell
   pyinstaller --onefile --windowed video_splitter.py
   ```

   - File .exe sẽ nằm trong thư mục `dist/` (ví dụ: `dist/video_splitter.exe`)
   - Tham số `--windowed` giúp ẩn cửa sổ console khi chạy app GUI
   - Không cần commit file .exe lên Git, đã có trong .gitignore

4. (Tuỳ chọn) Đổi icon cho app:

   ```powershell
   pyinstaller --onefile --windowed --icon=icon.ico video_splitter.py
   ```

   (Bạn cần chuẩn bị file icon.ico)

5. Nếu muốn build lại, hãy xoá thư mục `build/` và `dist/` trước khi chạy lại lệnh trên.

### Lưu ý:

- Chỉ cần commit source code, không commit file build (.exe, .spec, dist/)
- Nếu chia sẻ cho người dùng khác, chỉ cần gửi file .exe trong thư mục dist/

---

### Phương pháp 1: Sử dụng file run.bat (Windows)

1. Clone repository:

```bash
git clone https://github.com/nhanchidanh/video_splitter.git
cd video_splitter
```

2. Chạy file `run.bat` (double-click):
   - Tự động tạo virtual environment
   - Tự động cài đặt dependencies
   - Khởi chạy ứng dụng

### Phương pháp 2: Cài đặt thủ công

1. Clone repository:

```bash
git clone https://github.com/nhanchidanh/video_splitter.git
cd video_splitter
```

2. Tạo virtual environment:

```bash
python -m venv .venv
```

3. Kích hoạt virtual environment:

```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

4. Cài đặt dependencies:

```bash
pip install -r requirements.txt
```

5. Chạy ứng dụng:

```bash
python video_splitter.py
```

## 🚀 Cách sử dụng

1. **Chọn Video**: Nhấn nút "Chọn Video..." để chọn file video cần tách
2. **Chọn Thư Mục Lưu**: Nhấn nút "Chọn Thư Mục Lưu..." để chọn nơi lưu ảnh
3. **Đặt Khoảng Thời Gian**: Nhập số giây giữa mỗi khung hình được tách (VD: 1, 0.5, 2)
4. **Bắt Đầu**: Nhấn nút "Bắt Đầu Tách Khung Hình" và chờ hoàn tất

## 📸 Ví dụ Output

Sau khi xử lý, bạn sẽ có các file ảnh được đặt tên theo thứ tự:

```
frame_000001.png
frame_000002.png
frame_000003.png
...
```

## 🔧 Dependencies

- **customtkinter**: Thư viện GUI hiện đại cho Python
- **opencv-python**: Xử lý video và hình ảnh
- **tkinter**: GUI toolkit tích hợp sẵn trong Python

## 📁 Cấu trúc dự án

```
video_splitter/
├── video_splitter.py      # File chính của ứng dụng
├── run.bat               # Script khởi chạy tự động (Windows)
├── requirements.txt      # Danh sách dependencies
├── .gitignore           # Loại trừ files không cần thiết
└── README.md            # File hướng dẫn này
```

## 🐛 Báo lỗi

Nếu bạn gặp lỗi, vui lòng tạo issue trên GitHub với thông tin:

- Hệ điều hành
- Phiên bản Python
- Thông báo lỗi chi tiết
- Video định dạng gì đang xử lý

## 📄 License

Dự án này được phân phối dưới giấy phép MIT. Xem file `LICENSE` để biết thêm chi tiết.

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Vui lòng:

1. Fork dự án
2. Tạo branch cho tính năng mới (`git checkout -b feature/AmazingFeature`)
3. Commit thay đổi (`git commit -m 'Add some AmazingFeature'`)
4. Push lên branch (`git push origin feature/AmazingFeature`)
5. Tạo Pull Request

## 💡 Ý tưởng phát triển

- [ ] Hỗ trợ nhiều định dạng ảnh output (JPG, WEBP)
- [ ] Tùy chọn chất lượng ảnh
- [ ] Preview khung hình trước khi lưu
- [ ] Batch processing nhiều video
- [ ] Tích hợp AI để chọn khung hình "đẹp" nhất

---

⭐ Nếu dự án hữu ích, hãy cho một star trên GitHub!
