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
            tk.Button(frame, width=2, text="+", command=lambda index=i: self.increment_amount(index)).grid(row=i,
                                                                                                           column=2)  # Increment
            tk.Button(frame, width=2, text="-", command=lambda index=i: self.decrement_amount(index)).grid(row=i,
                                                                                                           column=3,
                                                                                                           padx=1)  # Decrement
        # Add acquired checkbox
        self.acquired = tk.IntVar()
        tk.Checkbutton(frame, text="Tower acquired", variable=self.acquired, command=self.check_status).grid(
            row=self.num_towers, column=0,
            columnspan=2)
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
        self.check_status()

    def decrement_amount(self, i):
        """
        Decrements amount[i] amount by 1
        """
        curr_amount = self.amount[i].get()
        new_amount = curr_amount - 1 if curr_amount > 1 else 0  # Don't go below 0
        self.amount[i].set(new_amount)
        self.check_status()

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

    def set_font_colors(self, color):
        """
        Sets all the font colors to color
        """
        self.frame.configure(fg=color)
        for i in range(0, self.num_towers):
            self.name_labels[i].configure(fg=color)
            self.amount_labels[i].configure(fg=color)

    def check_status(self):
        """
        Checks status for the requirement and
        adjusts the font colors accordingly
        """
        # Check if tower is acquired
        if self.acquired.get():
            self.set_font_colors("#00aa00")
        # Check if all the requirements are met
        elif self.check_full():
            self.set_font_colors("orange")
        else:
            self.set_font_colors("black")
            self.check_missing()

    def check_full(self):
        """
        Returns true if all the requirements are met
        """
        for i in range(0, self.num_towers):
            if self.amount[i].get() == 0:
                # All requirements not met
                return False
        # All requirements met
        return True

    def check_missing(self):
        """
        Checks if there is only one gem missing
        and changes that gem's font to red if so
        """
        color = "red"  # Color to set the missing pieces font to
        num_0 = 0
        for i in range(0, self.num_towers):
            if self.amount[i].get() == 0:
                num_0 += 1
        if num_0 == 1:
            for i in range(0, self.num_towers):
                if self.amount[i].get() == 0:
                    self.name_labels[i].configure(fg=color)
                    self.amount_labels[i].configure(fg=color)
