#CS175L
#Brandon Govea
#Chapter 7 Expense Pie Chart

import matplotlib.pyplot as plt

def main():
    try:
        expense_file = open("expenses.txt", "r")
    except IOError:
        print("File not found or cannot be opened")

    labels = []
    values = []

    for row in expense_file:
        row = row.strip('\n')
        label, value = row.split('\t')
        try:
            value = int(value)
            labels.append(label)
            values.append(value)
        except ValueError:
            print("Error")

    plt.pie(values, labels = labels)
    plt.title("Monthly Expenses")
    plt.show()

if __name__ == "__main__":
    main()
