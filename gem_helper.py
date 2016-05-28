import tkinter as tk


class Tower:
    def __init__(self, root, name, requirements):
        # Set name
        root.config(text=name)
        # Set up amount array
        self.amount = []
        for i in range(0, len(requirements)):
            self.amount.append(tk.IntVar())
        # Requirements
        for i in range(0, len(requirements)):
            tk.Label(root, width=16, anchor=tk.E, text=requirements[i]).grid(row=i, column=0)  # Req name
            tk.Label(root, textvariable=self.amount[i]).grid(row=i, column=1, padx=3)  # Req amount
            tk.Button(root, text="+", command=lambda i=i: self.increment_amount(i)).grid(row=i, column=2)  # Increment
            tk.Button(root, text="-", command=lambda i=i: self.decrement_amount(i)).grid(row=i, column=3,
                                                                                      padx=1)  # Decrement
        # Add to layout
        root.grid(row=0, column=0, padx=5, pady=5)

    def increment_amount(self, i):
        curr_amount = self.amount[i].get()
        new_amount = curr_amount + 1
        self.amount[i].set(new_amount)

    def decrement_amount(self, i):
        curr_amount = self.amount[i].get()
        new_amount = curr_amount - 1 if curr_amount > 1 else 0  # Don't go below 0
        self.amount[i].set(new_amount)


class GemHelper:
    def __init__(self, root):
        root.title("Gem Helper")
        root.geometry("500x500")

        # Create first tower
        tower1_frame = tk.LabelFrame(root)
        Tower(tower1_frame, "Malachite", ["Chipped opal", "Chipped emerald", "Flawless aquamarine"])

        # Create second tower
        tower2_frame = tk.LabelFrame(root)
        Tower(tower2_frame, "Silver", ["Chipped diamond", "Chipped sapphire", "Chipped topaz"])

        # Add to layout
        tower1_frame.grid(row=0, column=0, padx=10, pady=10)
        tower2_frame.grid(row=2, column=0, padx=10, pady=10)


root = tk.Tk()

GemHelper = GemHelper(root)
root.mainloop()
