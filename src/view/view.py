import csv


class RocketView:
    csv_file_name = "data.csv"

    def display_data(self, data):
        # Print the headers
        print(data)
        print("{:<15} {:<15} \t\t {:<15}".format("Sensor type", "Timestamp", "Sensor data"))
        # Loop through the data and print each item
        sensors = ["Temp1",
                   "Temp2",
                   "Temp3",
                   "Temp4",
                   "Accelerometer",
                   "Barometer",
                   "Gyroscope"]
        i = 0
        j = 1
        while i < 4:
            print(sensors[i] + "\t\t" + str(data[0]) + "\t",
                  '{0:.2f}'.format(data[j]), end="\n")
            i+=1
            j+=1
        while i < 7:
            print(sensors[i] + "\t" + str(data[0]) + "\t",
              '{0:.2f}'.format(data[j]),
              '\t{0:.2f}'.format(data[j+1]),
              '\t{0:.2f}'.format(data[j+2]), end="\n")
            i+=1
            j+=3
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
        '''for item in data:
            print(item.sensorType(), "{0:.2f}".format(item), end="\n")
            # print("{:<15} {:<15} {:<15}".format(*item))'''
        print()

    def write_data(self, data):
        with open(self.csv_file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            # Write the header
            writer.writerow(["Sensor type", "Timestamp", "Sensor data"])
            # Write the data
            writer.writerows(data if isinstance(data, list) else [data])
