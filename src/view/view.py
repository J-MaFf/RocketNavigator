import csv


class RocketView:
    csv_file_name = "data.csv"

    def display_data(self, data):
        sensorType = self.sensorType()
        # Print the headers
        print("{:<15} {:<15} {:<15}".format("Sensor type", "Timestamp", "Sensor data"))
        # Loop through the data and print each item
        for item in data:
            print(item, end="\t")
            # print("{:<15} {:<15} {:<15}".format(*item))
        print()

    def write_data(self, data):
        with open(self.csv_file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            # Write the header
            writer.writerow(["Sensor type", "Timestamp", "Sensor data"])
            # Write the data
            writer.writerows(data if isinstance(data, list) else [data])
