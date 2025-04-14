import csv
import random

# The path to the dataset file
dataset_path = './FER2013/fer2013.csv'
imbalanced_output_path = './FER2013/imbalanced_train_100.csv' #Save the processed dataset

with open(dataset_path, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  
    data = list(reader)

imbalanced_train_data = []

# The initialization dictionary stores the number of samples for each sentiment category in the Train data
train_class_counts = {}

# Define the target sample size
target_counts = {
    '0': 1308,  
    '1': 430,    
    '2': 1744,  
    '3': 4300,  
    '4': 2612,  
    '5': 872,   
    '6': 3488,  
}

for row in data:
    usage = row[2]  
    emotion = row[0]  
    if usage == 'Training':
        if emotion in train_class_counts:
            train_class_counts[emotion] += 1
        else:
            train_class_counts[emotion] = 1

# Samples in the Train dataset are filtered based on the target number of samples
for emotion in target_counts:
    if emotion in train_class_counts:
        emotion_data = [row for row in data if row[0] == emotion and row[2] == 'Training']
        random.shuffle(emotion_data)
        sampled_data = emotion_data[:target_counts[emotion]]
        imbalanced_train_data.extend(sampled_data)

random.shuffle(imbalanced_train_data)

imbalanced_training_data = [row[:2] for row in imbalanced_train_data]  


with open(imbalanced_output_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['emotion', 'pixels'])
    for row in imbalanced_training_data:
        writer.writerow(row)


imbalanced_class_counts = {emotion: 0 for emotion in target_counts}  
for row in imbalanced_training_data:
    emotion = row[0]
    imbalanced_class_counts[emotion] += 1


print("\nImbalanced dataset class counts for Train data:")
for emotion, count in imbalanced_class_counts.items():
    print(f"Emotion {emotion}: {count}")

