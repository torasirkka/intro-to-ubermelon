log_file = open("um-server-01.txt")

def clean_line(line: str):
    """Cleans the line."""
    line = line.rstrip()
    
    return line

def to_list(line: str):
    """Converts the line to a list of strings."""
    return line.split(' ')

def find_idx(lst, trigger:str) -> str:
    """Creates and returns a str formed by joining all list elements located before the list item 'trigger'."""
    
    idx = 0
    for word in lst:
        if word == trigger:
            break
        else:
            idx += 1

    return idx

def sales_message(count, melon_name, customer):
    """Prints the sale information."""

    return f'Delivered {count} {melon_name}s to customer {customer}.'

def sales_reports(log_file, daynumber):
    """Creates a sales report file based on the file and day number."""

    print(f'Sales report, day {daynumber}')
    for line in log_file:
        line = clean_line(line)
        line_list = to_list(line)

        day, count, customer = line_list[0], line_list[2], line_list[-1]
        start_idx = 3
        stop_idx = find_idx(line_list, 'delivered')
        melon_name = ' '.join(line_list[start_idx:stop_idx])
        #print(start_idx, stop_idx, melon_name)
        
        if day == "Mon":
            print(sales_message(count, melon_name, customer))


sales_reports(log_file, 1)
