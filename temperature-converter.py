import customtkinter as ctk 

def f_to_c(f: float) -> str:
    """
    Convert temperature from Fahrenheit to Celsius.

    Args:
        f (float): The temperature in Fahrenheit.

    Returns:
        str: The temperature in Celsius, formatted with two decimal places.
    """
    c = (f - 32) * 5 / 9
    return f"{c:.2f} °C"

def c_to_f(c: float) -> str:
    """
    Convert temperature in Celsius to Fahrenheit.

    Args:
        c: A float or integer representing the temperature in Celsius.

    Returns:
        A string representing the temperature in Fahrenheit with two decimal places.
    """
    f = c * 9 / 5 + 32
    return f"{f:.2f}°F"

def convert_temperature() -> None:
    """
    Converts temperature from Fahrenheit to Celsius or from Celsius to Fahrenheit based on the user's choice.

    Returns:
        None

    Raises:
        None
    """
    choice = selected_value.get()
    temperature = float(temp_entry.get())

    if choice.lower() == "c":
        result_text = f_to_c(temperature)
        label_result.configure(text = result_text, text_color = "green", font = ctk.CTkFont(size=20, weight="bold"))
    else:
        result_text = c_to_f(temperature)
        label_result.configure(text = result_text, text_color = "green", font = ctk.CTkFont(size=20, weight="bold"))


# Starting UI 
# Init
app = ctk.CTk()
# App's title
app.title('Temperature Converter')
# Set color mode
ctk.set_appearance_mode("dark")
# Window size
app.geometry("600x400")
# Title in window
title_label = ctk.CTkLabel(app, text="Temperature Converter", font= ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(30,20))

# Radio button frame
radio_frame = ctk.CTkFrame(app)
radio_frame.pack(fill="x", padx=50)

selected_value = ctk.StringVar(value="C")

radio_button_f2c = ctk.CTkRadioButton(radio_frame, text="Fahrenheit to Celsius", variable = selected_value, value = "C")
radio_button_f2c.pack(side="left", padx=(80,10), pady=10)

radio_button_c2f = ctk.CTkRadioButton(radio_frame, text="Celsius to Fahrenheit", variable = selected_value, value = "F")
radio_button_c2f.pack(side="left", padx=10, pady=10)

# Input frame
input_frame = ctk.CTkFrame(app)
input_frame.pack(fill = "x", padx = 50, pady = 30)

temp_entry = ctk.CTkEntry(input_frame, placeholder_text="enter temperature ....")
temp_entry.pack(side = "left", padx = (80,10), pady = (20))

convert_button = ctk.CTkButton(input_frame, text="Convert", command=convert_temperature)
convert_button.pack(side = "left", padx = 10, pady = 20)

# Result Frame
result_frame = ctk.CTkFrame(app)
result_frame.pack(fill = "x", padx = 50)

label_result = ctk.CTkLabel(result_frame, text = "")
label_result.pack()


# Init last ,i.e, between  app = ctk.CTk() and app.mainloop() define UI component of parent "app".
app.mainloop()