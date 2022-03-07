import random

quantity = 3
def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, quantity)
    print(numbers)


def append_random_numbers(numbers_list, quantity=1):
    for i in range(quantity):
        new_num = round(random.uniform(0, 50), 1) 
        numbers_list.append(new_num)

    
#pytest.main(["-v", "--tb=line", "-rN", __file__])
main()