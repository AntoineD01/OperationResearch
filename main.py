import functions as f

def main():
    while(True):
        nb_table = input("\n\nWhat table do you want to test ?\n")
        filename = 'table'+nb_table+'.txt'
        #filename = 'table1.txt'  
        table_data = f.read_table(filename)
        print(f"\nHere is the table {nb_table} :")
        f.display_table(table_data)
        method = int(input("\nWhat method do you want ? (1 for North-West, 2 for Balas-Hammer) ?\n"))
        if method == 1:
            nw_matrice = f.north_west_corner_method(table_data)
        else:
            print("SOON")
           
if __name__ == "__main__":
    main()
