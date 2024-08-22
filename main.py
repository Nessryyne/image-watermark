import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image, ImageDraw, ImageFont
import os


def add_watermark(image_path, text):
    image = Image.open(image_path).convert("RGBA")
    width, height = image.size
    watermark = Image.new("RGBA", image.size)
    draw = ImageDraw.Draw(watermark)
    font = ImageFont.load_default()

    text_bbox = draw.textbbox((0, 0), text, font)
    textxidth, textheight = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    x, y = width - textxidth - 10, height - textheight - 10

    draw.text((x, y), text, font=font, fill=(255, 255, 128))
    return Image.alpha_composite(image, watermark)


def open_file():
    desktop_path = os.path.join(os.path.expanduser('~'), "Desktop")
    file_path = filedialog.askopenfilename(initialdir=desktop_path, title="Select an Image",
                                           filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        text = simpledialog.askstring("Input", "Enter watermark text:")
        if text:
            watermarked_image = add_watermark(file_path, text)
            save_path = filedialog.asksaveasfilename(defaultextension=".png")
            if save_path:
                watermarked_image.save(save_path)


app = tk.Tk()
app.title("Image Watermarking App")
app.geometry("300x100")

tk.Button(app, text="Open Image", command=open_file).pack(expand=True)
app.mainloop()
