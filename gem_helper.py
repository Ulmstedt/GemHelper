import tkinter as tk
from tower import Tower


class GemHelper:
    def __init__(self, window):
        window.title("Gem Helper by Mattias Ulmstedt")
        window.resizable(0, 0)
        # Create category frames
        FRAME_WIDTH = 415
        FRAME_HEIGHT = 445
        mandatory_frame = tk.LabelFrame(window, text="Mandatory", height=FRAME_HEIGHT, width=FRAME_WIDTH)
        mandatory_frame.grid_propagate(False)
        situational_frame = tk.LabelFrame(window, text="Situational", height=FRAME_HEIGHT, width=FRAME_WIDTH)
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
        TOWER_PADX = 8
        TOWER_PADY = 5
        tower1_frame.grid(row=0, column=0, padx=TOWER_PADX, pady=TOWER_PADY, sticky=tk.N)
        tower2_frame.grid(row=1, column=0, padx=TOWER_PADX, pady=TOWER_PADY, sticky=tk.N)
        tower3_frame.grid(row=2, column=0, padx=TOWER_PADX, pady=TOWER_PADY, sticky=tk.N)
        tower4_frame.grid(row=0, column=1, padx=TOWER_PADX, pady=TOWER_PADY, sticky=tk.N)
        tower5_frame.grid(row=1, column=1, padx=TOWER_PADX, pady=TOWER_PADY, sticky=tk.N)
        tower6_frame.grid(row=2, column=1, padx=TOWER_PADX, pady=TOWER_PADY, sticky=tk.N)
        tower7_frame.grid(row=0, column=2, padx=TOWER_PADX, pady=TOWER_PADY, sticky=tk.N)
        tower8_frame.grid(row=1, column=2, padx=TOWER_PADX, pady=TOWER_PADY, sticky=tk.N)
        tower9_frame.grid(row=2, column=2, padx=TOWER_PADX, pady=TOWER_PADY, sticky=tk.N)
        tower10_frame.grid(row=0, column=3, padx=TOWER_PADX, pady=TOWER_PADY, sticky=tk.N)
        tower11_frame.grid(row=1, column=3, padx=TOWER_PADX, pady=TOWER_PADY, sticky=tk.N)
        tower12_frame.grid(row=2, column=3, padx=TOWER_PADX, pady=TOWER_PADY, sticky=tk.N)

        mandatory_frame.grid(row=0, column=0, padx=3, pady=3)
        situational_frame.grid(row=0, column=1, padx=3, pady=3)
