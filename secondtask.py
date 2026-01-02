def check_marks(marks):
    if marks >= 90:
        print("Grade: A")
        print("Excellent!")
    elif marks >= 75:
        print("Grade: B")
        print("Very good!")
    elif marks >= 60:
        print("Grade: C")
        print("Good effort!")
    else:
        print("Grade: F")
        print("Keep trying!")
while True:
    marks = int(input("Enter marks (0–100): "))

    if 0 <= marks <= 100:
        break
    else:
        print("Invalid marks! Please enter between 0 and 100.")
check_marks(marks)
