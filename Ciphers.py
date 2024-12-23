import tkinter as tk
from tkinter import ttk
import base64

def perform_cipher():
    cipher = cipher_var.get()
    m = text_entry.get()
    k = key_entry.get() if key_entry.get() else None
    mode = mode_var.get()
    r = ""

    if cipher == "Caesar" and k is not None:
        r = caesar_cipher(m, k, mode)
    elif cipher == "Pig Pen":
        r = pig_pen_cipher(m, mode)
    elif cipher == "Atbash":
        r = atbash_cipher(m)
    elif cipher == "Rail Fence" and k is not None:
        r = rail_fence_cipher(m, k, mode)
    elif cipher == "Polybius":
        r = polybius_cipher(m, mode)
    elif cipher == "Bifid":
        r = bifid_cipher(m, mode)
    elif cipher == "Vigenere" and k is not None:
        r = vigenere_cipher(m, k, mode)
    elif cipher == "Columnar Transposition" and k is not None:
        r = columnar_transposition_cipher(m, k, mode)
    elif cipher == "Morse Code":
        r = morse_code_cipher(m, mode)
    elif cipher == "Base64":
        r = base64_cipher(m, mode)
    elif cipher == "Affine" and k is not None:
        r = affine_cipher(m, k, mode)
    
    result_var.set(r)

def caesar_cipher(m, k, mode):
    k = int(k) 
    r = ""
    for i in m:
        if i.isalpha():
            if i.isupper():
                shift = (ord(i) + k - 65) % 26 + 65 if mode == "Encrypt" else (ord(i) - k - 65) % 26 + 65
            else:
                shift = (ord(i) + k - 97) % 26 + 97 if mode == "Encrypt" else (ord(i) - k - 97) % 26 + 97
            r += chr(shift)
        else:
            r += i
    return r

def pig_pen_cipher(m, mode):
    pigpen_dict = {
        'A': '⍁', 'B': '⍂', 'C': '⍃', 'D': '⍄', 'E': '⍅', 'F': '⍆',
        'G': '⍇', 'H': '⍈', 'I': '⍉', 'J': '⍊', 'K': '⍋', 'L': '⍌',
        'M': '⍍', 'N': '⍎', 'O': '⍏', 'P': '⍐', 'Q': '⍑', 'R': '⍒',
        'S': '⍓', 'T': '⍔', 'U': '⍕', 'V': '⍖', 'W': '⍗', 'X': '⍘',
        'Y': '⍙', 'Z': '⍚',
        'a': '⍛', 'b': '⍜', 'c': '⍝', 'd': '⍞', 'e': '⍟', 'f': '⍠',
        'g': '⍡', 'h': '⍢', 'i': '⍣', 'j': '⍤', 'k': '⍥', 'l': '⍦',
        'm': '⍧', 'n': '⍨', 'o': '⍩', 'p': '⍪', 'q': '⍫', 'r': '⍬',
        's': '⍭', 't': '⍮', 'u': '⍯', 'v': '⍰', 'w': '⍱', 'x': '⍲',
        'y': '⍳', 'z': '⍴'
    }
    if mode=="Encrypt":
        r = ""
        for char in m:
            r += pigpen_dict.get(char, char)
    elif mode=="Decrypt":
        r = ""
        for char in m:
            for k, value in pigpen_dict.items():
                if char == value:
                    r += k
                    break
            else:
                r += char
    return r


def atbash_cipher(m):
    r = ""
    for i in m:
        if i.isalpha():
            if i.isupper():
                r += chr(65 + (25 - (ord(i) - 65)))
            else:
                r += chr(97 + (25 - (ord(i) - 97)))
        else:
            r += i
    return r

