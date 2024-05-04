import sys

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
    max_rows = min(len(table_data), 21)  # Include the last row (Orders)
    max_columns = min(len(table_data[0]), 13)

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

def max_column(table_data):
    max_columns = min(len(table_data[0]) - 1, 13)  # Exclude the last column (Provision)
    max_colum = []
    for i in range(max_columns):
        max_value = float('-inf')  
        for row in table_data[:-1]:
            if row[i] > max_value:
                max_value = row[i]
        max_colum.append(max_value)
    return max_colum

def mx_row(table_data):
    max_rows = min(len(table_data) - 1, 21)  # Exclude the last row (Orders)
    max_row = []
    for i in range(max_rows):
        max_value = float('-inf')  
        for column in table_data[i][:-1]:
            if column > max_value:
                max_value = column
        max_row.append(max_value)
    return max_row

def mini_col(table_data):
    max_columns = min(len(table_data[0]) - 1, 13)  # Exclude the last column (Provision)
    min_colum = []
    for i in range(max_columns):
        min_value = float('inf')  
        for row in table_data[:-1]:
            if row[i] < min_value:
                min_value = row[i]
        min_colum.append(min_value)
    return min_colum

def mini_row(table_data):
    max_rows = min(len(table_data) - 1, 21)  # Exclude the last row (Orders)
    min_row = []
    for i in range(max_rows):
        min_value = float('inf')  
        for column in table_data[i][:-1]:
            if column < min_value:
                min_value = column
        min_row.append(min_value)
    return min_row

def max_difference(table_data): #return the position of the maximum difference of penalty 
    max_rows = min(len(table_data) - 1, 21)  # Exclude the last row (Orders)
    max_columns = min(len(table_data[0]) - 1, 13)  # Exclude the last column (Provision)
    difference_colum = []
    difference_row = []
    
    
    max_colum = max_column(table_data)
    max_row = mx_row(table_data)
    min_colum = mini_col(table_data)
    min_row = mini_row(table_data)

    # Calculate the differences between the maximum and minimum values in each column
    difference_colum = [max_colum[i] - min_colum[i] for i in range(max_columns)]
    
    # Calculate the differences between the maximum and minimum values in each row
    difference_row = [max_row[i] - min_row[i] for i in range(max_rows)]

    # Find the maximum value from both the difference columns and difference rows
    max_diff_col = max(difference_colum)
    max_diff_row = max(difference_row)
    max_diff = max(max_diff_col, max_diff_row)

    # Determine if the maximum difference is from a column or a row
    if max_diff_col > max_diff_row:
        max_diff_type = 'column'
        max_diff_index = difference_colum.index(max_diff_col)
    else:
        max_diff_type = 'row'
        max_diff_index = difference_row.index(max_diff_row)
    
    return max_diff_type, max_diff_index, max_diff

def find_cell(max_diff_type, max_diff_index, new_matrice):
    if max_diff_type == 'row':
        # Find the cell with the minimum value in the chosen row
        min_value = min(new_matrice[max_diff_index][:-1])
        min_index = new_matrice[max_diff_index][:-1].index(min_value)

        # If there are multiple cells with the same minimum value,
        # choose the one that has not been previously allocated
        for i in range(min_index + 1, len(new_matrice[max_diff_index][:-1])):
            if new_matrice[max_diff_index][i] == min_value and new_matrice[max_diff_index][i] == 0:
                min_index = i
                break
        for i in range(min_index - 1, -1, -1):
            if new_matrice[max_diff_index][i] == min_value and new_matrice[max_diff_index][i] == 0:
                min_index = i
                break

        return max_diff_index, min_index
    else:
        # Find the cell with the minimum value in the chosen column
        min_value = min(row[max_diff_index] for row in new_matrice[:-1])
        for i, row in enumerate(new_matrice[:-1]):
            if row[max_diff_index] == min_value:
                # If there are multiple cells with the same minimum value,
                # choose the one that has not been previously allocated
                for j in range(i + 1, len(new_matrice[:-1])):
                    if new_matrice[j][max_diff_index] == min_value and new_matrice[j][max_diff_index] == 0:
                        i = j
                        break
                for j in range(i - 1, -1, -1):
                    if new_matrice[j][max_diff_index] == min_value and new_matrice[j][max_diff_index] == 0:
                        i = j
                        break
                return i, max_diff_index

            
