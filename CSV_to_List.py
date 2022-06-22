import csv
import pathlib

data_list = [[]]

for path in pathlib.Path("sampled_data").iterdir():
    if path.is_file():
        current_file = open(path, "r")
        csv_reader = csv.DictReader(current_file)

        for row in csv_reader:
            if row["acc_x"] == "":
                data_list.append([])
                continue

            new_data = {
                        "acc_x" : float(row["acc_x"]),
                        "acc_y" : float(row["acc_y"]),
                        "acc_z" : float(row["acc_z"]),
                        "gyro_x": float(row["gyro_x"]),
                        "gyro_y": float(row["gyro_y"]),
                        "gyro_z": float(row["gyro_z"]),
                        "label" : row["label"]
                    }
            
            data_list[-1].append(new_data)

while True:
    try:
        data_list.remove([])
    except:
        break

total_dataset = []

for i in range(len(data_list)):
    sample = data_list[i]

    Acc_x = [elem["acc_x"] for elem in sample]
    Acc_y = [elem["acc_y"] for elem in sample]
    Acc_z = [elem["acc_z"] for elem in sample]
    Gyro_x = [elem["gyro_x"] for elem in sample]
    Gyro_y = [elem["gyro_y"] for elem in sample]
    Gyro_z = [elem["gyro_z"] for elem in sample]

    accelerations_and_rotations = [Acc_x, Acc_y, Acc_z, Gyro_x, Gyro_y, Gyro_z]

    label = sample[0]["label"]

    total_dataset.append((accelerations_and_rotations, label))

            