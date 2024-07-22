import numpy as np

# Initialize an empty list to store user inputs
data = []

# Define the number of entries to input
num_entries =  int(input("enter the number of entries you wanted"))# You can change this number based on how many entries you want to input

# Loop to input data
for _ in range(num_entries):
    name = input("Enter name: ")
    city = input("Enter city: ")
    college = input("Enter college: ")
    phone = input("Enter phone number: ")
    AIM = input("Enter Aim in life: ")
    data.append([name, city, college, phone,AIM])

# Create a NumPy array
data_array = np.array(data)

# Print the NumPy array
print(data_array)

