def bubble_sort(list_items):
    for i in range(len(list_items)):
        for j in range(len(list_items) - i - 1):
            if list_items[j] > list_items[j + 1]:
                temp = list_items[j]
                list_items[j] = list_items[j + 1]
                list_items[j + 1] = temp
    print(f"The sorted list using bubble sort: {list_items}")

def main():
    items = [5, 2, 6, 1, 4]
    bubble_sort(items)

if __name__ == "__main__":
    main()
