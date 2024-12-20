import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os
import platform

# 상수 정의
APP_TITLE = "이미지 워터마킹 앱"
INITIAL_WINDOW_SIZE = "1000x1000"
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FONT_SIZE = 36
WATERMARK_FILL = (255, 255, 255, 128)
PADDING = 10
BUTTON_WIDTH = 20
SUPPORTED_FILE_TYPES = [("이미지 파일", "*.png *.jpg *.jpeg *.bmp *.gif")]

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry(INITIAL_WINDOW_SIZE)

        self.image = None
        self.tk_image = None

        self.create_widgets()

    def create_widgets(self):
        self.create_upload_section()
        self.create_text_entry_section()
        self.create_position_selection()
        self.create_watermark_button()
        self.create_canvas()
        self.create_save_button()

    def create_upload_section(self):
        upload_frame = tk.Frame(self.root)
        upload_frame.pack(pady=PADDING)

        upload_btn = tk.Button(upload_frame, text="이미지 업로드", command=self.upload_image, width=BUTTON_WIDTH)
        upload_btn.pack()

    def create_text_entry_section(self):
        text_frame = tk.Frame(self.root)
        text_frame.pack(pady=PADDING)

        tk.Label(text_frame, text="워터마크 텍스트:").pack(side='left')
        self.text_entry = tk.Entry(text_frame, width=50)
        self.text_entry.pack(side='left', padx=5)

    def create_position_selection(self):
        position_frame = tk.Frame(self.root)
        position_frame.pack(pady=PADDING)

        tk.Label(position_frame, text="워터마크 위치:").pack(side='left', padx=5)
        self.position_var = tk.StringVar(value="bottom-right")
        positions = ["top-left", "top-right", "bottom-left", "bottom-right", "center"]
        for pos in positions:
            tk.Radiobutton(position_frame, text=pos.replace("-", " ").title(),
                           variable=self.position_var, value=pos).pack(side='left', padx=5)

    def create_watermark_button(self):
        watermark_frame = tk.Frame(self.root)
        watermark_frame.pack(pady=PADDING)

        add_watermark_btn = tk.Button(watermark_frame, text="워터마크 추가",
                                      command=self.add_watermark, width=BUTTON_WIDTH)
        add_watermark_btn.pack()

    def create_canvas(self):
        canvas_frame = tk.Frame(self.root)
        canvas_frame.pack(pady=PADDING)

        self.canvas = tk.Canvas(canvas_frame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='grey')
        self.canvas.pack()

    def create_save_button(self):
        save_frame = tk.Frame(self.root)
        save_frame.pack(pady=PADDING)

        save_btn = tk.Button(save_frame, text="이미지 저장", command=self.save_image, width=BUTTON_WIDTH)
        save_btn.pack()

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=SUPPORTED_FILE_TYPES)
        if file_path:
            try:
                self.image = Image.open(file_path).convert("RGBA")
                self.display_image(self.image)
            except Exception as e:
                messagebox.showerror("오류", f"이미지를 불러오는 중 오류가 발생했습니다.\n{e}")

    def display_image(self, img):
        img_for_display = img.copy()
        img_for_display.thumbnail((CANVAS_WIDTH, CANVAS_HEIGHT))
        self.tk_image = ImageTk.PhotoImage(img_for_display)
        self.canvas.delete("all")
        self.canvas.create_image(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, image=self.tk_image)

    def add_watermark(self):
        if not self.image:
            messagebox.showwarning("경고", "먼저 이미지를 업로드하세요.")
            return

        text = self.text_entry.get()
        if not text:
            messagebox.showwarning("경고", "워터마크 텍스트를 입력하세요.")
            return

        watermarked = self.image.copy()
        draw = ImageDraw.Draw(watermarked)

        font = self.get_font()

        text_width, text_height = self.get_text_size(draw, text, font)

        x, y = self.calculate_position(watermarked.size, text_width, text_height)

        draw.text((x, y), text, font=font, fill=WATERMARK_FILL)

        self.image = watermarked
        self.display_image(self.image)
        messagebox.showinfo("성공", "워터마크가 추가되었습니다.")

    def get_font(self):
        font_path = self.get_system_font_path()
        try:
            return ImageFont.truetype(font_path, FONT_SIZE)
        except IOError:
            return ImageFont.load_default()

    def get_system_font_path(self):
        system = platform.system()
        if system == "Darwin":
            possible_fonts = ["/Library/Fonts/Arial.ttf", "/Library/Fonts/Helvetica.ttf"]
        elif system == "Windows":
            possible_fonts = [os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts", "arial.ttf"),
                              os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts", "Helvetica.ttf")]
        else:
            possible_fonts = ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                              "/usr/share/fonts/truetype/freefont/FreeSans.ttf"]

        for font in possible_fonts:
            if os.path.exists(font):
                return font
        return ""

    def get_text_size(self, draw, text, font):
        try:
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
        except AttributeError:
            text_width, text_height = draw.textsize(text, font=font)
        return text_width, text_height

    def calculate_position(self, image_size, text_width, text_height):
        width, height = image_size
        position = self.position_var.get()

        if position == "top-left":
            x, y = 10, 10
        elif position == "top-right":
            x, y = width - text_width - 10, 10
        elif position == "bottom-left":
            x, y = 10, height - text_height - 10
        elif position == "bottom-right":
            x, y = width - text_width - 10, height - text_height - 10
        elif position == "center":
            x, y = (width - text_width) / 2, (height - text_height) / 2
        else:
            x, y = 10, 10

        return x, y

    def save_image(self):
        if not self.image:
            messagebox.showwarning("경고", "저장할 이미지가 없습니다.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG 파일", "*.png"), ("JPEG 파일", "*.jpg;*.jpeg"), ("모든 파일", "*.*")]
        )
        if file_path:
            try:
                self.image.save(file_path)
                messagebox.showinfo("성공", f"이미지가 저장되었습니다:\n{file_path}")
            except Exception as e:
                messagebox.showerror("오류", f"이미지를 저장하는 중 오류가 발생했습니다.\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
