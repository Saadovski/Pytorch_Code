import torch
import torchvision
from torch.utils.data import Dataset
from CSV_to_List import total_dataset
import torchvision.transforms as transforms

labels = {"STD" : 0,
          "WAL" : 1,
          "JOG" : 2,
          "JUM" : 3,
          "STU" : 4,
          "STN" : 5,
          "SCH" : 6,
          "SIT" : 7,
          "CHU" : 8,
          "CSI" : 9,
          "CSO" : 10,
          "FOL" : 11,
          "FKL" : 12,
          "BSC" : 13,
          "SDL" : 14}
          
class MobifallData(Dataset):
    def __init__(self):
        self.samples = total_dataset

    def __len__(self):
        return len(self.samples)

    #returns data, label
    def __getitem__(self, idx):
         data = [torch.FloatTensor(channel) for channel in self.samples[idx][0]]
         target = labels[self.samples[idx][1]]

         return torch.stack(data), target

dataset = MobifallData()
