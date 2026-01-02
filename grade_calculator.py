# Grade Calculator Program
# Calculates total marks, percentage, and grade

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "Fail"


def main():
    subjects = 5
    marks = []

    print("Enter marks for 5 subjects (0 - 100):")

    for i in range(1, subjects + 1):
        while True:
            try:
                mark = int(input(f"Subject {i}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter numbers only.")

    total = sum(marks)
    percentage = total / subjects

    print("\n----- Result -----")
    print("Total Marks:", total)
    print("Percentage:", percentage, "%")
    print("Grade:", calculate_grade(percentage))


if __name__ == "__main__":
    main()
