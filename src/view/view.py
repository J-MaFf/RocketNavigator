import csv


class RocketView:
    csv_file_name = "data.csv"

    def display_data(self, data):
        # Print the headers
<<<<<<< HEAD
        self.write_data(data)
        print("{:<15} {:<15} \t\t {:<15}".format("Sensor type", "Timestamp", "Sensor data"))
=======
        print(data)
        print(
            "{:<15} {:<15} \t\t {:<15}".format(
                "Sensor type", "Timestamp", "Sensor data"
            )
        )
>>>>>>> 5c1abdc9c0852defc974838c4fb5025b56e5d746
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
        j = 1
        while i < 4:
            print(
                sensors[i] + "\t\t" + str(data[0]) + "\t",
                "{0:.2f}".format(data[j]),
                end="\n",
            )
            i += 1
            j += 1
        while i < 7:
<<<<<<< HEAD
            print(sensors[i] + "\t" + str(data[0]) + "\t",
              '{0:.1f}'.format(data[j]),
              '\t{0:.1f}'.format(data[j+1]),
              '\t{0:.1f}'.format(data[j+2]), end="\n")
            i+=1
            j+=3
=======
            print(
                sensors[i] + "\t" + str(data[0]) + "\t",
                "{0:.2f}".format(data[j]),
                "\t{0:.2f}".format(data[j + 1]),
                "\t{0:.2f}".format(data[j + 2]),
                end="\n",
            )
            i += 1
            j += 3
>>>>>>> 5c1abdc9c0852defc974838c4fb5025b56e5d746
        """
        print(sensors[i] + "\t" + str(data[0]),
              '{0:.2f}'.format(data[j]),
              '{0:.2f}'.format(data[j+1]),
              '{0:.2f}'.format(data[j+2]), end="\n")
        i+=1
        j+=3
        print(sensors[i],
              '{0:.2f}'.format(data[j]),
              '{0:.2f}'.format(data[j+1]),
              '{0:.2f}'.format(data[j+2]))
        i+=1
        j+=3
        print(sensors[i],
              '{0:.2f}'.format(data[j]),
              '{0:.2f}'.format(data[j+1]),
              '{0:.2f}'.format(data[j+2]), end="\n")"""
        """for item in data:
        while i < len(data):
            print(sensors[i], "{0:.2f}".format(data[i]), end="\n")
            i += 1
        for item in data:
            print(item.sensorType(), "{0:.2f}".format(item), end="\n")
            # print("{:<15} {:<15} {:<15}".format(*item))"""
        print()

    def write_data(self, data):
        with open(self.csv_file_name, mode="a", newline="") as file:
            writer = csv.writer(file, delimiter = ',', quoting = csv.QUOTE_MINIMAL)
            # Write the data
            writer.writerow(data)
