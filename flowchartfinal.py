

def sort_list(numbers:list):
  
    
    numbers = [1, 2, 56, 32, 51, 2, 8, 92, 15]
    
    i = 0
    N = len(numbers)
    while i < N - 1:
        j = 0
        while j < N - i - 1:
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j + 1]
                numbers[j + 1] = numbers[j]
                numbers[j] = temp
            else:
                j = j + 1
        i = i + 1
    return (numbers)



def main():
    
    numbers=[1,2,56,32,51,89,21,2,8,92,15]
    print(numbers)
    numbers1=sort_list(numbers)
    print(numbers1)
        
    
if __name__ == '__main__':
    main()