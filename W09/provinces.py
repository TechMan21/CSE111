
def main():
    provinces_list = read_list("provinces.txt")
    print(provinces_list)


    provinces_list = provinces_list[1:-1]
    for i in range(0,len(provinces_list)): 
            if provinces_list[i] == "AB": 
                provinces_list[i] = "Alberta"

    
    occurrences = provinces_list.count("Alberta")

    print(f"Occurances of 'Alberta' in the modified list: {occurrences}")

def read_list(filename):

    provinces_list = []





    with open('W09/provinces.txt') as python_file:

        for line in python_file:

            # no_ab =
            # provinces_list.append(no_ab)
            clean_line = line.strip()
            provinces_list.append(clean_line)
            

        # for i in python_file:
        #     if i == "AB":
        #         i == "Alberta"

                # line = line.replace('AB', 'Alberta')



            # provinces_list.pop(0)

    # prov_list = []

    # with open("provinces.txt") as prov_file:

    #     for line in prov_file:

    #         no_ab = line.replace('AB', 'Alberta')
    #         prov_list.append(no_ab)
    #         no_space = line.strip()
    #         prov_list.append(no_space)
    #
        return provinces_list




if __name__ == "__main__":
    main()