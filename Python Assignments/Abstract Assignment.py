from abc import ABC, abstractmethod

#this is the abstract parent class
class car(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ", amount)
    @abstractmethod
    def payment(self, amount):
            pass
#this class defines the abstract parent class with more detail
class DebitCardPayment(car):
    def payment(self,amount):
        print('Your purchase amount of {} exceedd your $100 limit '.format(amount))

obj = DebitCardPayment()
obj.paySlip("$400")
obj.payment("400")
