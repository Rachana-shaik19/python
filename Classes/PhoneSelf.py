"""

"""


class Phone:
    def __init__(self, number, name, country_code):
        self.number = number
        self.name = name
        self.country_code = country_code

    @staticmethod  # @staticmethod is decorator
    # staticmethod(function_name)
    def contact(number, name, country_code):
        return f"name : {name}\nnumber: {country_code}: {number}"

    def add_contact(self):
        Phone.contact(self.number, self.name, self.country_code)


contact_1 = Phone("7283721667", "Revanth", "+91")
print(contact_1.contact("9951290889", "Rachana", "+91"))
number_1 = int(input("Enter number of contacts: "))
print(contact_1.add_contact())
