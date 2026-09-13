class Student:
    college_name = "ABC College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        return sum(self.marks) / len(self.marks)

student1 = Student("Alice", [99, 100, 94])
print(f"Student Name: {student1.name}")
print(f"Average Marks: {student1.get_avg()}")