class School:
    def __init__(self, class_name, teacher, students, room_number, subject):
        self.class_name = class_name
        self.teacher = teacher
        self.students = students
        self.room_number = room_number
        self.subject = subject


class1 = School("Math A", "Mr. Smith", ["Alice", "Bob", "Charlie"], 101, "Mathematics")
class2 = School("English B", "Ms. Johnson", ["David", "Emma", "Frank"], 102, "English")
class3 = School("Science C", "Mr. Wilson", ["Grace", "Henry", "Ivy"], 103, "Science")
class4 = School("History D", "Mrs. Davis", ["Jack", "Kate", "Liam"], 104, "History")
class5 = School("Art E", "Mr. Brown", ["Olivia", "Peter", "Quinn"], 105, "Art")
class6 = School("Music F", "Ms. Lee", ["Rachel", "Sam", "Tom"], 106, "Music")
class7 = School("Physical Education G", "Coach Smith", ["Sophia", "Tyler", "Victoria"], 107, "Physical Education")
class8 = School("Computer Science H", "Mr. Johnson", ["William", "Xavier", "Yasmine"], 108, "Computer Science")
class9 = School("Geography I", "Mrs. Adams", ["Zoe", "Daniel", "Ella"], 109, "Geography")
class10 = School("Foreign Language J", "Ms. Garcia", ["Gabriel", "Hannah", "Isaac"], 110, "Foreign Language")


print(class1.class_name)
print(class2.teacher)
print(class3.students)
print(class4.room_number)
print(class5.subject)