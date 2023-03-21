from tkinter import *
import numpy as np
from scipy.optimize import linprog

root = Tk()
root.title("Simplex Method Calculator")

# Berfungsi untuk menghitung Metode Simpleks
def solve():
    # Dapatkan nilai input dari GUI
    obj_fun = [float(x) for x in obj_fun_entry.get().split(',')]
    constraints = [[float(y) for y in x.split(',')] for x in constraints_entry.get().split(';')]
    rhs = [float(x) for x in rhs_entry.get().split(',')]
    sense = [x for x in sense_entry.get().split(',')]

    # Ubah batasan menjadi bentuk matriks
    A = np.array(constraints)
    b = np.array(rhs)

    # Selesaikan menggunakan fungsi linprog
    result = linprog(c=obj_fun, A_ub=A, b_ub=b, method="simplex")

   # Menampilkan hasil dalam GUI
    result_label.config(text="Optimal Value: {}\nOptimal Solution: {}".format(result.fun, result.x))

# Buat elemen GUI
obj_fun_label = Label(root, text="Objective Function:")
obj_fun_entry = Entry(root)
constraints_label = Label(root, text="Constraints:")
constraints_entry = Entry(root)
rhs_label = Label(root, text="RHS:")
rhs_entry = Entry(root)
sense_label = Label(root, text="Sense:")
sense_entry = Entry(root)
solve_button = Button(root, text="Solve", command=solve)
result_label = Label(root, text="")

# Tambahkan elemen GUI ke tata letak
obj_fun_label.grid(row=0, column=0)
obj_fun_entry.grid(row=0, column=1)
constraints_label.grid(row=1, column=0)
constraints_entry.grid(row=1, column=1)
rhs_label.grid(row=2, column=0)
rhs_entry.grid(row=2, column=1)
sense_label.grid(row=3, column=0)
sense_entry.grid(row=3, column=1)
solve_button.grid(row=4, column=0, columnspan=2)
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()