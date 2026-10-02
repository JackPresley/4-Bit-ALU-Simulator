import tkinter as tk
from tkinter import messagebox

class LogicGates:
    @staticmethod
    def xor_gate(a, b): return a ^ b
    
    @staticmethod
    def and_gate(a, b): return a & b
    
    @staticmethod
    def or_gate(a, b): return a | b

class ALU:
    def __init__(self):
        self.carry_out = 0

    def full_adder(self, a, b, c_in):
        sum_out = LogicGates.xor_gate(LogicGates.xor_gate(a, b), c_in)
        c_out = LogicGates.or_gate(LogicGates.and_gate(a, b), LogicGates.and_gate(c_in, LogicGates.xor_gate(a, b)))
        return sum_out, c_out

    def add_4_bit(self, a_bits, b_bits):
        result = [0] * 4
        carry = 0
        
        for i in range(3, -1, -1):
            result[i], carry = self.full_adder(a_bits[i], b_bits[i], carry)
            
        self.carry_out = carry
        return result

def calculate_alu():
    val_a_str = entry_a.get().strip()
    val_b_str = entry_b.get().strip()

    if len(val_a_str) != 4 or len(val_b_str) != 4 or not all(c in '01' for c in val_a_str + val_b_str):
        messagebox.showerror("Input Error", "Please enter exactly four binary digits (0 or 1).")
        return

    a_bits = [int(b) for b in val_a_str]
    b_bits = [int(b) for b in val_b_str]

    cpu_alu = ALU()
    result_bits = cpu_alu.add_4_bit(a_bits, b_bits)

    result_str = "".join(str(b) for b in result_bits)
    result_label.config(text=f"Result: {result_str}  |  Carry: {cpu_alu.carry_out}")

root = tk.Tk()
root.title("4-Bit ALU Simulator")
root.geometry("300x200")
root.eval('tk::PlaceWindow . center')

tk.Label(root, text="Input A (4-bit binary):").pack(pady=(10, 0))
entry_a = tk.Entry(root, justify="center")
entry_a.insert(0, "0101")
entry_a.pack()

tk.Label(root, text="Input B (4-bit binary):").pack(pady=(10, 0))
entry_b = tk.Entry(root, justify="center")
entry_b.insert(0, "0110")
entry_b.pack()

tk.Button(root, text="Add Binary", command=calculate_alu).pack(pady=15)

result_label = tk.Label(root, text="Result: ----  |  Carry: -", font=("SansSerif", 12, "bold"))
result_label.pack()

root.mainloop()