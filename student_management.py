import json


class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = {}
        self.load_students()

    def load_students(self):
        try:
            with open(self.filename, "r") as file:
                self.students = json.load(file)
        except FileNotFoundError:
            self.students = {}

    def save_students(self):
        with open(self.filename, "w") as file:
            json.dump(self.students, file)

    def get_grade(self, score):
        if score >= 70:
            return "A"
        elif score >= 60:
            return "B"
        elif score >= 50:
            return "C"
        elif score >= 45:
            return "D"
        elif score >= 40:
            return "E"
        else:
            return "F"

    def get_valid_score(self):
        while True:
            try:
                score = int(input("Enter score (0–100): "))
                if 0 <= score <= 100:
                    return score
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a number.")

    def add_student(self):
        name = input("Enter student name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        score = self.get_valid_score()
        grade = self.get_grade(score)

        self.students[name] = {
            "score": score,
            "grade": grade
        }

        self.save_students()
        print("Student added successfully")

    def display_students(self):
        if not self.students:
            print("No students available")
            return

        print("\n--- Student Records ---")
        for name, info in self.students.items():
            print(name, "- Score:", info["score"], "Grade:", info["grade"])

    def calculate_average(self):
        if not self.students:
            print("No students to calculate average")
            return

        total = sum(info["score"] for info in self.students.values())
        average = total / len(self.students)
        print("Average Score:", average)

    def update_student(self):
        name = input("Enter student name to update: ").strip()

        if name not in self.students:
            print("Student not found.")
            return

        new_score = self.get_valid_score()
        new_grade = self.get_grade(new_score)

        self.students[name]["score"] = new_score
        self.students[name]["grade"] = new_grade

        self.save_students()
        print("Student updated successfully")

    def delete_student(self):
        name = input("Enter student name to delete: ").strip()

        if name not in self.students:
            print("Student not found.")
            return

        del self.students[name]
        self.save_students()
        print("Student deleted successfully")


def main():
    manager = StudentManager()

    while True:
        print("\n1. Add Student")
        print("2. Display Students")
        print("3. Calculate Average")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.display_students()
        elif choice == "3":
            manager.calculate_average()
        elif choice == "4":
            manager.update_student()
        elif choice == "5":
            manager.delete_student()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
=======
import json


class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = {}
        self.load_students()

    def load_students(self):
        try:
            with open(self.filename, "r") as file:
                self.students = json.load(file)
        except FileNotFoundError:
            self.students = {}

    def save_students(self):
        with open(self.filename, "w") as file:
            json.dump(self.students, file)

    def get_grade(self, score):
        if score >= 70:
            return "A"
        elif score >= 60:
            return "B"
        elif score >= 50:
            return "C"
        elif score >= 45:
            return "D"
        elif score >= 40:
            return "E"
        else:
            return "F"

    def get_valid_score(self):
        while True:
            try:
                score = int(input("Enter score (0–100): "))
                if 0 <= score <= 100:
                    return score
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a number.")

    def add_student(self):
        name = input("Enter student name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        score = self.get_valid_score()
        grade = self.get_grade(score)

        self.students[name] = {
            "score": score,
            "grade": grade
        }

        self.save_students()
        print("Student added successfully")

    def display_students(self):
        if not self.students:
            print("No students available")
            return

        print("\n--- Student Records ---")
        for name, info in self.students.items():
            print(name, "- Score:", info["score"], "Grade:", info["grade"])

    def calculate_average(self):
        if not self.students:
            print("No students to calculate average")
            return

        total = sum(info["score"] for info in self.students.values())
        average = total / len(self.students)
        print("Average Score:", average)

    def update_student(self):
        name = input("Enter student name to update: ").strip()

        if name not in self.students:
            print("Student not found.")
            return

        new_score = self.get_valid_score()
        new_grade = self.get_grade(new_score)

        self.students[name]["score"] = new_score
        self.students[name]["grade"] = new_grade

        self.save_students()
        print("Student updated successfully")

    def delete_student(self):
        name = input("Enter student name to delete: ").strip()

        if name not in self.students:
            print("Student not found.")
            return

        del self.students[name]
        self.save_students()
        print("Student deleted successfully")


def main():
    manager = StudentManager()

    while True:
        print("\n1. Add Student")
        print("2. Display Students")
        print("3. Calculate Average")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.display_students()
        elif choice == "3":
            manager.calculate_average()
        elif choice == "4":
            manager.update_student()
        elif choice == "5":
            manager.delete_student()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()