def balas_hammer_method(table_data):
    max_rows = min(len(table_data) - 1, 21)  # Exclude the last row (Orders)
    max_columns = min(len(table_data[0]) - 1, 13)  # Exclude the last column (Provision)

    # Initialize the indices for the northwest corner of the matrix
    row_index = 0
    col_index = 0

    new_matrice = table_data

    # Change each value to 0 except the last line and last column
    for i in range(max_rows):
        for j in range(max_columns):
            new_matrice[i][j] = 0

    # Iterate until we reach the last row or column
    while row_index < max_rows and col_index < max_columns:
        # Find the row or column with the maximum penalty
        max_diff_type, max_diff_index, max_diff = max_difference(new_matrice)

        # Find the cell with the minimum value in the chosen row or column
        row_index, col_index = find_cell(max_diff_type, max_diff_index, new_matrice)

        # Allocate the maximum possible value to the current cell
        min_value = min(new_matrice[row_index][-1], new_matrice[-1][col_index])
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


def get_potentials(table_data):
    max_rows = len(table_data) - 1
    max_columns = len(table_data[0]) - 1

    row_potentials = [0] * max_rows
    col_potentials = [0] * max_columns

    for i in range(max_rows):
        allocated_cells = [j for j in range(max_columns) if table_data[i][j] > 0]
        if len(allocated_cells) > 0:
            row_potentials[i] = min(table_data[i][j] - col_potentials[j] for j in allocated_cells)

    for j in range(max_columns):
        allocated_cells = [i for i in range(max_rows) if table_data[i][j] > 0]
        if len(allocated_cells) > 0:
            col_potentials[j] = min(table_data[i][j] - row_potentials[i] for i in allocated_cells)

    return row_potentials, col_potentials

def is_optimal(table_data, row_potentials, col_potentials):
    max_rows = len(table_data) - 1
    max_columns = len(table_data[0]) - 1

    for i in range(max_rows):
        for j in range(max_columns):
            if table_data[i][j] - row_potentials[i] - col_potentials[j] > 0:
                return False

    return True

def get_next_edge(table_data, row_potentials, col_potentials):
    max_rows = len(table_data) - 1
    max_columns = len(table_data[0]) - 1

    min_penalty = sys.maxsize
    selected_row = -1
    selected_col = -1

    for i in range(max_rows):
        for j in range(max_columns):
            if table_data[i][j] > 0:
                penalty = table_data[i][j] - row_potentials[i] - col_potentials[j]
                if penalty < min_penalty:
                    min_penalty = penalty
                    selected_row = i
                    selected_col = j

    return selected_row, selected_col

def update_transport_graph(table_data, row_index, col_index):
    max_rows = len(table_data) - 1
    max_columns = len(table_data[0]) - 1

    # Find the cycle or unconnected part of the transport graph
    visited = [[False] * max_columns for _ in range(max_rows)]
    stack = [(row_index, col_index)]
    while stack:
        i, j = stack.pop()
        if not visited[i][j]:
            visited[i][j] = True
            for k in range(max_columns):
                if table_data[i][k] > 0 and not visited[i][k]:
                    stack.append((i, k))
            for k in range(max_rows):
                if table_data[k][j] > 0 and not visited[k][j]:
                    stack.append((k, j))

    # Modify the transport graph
    for i in range(max_rows):
        for j in range(max_columns):
            if visited[i][j] and table_data[i][j] > 0:
                table_data[i][j] -= 1
                table_data[i][-1] -= 1
                table_data[-1][j] -= 1
            elif not visited[i][j] and table_data[i][j] < table_data[row_index][col_index]:
                table_data[i][j] += 1
                table_data[i][-1] += 1
                table_data[-1][j] += 1

def stepping_stone_method(table_data):
    row_potentials, col_potentials = get_potentials(table_data)

    while not is_optimal(table_data, row_potentials, col_potentials):
        row_index, col_index = get_next_edge(table_data, row_potentials, col_potentials)

        # Display the transport proposal and the total transport cost
        print("Transport proposal:")
        display_table(table_data)
        print(f"Total transport cost: {get_total_cost(table_data)}")

        # Update the transport graph
        update_transport_graph(table_data, row_index, col_index)

        # Recalculate potentials
        row_potentials, col_potentials = get_potentials(table_data)

    # Display the minimal transportation proposal and its cost
    print("Minimal transportation proposal:")
    display_table(table_data)
    print(f"Minimal cost: {get_total_cost(table_data)}")

def get_total_cost(table_data):
    max_rows = len(table_data) - 1
    max_columns = len(table_data[0]) - 1
    total_cost = 0

    for i in range(max_rows):
        for j in range(max_columns):
            total_cost += table_data[i][j] * table_data[i][-1] * table_data[-1][j]

    return total_cos