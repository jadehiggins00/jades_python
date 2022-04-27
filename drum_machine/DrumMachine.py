from tkinter import Tk, Frame, Label, Spinbox, Entry
PROGRAM_NAME = "Explosion Drum Machine"
# creating symbollic names
MAX_NUMBER_OF_PATTERNS =10
MAX_NUMBER_OF_DRUM_SAMPLES =5
MAX_NUMBER_OF_UNITS =5
MAX_BPU =5
INITIAL_NUMBER_OF_UNITS =4
INITIAL_BPU =4
INITIAL_BEATS_PER_MINUTE =240



# here we create a class structure and intialise the toplevel window
# and pass it as an argument to it
class DrumMachine:
    def __init__(self, root):
        self.root = root
        self.root.title(PROGRAM_NAME)
        self.init_gui()
        




    def init_all_patterns(self):
        # defining a list to keep info about beat patterns
        # each pattern is denoted in a dictionary
        self.all_patterns = [
            {
                'list_of_drum_files': [None] * MAX_NUMBER_OF_DRUM_SAMPLES,
                'number_of_units': INITIAL_NUMBER_OF_UNITS,
                'bpu': INITIAL_BPU,
                'is_button_clicked_list':
                self.init_is_button_clicked_list(
                    MAX_NUMBER_OF_DRUM_SAMPLES,
                    INITIAL_NUMBER_OF_UNITS * INITIAL_BPU
                )
            }

            for k in range(MAX_NUMBER_OF_PATTERNS)]


    # initialising all values to be false
    def init_is_button_clicked_list(self, num_of_rows, num_of_columns):
        return[[False] * num_of_columns for x in range(num_of_rows)]


    def on_pattern_changed(self):
        pass

    def on_number_of_units_changed(self):
        pass

    # creating the top bar
    def create_top_bar(self):
        # creating the top_bar frame widget
        topbar_frame = Frame(self.root, height=25)
        topbar_frame.grid(row=0, columnspan=12, rowspan=10, padx=5,pady=5)

        # label for 'pattern number'
        Label(topbar_frame, text='Pattern Number').grid(row=0, column=1)
        # adding the spinbox widget
        self.pattern_index_widget = Spinbox(topbar_frame, from_=0, to=MAX_NUMBER_OF_PATTERNS-1, width=5,
                                            command=self.on_pattern_changed)
        # this keeps track of the current active pattern
        self.pattern_index_widget.grid(row=0, column=2)
        # creating the entry widget
        self.current_pattern_name_widget = Entry(topbar_frame)
        # setting the postion for the entry widget
        self.current_pattern_name_widget.grid(row=0, column=3, padx=7, pady=2)

        # label for 'number of units'
        Label(topbar_frame, text='Number of Units').grid(row=0, column=4)
        # creating spinbox
        self.number_of_units_widget = Spinbox(topbar_frame, from_=0, to=MAX_NUMBER_OF_UNITS, width=5,
                                               command=self.on_number_of_units_changed)
        self.number_of_units_widget.delete(0,'end')
        self.number_of_units_widget.insert(0, INITIAL_NUMBER_OF_UNITS)
        self.number_of_units_widget.grid(row=0, column=5)

        # label for bpu
        Label(topbar_frame, text='BPUs').grid(row=0, column=6)
        # adding a spin box
        self.bpu_widget = Spinbox(topbar_frame, from_=1, to=MAX_BPU, width=5, command=self.on_bpu_changed)
        self.bpu_widget.grid(row=0, column=7)
        self.bpu_widget.delete(0, "end")
        self.bpu_widget.insert(0,INITIAL_BPU)

    def create_left_drum_loader(self):
        pass

    def create_right_button_matrix(self):
        pass

    def create_play_bar(self):
        pass

    def on_bpu_changed(self):
        pass

    # define all 4 methods within this gui method
    def init_gui(self):
        self.create_top_bar()
        self.create_left_drum_loader()
        self.create_right_button_matrix()
        self.create_play_bar()

# if the script is run as a standalone program
if __name__ == '__main__':
    # then a new tk root object is created
    root = Tk()
    # then the root window is passed as an argument to the drum machine object
    DrumMachine(root)
    root.mainloop()