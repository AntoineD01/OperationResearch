import functions as f

def main():
    while(True):
        test = int(input("\nDo you want to try the tables provided (1) or create one (2) ?\n"))
        if test == 1:
            nb_table = input("\n\nWhat table do you want to test ?\n")
            filename = 'table'+nb_table+'.txt'
            table_data = f.read_table(filename)
            table_penalties = f.copy.deepcopy(table_data)  
            print(f"\nHere is the table {nb_table} :")
            f.display_table(table_data)
            method = int(input("\nWhat method do you want ? (1 for North-West, 2 for Balas-Hammer) ?\n"))
            if method == 1:
                nw_matrice = f.north_west_corner_method(table_data)
                f.total_cost(nw_matrice, table_penalties)
            else:
                vogel_matrice = f.vogel(table_data)
        else:
            random_matrix = f.generate_transportation_problem(38)
            f.display_table(random_matrix)
            table_penalties = f.copy.deepcopy(random_matrix)  
            method = int(input("\nWhat method do you want ? (1 for North-West, 2 for Balas-Hammer) ?\n"))
            if method == 1:
                nw_matrice = f.north_west_corner_method(random_matrix)
                f.total_cost(nw_matrice, table_penalties)
            else:
                vogel_matrice = f.vogel(random_matrix)
        
if __name__ == "__main__":
    main()