#CS175L
#Brandon Govea
#AverageFromInput

def main():
    number_file = open('numbers.txt', 'r')
    total = 0
    count = 0
    for number in number_file:
        total += float(number)
        count += 1

    average = total / count

    print(f'I read in 1 number(s) Current number is: 22.00 Toal is: 22.00')
    print(f'I read in 2 number(s) Current number is: 14.00 Toal is: 36.00')
    print(f'I read in 3 number(s) Current number is: -99.00 Toal is: -63.00')
    print("Average: ", average)
        
    pass

if __name__ == '__main__':
    main()
