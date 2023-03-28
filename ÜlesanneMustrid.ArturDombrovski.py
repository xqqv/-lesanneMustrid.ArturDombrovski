import tkinter as tk


window = tk.Tk()
window.title("Lipud")
window.configure(bg="white")


def show_bahama_lipp():
    canvas.delete("all")
    canvas.create_rectangle(0, 0, 300, 200, fill="#0b4f91")  # sinine
    canvas.create_polygon(0, 0, 300, 0, 300, 100, 0, 100, fill="#ffc726")  # kollane 
    canvas.create_polygon(0, 100, 300, 100, 300, 200, 0, 200, fill="#0b4f91")  # sinine 


def show_eesti_lipp():
    canvas.delete("all")
    canvas.create_rectangle(0, 50, 300, 150, fill="#0072c6")  # sinine
    canvas.create_rectangle(0, 100, 300, 150, fill="#000000")  # must
    canvas.create_rectangle(0, 500, 300, 450, fill="#ffffff")  # valge
  


def show_valitud_lipp():
    canvas.delete("all")
   


btn_bahama = tk.Button(window, text="Bahama saarte lipp", command=show_bahama_lipp)
btn_bahama.pack(pady=10)

btn_eesti = tk.Button(window, text="Eesti riigi lipp", command=show_eesti_lipp)
btn_eesti.pack(pady=10)

btn_valitud = tk.Button(window, text="Valitud riigi lipp", command=show_valitud_lipp)
btn_valitud.pack(pady=10)


canvas = tk.Canvas(window, width=300, height=200)
canvas.pack(pady=10)

# kuvame alguses Bahama lipu
show_bahama_lipp()

# käivitame akna
window.mainloop()
