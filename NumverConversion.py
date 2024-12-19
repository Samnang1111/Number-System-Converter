import tkinter as tk
from tkinter import ttk, messagebox

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number System Converter")
        self.root.geometry("400x350")
        self.root.configure(bg="#E8F0FE")

        self.canvas = tk.Canvas(self.root, bg="#E8F0FE", height=350, width=400)
        self.canvas.pack()

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Number System Converter", font=("Helvetica", 16, "bold"), bg="#E8F0FE")
        self.canvas.create_window(200, 30, window=self.title_label)

        # Conversion Type Label
        self.label = tk.Label(self.root, text="Select Conversion Type:", font=("Helvetica", 12, "bold"), bg="#E8F0FE")
        self.canvas.create_window(200, 80, window=self.label)

        # Conversion Options
        self.conversion_type = tk.StringVar()
        self.conversion_options = ttk.Combobox(self.root, textvariable=self.conversion_type, font=("Helvetica", 12), width=20)
        self.conversion_options['values'] = [
            "Binary to Decimal",
            "Decimal to Binary",
            "Decimal to Octal",
            "Octal to Decimal",
            "Hexadecimal to Binary",
            "Binary to Hexadecimal"
        ]
        self.canvas.create_window(200, 120, window=self.conversion_options)

        # Input Entry
        self.input_label = tk.Label(self.root, text="Enter Value:", font=("Helvetica", 12), bg="#E8F0FE")
        self.canvas.create_window(200, 160, window=self.input_label)
        self.input_entry = tk.Entry(self.root, font=("Helvetica", 12), bg="#FFFFFF")
        self.canvas.create_window(200, 190, window=self.input_entry)

        # Convert Button
        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert, font=("Helvetica", 12, "bold"), bg="#007BFF", fg="white")
        self.canvas.create_window(200, 230, window=self.convert_button)

        # Result Label
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12, "bold"), bg="#FFFFFF")
        self.canvas.create_window(200, 270, window=self.result_label)

    def binary_to_decimal(self, binary_str):
        """Convert Binary to Decimal Number System."""
        if not all(bit in '01' for bit in binary_str):
            raise ValueError("Input must be a binary string containing only 0s and 1s.")
        decimal_value = 0
        for bit in binary_str:
            decimal_value = decimal_value * 2 + int(bit)
        return decimal_value

    def decimal_to_binary(self, decimal_num):
        """Convert Decimal to Binary Number System."""
        binary_value = ""
        while decimal_num > 0:
            binary_value = str(decimal_num % 2) + binary_value
            decimal_num = decimal_num // 2
        return binary_value or "0"

    def decimal_to_octal(self, decimal_num):
        """Convert Decimal to Octal Number System."""
        decimal_num = int(decimal_num)
        octal_value = ""
        if decimal_num == 0:
            return "0"
        while decimal_num > 0:
            octal_value = str(decimal_num % 8) + octal_value
            decimal_num = decimal_num // 8
        return octal_value

    def octal_to_decimal(self, octal_str):
        """Convert Octal to Decimal Number System."""
        decimal_value = 0
        for digit in octal_str:
            decimal_value = decimal_value * 8 + int(digit)
        return decimal_value

    def hexadecimal_to_binary(self, hex_str):
        """Convert Hexadecimal to Binary Number System."""
        hex_str = hex_str.lower().replace('0x', '')
        if not hex_str:
            raise ValueError("Input cannot be empty.")
        
        try:
            # Convert hexadecimal to decimal
            decimal_value = int(hex_str, 16)
        except ValueError:
            raise ValueError("Input must be a valid hexadecimal number.")

        # Convert decimal to binary and remove any leading zeros
        binary_value = bin(decimal_value)[2:]  # Strip the '0b' prefix
        return binary_value  # Return without adding extra leading zeros


    def binary_to_hexadecimal(self, binary_str):
        """Convert Binary to Hexadecimal Number System."""
        decimal_value = int(binary_str, 2)
        hexadecimal_value = hex(decimal_value)[2:]
        return hexadecimal_value.upper()

    def convert(self):
        conversion_type = self.conversion_type.get()
        input_value = self.input_entry.get()

        # Check if the conversion type is selected and input value is provided
        if not conversion_type:
            messagebox.showwarning("Input Error", "Please select a conversion type.")
            return
        elif not input_value:
            messagebox.showwarning("Input Error", "Please enter a value to convert.")
            return

        try:
            # Proceed with the conversion based on the selected type
            if conversion_type == "Binary to Decimal":
                result = self.binary_to_decimal(input_value)
                self.result_label.config(text=f"Result: {result}")

            elif conversion_type == "Decimal to Binary":
                decimal_num = int(input_value)
                result = self.decimal_to_binary(decimal_num)
                self.result_label.config(text=f"Result: {result}")

            elif conversion_type == "Decimal to Octal":
                result = self.decimal_to_octal(input_value)
                self.result_label.config(text=f"Result: {result}")

            elif conversion_type == "Octal to Decimal":
                result = self.octal_to_decimal(input_value)
                self.result_label.config(text=f"Result: {result}")

            elif conversion_type == "Hexadecimal to Binary":
                result = self.hexadecimal_to_binary(input_value)
                self.result_label.config(text=f"Result: {result}")

            elif conversion_type == "Binary to Hexadecimal":
                result = self.binary_to_hexadecimal(input_value)
                self.result_label.config(text=f"Result: {result}")

        except ValueError as e:
            messagebox.showerror("Error", str(e))

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()
