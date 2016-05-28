import tkinter as tk


class Tower:
    def __init__(self, root, name, requirements):
        self.root = root  # Save reference to root
        self.num_towers = len(requirements)
        # Set name
        root.config(text=name)
        # Set up amount array
        self.amount = []
        self.name_labels = []
        self.amount_labels = []
        for i in range(0, self.num_towers):
            self.amount.append(tk.IntVar())
        # Requirements
        for i in range(0, self.num_towers):
            # Req name
            temp = tk.Label(root, width=16, anchor=tk.E, text=requirements[i])
            self.amount_labels.append(temp)  # Save reference
            temp.grid(row=i, column=0)
            # Req amount
            temp = tk.Label(root, textvariable=self.amount[i])
            self.name_labels.append(temp)  # Save reference
            temp.grid(row=i, column=1, padx=3)
            tk.Button(root, text="+", command=lambda i=i: self.increment_amount(i)).grid(row=i, column=2)  # Increment
            tk.Button(root, text="-", command=lambda i=i: self.decrement_amount(i)).grid(row=i, column=3,
                                                                                         padx=1)  # Decrement
        # Add to layout
        root.grid(row=0, column=0, padx=5, pady=5)

    def increment_amount(self, i):
        curr_amount = self.amount[i].get()
        new_amount = curr_amount + 1
        self.amount[i].set(new_amount)
        self.check_amount()

    def decrement_amount(self, i):
        curr_amount = self.amount[i].get()
        new_amount = curr_amount - 1 if curr_amount > 1 else 0  # Don't go below 0
        self.amount[i].set(new_amount)
        self.check_amount()

    def check_amount(self):
        self.check_full()
        self.check_missing()

    def check_full(self):
        color = "#00aa00"
        for i in range(0, self.num_towers):
            if self.amount[i].get() == 0:
                color = "black"  # Set color to black if not all are at least 1
        # Set all the components colors
        self.root.configure(fg=color)
        for i in range(0, self.num_towers):
            self.name_labels[i].configure(fg=color)
            self.amount_labels[i].configure(fg=color)

    def check_missing(self):
        num_0 = 0
        for i in range(0, self.num_towers):
            if self.amount[i].get() == 0:
                num_0 += 1
        if num_0 == 1:
            for i in range(0, self.num_towers):
                if self.amount[i].get() == 0:
                    self.name_labels[i].configure(fg="red")
                    self.amount_labels[i].configure(fg="red")
                else:
                    self.name_labels[i].configure(fg="black")
                    self.amount_labels[i].configure(fg="black")


class GemHelper:
    def __init__(self, root):
        root.title("Gem Helper by Mattias Ulmstedt")
        root.resizable(0,0)
        # Create category frames
        mandatory_frame = tk.LabelFrame(root, text="Mandatory", height=395, width=398)
        mandatory_frame.grid_propagate(False)
        situational_frame = tk.LabelFrame(root, text="Situational", height=395, width=398)
        situational_frame.grid_propagate(False)

        # Create towers
        tower1_frame = tk.LabelFrame(mandatory_frame)
        Tower(tower1_frame, "Gold", ["Flawed Diamond", "Flawless Amethyst", "Perfect Amethyst"])

        tower2_frame = tk.LabelFrame(mandatory_frame)
        Tower(tower2_frame, "Black Opal", ["Aquamarine", "Flawless Diamond", "Perfect Opal"])

        tower3_frame = tk.LabelFrame(mandatory_frame)
        Tower(tower3_frame, "Paraiba Tourmaline",
              ["Flawed Aquamarine", "Flawed Emerald", "Flawless Opal", "Perfect Aquamarine"])

        tower4_frame = tk.LabelFrame(mandatory_frame)
        Tower(tower4_frame, "Jade", ["Flawed Sapphire", "Opal", "Flawless Emerald"])

        tower5_frame = tk.LabelFrame(mandatory_frame)
        Tower(tower5_frame, "Dark Emerald", ["Flawed Topaz", "Flawless Sapphire", "Perfect Emerald"])

        tower6_frame = tk.LabelFrame(mandatory_frame)
        Tower(tower6_frame, "Pink Diamond", ["Topaz", "Diamond", "Perfect Diamond"])

        tower7_frame = tk.LabelFrame(situational_frame)
        Tower(tower7_frame, "Red Crystal", ["Flawed Amethyst", "Emerald", "Ruby"])

        tower8_frame = tk.LabelFrame(situational_frame)
        Tower(tower8_frame, "Uranium", ["Flawed Opal", "Sapphire", "Perfect Topaz"])

        tower9_frame = tk.LabelFrame(situational_frame)
        Tower(tower9_frame, "Yellow Sapphire", ["Flawless Ruby", "Flawless Topaz", "Perfect Sapphire"])

        tower10_frame = tk.LabelFrame(situational_frame)
        Tower(tower10_frame, "Blood Stone", ["Amethyst", "Flawless Aquamarine", "Perfect Ruby"])

        tower11_frame = tk.LabelFrame(situational_frame)
        Tower(tower11_frame, "Star Ruby", ["Chipped Ruby", "Flawed Ruby", "Chipped Amethyst"])

        tower12_frame = tk.LabelFrame(situational_frame)
        Tower(tower12_frame, "Malachite", ["Chipped Aquamarine", "Chipped Opal", "Chipped Emerald"])



        # Add to layout
        tower1_frame.grid(row=0, column=0, padx=10, pady=10)
        tower2_frame.grid(row=1, column=0, padx=10, pady=10)
        tower3_frame.grid(row=2, column=0, padx=10, pady=10)
        tower4_frame.grid(row=0, column=1, padx=10, pady=10)
        tower5_frame.grid(row=1, column=1, padx=10, pady=10)
        tower6_frame.grid(row=2, column=1, padx=10, pady=10, sticky=tk.N)
        tower7_frame.grid(row=0, column=2, padx=10, pady=10)
        tower8_frame.grid(row=1, column=2, padx=10, pady=10)
        tower9_frame.grid(row=2, column=2, padx=10, pady=10)
        tower10_frame.grid(row=0, column=3, padx=10, pady=10)
        tower11_frame.grid(row=1, column=3, padx=10, pady=10)
        tower12_frame.grid(row=2, column=3, padx=10, pady=10)

        mandatory_frame.grid(row=0,column=0, padx=3, pady=3)
        situational_frame.grid(row=0,column=1, padx=3, pady=3)

root = tk.Tk()

GemHelper = GemHelper(root)
root.mainloop()
