import csv


class RocketView:
    csv_file_name = "data.csv"

    def display_data(self, data):
        # Print the headers
        print("{:<15} {:<15} {:<15}".format("Sensor type", "Timestamp", "Sensor data"))
        # Loop through the data and print each item
        sensors = [
            "Temp1",
            "Temp2",
            "Temp3",
            "Temp4",
            "Accelerometer",
            "Barometer",
            "Gyroscope",
        ]
        i = 0
        while i < len(data):
            print(sensors[i], "{0:.2f}".format(data[i]), end="\n")
            i += 1
        """for item in data:
            print(item.sensorType(), "{0:.2f}".format(item), end="\n")
            # print("{:<15} {:<15} {:<15}".format(*item))"""
        print()

    def write_data(self, data):
        with open(self.csv_file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            # Write the header
            writer.writerow(["Sensor type", "Timestamp", "Sensor data"])
            # Write the data
            writer.writerows(data if isinstance(data, list) else [data])
