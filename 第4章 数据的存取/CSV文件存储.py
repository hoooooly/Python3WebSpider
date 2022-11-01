import csv

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['1001', 'Bob', '20'])
    writer.writerow(['1002', 'Mike', '18'])
    writer.writerow(['1003', 'Jack', '27'])

    csvfile.close()

