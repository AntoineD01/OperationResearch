import functions as f

def main():
    while(True):
        test = -1
        while (test != 1 and test != 2):
            test = int(input("\nDo you want to try the tables provided (1) or create one (2) ?\n"))
        if test == 1:
            nb_table = input("\n\nWhat table do you want to test ?\n")
            filename = 'table'+nb_table+'.txt'
            table_data = f.read_table(filename)
            table_penalties = f.copy.deepcopy(table_data)  
            print(f"\nHere is the table {nb_table} :")
            f.display_table(table_data)
            method = -1
            while (method != 1 and method != 2):
                method = int(input("\nWhat method do you want ? (1 for North-West, 2 for Balas-Hammer) ?\n"))
            if method == 1:
                nw_matrice = f.north_west_corner_method(table_data)
                f.total_cost(nw_matrice, table_penalties)
            else:
                start_time = f.time.time()  # start time before the loop
                vogel_matrice = f.vogel(table_data)
                end_time = f.time.time()  # end time after the loop
                theta_nw = end_time - start_time  # compute the execution time
                print(f"Execution time is {theta_nw} secondes")
        else:
            size = -1
            while (size <4):
                size = int(input("What should be the size of the table ? (bigger than 4*4 needed)"))
            random_matrix = f.generate_transportation_problem(size)
            f.display_table(random_matrix)
            table_penalties = f.copy.deepcopy(random_matrix)  
            method = -1
            while (method != 1 and method != 2):
                method = int(input("\nWhat method do you want ? (1 for North-West, 2 for Balas-Hammer) ?\n"))
            if method == 1:
                nw_matrice = f.north_west_corner_method(random_matrix)
                f.total_cost(nw_matrice, table_penalties)
            else:
                start_time = f.time.time()  # start time before the loop
                vogel_matrice = f.vogel(random_matrix)
                end_time = f.time.time()  # end time after the loop
                theta_nw = end_time - start_time  # compute the execution time
                print(f"Execution time is {theta_nw} secondes")
        
if __name__ == "__main__":
    main()