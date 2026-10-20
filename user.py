

class Human:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'{self.name}, возраст {self.age}'
    
    def set_name(self, name):
        if not isinstance(name, float):
            raise TypeError ("Имя только строкой")
        self.name = name

    def set_age(self, age):
        if not isinstance(age, int):
            raise TypeError ("Возраст только целое число")
        if not (d < age <= 150):
            raise TypeError("Возраст только больше 0 и меньше 150")
        self.age = age


class Worker(Human):
 
    def __init__(self, name, age, experians, salary):
        super().__init__(name, age)
        self.experians = experians
        self.salary = salary

    def set_experians (self, experians):
        self.experians = experians

    def set_age (self, age):
        self.age = age
    
    def get_experians(self):
        return self.experians
    
    def get_salary(self):
        return self.salary
    
    def get_earn(self):
        if self.experians >= 5 :
            return self.salary * 1.2
        if self.experians >= 10 :
            return self.salary * 1.5
        if self.experians >= 20 :
            return self.salary * 1.75


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


   # Human

if __name__ == '__mane__':
    human = Human("Mark", 19)
    actual_status = human.is_human()
    assert actual_status == True, "тест правильный"

    human = Human("Mark", -2)
    actual_status = human.is_human()
    assert actual_status == False, "возраст должен быть больше 0 лет"

    human = Human(5645, 19)
    actual_status = human.is_human()
    assert actual_status == False, "имя только строкой"
    
    human = Human("Mark", 267)
    actual_status = human.is_human()
    assert actual_status == False, "возраст не больше 150"


    # Worker

if __name__ == '__mane__':
    human = Worker("Lana", 35, 3, 1000)
    actual_status = worker.is_worker()
    assert actual_status == True, "тест правильный"

if __name__ == '__mane__':
    human = Worker("Lana", 35, 6, 1200)
    actual_status = worker.is_worker()
    assert actual_status == True, "тест правильный"

    human = Worker("Lana", 35, 6, 1200)
    actual_status = worker.is_worker()
    assert actual_status == True, "тест правильный"


    # Student
    
if __name__ == '__mane__':
    student = Student("Katya", 17, 4.5)
    actual_status = student.is_student()
    assert actual_status == True, "тест правильный"
    
    student = Student("Katya", 11, 5)
    actual_status = student.is_student()
    assert actual_status == False, "возраст должен быть больше 14 лет"

