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