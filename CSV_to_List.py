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
                        "azimuth":float(row["azimuth"]),
                        "pitch" : float(row["pitch"]),
                        "roll" :  float(row["roll"]), 
                        "label" : row["label"]
                    }
            
            data_list[-1].append(new_data)

while True:
    try:
        data_list.remove([])
    except:
        break

def get_dataset(reduced_frequency = False, target_frequency_ratio = 1):

    total_dataset = []

    for i in range(len(data_list)):
        sample = data_list[i]

        Acc_x = [elem["acc_x"] for elem in sample]
        Acc_y = [elem["acc_y"] for elem in sample]
        Acc_z = [elem["acc_z"] for elem in sample]
        Gyro_x = [elem["gyro_x"] for elem in sample]
        Gyro_y = [elem["gyro_y"] for elem in sample]
        Gyro_z = [elem["gyro_z"] for elem in sample]
        Azimuth= [elem["azimuth"] for elem in sample]
        Pitch =  [elem["pitch"] for elem in sample]
        Roll =   [elem["roll"] for elem in sample]

        accelerations_and_rotations = [Acc_x, Acc_y, Acc_z, Gyro_x, Gyro_y, Gyro_z]

        label = sample[0]["label"]

        total_dataset.append((accelerations_and_rotations, label))

    if(reduced_frequency):
        assert(target_frequency_ratio >= 1)
        reduced_frequency_dataset = []
        for i in range(len(total_dataset)):
            reduced_frequency_dataset.append(([], total_dataset[i][1]))
            for j in range(len(total_dataset[i][0])):
                entry = total_dataset[i][0][j][0:-1:target_frequency_ratio]
                reduced_frequency_dataset[i][0].append(entry)

        return reduced_frequency_dataset

    return total_dataset
            