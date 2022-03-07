import csv

def main():
    STUDENT_ID = 0
    STUDENT_NAME = 1

    id_request = input('Please enter the student ID to retrieve name (without dashes): ')
    student_dict= read_dict('W09/students.csv', STUDENT_ID)

    # value = student_dict[id_request]
    # name_value = value[STUDENT_NAME]

    # #student name from input id
    # print(name_value)

    if id_request not in student_dict:
                print("No such student")
    else:
            # Retrieve the student name that corresponds
                # to the I-Number that the user entered.
        value = student_dict[id_request]
        name = value

                # Print the student name.
        print(name)

    

    # if id_request == student_dict[0]:
    #     student_info = student_dict[1]
    #     print (student_info)
    # else:
    #     print('No such student')


    print(student_dict)
    



def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, 'rt') as students_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(students_file)

        next(reader)
        
        students = []

        inumber = []



        for student in reader:

            students.append(student[0])

            inumber.append(student[1])

       

            dictionary = dict(zip(students, inumber))

        # student_dict = {rows[0]:rows[1] for rows in reader}

        # for row_list in reader:
        #     key = row_list[key_column_index]
        #     dictionary[key] = row_list
            # print(dictionary)


    return dictionary

        # for key, value in students_file:
if __name__ == "__main__":
    main()