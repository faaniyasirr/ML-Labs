# SECTION A - PYTHON

# Q1
a = 25
b = 45

a, b = b, a

print("a =", a)
print("b =", b)


# Q2
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


print(is_prime(13))


# Q3
terms = 9
a = 0
b = 1

for i in range(terms):
    print(a, end=" ")
    a, b = b, a + b

print()


# Q4
def remove_duplicates(values):
    new_list = []

    for value in values:
        if value not in new_list:
            new_list.append(value)

    return new_list


values = [4, 7, 4, 9, 2, 7, 5, 2]

print(remove_duplicates(values))


# Q5
def multiply(*numbers):
    answer = 1

    for num in numbers:
        answer *= num

    return answer


print(multiply(4, 3, 2))


# Q6
word = "computer"

frequency = {}

for letter in word:
    frequency[letter] = word.count(letter)

print(frequency)


# Q7
employees = [
    {"name": "Bilal", "department": "Accounts", "salary": 64000},
    {"name": "Sana", "department": "HR", "salary": 79000},
    {"name": "Usman", "department": "IT", "salary": 71000}
]

highest = employees[0]

for employee in employees:
    if employee["salary"] > highest["salary"]:
        highest = employee

print(highest)


# Q8
numbers = [4, 7, 10, 13, 16, 19, 22, 25]

odd_numbers = list(
    filter(lambda n: n % 2 != 0, numbers)
)

print(odd_numbers)


# SECTION B - NUMPY

import numpy as np


# Q9
numbers = np.arange(1, 31)
matrix = numbers.reshape(5, 6)

print(matrix)


# Q10
matrix = np.eye(6)

for i in range(6):
    matrix[i, i] = (i + 1) * 2

print(matrix)


# Q11
numbers = np.random.randint(1, 101, 25)

print(numbers)
print("Sum:", numbers.sum())
print("Mean:", numbers.mean())
print("Standard deviation:", numbers.std())


# Q12
matrix = np.array([
    [3, 5, 7, 9],
    [11, 13, 15, 17],
    [19, 21, 23, 25],
    [27, 29, 31, 33]
])

diagonal = np.diagonal(matrix)

print(diagonal)
print("Diagonal sum:", diagonal.sum())


# Q13
A = np.array([
    [2, 3, 4],
    [5, 6, 7],
    [8, 9, 10]
])

B = np.array([
    [10, 9, 8],
    [7, 6, 5],
    [4, 3, 2]
])

element_result = A * B
matrix_result = A @ B

print("Element-wise multiplication:")
print(element_result)

print("Matrix multiplication:")
print(matrix_result)


# Q14
temperatures = np.array([
    28, 36, 39, 32, 37, 34,
    41, 30, 38, 33, 40, 31
])

hot_days = temperatures[temperatures > 35]

print(hot_days)
print("Number of days:", len(hot_days))


# Q15
numbers = np.array([8, 18, 28, 38, 48])

minimum = numbers.min()
maximum = numbers.max()

normalized = (numbers - minimum) / (maximum - minimum)

print(normalized)


# Q16
marks = np.array([
    [74, 82, 69],
    [61, 77, 73],
    [89, 84, 91],
    [56, 65, 62],
    [78, 88, 81]
])

total = marks.sum(axis=1)
average = marks.mean(axis=1)

print("Total marks:", total)
print("Average marks:", average)


# Q17
numbers = np.array([5, 8, 11, 14, 17, 20, 23, 26])

numbers[numbers % 2 == 0] = -1

print(numbers)


# SECTION C - PANDAS

import pandas as pd


# Q18
students = pd.DataFrame({
    "name": [
        "Bilal", "Sana", "Usman", "Laiba",
        "Haris", "Anaya", "Saad", "Maha"
    ],
    "section": [
        "A", "B", "A", "B",
        "A", "B", "A", "B"
    ],
    "marks": [
        82, 69, 91, 47,
        86, 58, 42, 79
    ]
})

print(students)
print(students.describe())


# Q19
try:
    df = pd.read_csv("students.csv")
except FileNotFoundError:
    df = pd.DataFrame({
        "name": ["Bilal", "Sana", "Usman", "Laiba"],
        "marks": [82, 69, np.nan, 74],
        "attendance": [89, 71, 76, np.nan]
    })

print(df.isnull().sum())

numeric_columns = df.select_dtypes(
    include="number"
).columns

for column in numeric_columns:
    df[column] = df[column].fillna(
        df[column].mean()
    )

print(df)


# Q20
below_50 = students.loc[
    students["marks"] < 50,
    ["name", "marks"]
]

print(below_50)


# Q21
section_marks = students.groupby(
    "section"
)["marks"].agg(["mean", "max"])

print(section_marks)


# Q22
attendance = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "attendance": [89, 71, 94, 67, 92, 76, 69, 83]
})

students_with_id = students.copy()
students_with_id["student_id"] = range(1, 9)

merged = pd.merge(
    students_with_id,
    attendance,
    on="student_id"
)

low_attendance = merged.loc[
    merged["attendance"] < 75,
    ["name", "attendance"]
]

print(low_attendance)


# SECTION D - MATPLOTLIB

import matplotlib.pyplot as plt


# Q23
average_marks = students.groupby(
    "section"
)["marks"].mean()

plt.bar(
    average_marks.index,
    average_marks.values
)

plt.xlabel("Section")
plt.ylabel("Average Marks")
plt.title("Average Marks by Section")

plt.show()


# Q24
plt.hist(
    students["marks"],
    bins=5
)

plt.xlabel("Marks")
plt.ylabel("Students")
plt.title("Student Marks Distribution")

plt.show()


# Q25
fig, axes = plt.subplots(
    1, 2,
    figsize=(10, 4)
)

axes[0].plot(
    students["name"],
    students["marks"],
    marker="o"
)

axes[0].set_title("Student Marks")
axes[0].set_xlabel("Student")
axes[0].set_ylabel("Marks")
axes[0].tick_params(
    axis="x",
    rotation=45
)

student_numbers = range(
    1,
    len(students) + 1
)

axes[1].scatter(
    student_numbers,
    students["marks"]
)

axes[1].set_title("Marks Scatter Plot")
axes[1].set_xlabel("Student Number")
axes[1].set_ylabel("Marks")

plt.tight_layout()
plt.show()