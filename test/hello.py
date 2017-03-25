import tkinter as tk
root = tk.Tk()

w = tk.Label(root, text="Hello Marco!")
w.pack(side='right')


w2 = tk.Label(root, justify=tk.LEFT, padx=10, text="This is something explanable").pack(side="left")

counter = 0
def counter_label(label):
	def count():
		global counter
		counter += 1
		label.config(text=str(counter))
		label.after(1000,count)
	count()

button = tk.Button(root, text='Stop', width=25, command=root.destroy).pack()

counter_label(w)
root.mainloop()
