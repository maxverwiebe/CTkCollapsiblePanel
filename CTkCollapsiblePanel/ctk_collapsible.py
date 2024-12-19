import customtkinter as ctk

class CTkCollapsiblePanel(ctk.CTkFrame):
    def __init__(self, master, title="Section", *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.title = title
        self._collapsed = True

        self.header_frame = ctk.CTkFrame(self)
        self.header_frame.pack(fill="x")

        self._content_frame = ctk.CTkFrame(self)

        header_button_fg = self._content_frame.cget("fg_color")
        
        self.header_button = ctk.CTkButton(
            self.header_frame,
            text="▸ " + self.title,
            command=self.toggle,
            corner_radius=0,
            anchor="w",
            font=("Arial", 20, 'bold'),
            fg_color=header_button_fg,
            hover_color=header_button_fg,
            text_color=("#2e2e2e", "#ebebeb")
        )
        self.header_button.pack(fill="x", padx=5, pady=2)

    def toggle(self):
        if self._collapsed:
            self._content_frame.pack(fill="x", expand=False)
            self.header_button.configure(text="▾ " + self.title)
        else:
            self._content_frame.pack_forget()
            self.header_button.configure(text="▸ " + self.title)
        self._collapsed = not self._collapsed
