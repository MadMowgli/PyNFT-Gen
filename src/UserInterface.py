import tkinter as tk


class UserInterface:
    # Fields
    window_name = str()
    window_width = str()
    window_height = str()
    window_size = str()
    center_x = int()
    center_y = int()
    screen_width = int()
    screen_height = int()

    root = None

    # Constructor
    def __init__(self, screen_width, screen_height):
        self.window_name = 'FungiPy NFT-Img Generator'
        self.window_width = '1265'
        self.window_height = '625'
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.window_size = f'{self.window_width}x{self.window_height}'
        self.center_x = int(self.screen_width / 2 - int(self.window_width) / 2)
        self.center_y = int(self.screen_height / 2 - int(self.window_height) / 2)

    # Methods
    def createUI(self):
        # Set up root container
        self.root = tk.Tk()
        self.root.title(self.window_name)
        self.root.geometry(f'{self.window_width}x{self.window_height}+{self.center_x}+{int(self.center_y)-80}')

    def run(self):
        self.createUI()
        self.root.mainloop()
