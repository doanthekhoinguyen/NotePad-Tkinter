
import tkinter
from PIL import ImageTk, Image
from tkinter import StringVar, IntVar, scrolledtext, END, messagebox, filedialog, Label, Toplevel

class NotePadApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Note Pad')
        self.root.iconbitmap('iconnotepad.ico')
        self.root.geometry('650x650')
        self.root.resizable(True, True)

        # Define font & color
        self.text_color = "#fffacd"
        self.menu_color = "#dbd9db"
        self.root_color = "#6c9a8f"
        self.root.config(bg=self.root_color)

        # Define font options
        self.font_family = StringVar()
        self.font_size = IntVar()
        self.font_option = StringVar()
        self.font_family.set('Terminal')
        self.font_size.set(12)
        self.font_option.set('none')

        # Define frame
        # Create menu frame and text frame
        self.menu_frame = tkinter.Frame(self.root, bg=self.menu_color)
        self.text_frame = tkinter.Frame(self.root, bg=self.text_color)
        self.menu_frame.pack(padx=5, pady=5)
        self.text_frame.pack(padx=5, pady=5)

        # Create menu buttons
        self.create_menu_buttons()
        self.create_font_dropdowns()

        # Create text input area
        self.create_text_input()

    
    #define funcion
    #create menu: new, open, save, close ,font family, fontsize, font opinion
    def create_menu_buttons(self):
        new_image = ImageTk.PhotoImage(Image.open('new.png'))
        new_button = tkinter.Button(self.menu_frame, image=new_image, command=self.new_note)
        new_button.image = new_image
        new_button.grid(row=0, column=0, padx=5, pady=5)

        open_image = ImageTk.PhotoImage(Image.open('open.png'))
        open_button = tkinter.Button(self.menu_frame, image=open_image, command=self.open_note)
        open_button.image = open_image
        open_button.grid(row=0, column=1, padx=5, pady=5)

        save_image = ImageTk.PhotoImage(Image.open('save.png'))
        save_button = tkinter.Button(self.menu_frame, image=save_image, command=self.save_note)
        save_button.image = save_image
        save_button.grid(row=0, column=2, padx=5, pady=5)

        close_image = ImageTk.PhotoImage(Image.open('close.png'))
        close_button = tkinter.Button(self.menu_frame, image=close_image, command=self.close_note)
        close_button.image = close_image
        close_button.grid(row=0, column=3, padx=5, pady=5)

        help_button = tkinter.Button(self.menu_frame, text="Hướng dẫn", command=self.show_help)
        help_button.grid(row=0, column=4, padx=5, pady=5)

    def create_font_dropdowns(self):
        # create list of fonts
        families = ['Terminal', 'Modern', 'Roman', 'Script', 'Arial', 'Javanese Text', 'Times New Roman']
        font_family_drop = tkinter.OptionMenu(self.menu_frame, self.font_family, *families, command=self.change_font)
        font_family_drop.config(width=16)
        font_family_drop.grid(row=0, column=5, padx=5, pady=5)
        #create list of size
        sizes = [8, 10, 12, 14, 16, 20, 24, 28, 32, 64]
        font_size_drop = tkinter.OptionMenu(self.menu_frame, self.font_size, *sizes, command=self.change_font)
        font_size_drop.config(width=2)
        font_size_drop.grid(row=0, column=6, padx=5, pady=5)
        #create list of style text
        options = ['none', 'bold', 'italic']
        font_option_drop = tkinter.OptionMenu(self.menu_frame, self.font_option, *options, command=self.change_font)
        font_option_drop.config(width=5)
        font_option_drop.grid(row=0, column=7, padx=5, pady=5)

    def create_text_input(self):
        my_font = (self.font_family.get(), self.font_size.get())
        self.text_input = scrolledtext.ScrolledText(self.text_frame, width=1000, height=100, bg=self.text_color,font=my_font)
        self.text_input.pack()

    def change_font(self, event=None):
        if self.font_option.get() == 'none':
            my_font = (self.font_family.get(), self.font_size.get())
        else:
            my_font = (self.font_family.get(), self.font_size.get(), self.font_option.get())

        self.text_input.config(font=my_font)

    def new_note(self):
        question = messagebox.askyesno("New Note:", "Bạn có chắc muốn bắt đầu một ghi chú mới?")
        if question == 1:
            self.text_input.delete("1.0", END)

    def close_note(self):
        question = messagebox.askyesno("Close Note:", "Bạn có chắc muốn đóng ghi chú?")
        if question == 1:
            self.root.destroy()

    def save_note(self):
        save_name = filedialog.asksaveasfilename(initialdir="./", title="Save Note",filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        with open(save_name, 'w') as f:
            f.write(self.font_family.get() + "\n")
            f.write(str(self.font_size.get()) + "\n")
            f.write(self.font_option.get() + "\n")
            f.write(self.text_input.get("1.0", END))

    def open_note(self):
        open_name = filedialog.askopenfilename(initialdir="./", title="Open Note",filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        with open(open_name, 'r') as f:
            self.text_input.delete("1.0", END)

            self.font_family.set(f.readline().strip())
            self.font_size.set(int(f.readline().strip()))
            self.font_option.set(f.readline().strip())

            self.change_font()

            text = f.read()
            self.text_input.insert("1.0", text)

    def show_help(self):
        help_window = Toplevel(self.root)
        help_window.title("Hướng dẫn sử dụng")
        help_window.geometry("400x200")

        help_label = Label(help_window, text="Hướng dẫn sử dụng ứng dụng Note Pad:\n1. Để bắt đầu ghi chú mới, nhấn nút 'New'.\n2. Để mở một ghi chú đã lưu, nhấn nút 'Open'.\n3. Để lưu ghi chú hiện tại, nhấn nút 'Save'.\n4. Để đóng ứng dụng, nhấn nút 'Close'.\n5. Bạn có thể thay đổi font và kích thước font bằng các dropdown.",font=("Helvetica", 10), justify="left")
        help_label.pack()

if __name__ == "__main__":
    root = tkinter.Tk()
    app = NotePadApp(root)
    root.mainloop()
