class Human:
    def __init__(self, name, age, sex) :
        self.name = name
        self.age = age
        self.sex = sex
    pass

chi = Human("치이카와", 1, "??")
print(chi.name)

class Stock:
    def __init__(self, name, number, updown) :
        self.name = name
        self.number = number
        self.updown = updown
    pass

    def code(self, code) :
        self.code = code
    pass

stock = Stock("samsung", 1000, "up")
stock.code ("00590")
print(stock.name, stock.number, stock.updown)
print(stock.code)
