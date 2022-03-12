import csv
from datetime import datetime


def main():
    try:
        print("Jergon's Grocery")

        products_dict = read_dict('w09/products.csv')
        # print(products_dict)





        with open('W09/request.csv', 'rt') as request_file:

                # Use the csv module to create a reader
                # object that will read from the opened file.
            reader = csv.reader(request_file)

            next(reader)
            print()
            
            #for when order sent to store for order pick-up
            # print("Requested Order:")

            total_quantity= 0
            subtotal = 0
            total_item_price = 0
            for row in reader:
                product_num = row[0]
                quantity = row[1]
                product_info_list = products_dict[product_num]
                product_name = product_info_list[1]
                product_price = product_info_list[2]
                total_quantity += int(quantity)
                total_item_price = int(quantity) * float(product_price)
                subtotal += float(total_item_price)
                
                
                print(f'''{product_name}: {quantity} @ {product_price}''')
                
        row_count = sum(1 for row in csv.reader( open('W09/request.csv') )  )

        print()    
        print(f"Number of items: {total_quantity}")
        print(f"Subtotal: ${subtotal:.2f}")
        tax = subtotal * 0.06
        print(f"Sales Tax: ${tax:.2f}")
        complete_total = subtotal + tax
        print(f"Total: ${complete_total:.2f}")
        print()

        print("Thanks for shopping at your local Jergon's Grocery Store.")
        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%c}")
        print()

        print('Here about our monthly giveaway yet? We are giving a $100')
        print('gift card to one of our wonderful customers. Want a chnace to win? ')
        print("It's simple. Just go to our online website at www.jergonsgrocer.com")
        print("and fill out a survey on how well we did on your visit. That's all!")
        print('Good luck and have a great day!')
        print('(Name drawn the first day of the following month)')


                # for i in product_info_list[0]:
                #     i =+ 1 
                # product_count = len(row)

        #if order sent to store to be prepared for customer for pickup:
        # print('Please prepare order promptly')        
        # order_time = row_count  * 5
        # print(f'Estimated fullfllment time: {order_time} minutes')    
        print()   

    except FileNotFoundError as not_found_err:
        print("Error: File not found or missing")
        print(not_found_err)

    except PermissionError as perm_err:
        print(perm_err)
        print("Access is denied to the requested file. Please gain access to continue.")

    except KeyError as key_err:
        print("Error: Product ID unkown in request.csv file")
        print(key_err)    



        # for line in request_file:
        #     request_list.append(line)
        #     if item in request_list:




def read_dict(filename):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    product_dict = {}

    with open(filename, 'rt') as product_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(product_file)

        next(reader)
        # for line in product_file:
        
        print()
        # print("All Store Products:")
        for row in reader:
            key = row[0]
            product_dict[key]= [row[0], row[1], row[2]]
            # print(product_dict[key])




            # item_id = key
            # value_list = product_file[0-2]

    # return key, value_list
    return product_dict

if __name__ == "__main__":
    main()


