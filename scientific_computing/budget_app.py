
class Category:
    HEADER_LENGTH = 30
    DESCRIPTION_LENGTH = 23
    AMOUNT_PATTERN = "{0:>7.2f}"
    TOTAL_PATTERN = "{0:.2f}"

    def __init__(self, label):
        self.label = label
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.withdraw(amount, "Transfer to " + category.label):
            category.deposit(amount, "Transfer from " + self.label)
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        output = self.label.center(self.HEADER_LENGTH, "*") + "\n"
        for item in self.ledger:
            output += item["description"].ljust(self.DESCRIPTION_LENGTH, " ")[:self.DESCRIPTION_LENGTH]
            output += self.AMOUNT_PATTERN.format(item["amount"])
            output += '\n'
        output += "Total: " + self.TOTAL_PATTERN.format(self.get_balance())
        return output


def create_spend_chart(categories):
    output = "Percentage spent by category\n"
    total = 0
    expenses = []
    labels = []
    max_label_len = 0

    for category in categories:
        expense = sum([-item['amount'] for item in category.ledger if item['amount'] < 0])
        total += expense

        if len(category.label) > max_label_len:
            max_label_len = len(category.label)

        expenses.append(expense)
        labels.append(category.label)

    percentages = [(item / total) * 100 for item in expenses]
    labels = [item.ljust(max_label_len, " ") for item in labels]

    for level in range(100, -1, -10):
        output += str(level).rjust(3, " ") + '|'
        for percentage in percentages:
            output += " o " if percentage >= level else "   "
        output += " \n"

    output += "    " + "---" * len(labels) + "-\n"

    for i in range(max_label_len):
        output += "    "
        for label in labels:
            output += " " + label[i] + " "
        output += " \n"

    return output.strip('\n')


food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
clothing.deposit(1000, "deposit")
food.transfer(50, clothing)
clothing.withdraw(10, "shopping")
auto = Category("Auto")
auto.deposit(1000, "deposit")
auto.withdraw(23, "repair")
print('\n', food)
print('\n', clothing)
print('\n', auto)
print('\n', create_spend_chart([food, clothing, auto]))
