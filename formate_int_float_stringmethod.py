# FORMATING OF INTEGER

# using f-string

value = 123456789

# Default formatting
formatted = f"{value}"
print(formatted)                                        # Output: 123456789

# Including commas as thousand separators
formatted = f"{value:,}"
print(formatted)                                        # Output: 123,456,789

# Padding with zeros (width 10)
formatted = f"{value:010}"
print(formatted)                                        # Output: 0123456789

# Padding with spaces (width 10)
formatted = f"{value:10}"
print(formatted)                                        # Output:  123456789

# Binary format
formatted = f"{value:b}"
print(formatted)                                        # Output: 111010110111100110100010101

# Hexadecimal format
formatted = f"{value:x}"
print(formatted)                                        # Output: 75bcd15

# Octal format
formatted = f"{value:o}"
print(formatted)                                        # Output: 726746425


# using "format()" method

value = 123456789

# Default formatting
formatted = "{}".format(value)
print(formatted)                                        # Output: 123456789

# Including commas as thousand separators
formatted = "{:,}".format(value)
print(formatted)                                        # Output: 123,456,789

# Padding with zeros (width 10)
formatted = "{:010}".format(value)
print(formatted)                                        # Output: 0123456789

# Padding with spaces (width 10)
formatted = "{:10}".format(value)
print(formatted)                                        # Output:  123456789

# Binary format
formatted = "{:b}".format(value)
print(formatted)                                        # Output: 111010110111100110100010101

# Hexadecimal format
formatted = "{:x}".format(value)
print(formatted)                                        # Output: 75bcd15

# Octal format
formatted = "{:o}".format(value)
print(formatted)                                        # Output: 726746425


# using " % " operator

value = 123456789

# Default formatting
formatted = "%d" % value
print(formatted)                                        # Output: 123456789

# Including commas as thousand separators (requires a workaround)
formatted = "%d" % value
formatted = "{:,}".format(int(formatted))
print(formatted)                                        # Output: 123,456,789

# Padding with zeros (width 10)
formatted = "%010d" % value
print(formatted)                                        # Output: 0123456789

# Padding with spaces (width 10)
formatted = "%10d" % value
print(formatted)                                        # Output:  123456789

# Binary format (requires a workaround)
formatted = bin(value)[2:]
print(formatted)                                        # Output: 111010110111100110100010101

# Hexadecimal format
formatted = "%x" % value
print(formatted)                                        # Output: 75bcd15

# Octal format
formatted = "%o" % value
print(formatted)                                        # Output: 726746425



# FORMATING OF FLOAT

# using f-string :

value = 1234.56789

# Default formatting
formatted = f"{value}"
print(formatted)                                        # Output: 1234.56789

# Specifying the number of decimal places
formatted = f"{value:.2f}"
print(formatted)                                        # Output: 1234.57

# Including commas as thousand separators
formatted = f"{value:,.2f}"
print(formatted)                                        # Output: 1,234.57

# Scientific notation
formatted = f"{value:.2e}"
print(formatted)                                        # Output: 1.23e+03


# using format() method

value = 1234.56789

# Default formatting
formatted = "{}".format(value)
print(formatted)                                        # Output: 1234.56789

# Specifying the number of decimal places
formatted = "{:.2f}".format(value)
print(formatted)                                        # Output: 1234.57

# Including commas as thousand separators
formatted = "{:,.2f}".format(value)
print(formatted)                                        # Output: 1,234.57

# Scientific notation
formatted = "{:.2e}".format(value)
print(formatted)                                        # Output: 1.23e+03


# using " % " operator

value = 1234.56789

# Default formatting
formatted = "%f" % value
print(formatted)                                        # Output: 1234.567890

# Specifying the number of decimal places
formatted = "%.2f" % value
print(formatted)                                        # Output: 1234.57

# Including commas as thousand separators (requires a workaround)
formatted = "%0.2f" % value
formatted = "{:,}".format(float(formatted))
print(formatted)                                        # Output: 1,234.57

# Scientific notation
formatted = "%.2e" % value
print(formatted)                                        # Output: 1.23e+03


