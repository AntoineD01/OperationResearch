import functions as f

def main():
    while(True):
        nb_table = input("\n\nWhat table do you want to test ?\n")
        filename = 'table'+nb_table+'.txt'
        #filename = 'table1.txt'  
        table_data = f.read_table(filename)
        f.display_table(table_data)
        #nw_matrice = f.north_west_corner_method(table_data)
        max_diff_type, max_diff_index, max_diff = f.max_difference(table_data)
        print("Maximum difference type:", max_diff_type)
        print("Maximum difference index:", max_diff_index)
        print("Maximum difference in columns and rows:", max_diff)
        
if __name__ == "__main__":
    main()
