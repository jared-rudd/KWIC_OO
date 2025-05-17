# handles reading and storing the input lines
class KWIC_InputHandler:
    # constructor for the input handler
    def __init__(self):
        self.lines = []

    # splits each input line into words and stores them as lists
    def read_input(self, input_lines):
        for line in input_lines:
            words = line.strip().split()
            if words:
                self.lines.append(words)

    # returns the parsed lines as lists of words
    def get_lines(self):
        return self.lines

# handles generating all circular shifts for each line
class KWIC_CircularShifter:
    # consutrctor for the circular shifter, takes lines as input
    def __init__(self, lines):
        self.original_lines = lines
        self.shifted_lines = []

    # for each line, rotate words to create all circular shifts   
    def generate_shifts(self):
        for line in self.original_lines:
            for i in range(len(line)):
                shifted = line[i:] + line[:i]
                self.shifted_lines.append(shifted)

    # returns the list of all generated circular shifts
    def get_shifts(self):
        return self.shifted_lines

# handles sorting the circularly shifted lines alphabetically
class KWIC_Alphabetizer:
    #constructor for the alphabetizer, takes shifts as input
    def __init__(self, shifts):
        self.shifts = shifts

    # sorts the list of shifted lines alphabetically (case-insensitive)
    def sort_shifts(self):
        self.shifts.sort(key=lambda x: ' '.join(x).lower())
        return self.shifts

# handles displaying the final sorted list of circular shifts
class KWIC_OutputHandler:
    #consutrctor for the output handler, takes list of sorted shifts as input
    def __init__(self, sorted_shifts):
        self.sorted_shifts = sorted_shifts

    # prints each sorted circular shift as a single line of text
    def display_output(self):
        for line in self.sorted_shifts:
            print(' '.join(line))

# coordinates the entire KWIC process by invoking each component in order
class KWIC_MasterController:
    # constructor for the master controller, takes list of input lines as input
    def __init__(self, input_lines):
        self.input_lines = input_lines

    # run execution method: input -> shift -> sort -> output
    def run(self):
        input_handler = KWIC_InputHandler()
        input_handler.read_input(self.input_lines)

        circular_shifter = KWIC_CircularShifter(input_handler.get_lines())
        circular_shifter.generate_shifts()

        alphabetizer = KWIC_Alphabetizer(circular_shifter.get_shifts())
        sorted_shifts = alphabetizer.sort_shifts()

        output_handler = KWIC_OutputHandler(sorted_shifts)
        output_handler.display_output()

# entry point of the program with sample input lines
def main():
    # input list for the master controller
    input_lines = [
        "CSI 5352 Advanced Object/Oriented",
        "Assignment 2.1",
        "KWIC Implementation Part 1",
        "KWIC Implementation  Part 2",
        "Groups 1, 2, 3, 4"
    ]

    # create and run the KWIC system i.e. entering through master controller
    kwic_controller = KWIC_MasterController(input_lines)
    kwic_controller.run()

# runs the main function
if __name__ == "__main__":
    main()