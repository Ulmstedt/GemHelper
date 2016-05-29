import tkinter as tk


class Tower:
    def __init__(self, frame, name, requirements):
        self.frame = frame  # Save reference to root
        self.num_towers = len(requirements)
        # Set name
        frame.config(text=name)
        # Set up arrays with references to objects
        self.amount = []
        self.name_labels = []
        self.amount_labels = []
        for i in range(0, self.num_towers):
            self.amount.append(tk.IntVar())
        # Requirements
        for i in range(0, self.num_towers):
            # Req name
            temp = tk.Label(frame, width=16, anchor=tk.E, text=requirements[i])
            self.amount_labels.append(temp)  # Save reference
            temp.grid(row=i, column=0)
            # Req amount
            temp = tk.Label(frame, textvariable=self.amount[i])
            self.name_labels.append(temp)  # Save reference
            temp.grid(row=i, column=1, padx=3)
            tk.Button(frame, width=2, text="+", command=lambda i=i: self.increment_amount(i)).grid(row=i,
                                                                                                   column=2)  # Increment
            tk.Button(frame, width=2, text="-", command=lambda i=i: self.decrement_amount(i)).grid(row=i, column=3,
                                                                                                   padx=1)  # Decrement
        # Add inc/dec all buttons
        tk.Button(frame, text="+", width=2, command=self.increment_all).grid(row=self.num_towers, column="2")
        tk.Button(frame, text="-", width=2, command=self.decrement_all).grid(row=self.num_towers, column="3")
        # Add to layout
        frame.grid(row=0, column=0)

    def increment_amount(self, i):
        """
        Increments amount[i] amount by 1
        """
        curr_amount = self.amount[i].get()
        new_amount = curr_amount + 1
        self.amount[i].set(new_amount)
        self.check_amount()

    def decrement_amount(self, i):
        """
        Decrements amount[i] amount by 1
        """
        curr_amount = self.amount[i].get()
        new_amount = curr_amount - 1 if curr_amount > 1 else 0  # Don't go below 0
        self.amount[i].set(new_amount)
        self.check_amount()

    def increment_all(self):
        """
        Increments all amounts by 1
        """
        for i in range(0, self.num_towers):
            self.increment_amount(i)

    def decrement_all(self):
        """
        Decrements all amounts by 1
        """
        for i in range(0, self.num_towers):
            self.decrement_amount(i)

    def check_amount(self):
        """
        Checks status for the requirement and
        adjusts the font color accordingly
        """
        self.check_full()
        self.check_missing()

    def check_full(self):
        """
        Checks if all the requirements are met
        and changes font color to green if so
        """
        color = "#00aa00"  # Green
        for i in range(0, self.num_towers):
            if self.amount[i].get() == 0:
                # Set color to black if not all are at least 1
                color = "black"
        # Set all the components colors
        self.frame.configure(fg=color)
        for i in range(0, self.num_towers):
            self.name_labels[i].configure(fg=color)
            self.amount_labels[i].configure(fg=color)

    def check_missing(self):
        """
        Checks if there is only one gem missing
        and changes that gem's font to red if so
        """
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
    def __init__(self, window):
        window.title("Gem Helper by Mattias Ulmstedt")
        window.resizable(0, 0)
        # Create category frames
        frame_width = 415
        frame_height = 445
        mandatory_frame = tk.LabelFrame(window, text="Mandatory", height=frame_height, width=frame_width)
        mandatory_frame.grid_propagate(False)
        situational_frame = tk.LabelFrame(window, text="Situational", height=frame_height, width=frame_width)
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
        tower_padx = 8
        tower_pady = 5
        tower1_frame.grid(row=0, column=0, padx=tower_padx, pady=tower_pady, sticky=tk.N)
        tower2_frame.grid(row=1, column=0, padx=tower_padx, pady=tower_pady, sticky=tk.N)
        tower3_frame.grid(row=2, column=0, padx=tower_padx, pady=tower_pady, sticky=tk.N)
        tower4_frame.grid(row=0, column=1, padx=tower_padx, pady=tower_pady, sticky=tk.N)
        tower5_frame.grid(row=1, column=1, padx=tower_padx, pady=tower_pady, sticky=tk.N)
        tower6_frame.grid(row=2, column=1, padx=tower_padx, pady=tower_pady, sticky=tk.N)
        tower7_frame.grid(row=0, column=2, padx=tower_padx, pady=tower_pady, sticky=tk.N)
        tower8_frame.grid(row=1, column=2, padx=tower_padx, pady=tower_pady, sticky=tk.N)
        tower9_frame.grid(row=2, column=2, padx=tower_padx, pady=tower_pady, sticky=tk.N)
        tower10_frame.grid(row=0, column=3, padx=tower_padx, pady=tower_pady, sticky=tk.N)
        tower11_frame.grid(row=1, column=3, padx=tower_padx, pady=tower_pady, sticky=tk.N)
        tower12_frame.grid(row=2, column=3, padx=tower_padx, pady=tower_pady, sticky=tk.N)

        mandatory_frame.grid(row=0, column=0, padx=3, pady=3)
        situational_frame.grid(row=0, column=1, padx=3, pady=3)


root = tk.Tk()
GemHelper = GemHelper(root)
root.mainloop()
