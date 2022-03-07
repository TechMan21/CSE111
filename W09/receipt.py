import csv

def main():

    products_dict = read_dict('w09/products.csv')
    # print(products_dict)
    

    

    with open('W09/request.csv', 'rt') as request_file:

         # Use the csv module to create a reader
         # object that will read from the opened file.
        reader = csv.reader(request_file)

        next(reader)
        print()
        
        print("Requested Order:")

        for row in reader:
            product_num = row[0]
            quantity = row[1]
            product_info_list = products_dict[product_num]
            product_name = product_info_list[1]
            product_price = product_info_list[2]
            

            
            print(f'''{product_name}: {quantity} @ {product_price}''')
            print()
    row_count = sum(1 for row in csv.reader( open('W09/request.csv') )  )
    
            # for i in product_info_list[0]:
            #     i =+ 1 
            # product_count = len(row)
    print('Please prepare order promptly')        
    order_time = row_count  * 5
    print(f'Estimated fullfllment time: {order_time} minutes')    
    print()   





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
        print("All Store Products:")
        for row in reader:
            key = row[0]
            product_dict[key]= [row[0], row[1], row[2]]
            print(product_dict[key])




            # item_id = key
            # value_list = product_file[0-2]

    # return key, value_list
    return product_dict

if __name__ == "__main__":
    main()


