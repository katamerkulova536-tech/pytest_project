

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

