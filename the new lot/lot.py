#admin section#
class Admin:
    def __init__(self):
        self.admin_name = ""
        self.admin_id = ""
        self.phone_number = ""
        self.duty_day = ""
        self.duty_time = ""

    def input_details(self):
        self.admin_name = input("Enter Admin Name: ")
        self.admin_id = input("Enter Admin ID: ")
        self.phone_number = input("Enter Phone Number (starting with +254): ")
        self.duty_day = input("Enter Duty Day: ")
        self.duty_time = input("Enter Duty Time: ")

    def display_details(self):
        print("\n--- Admin Details ---")
        print(f"Admin Name: {self.admin_name}")
        print(f"Admin ID: {self.admin_id}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Duty Day: {self.duty_day}")
        print(f"Duty Time: {self.duty_time}")
        print("----------------------")


def main():
    admin = Admin()

    print("Welcome to Admin Details Input Program!")
    admin.input_details()

    print("\nThank you for providing the admin details. Here is what you entered:")
    admin.display_details()


if __name__ == "__main__":
    main()


#vechile section#
class Vehicle:
    def __init__(self):
        self.vehicle_name = ""
        self.vehicle_type = ""
        self.drive = ""

    def input_details(self):
        self.vehicle_name = input("Enter Vehicle Name: ")
        self.vehicle_type = input("Enter Vehicle Type: ")
        self.drive = input("Enter Drive (e.g. FWD, RWD, AWD): ")

    def display_details(self):
        print("\n--- Vehicle Details ---")
        print(f"Vehicle Name: {self.vehicle_name}")
        print(f"Vehicle Type: {self.vehicle_type}")
        print(f"Drive: {self.drive}")
        print("----------------------")

def main():
    vehicle = Vehicle()

    print("Welcome to Vehicle Details Input Program!")
    vehicle.input_details()

    print("\nThank you for providing the vehicle details. Here is what you entered:")
    vehicle.display_details()


if __name__ == "__main__":
    main()

#parking section#
class Parking:
    def __init__(self):
        self.parking_number = ""
        self.name = ""
        self.parking_type = ""

    def input_details(self):
        self.parking_number = input("Enter Parking Number: ")
        self.name = input("Enter Name: ")
        self.parking_type = input("Enter Parking Type: ")

    def display_details(self):
        print("\n--- Parking Details ---")
        print(f"Parking Number: {self.parking_number}")
        print(f"Name: {self.name}")
        print(f"Parking Type: {self.parking_type}")
        print("------------------------")


def main():
    parking = Parking()

    print("Welcome to Parking Details Input Program!")
    parking.input_details()

    print("\nThank you for providing the parking details. Here is what you entered:")
    parking.display_details()


if __name__ == "__main__":
    main()

#payment section#
class Payment:
    def __init__(self):
        self.payment_type = ""
        self.amount = 0
        self.paid_by = ""

    def input_details(self):
        self.payment_type = input("Enter Payment Type: ")
        self.amount = float(input("Enter Amount: "))
        self.paid_by = input("Enter Name of the Person who Paid: ")

    def display_details(self):
        print("\n--- Payment Details ---")
        print(f"Payment Type: {self.payment_type}")
        print(f"Amount: ${self.amount}")
        print(f"Paid By: {self.paid_by}")
        print("----------------------")


def main():
    payment = Payment()

    print("Welcome to Payment Details Input Program!")
    payment.input_details()

    print("\nThank you for providing the payment details. Here is what you entered:")
    payment.display_details()


if __name__ == "__main__":
    main()

class Customer:
    def __init__(self):
        self.customer_name = ""
        self.customer_id = ""
        self.phone_number = ""

    def input_details(self):
        self.customer_name = input("Enter Customer Name: ")
        self.customer_id = input("Enter Customer ID: ")
        self.phone_number = input("Enter Phone Number (starting with +254): ")

    def display_details(self):
        print("\n--- Customer Details ---")
        print(f"Customer Name: {self.customer_name}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Phone Number: {self.phone_number}")
        print("------------------------")

def main():
    customer = Customer()

    print("Welcome to Customer Details Input Program!")
    customer.input_details()

    print("\nThank you for providing the customer details. Here is what you entered:")
    customer.display_details()

if __name__ == "__main__":
    main()
