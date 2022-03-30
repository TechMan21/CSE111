def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    fruit_list.reverse()
    print(f'Reversed: {fruit_list}')
    fruit_list.append("orange")
    print(f'Append Orange: {fruit_list}')
    index = fruit_list.index("apple")
    fruit_list.insert(index, "cherry")
    print(f'Index cherry at apple: {fruit_list}')
    fruit_list.remove("banana")
    print(f'Removed Banana: {fruit_list}')
    i = fruit_list.pop()
    print(f"Popped item: {i}")
    print(f'Popped last: {fruit_list}')
    fruit_list.sort()
    print(f'Sorted: {fruit_list}')
    fruit_list.clear()
    print(f'Cleared: {fruit_list}')




if __name__ == "__main__":
    main()