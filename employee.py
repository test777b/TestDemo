# employee.py

from datetime import date
y_added_line 1
class Employee:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
x_added_line 3
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()
y_added_line 2
    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = date.fromisoformat(value)

a =Employee("sam", "2001-02-07")
a2 =Employee("a2", "2001-02-07")
print(a.name)
a.name = "dam"
print(a.name)
Employee.name = "rfvrfv"
print("----------------")
print(a.name)
print(a2.name)
print("----------------")

x_added_line 1

x_added_line 2

y_added_line 3

y_added_line 4
