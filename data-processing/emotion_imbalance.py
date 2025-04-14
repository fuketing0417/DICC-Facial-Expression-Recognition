import os
import random

# Process Emotion-domestic datasets and MMAFEDB datasets

def count_images(directory):
    
    extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']  
    count = 0
    for file in os.listdir(directory):
        if any(file.lower().endswith(ext) for ext in extensions):
            count += 1
    return count

def remove_random_images(directory, num_to_keep):
    extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']  
    images = [file for file in os.listdir(directory) if any(file.lower().endswith(ext) for ext in extensions)]
    num_to_remove = max(0, len(images) - num_to_keep)
    
    if num_to_remove > 0:
        random.shuffle(images)
        for image in images[:num_to_remove]:
            os.remove(os.path.join(directory, image))
            # print(f"Deleted image: {image}")

#Specify the dataset path
image_directory = './data/emotion-domestic/imbalanced_train_100/fear'
# image_directory = './data/MMAFEDB/imbalanced_train_100/fear'

# Count the number of initial images
initial_count = count_images(image_directory)
print(f"Initial number of images in '{image_directory}': {initial_count}")

# The number of target images
target_count = 1000

# Delete pictures randomly
remove_random_images(image_directory, target_count)

# Count the number of remaining images
final_count = count_images(image_directory)
print(f"Number of images after removal in '{image_directory}': {final_count}")