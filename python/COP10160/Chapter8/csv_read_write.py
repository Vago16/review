import csv
#to go with a csv file
with open('MOCK_DATA.csv', 'r') as f:
    mock_data_reader = csv.reader(f)

    line_count = 1

    for row in mock_data_reader:

        if line_count > 1: # skipping line 1 which is the header row
            print(row)

        line_count += 1
         
'''
writing
with open('example.csv', 'w', newline='') as f:
    example_data_writer = csv.writer(f)

    example_data_writer.writerow(['name', 'age'])
    example_data_writer.writerow(['Steven', 25])
    '''

'''writing a dict
with open('people.csv', 'w') as f:
    fields = ['name', 'age']
    people_writer = csv.DictWriter(f, fieldnames=fields)

    people_writer.writeheader() # writes the fields as the first row
    people_writer.writerow({'name': 'Santa Claus', 'age': 1000})
'''
