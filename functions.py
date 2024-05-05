import copy
import random

def read_table(filename):
    table_data = []

    with open(filename, 'r') as file:
        rows, columns = map(int, file.readline().split())

        for _ in range(rows):
            row_data = list(map(int, file.readline().split()))
            table_data.append(row_data)
        
        orders_data = list(map(int, file.readline().split()))
        table_data.append(orders_data)

    return table_data

def display_table(table_data):
    max_rows = min(len(table_data), 101)  # Include the last row (Orders)
    max_columns = min(len(table_data[0]), 101)

    # Display column headers
    print('\n\n          ', end='')  
    for col in range(1, max_columns):
        print(f'C{col:<4}', end='')  # Updated column headers
    print('P')

    # Display table data
    for i in range(max_rows - 1):  # Exclude the last row (Orders)
        print('    ', end='')  
        print(f'P{i + 1:2}', end='')
        for j in range(max_columns):
            print(f'{table_data[i][j]:5}', end='')
        print()

    # Display capacities
    print('Orders:', end='')
    for j in range(max_columns - 1):  # Exclude the last capacity
        print(f'{table_data[-1][j]:5}', end='')
    print()  # Add a new line for formatting


def north_west_corner_method(table_data):
    max_rows = min(len(table_data) - 1, 21)  # Exclude the last row (Orders)
    max_columns = min(len(table_data[0]) - 1, 13)  # Exclude the last column (Orders)

    # Initialize the indices for the northwest corner of the matrix
    row_index = 0
    col_index = 0

    new_matrice = table_data
    
    # Change each value to 0 except the last line and last column
    for i in range(max_rows):
        for j in range(max_columns):
            new_matrice[i][j] = 0
    
    display_table(new_matrice)

    # Iterate until we reach the last row or column
    while row_index < max_rows and col_index < max_columns:
        # Find the minimum between supply and demand
        min_value = min(table_data[row_index][-1], table_data[-1][col_index])

        # Allocate the minimum value to the current cell
        new_matrice[row_index][col_index] = min_value

        # Update supply and demand
        new_matrice[row_index][-1] -= min_value
        new_matrice[-1][col_index] -= min_value

        # Move to the next row or column if supply or demand becomes zero
        if new_matrice[row_index][-1] == 0:
            row_index += 1
        else:
            col_index += 1

        # Display the updated table
        display_table(new_matrice)

    # Return the updated matrix
    return new_matrice

def remove_flagged_items(data):
    data_copy = copy.deepcopy(data)
    for ind in range(len(data)):
        if data[ind] == -1:
            data_copy.remove(-1)
    return data_copy

def row_diff(line):
    if ((len(line)-1)>=1):
        line_copy = copy.deepcopy(line)
        line_copy.pop(len(line)-1) # Remove the "order" info
        line_copy = remove_flagged_items(line_copy)
        line_copy.sort()

        if len(line_copy) == 0:
            return -1
        if len(line_copy) == 1:
            return line_copy[0]
        val1 = line_copy[0]
        val2 = line_copy[1]
        return abs(val1-val2)
    return line[0]

def col_diff(line):
    if ((len(line)-1)>=1):
        line_copy = copy.deepcopy(line)
        line_copy = remove_flagged_items(line_copy)
        line_copy.sort()
        if len(line_copy) == 0:
            return -1
        if len(line_copy) == 1:
            return line_copy[0]        
        val1 = line_copy[0]
        val2 = line_copy[1]
        return abs(val1-val2)
    return line[0]

def create_alloc_table(table_data, max_rows, max_cols):
    alloc_table = [[0 for x in range(max_cols+1)] for y in range(max_rows+1)]

    for ind in range (max_cols):
        alloc_table[max_rows][ind] = table_data[max_rows][ind]

    for ind in range (max_rows):
        alloc_table[ind][max_cols] = table_data[ind][max_cols]

    return alloc_table

def display_alloc_table(alloc_table):
    max_rows = len(alloc_table)
    max_columns = len(alloc_table[0])

    # Display column headers
    print('\n\n          ', end='')  
    for col in range(1, max_columns):
        print(f'C{col:<4}', end='')
    print('Supply')

    # Display table data
    for i in range(max_rows - 1):  # Exclude the last row (Orders)
        print('    ', end='')  
        print(f'P{i + 1:2}', end='')
        for j in range(max_columns):
            print(f'{alloc_table[i][j]:5}', end='')
        print()

    # Display capacities
    print('Orders:', end='')
    for j in range(max_columns - 1):  # Exclude the last capacity
        print(f'{alloc_table[-1][j]:5}', end='')
    print()  # Add a new line for formatting

