#CS175L
#Brandon Govea
#AverageFromInput

def main():
    try:
        number_file = open('numbers.txt', 'r')
        total = 0
        count = 0
        for number in number_file:
            try:
            
                total += float(number)
                count += 1
                print(f'I read in {count} number(s) Current number is: {number.strip()} Total is: {total:.2f}')
            except ValueError:
                print(f'Bad data: {number.strip()} skipping')

        if count == 0:
            print("No numbers found in the file.")
        else:
            average = total / count

    except IOError:
        print("File not found: numbers.txt - existing")

    


    print("Average: ", average)
        
    pass

if __name__ == '__main__':
    main()
