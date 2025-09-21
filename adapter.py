class BankService:
    def make_payment(self, amount):
        print(f"Processing payment of ${amount} through BankService.")

#interface jeta client expect korbe
class PaymentService:
    def pay(self, amount):
        print(f"Processing payment of ${amount} through PaymentService.")

#ekhon adapter lagbe, BankService ke PaymentService er moto banate
class BankServiceAdapter(PaymentService): #inherit from PaymentService
    def __init__(self, bank_service):
        self.bank_service = bank_service # simply composition, mane BankService er instance ke rakhbo

    def pay(self, amount): #implementing the expected method
        self.bank_service.make_payment(amount) #call the method of BankService

#client code: expecting a 'pay(amount)' method
def process_payment(payment_service, amount):
    payment_service.pay(amount)

# #Attempt to use the BankService directly
# bank_service = BankService()
# process_payment(bank_service, 100)  # This will fail since BankService has no 'pay' method

#attempt to use the adapter
bank_service_adapter = BankServiceAdapter(BankService())#passing BankService instance to adapter
process_payment(bank_service_adapter, 100)  # This will work through the adapter