def rail_fence_cipher(m, k, mode):
    k=int(k)
    if mode == "Encrypt":
        rail = [['\n' for i in range(len(m))] for j in range(k)]
        dir_down = False
        row, col = 0, 0

        for i in range(len(m)):
            if row == 0 or row == k - 1:
                dir_down = not dir_down
            rail[row][col] = m[i]
            col += 1
            row += 1 if dir_down else -1

        r = []
        for i in range(k):
            for j in range(len(m)):
                if rail[i][j] != '\n':
                    r.append(rail[i][j])
        return "".join(r)

    elif mode == "Decrypt":
        rail = [['\n' for i in range(len(m))] for j in range(k)]
        dir_down = None
        row, col = 0, 0

        for i in range(len(m)):
            if row == 0:
                dir_down = True
            if row == k - 1:
                dir_down = False
            rail[row][col] = '*'
            col += 1
            row += 1 if dir_down else -1

        index = 0
        for i in range(k):
            for j in range(len(m)):
                if rail[i][j] == '*' and index < len(m):
                    rail[i][j] = m[index]
                    index += 1
        
        r = []
        row, col = 0, 0
        for i in range(len(m)):
            if row == 0:
                dir_down = True
            if row == k - 1:
                dir_down = False
            if rail[row][col] != '*':
                r.append(rail[row][col])
                col += 1
            row += 1 if dir_down else -1

        return "".join(r)
    return


def polybius_cipher(m, mode):
    polybius_dict = {
        'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
        'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '24', 'K': '25',
        'L': '31', 'M': '32', 'N': '33', 'O': '34', 'P': '35', 
        'Q': '41', 'R': '42', 'S': '43', 'T': '44', 'U': '45',
        'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55'
    }
    r = ""
    if mode == "Encrypt":
       
        for char in m:
            if char.isalpha():
                r += polybius_dict[char.upper()]
            else:
                r += char
        return r

    elif mode == "Decrypt":
        i = 0
        while i < len(m):
            if m[i].isdigit() and i + 1 < len(m) and m[i + 1].isdigit():
                r += [k for k, value in polybius_dict.items() if value == m[i:i + 2]][0]
                i += 2
            else:
                r += m[i]
                i += 1
        return r
    return

def bifid_cipher(m, mode):
    bifid_square = [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'K'],
        ['L', 'M', 'N', 'O', 'P'],
        ['Q', 'R', 'S', 'T', 'U'],
        ['V', 'W', 'X', 'Y', 'Z']
    ]

    def get_coordinates(char):
        for row in range(5):
            for col in range(5):
                if bifid_square[row][col] == char:
                    return row, col
        return None

    def get_char(row, col):
        return bifid_square[row][col]

    m = m.replace('J', 'I').upper()
    coordinates = []

    if mode == "Encrypt":
        for char in m:
            if char.isalpha():
                row, col = get_coordinates(char)
                coordinates.append(row)
                coordinates.append(col)

        rows = coordinates[::2]
        cols = coordinates[1::2]

        combined = rows + cols
        r = ""
        for i in range(0, len(combined), 2):
            r += get_char(combined[i], combined[i + 1])

    elif mode == "Decrypt":
        for char in m:
            if char.isalpha():
                row, col = get_coordinates(char)
                coordinates.append(row)
                coordinates.append(col)

        half_len = len(coordinates) // 2
        rows = coordinates[:half_len]
        cols = coordinates[half_len:]

        r = ""
        for i in range(half_len):
            r += get_char(rows[i], cols[i])

    return r

def vigenere_cipher(m, k, mode):
    r = ""
    if k is not None:
        k = k.upper()
    key_index = 0

    for i in m:
        if i.isalpha():
            if i.isupper():
                shift = (ord(i) + ord(k[key_index]) - 130) % 26 + 65 if mode == "Encrypt" else (ord(i) - ord(k[key_index]) + 26) % 26 + 65
            else:
                shift = (ord(i) + ord(k[key_index]) - 194) % 26 + 97 if mode == "Encrypt" else (ord(i) - ord(k[key_index]) + 26) % 26 + 97
            r += chr(shift)
            key_index = (key_index + 1) % len(k)
        else:
            r += i
    return r

