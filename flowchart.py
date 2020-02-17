
list = [1,2,56,32,51,2,8,92,15]


def sort_list():
    
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return(list)
    

                



def main():
    
    while True:
        numbers=[1,2,56,32,51,2,8,92,15]
        print(numbers)
        numbers1=sort_list()
        print(numbers1)
        break
    
if __name__ == '__main__':
    main()

