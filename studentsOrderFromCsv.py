import os
import pandas as pd

csv_file_path = 'students_data.csv'

if os.path.exists(csv_file_path) and os.path.getsize(csv_file_path) > 0:
    df = pd.read_csv(csv_file_path)
    df = df.sort_values(by=['StudentID', 'FirstName', 'LastName'])
    df.to_csv(csv_file_path, index=False)
    exit(f'Student records sorted and saved to {csv_file_path}')

import csv
from faker import Faker

fake = Faker()

num_students = 100

headers = ['StudentID', 'FirstName', 'LastName', 'Email', 'DateOfBirth']

students_data = []
for _ in range(num_students):
    student = {
        'StudentID': fake.unique.random_int(min=1000, max=9999),
        'FirstName': fake.first_name(),
        'LastName': fake.last_name(),
        'Email': fake.email(),
        'DateOfBirth': fake.date_of_birth(minimum_age=18, maximum_age=25).strftime('%Y-%m-%d')
    }
    students_data.append(student)

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(students_data)

print(f'Successfully generated {num_students} student records and saved to {csv_file_path}')



