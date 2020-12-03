from torchvision.datasets import ImageFolder
from torchvision import transforms
import numpy as np
import torch

class Preprocessing():

    def __init__(self, path=None, img=None):
        self.directory = path
        self.img = img
    
    def __image_transformation(self):
        transform = transforms.Compose([
                transforms.Resize((130,130)),
                transforms.CenterCrop(128),
                transforms.Grayscale(1),
                transforms.ToTensor(),
                transforms.Normalize(0.5,0.5)
        ])
        return transform
    
    
    def preprocessed_arrays(self):
        # proprocessing for predicting predicting
        img = self.img
        transforms =  self.__image_transformation()
        return torch.tensor(np.expand_dims(transforms(img),0))

    def preprocessed_dataset(self):
        # get data and apply transforms
        transformations =  transforms.Compose([
                transforms.RandomHorizontalFlip(),
                transforms.RandomPerspective(0.2,p=0.5),
                self.__image_transformation()])
        
        dataset_train = ImageFolder(self.directory['train'], 
                                transform=transformations)
        dataset_test = ImageFolder(self.directory['test'], 
                                transform=self.__image_transformation())
    
        return dataset_train, dataset_test
