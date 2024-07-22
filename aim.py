import numpy as np

# Define the data
data = [
    ["Vishal Singh", "Jaipur", "SKIT", "9636575691", "devops engineer"],
    ["Bhavesh Trivedi", "Kota", "Manipal", "8875364339", "prompt engineer"],
    ["Md Mushahid", "Dhanbad", "BCR", "9693251345", "software engineer"],
    ["Nikhil Garhwal", "Sikar", "SIET", "800706380", "entrepreneur"],
    ["Abhishek Giri", "Lucknow", "AKTU", "6307920537", "Software engineer"],
    ["Manthan Rudra", "Amravati", "BRMIT", "9404902644", "cloud engineer"],
    ["Yugal Singh", "Jaipur", "ISIM", "7976527610", "linux engineer"],
    ["Sahil Verma", "Bhiwani", "AMITY", "9518157511", "prompt engineer"],
    ["Abhinav Agarwal", "Jaipur", "Manipal", "8000499522", "Software engineer"],
    ["Harshita Sharma", "Jaipur", "amity", "9351529233", "devops engineer"],
    ["Anshul Mathur", "Jodhpur", "SPSU", "9636274630", "entrepreneur"],
    ["Pranav Jain", "Jaspur", "GLA", "9410780293", "Devops engineer"],
    ["Araman Anshari", "Kota", "RTU", "8306754589", "Software engineer"],
    ["Anil Pooniya", "Jaipur", "SKIT", "6376036737", "prompt engineer"],
    ["Ritesh Shani", "Raipur", "KU", "8434568290", "Software engineer"],
    ["Krish Yadav", "Jaipur", "SKIT", "7357689192", "Prompt engineer"],
    ["Sanjeev Ranjan", "Jaipur", "PIET", "7627095913", "to die"],
    ["Rahul Wankhade", "Nagpur", "GCEK", "9359733858", "data analyst"],
]

# Create a NumPy array
data_array = np.array(data)

# Function to get life purpose by college name
def get_life_purpose(college_name, data):
    life_purposes = []
    for row in data:
        if row[2].strip().lower() == college_name.strip().lower():
            life_purposes.append((row[0], row[4]))
    return life_purposes

# Example usage
college_name = "SKIT"
life_purposes = get_life_purpose(college_name, data_array)

if life_purposes:
    print(f"Life purposes of students from {college_name}:")
    for student, purpose in life_purposes:
        print(f"{student}: {purpose}")
else:
    print(f"No students found from {college_name}")
