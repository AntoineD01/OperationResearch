import functions as f

def main():
    while(True):
        nb_table = input("\n\nWhat table do you want to test ?\n")
        filename = 'table'+nb_table+'.txt'
        #filename = 'table1.txt'  
        table_data = f.read_table(filename)
        f.display_table(table_data)
        f.north_west_corner_method(table_data)
        
if __name__ == "__main__":
    main()
