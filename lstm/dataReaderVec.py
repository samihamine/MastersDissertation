import torch
import numpy as np
from torch.utils.data import Dataset

class VectorDataset(Dataset):

    def __init__(self, file_paths, labels, seq_dim, batch_size=1):
        self.file_paths = file_paths
        self.num_files  = len(file_paths)
        self.batch_size = batch_size
        self.labels     = np.asarray(labels)
        self.seq_dim    = seq_dim

    def __len__(self):
        return self.num_files/self.batch_size

    def __getitem__(self, idx):

        randindex = np.random.randint(low=0, high=self.num_files)
        file   = open(self.file_paths[randindex], 'r', encoding='utf8')

        vectors   = list()
        for i in range(0, self.seq_dim):
            arr = np.fromstring(file.readline(), dtype=float, sep=" ")
            vectors.append(arr)

        return torch.tensor([np.asarray(vectors)]).float(), torch.tensor([self.labels[randindex]]).long()

