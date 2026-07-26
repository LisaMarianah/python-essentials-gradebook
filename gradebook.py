# Student Gradebook Manager - Lisa Hlongwane - Python Essentials 1

# Returns the average of a list of marks, or None if the list is empty
def calculate_average(marks):
  if len(marks) == 0:
      return None

  return sum(marks)/len(marks)


# Returns the highest and lowest mark as a tuple: (highest, lowest)
def highest_and_lowest(marks):
    highest = max(marks)
    lowest = min(marks)

    return highest, lowest
  

# Asks for a mark, validates it with try-except, returns the float or None
def read_valid_mark():
   try:
        mark = float(input("Mark (0-100): "))

        if mark < 0 or mark > 100:
            print("Mark must be between 0 and 100.")
            return None

        return mark

    except ValueError:
        print("That is not a number.")
        return None

# Adds a new student to the gradebook dictionary
def add_student(gradebook):
    name = input("Student name: ").strip()

    if name == "":
        print("Student name cannot be blank.")
        return

    if name in gradebook:
        print(f"{name} already exists.")
    else:
        gradebook[name] = []
        print(f"{name} added.")

# Adds one validated mark to an existing student
def add_mark(gradebook):
    name = input("Student name: ")

    if name not in gradebook:
        print("Student not found.")
        return

    mark = read_valid_mark()

    if mark is None:
        return

    gradebook[name].append(mark)
    print("Mark added.")

# Prints every student with marks and average
def view_all(gradebook):
    if len(gradebook) == 0:
        print("No students yet.")
        return

    for student, marks in gradebook.items():
        if len(marks) == 0:
        print(f"{student}: No marks")
        else:
        average = calculate_average(marks)
        print(f"{student}: {marks} - Average: {average:.2f}

# Prints one student's full summary
def student_summary(gradebook):
...

# Prints class statistics including pass/fail lists
def class_statistics(gradebook):
...

# Removes a student after y/n confirmation
def remove_student(gradebook):
...

# ---- main program ----

gradebook = {}
while True:
# print the menu, read the choice, call the right function

