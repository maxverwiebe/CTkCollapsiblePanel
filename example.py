import customtkinter as ctk
from CTkCollapsiblePanel import *

if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # "System", "Dark", "Light"
    app = ctk.CTk()
    app.title("Collapsible Panel Example with Content")

    panel1 = CollapsiblePanel(app, title="Panel 1")
    panel1.pack(fill="x", pady=10, padx=10)
    
    # use panel1._content_frame to do add controls

    panel2 = CollapsiblePanel(app, title="Panel 2")
    extra_label = ctk.CTkLabel(panel2._content_frame, text="CONTENT HERE", anchor="w")
    extra_label.pack(fill="x", padx=10, pady=5)

    panel2.pack(fill="x", pady=10, padx=10)

    app.mainloop()
