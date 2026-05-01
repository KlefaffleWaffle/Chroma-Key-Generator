
import tkinter as tk
from tkinter import ttk
 
class ColorPickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Picker")
        #self.root.geometry("500x400")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(True, True)
 
        # Color values
        self.r = tk.IntVar(value=99)
        self.g = tk.IntVar(value=102)
        self.b = tk.IntVar(value=241)
 
        # Panel open state
        self.panel_open = False
        self.panel_frame = None
 
        # Top bar
        topbar = tk.Frame(self.root, bg="#16213e", height=50)
        topbar.pack(fill="x", side="top")
        topbar.pack_propagate(False)
       

        title = tk.Label(
            topbar,
            bg="#16213e", fg="#e2e8f0",
            font=("Georgia", 14, "italic")
        )

        title.pack(side="left", padx=20, pady=12)
 
        # Palette button (upper right)
        self.btn = tk.Button(
            topbar,
            text="🎨  Palette",
            command=self.toggle_panel,
            bg="#6366f1",
            fg="white",
            font=("Helvetica", 10, "bold"),
            relief="flat",
            padx=14,
            pady=6,
            cursor="hand2",
            activebackground="#4f46e5",
            activeforeground="white",
            bd=0
        )
        self.btn.pack(side="right", padx=16, pady=9)
 

            ######### Main Area to focus on
        # Main preview area

        color = self.get_color()
        self.preview_canvas = tk.Canvas(
            self.root, bg=color, highlightthickness=0
        )
        self.preview_canvas.pack(fill="both", expand=True)
        self.draw_preview()
 
        # Trace changes
        for var in (self.r, self.g, self.b):
            var.trace_add("write", lambda *_: self.draw_preview())
 
    def toggle_panel(self):
        if self.panel_open:
            self.close_panel()
        else:
            self.open_panel()
 
    def open_panel(self):
        self.panel_open = True
        self.btn.config(text="✕  Close")
 
        self.panel_frame = tk.Frame(
            self.root, bg="#0f3460", bd=0,
            highlightthickness=1, highlightbackground="#6366f1"
        )
        self.panel_frame.place(relx=1.0, rely=0.0, anchor="ne", x=-16, y=58)
 
        header = tk.Label(
            self.panel_frame, text="RGB  SLIDERS",
            bg="#0f3460", fg="#94a3b8",
            font=("Courier", 9, "bold"),
            padx=20, pady=10
        )
        header.pack(fill="x")
 
        sep = tk.Frame(self.panel_frame, bg="#6366f1", height=1)
        sep.pack(fill="x")
 
        sliders_frame = tk.Frame(self.panel_frame, bg="#0f3460", padx=20, pady=16)
        sliders_frame.pack()
 
        channels = [
            ("R", self.r, "#f87171"),
            ("G", self.g, "#4ade80"),
            ("B", self.b, "#60a5fa"),
        ]
 
        for name, var, color in channels:
            row = tk.Frame(sliders_frame, bg="#0f3460")
            row.pack(fill="x", pady=6)
 
            lbl = tk.Label(
                row, text=name, bg="#0f3460", fg=color,
                font=("Courier", 11, "bold"), width=2
            )
            lbl.pack(side="left")
 
            style_name = f"{name}.Horizontal.TScale"
            style = ttk.Style()
            style.theme_use("clam")
            style.configure(
                style_name,
                background="#0f3460",
                troughcolor="#1e3a5f",
                sliderlength=18,
                sliderrelief="flat",
            )
 
            slider = ttk.Scale(
                row, from_=0, to=255, orient="horizontal",
                variable=var, length=180, style=style_name
            )
            slider.pack(side="left", padx=10)
 
            val_lbl = tk.Label(
                row, textvariable=var, bg="#0f3460", fg="#e2e8f0",
                font=("Courier", 10), width=4
            )
            val_lbl.pack(side="left")
 
        # Hex display
        sep2 = tk.Frame(self.panel_frame, bg="#334155", height=1)
        sep2.pack(fill="x", padx=20)
 
        hex_row = tk.Frame(self.panel_frame, bg="#0f3460", padx=20, pady=12)
        hex_row.pack(fill="x")
 
        tk.Label(
            hex_row, text="HEX", bg="#0f3460", fg="#94a3b8",
            font=("Courier", 9, "bold")
        ).pack(side="left")
 
        self.hex_var = tk.StringVar()
        self.update_hex()
        for var in (self.r, self.g, self.b):
            var.trace_add("write", lambda *_: self.update_hex())
 
        hex_lbl = tk.Label(
            hex_row, textvariable=self.hex_var,
            bg="#0f3460", fg="#6366f1",
            font=("Courier", 12, "bold")
        )
        hex_lbl.pack(side="right")
 
    def close_panel(self):
        self.panel_open = False
        self.btn.config(text="🎨  Palette")
        if self.panel_frame:
            self.panel_frame.destroy()
            self.panel_frame = None
 
    def get_color(self):
        return f"#{self.r.get():02x}{self.g.get():02x}{self.b.get():02x}"
 
    def update_hex(self):
        if hasattr(self, "hex_var"):
            self.hex_var.set(self.get_color().upper())
 
    def draw_preview(self):
        self.preview_canvas.delete("all")
        w = self.preview_canvas.winfo_width()
        h = self.preview_canvas.winfo_height()
 
        color = self.get_color()
        r, g, b = self.r.get(), self.g.get(), self.b.get()
 
      
        #strip_color = f"#{bg_r:02x}{bg_g:02x}{bg_b:02x}"
        self.preview_canvas.create_rectangle(
            0, 0, w, h,
            fill=color, outline=""
        )
        
       
        '''
        # Hex label below circle
        self.preview_canvas.create_text(
            w//2, 80,
            text=color.upper(),
            fill="#e2e8f0",
            font=("Courier", 16, "bold")
        )
        

        # RGB label
        self.preview_canvas.create_text(
            w//2, 106,
            #text=f"rgb({r}, {g}, {b})",
            fill="#94a3b8",
            font=("Courier", 10)
        )
        '''
        
 
 
if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPickerApp(root)
    root.mainloop()