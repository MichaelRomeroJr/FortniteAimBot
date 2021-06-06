# -*- coding: utf-8 -*-
import torch 

def objects_detected_list(tensor, classes):
    objects=[]
    PersonIndexes = [] #Index of 'person' in tensor
    CurrentIndex = 0

    for t in tensor:
        cls = int(t[-1])
        ObjectDetected = "{0}".format(classes[cls]) #label
        objects.append(ObjectDetected)
        
        print(ObjectDetected, ' ',end =" ")
        if ObjectDetected == 'person':
            PersonIndexes.append(CurrentIndex)
        CurrentIndex+=1
        
    Vectors_List = []
    for i in PersonIndexes:
        vector = tensor[i].tolist()
        Vectors_List.append(vector)
      
    Tensor_People = torch.tensor(Vectors_List, device='cuda:0')
  
    return Tensor_People


def DeterminePeople(tensor, classes):
    """ Input: Tensor of all objects detected on screen
        Output: Tensor of only 'people' detected on screen """

    PersonIndexes = [] #Index of 'person' in tensor
    CurrentIndex = 0
    for t in tensor:
        cls = int(t[-1])
        ObjectDetected = "{0}".format(classes[cls]) #label 
        print(ObjectDetected, ' ',end =" ")
        if ObjectDetected == 'person':
            PersonIndexes.append(CurrentIndex)
        CurrentIndex+=1
        
    Vectors_List = []
    for i in PersonIndexes:
        vector = tensor[i].tolist()
        Vectors_List.append(vector)
      
    Tensor_People = torch.tensor(Vectors_List, device='cuda:0')
  
    return Tensor_People

def BottomObjectIndex(tensor):
    """Object with highest Y Coordinate is at the the bottom of the screen
        self is likely detected and has the highest Y Coordinate value"""
    tens = tensor[0] #.int() #tensor with integer values
    y2 = int(tens[4].item()) #tensor = [something, x1, y1, x2, y2, confidence, confidence, something]
    CurrentYMax = y2  #Assume Object with YMax is the first object
    
    TensorIndex = 0
    TensorIndex_BottomObject = 0
    
    for t in tensor:
        tens = t #.int() #Bottom Right Coordinates of rectangle
        y2 = int(tens[4].item())
        
        if y2 > CurrentYMax: #Update CurrentYMax when new max is found
            CurrentYMax = y2
            TensorIndex_BottomObject = TensorIndex 
        
        TensorIndex+=1
        
    return TensorIndex_BottomObject

def CreateNewOutput(tensor, index):
    NewOutput = torch.cat([tensor[0:index], tensor[index+1:]])
    return NewOutput

def RemoveSelf(tensor):
    """ Input:  Tensor of only 'people' detected on screen
                & Index of person detected at the bottom of the screen
        Output: Tensor with index of bottom index removed from tensor"""
    
    SelfIndex = BottomObjectIndex(tensor) #Find tensor index of object at bottom of screen
    Tensor_WithoutSelf = CreateNewOutput(tensor, SelfIndex) 
    
    return Tensor_WithoutSelf
