import customtkinter as ctk
from tkinter import filedialog, messagebox
import cv2
import os
import threading

class VideoSplitterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Cấu hình cửa sổ chính ---
        self.title("Trình Tách Khung Hình Video")
        self.geometry("700x450")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1) # Dành không gian cho thanh trạng thái

        # --- Biến lưu trữ đường dẫn ---
        self.video_path = ctk.StringVar()
        self.output_folder = ctk.StringVar()

        # --- Giao diện người dùng ---
        self.create_widgets()

    def create_widgets(self):
        # --- Frame chính ---
        main_frame = ctk.CTkFrame(self, corner_radius=10)
        main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        main_frame.grid_columnconfigure(1, weight=1)

        # 1. Chọn file video
        select_video_btn = ctk.CTkButton(main_frame, text="Chọn Video...", command=self.select_video)
        select_video_btn.grid(row=0, column=0, padx=15, pady=15, sticky="w")
        self.video_path_label = ctk.CTkLabel(main_frame, text="Chưa chọn file video nào", text_color="gray", wraplength=450, justify="left")
        self.video_path_label.grid(row=0, column=1, padx=15, pady=15, sticky="w")

        # 2. Chọn thư mục lưu ảnh
        select_folder_btn = ctk.CTkButton(main_frame, text="Chọn Thư Mục Lưu...", command=self.select_output)
        select_folder_btn.grid(row=1, column=0, padx=15, pady=15, sticky="w")
        self.output_folder_label = ctk.CTkLabel(main_frame, text="Chưa chọn thư mục nào", text_color="gray", wraplength=450, justify="left")
        self.output_folder_label.grid(row=1, column=1, padx=15, pady=15, sticky="w")

        # 3. Nhập số giây
        interval_label = ctk.CTkLabel(main_frame, text="Tách mỗi (giây):")
        interval_label.grid(row=2, column=0, padx=15, pady=15, sticky="w")
        self.interval_entry = ctk.CTkEntry(main_frame, placeholder_text="Ví dụ: 1 hoặc 0.5")
        self.interval_entry.grid(row=2, column=1, padx=15, pady=15, sticky="ew")
        self.interval_entry.insert(0, "1") # Giá trị mặc định

        # 4. Nút bắt đầu
        self.start_button = ctk.CTkButton(self, text="Bắt Đầu Tách Khung Hình", height=40, font=("", 14, "bold"), command=self.start_processing_thread)
        self.start_button.grid(row=1, column=0, padx=20, pady=(0, 10))

        # 5. Thanh tiến trình
        self.progress_bar = ctk.CTkProgressBar(self, mode='determinate')
        self.progress_bar.set(0)
        self.progress_bar.grid(row=2, column=0, padx=20, pady=5, sticky="ew")

        # 6. Thanh trạng thái
        self.status_label = ctk.CTkLabel(self, text="Sẵn sàng", text_color="gray")
        self.status_label.grid(row=3, column=0, padx=20, pady=(0, 10), sticky="w")

    def select_video(self):
        file_path = filedialog.askopenfilename(
            title="Chọn file video",
            filetypes=(("Video files", "*.mp4 *.avi *.mov *.mkv"), ("All files", "*.*"))
        )
        if file_path:
            self.video_path.set(file_path)
            self.video_path_label.configure(text=os.path.basename(file_path), text_color="white")

    def select_output(self):
        folder_path = filedialog.askdirectory(title="Chọn thư mục để lưu ảnh")
        if folder_path:
            self.output_folder.set(folder_path)
            self.output_folder_label.configure(text=folder_path, text_color="white")

    def start_processing_thread(self):
        # Chạy tác vụ xử lý trong một luồng riêng để không làm treo giao diện
        processing_thread = threading.Thread(target=self.process_video)
        processing_thread.daemon = True # Thoát luồng khi chương trình chính đóng
        processing_thread.start()

    def process_video(self):
        video_file = self.video_path.get()
        output_dir = self.output_folder.get()
        interval_str = self.interval_entry.get()

        # --- Kiểm tra đầu vào ---
        if not video_file or not output_dir:
            messagebox.showerror("Lỗi", "Vui lòng chọn cả file video và thư mục lưu trữ.")
            return

        try:
            interval_sec = float(interval_str)
            if interval_sec <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Lỗi", "Số giây phải là một số lớn hơn 0.")
            return

        # --- Vô hiệu hóa nút và cập nhật trạng thái ---
        self.start_button.configure(state="disabled", text="Đang xử lý...")
        self.status_label.configure(text="Đang mở video...")
        self.progress_bar.set(0)

        try:
            # --- Bắt đầu xử lý ---
            cap = cv2.VideoCapture(video_file)
            if not cap.isOpened():
                raise IOError("Không thể mở file video.")

            fps = cap.get(cv2.CAP_PROP_FPS) # Lấy số khung hình trên giây
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            frame_interval = int(fps * interval_sec) # Số khung hình cần bỏ qua

            if frame_interval == 0:
                frame_interval = 1 # Đảm bảo luôn lấy ít nhất 1 khung hình

            current_frame = 0
            saved_frame_count = 0
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break # Kết thúc video

                if current_frame % frame_interval == 0:
                    saved_frame_count += 1
                    # Tạo tên file ảnh với số thứ tự, ví dụ: frame_000001.png
                    file_name = f"frame_{saved_frame_count:06d}.png"
                    save_path = os.path.join(output_dir, file_name)
                    cv2.imwrite(save_path, frame)

                current_frame += 1
                
                # Cập nhật thanh tiến trình
                progress = current_frame / total_frames
                self.progress_bar.set(progress)
                self.status_label.configure(text=f"Đã xử lý {current_frame}/{total_frames} khung hình...")

            cap.release()
            self.status_label.configure(text=f"Hoàn tất! Đã lưu {saved_frame_count} ảnh vào thư mục.", text_color="lightgreen")

        except Exception as e:
            self.status_label.configure(text=f"Lỗi: {e}", text_color="red")
            messagebox.showerror("Lỗi Xử Lý", str(e))
        finally:
            # --- Kích hoạt lại nút ---
            self.start_button.configure(state="normal", text="Bắt Đầu Tách Khung Hình")

if __name__ == "__main__":
    app = VideoSplitterApp()
    app.mainloop()
