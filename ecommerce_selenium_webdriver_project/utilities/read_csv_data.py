import csv


def get_csv_data(filename):
    """
    Read CSV data from a file

    Parameters:
        filename(file): Name of the CSV file to be opened

    Returns:
        List: A list of row lists from the CSV file
    """
    rows = []
    file = open(filename, newline="")
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        rows.append(row)

    return rows
