import os
import tkinter as tk

# полный путь к PV файлу
full_path = __file__

# путь к папке с файлом 
directory_path = os.path.dirname(full_path)

image_path_ = os.path.join(directory_path, 'quiz')

images_path = os.path.join(image_path_, 'картинки')

image_path = os.path.join(images_path, '001.png')

window = tk.Tk()
photo_image = tk.PhotoImage(file=image_path)

tk.Label(window, image=photo_image).pack()

window.mainloop()
