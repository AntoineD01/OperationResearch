import functions as f

def main():
    while True:
        nb_table = input("Enter the name of the file containing the table data: ")
        filename = "table"+nb_table+".txt"
        table_data = f.read_table(filename)

        print("\nInitial table:")
        f.display_table(table_data)

        while True:
            algorithm = input("\nChoose the algorithm for the initial basic feasible solution (N for North-West Corner Method, B for Balas-Hammer Method): ")

            if algorithm.lower() == 'n':
                initial_solution = f.north_west_corner_method(table_data)
                break
            elif algorithm.lower() == 'b':
                initial_solution = f.balas_hammer_method(table_data)
                break
            else:
                print("Invalid algorithm choice. Please try again.")

        print("\nInitial basic feasible solution:")
        f.display_table(initial_solution)

        f.stepping_stone_method(initial_solution)

        continue_program = input("\nDo you want to solve another transportation problem? (Y/N): ")
        if continue_program.lower() != 'y':
            print("Exiting the program...")
            break

if __name__ == "__main__":
    main()