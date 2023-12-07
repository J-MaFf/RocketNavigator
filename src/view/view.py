# The View will be how you present the information to the user.
csv_file_name = "data.csv"


class RocketView:
    # TODO: Add a method to display the data
    def display_data(self, data):
        # Print the data or update the display
        if isinstance(data, str):
            print(data)
        elif isinstance(data, list):
            print(", ".join(data))

    # TODO: Add a method to wirte the data to a csv file
    def write_data(self, data):
        with open(csv_file_name, mode=w) as file:
            if isinstance(data, str):
                file.write(data + ',')
            elif isinstance(data, list):
                 file.write(", ".join(data))
