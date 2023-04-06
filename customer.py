from person import Person


class Customer(Person):

    def __init__(self, name, gender, acc_type, acc_num):
        super().__init__(name, gender)
        self._acc_type = acc_type
        self._acc_num = acc_num

    def __str__(self):
        return super().__str__() + "\nAccount Type; " + self._acc_type + "\nAccount Number; " + self._acc_num