def columnar_transposition_cipher(m, k, mode):
    key_indices = sorted(range(len(k)), key=lambda x: k[x])
    num_cols = len(k)
    num_rows = len(m) // num_cols + (len(m) % num_cols != 0)

    if mode == "Encrypt":
        matrix = ['' for _ in range(num_cols)]
        for index, char in enumerate(m):
            matrix[index % num_cols] += char

        r = ''
        for col in key_indices:
            r += matrix[col]
        return r

    elif mode == "Decrypt":
        col_lengths = [len(m) // num_cols + (1 if i < len(m) % num_cols else 0) for i in range(num_cols)]
        matrix = ['' for _ in range(num_cols)]
        index = 0

        for col in key_indices:
            for _ in range(col_lengths[col]):
                matrix[col] += m[index]
                index += 1

        r = ''
        for i in range(num_rows):
            for col in range(num_cols):
                if i < len(matrix[col]):
                    r += matrix[col][i]
        return r
    return

def morse_code_cipher(m, mode):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        ' ': '/'
    }

    if mode == "Encrypt":
        r = " ".join([morse_code_dict.get(i.upper(), '') for i in m])
    elif mode == "Decrypt":
        r = "".join([k for char in m.split() for k, value in morse_code_dict.items() if value == char])
    return r

def base64_cipher(m, mode):
    if mode == "Encrypt":
        r = base64.b64encode(m.encode()).decode()
    elif mode == "Decrypt":
        r = base64.b64decode(m.encode()).decode()
    return r

def affine_cipher(m, k, mode):
    try:
        a, b = map(int, k.split(','))
    except ValueError:
        raise ValueError("Key must be two integers separated by a comma.")

    r = ""

    def mod_inverse(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    if mode == "Decrypt":
        a_inv = mod_inverse(a, 26)
        if a_inv is None:
            raise ValueError("Invalid key, 'a' has no modular inverse.")
    
    for i in m:
        if i.isalpha():
            if mode == "Encrypt":
                shift = (a * (ord(i.upper()) - 65) + b) % 26 + 65
            else:
                shift = (a_inv * ((ord(i.upper()) - 65) - b)) % 26 + 65
            r += chr(shift)
        else:
            r += i
    return r
   
def update_key_input(event):
    cipher = cipher_combobox.get()
    if cipher in ["Pig Pen", "Atbash", "Morse Code", "Base64", "Polybius", "Bifid" ]:
        key_label.grid_forget()
        key_entry.grid_forget()
    else:
        key_label.grid(row=2, column=0, padx=10, pady=10)
        key_entry.grid(row=2, column=1, padx=10, pady=10)


root = tk.Tk()
root.title("Cipher Tools")


cipher_var = tk.StringVar()
mode_var = tk.StringVar()
result_var = tk.StringVar()


cipher_label = ttk.Label(root, text="Select Cipher")
cipher_label.grid(row=0, column=0, padx=5, pady=5)
cipher_combobox = ttk.Combobox(root, textvariable=cipher_var, values=["Caesar", "Affine", "Pig Pen", "Morse Code", "Base64", "Atbash", "Rail Fence", "Polybius", "Bifid", "Vigenere", "Columnar Transposition"])
cipher_combobox.grid(row=0, column=1, padx=5, pady=5)
cipher_combobox.bind("<<ComboboxSelected>>", update_key_input)
cipher_combobox.set("Caesar")

mode_label = ttk.Label(root, text="Select Mode")
mode_label.grid(row=1, column=0, padx=5, pady=5)
mode_combobox = ttk.Combobox(root, textvariable=mode_var, values=["Encrypt", "Decrypt"])
mode_combobox.grid(row=1, column=1, padx=5, pady=5)
mode_combobox.set("Encrypt")

key_label = ttk.Label(root, text="Key")
key_label.grid(row=2, column=0, padx=5, pady=5)
key_entry = ttk.Entry(root)
key_entry.grid(row=2, column=1, padx=5, pady=5)

text_label = ttk.Label(root, text="Message")
text_label.grid(row=3, column=0, padx=5, pady=5)
text_entry = ttk.Entry(root)
text_entry.grid(row=3, column=1, padx=5, pady=5)

result_label = ttk.Label(root, text="Result")
result_label.grid(row=4, column=0, padx=5, pady=5)
result_entry = ttk.Entry(root, textvariable=result_var, state="readonly")
result_entry.grid(row=4, column=1, padx=5, pady=5)

perform_button = ttk.Button(root, text="Perform", command=perform_cipher)
perform_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


root.mainloop()