def get_min_not_flagged(line):
    line_copy = remove_flagged_items(line)
    return min(line_copy)

def get_column_data(table_data, col, max_rows):
    col_data = [0]*(max_rows)
    for ind in range(max_rows):
        col_data[ind]=table_data[ind][col]
    return col_data

def is_column_flagged(col_data):
    for ind in range(len(col_data)):
        if col_data[ind] != -1:
            return False
    return True

def vogel(table_data):

    initial_table_data = copy.deepcopy(table_data)

    max_rows = len(table_data)-1
    max_cols = len(table_data[0])-1

    alloc_table = create_alloc_table(table_data, max_rows, max_cols)

    # Algorithm start
    do_loop = True
    while do_loop:

        row_diffs = [0]*max_rows
        col_diffs = [0]*max_cols

        # Compute row differences and col differences
        for line in range(max_rows):
            row_diffs[line] = row_diff(table_data[line])

        # Compute col differences
        row_ind=0
        for col in range(max_cols):
            
            col_data = get_column_data(table_data, col, max_rows)
            if is_column_flagged(col_data):
                col_diffs[col] = -1
                row_ind +=1
                continue

            col_diffs[col] = col_diff(col_data)
            row_ind +=1

        print ("Row-diffs => ",row_diffs)
        print ("Col-diffs => ",col_diffs)

        # Now identify the max between rows diff and cols diff
        max_rows_diff = max(row_diffs)
        max_cols_diff = max(col_diffs)

        # Stop here if everything has already been processed
        if max_rows_diff == -1 and max_cols_diff == -1:
            # Compute and return the total cost
            total_cost = 0
            for row in range(max_rows):
                for col in range(max_cols):
                    alloc = alloc_table[row][col]
                    if alloc != 0:
                        total_cost += initial_table_data[row][col]*alloc
            print(f'Total cost: {total_cost}')
            return total_cost

        alloc_row = 0
        alloc_col = 0

        # Compute allocation row/col
        if(max_rows_diff > max_cols_diff):
            row_ind = row_diffs.index(max_rows_diff)

            # Get min cost of that row
            min_cost = get_min_not_flagged(table_data[row_ind])

            # Identify col with the min cost
            alloc_row = row_ind
            alloc_col = table_data[row_ind].index(min_cost)
            
            supply = alloc_table[row_ind][max_cols]
            orders = alloc_table[max_rows][alloc_col]

        else:
            col_ind = col_diffs.index(max_cols_diff)

            # Collect this col data
            col_data = get_column_data(table_data, col_ind, max_rows)

            # Get min cost of that col
            min_cost = get_min_not_flagged(col_data)

            # Identify row with the min cost
            alloc_row = col_data.index(min_cost)
            alloc_col = col_ind

            supply = alloc_table[alloc_row][max_cols]
            orders = alloc_table[max_rows][alloc_col]

        # Check supply vs orders
        # Save allocation
        if orders <= supply:
            alloc_table[max_rows][alloc_col] = 0 # Enough supply => is fulfilled
            alloc_table[alloc_row][max_cols] = supply - orders # Spare supply
            alloc_table[alloc_row][alloc_col] = orders # Orders completed

            for ind in range(max_rows):
                table_data[ind][alloc_col] = -1 # flag this entire column as it is now processed

        else:
            alloc_table[max_rows][alloc_col] = orders-supply # Not all orders fulfilled
            alloc_table[alloc_row][max_cols] = 0 # Spare supply
            alloc_table[alloc_row][alloc_col] += supply # Orders completed

            for ind in range(max_cols):
                table_data[alloc_row][ind] = -1 # flag this entire row as it is now processed

        display_alloc_table(alloc_table)

def total_cost(table_data, table_penalties):
    max_rows = len(table_data) - 1
    max_cols = len(table_data[0]) - 1

    total_cost = 0
    for row in range(max_rows):
        for col in range(max_cols):
            allocation = table_data[row][col]
            penalty = table_penalties[row][col]
            if allocation > 0:
                total_cost += allocation * penalty

    print(f'Total cost: {total_cost}')
    return total_cost


""" Part 3 """

def generate_transportation_problem(size):
    random_matrix = [[0 for _ in range(size)] for _ in range(size)] + [[0 for _ in range(size - 1)]]

    for i in range (size):
        for j in range (size):
            value = random.randint(1, 100)
            random_matrix[i][j] = value
    
    for i in range (size-1):
        value = random.randint(1, 100)
        random_matrix[size][i] = value
    return random_matrix