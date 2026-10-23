

class Student(Human):
   
    def __init__(self, name, age, everage_mark):
        super().__init__(name, age)
        self.everage_mark = everage_mark

    def set_everage_mark (self, everage_mark):
        self.everage_mark = everage_mark
        
    def is_student(self):
        if self.age <= 14:
            return False
        return True
    

    if __name__ == '__mane__':
    student = Student("Katya", 17, 4.5)
    actual_status = student.is_student()
    assert actual_status == True, "тест правильный"
    
    student = Student("Katya", 11, 5)
    actual_status = student.is_student()
    assert actual_status == False, "возраст должен быть больше 14 лет"

