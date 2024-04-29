import functions as f

def main():
    while(True):
        nb_table = input("\n\nWhat table do you want to test ?\n")
        filename = 'table'+nb_table+'.txt'
        #filename = 'table1.txt'  
        table_data = f.read_table(filename)
        print(table_data)
        f.display_table(table_data)
        nw_matrice = f.north_west_corner_method(table_data)
        print(nw_matrice)
        
        
        
if __name__ == "__main__":
    main()
