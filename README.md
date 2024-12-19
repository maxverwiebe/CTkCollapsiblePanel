# CTkCollapsiblePanel

**CTkCollapsiblePanel** is a custom collapsible panel widget built on top of [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter). It provides a collapsible area to neatly show or hide content on demand, making your GUI more organized and space-efficient.

![grafik](https://github.com/user-attachments/assets/2ae78433-781c-439a-be8d-97e54c5a46e4)


## Features

- **Collapsible Content Area**: Users can toggle the visibility of the panel’s content by clicking a header button.
- **Theme Compatibility**: Adapts to CustomTkinter’s appearance settings (colors, fonts, modes).
- **Easy Content Addition**: Add any widgets (labels, buttons, entries, etc.) to the `_content_frame`.
- **Minimalistic API**: Simple integration into your existing CustomTkinter applications.

## Installation

Make sure [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) is installed:

```bash
pip install customtkinter
```

Then, simply add `CTkCollapsiblePanel.py` to your project or copy the class code into your own file.

## Usage

### Basic Example

```python
import customtkinter as ctk
from CTkCollapsiblePanel import *

if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # "System", "Dark", or "Light"
    app = ctk.CTk()
    app.title("Collapsible Panel Example")

    # Create a panel
    panel1 = CTkCollapsiblePanel(app, title="Panel 1")
    panel1.pack(fill="x", pady=10, padx=10)
    
    # Add content to the panel
    label = ctk.CTkLabel(panel1._content_frame, text="Content of Panel 1", anchor="w")
    label.pack(fill="x", padx=10, pady=5)

    app.mainloop()
```

### Adding More Content

To add more widgets, simply place them into `panel._content_frame`:

```python
panel2 = CTkCollapsiblePanel(app, title="Panel 2")
panel2.pack(fill="x", pady=10, padx=10)

extra_label = ctk.CTkLabel(panel2._content_frame, text="More content in Panel 2", anchor="w")
extra_label.pack(fill="x", padx=10, pady=5)
```

## Methods

### `toggle()`

- **Description**: Toggles the panel’s content visibility.
- **Usage**: Automatically called when the header button is clicked, but can also be called manually if needed.

### `_content_frame`

- **Description**: Contains the widgets displayed within the panel.
- **Access**:
  ```python
  panel = CTkCollapsiblePanel(app, title="Panel")
  # Add widgets inside the panel’s content frame
  panel._content_frame
  ```

## Customization

- **Title**: Set the panel’s title via the `title` parameter in the constructor.
- **Styles and Colors**: Since the panel inherits from `CTkFrame` and uses `CTkButton`, it will follow the theme settings from CustomTkinter. You can further customize colors, fonts, and other properties via the `configure` methods of the internal widgets.

For example, adjusting the font:

```python
panel1.header_button.configure(font=("Arial", 16, "italic"))
```

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for providing a great framework for creating modern and customizable GUI applications in Python.
