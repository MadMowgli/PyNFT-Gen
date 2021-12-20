import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image
from functools import partial
import Functions


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
    left_container = None
    right_container = None
    root = None
    entry_text_vars = list()

    # Constructor
    def __init__(self, screen_width, screen_height):
        self.window_name = 'FungiPy NFT-Img Generator'
        self.window_width = '1265'
        self.window_height = '520'
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.window_size = f'{self.window_width}x{self.window_height}'
        self.center_x = int(self.screen_width / 2 - int(self.window_width) / 2)
        self.center_y = int(self.screen_height / 2 - int(self.window_height) / 2)
        self.entry_text_vars = []

    # Methods
    def createUI(self):
        # Set up root container
        self.root = tk.Tk()
        self.root.title(self.window_name)
        self.root.iconbitmap(r'resources\disgusted.ico')
        self.root.geometry(f'{self.window_width}x{self.window_height}+{self.center_x}+{int(self.center_y) - 80}')
        self.root.minsize(int(self.window_width), int(self.window_height))
        self.root.attributes('-alpha', 0.95)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)
        self.root.rowconfigure(0, weight=1)

        # Set up basic 'container frames'
        self.left_container = tk.Frame(self.root, height=int(self.window_height), bg='white')
        self.left_container.grid(row=0, column=0, sticky='nsew')

        self.right_container = tk.Frame(self.root, height=int(self.window_height), bg='white')
        self.right_container.grid(row=0, column=1, sticky='nsew')

        # Left Col
        self.setUpLeftCol()

        # Right col
        self.setUpRightCol()

    def setUpLeftCol(self):
        # Prepare top left collection img (put it inside a label)
        collection_img = Image.open(r'resources/disgusted.png')
        collection_img = collection_img.resize((175, 175))
        collection_img = ImageTk.PhotoImage(collection_img)
        img_label = tk.Label(self.left_container, image=collection_img, bg='white')
        img_label.image = collection_img
        img_label.pack(anchor='n', padx=20, pady=20)

        # Collection name label
        collection_label = tk.Label(self.left_container, text='FungiPy NFT Gen')
        collection_label.pack(anchor='n', padx=20, pady=0)
        collection_label.config(bg='white', font='Calibri 18 bold')

        # Top left separator
        top_left_separator = ttk.Separator(self.left_container, orient='horizontal')
        top_left_separator.pack(anchor='n', padx=50, pady=20, fill=tk.BOTH)

    def setUpRightCol(self):
        # Contents: 6 rows, 2 cols
        self.createInputFields(self.right_container, 7)

        # Create output col
        # Create containing frame
        container_frame = tk.Frame(self.right_container, bg='white')
        container_frame.grid(sticky='w', row=0, column=1, padx=20, pady=10)

        # Create label
        label_text = 'Output Directory'
        label = tk.Label(container_frame, text=label_text)
        label.config(bg='white', font='Calibri 12 bold')
        label.grid(sticky='w', row=0, column=0)

        # Create entry field
        output_directory_text = tk.StringVar()
        output_directory_entry = tk.Entry(container_frame, textvariable=output_directory_text)
        self.entry_text_vars.append(output_directory_text)
        output_directory_entry.grid(sticky='w', row=1, column=1, ipadx=100)

        # Create button
        button_style = ttk.Style()
        button_style.configure('TButton', font=('Calibri', 10, 'bold'), background='white')

        # We need a partial function for the button callback since we need to pass args
        button_callback = partial(self.setDirectory, len(self.entry_text_vars)-1)
        button = ttk.Button(container_frame, text='Browse', style='TButton', command=button_callback)
        button.grid(sticky='w', row=1, column=0, padx=(0, 20))

        # Collection name input field
        collection_name_frame = tk.Frame(self.right_container, bg='white')
        collection_name_frame.grid(sticky='w', row=1, column=1, padx=20, pady=10)

        collection_name_label = tk.Label(collection_name_frame, text='Collection name: ')
        collection_name_label.config(bg='white', font='Calibri 12 bold')
        collection_name_label.grid(sticky='w', row=0, column=0)

        # Create entry field
        collection_name_string_var = tk.StringVar()
        collection_name_entry = tk.Entry(collection_name_frame, textvariable=collection_name_string_var)
        collection_name_entry.grid(sticky='w', row=0, column=1, ipadx=100)

        # Create 'Generate' Button with partial function
        generate_button_callback = partial(Functions.generate, self.entry_text_vars,
                                           output_directory_text, collection_name_string_var)
        generate_button = ttk.Button(collection_name_frame, text='Generate',
                                     style='TButton', command=generate_button_callback)
        generate_button.grid(sticky='e', row=1, column=1, padx=(20, 0))

    def createInputFields(self, parent, amount):
        '''
        Creates x Entry fields inside the given parent.
        :param parent:
        :param amount:
        :return:
        '''
        for index in range(amount):
            # Create containing frame
            container_frame = tk.Frame(parent, bg='white')
            container_frame.grid(sticky='w', row=index, column=0, pady=10)

            # Create label
            label_text = 'Base Layer' if index == 0 else f'Layer {index}'
            label = tk.Label(container_frame, text=label_text)
            label.config(bg='white', font='Calibri 12 bold')
            label.grid(sticky='w', row=index, column=0)

            # Create button
            button_style = ttk.Style()
            button_style.configure('TButton', font=('Calibri', 10, 'bold'), background='white')

            # We need a partial function for the button callback since we need to pass args
            button_callback = partial(self.setDirectory, index)
            button = ttk.Button(container_frame, text='Browse', style='TButton', command=button_callback)
            button.grid(sticky='w', row=(index + 1), column=0, padx=(0, 20))

            # Create entry field
            entry_text = tk.StringVar()
            entry = tk.Entry(container_frame, textvariable=entry_text)
            self.entry_text_vars.append(entry_text)
            entry.grid(sticky='w', row=(index + 1), column=1, ipadx=100)

    def setDirectory(self, entry_field_index):
        directory = str(tk.filedialog.askdirectory())
        self.entry_text_vars[entry_field_index].set(directory)

    def run(self):
        self.createUI()
        self.root.mainloop()
