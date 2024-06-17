import csv

# reading the csv filr
with open('portfolio.csv') as pfile:
    csv_reader=csv.reader(pfile,delimiter=",")
    linecount=0
    for row in csv_reader:
        if linecount==0:
            print(f'Column names are {",".join(row)}')  # join the headings of csv file
            linecount+=1
        else:
            print(f'\t{row[0]} has {row[1]} no of shares at price {row[2]}') #selecting values from each row for corresponding colunm==mn
            linecount+=1
    print(f'Read {linecount} shares from the portfolio')

# writing or insering a new value create a new file becausswe we have not given the coumn name etc so it  wil be added as a new file only

with open('portfolio1.csv',mode='w') as pfile:
    pfile_writer=csv.writer(pfile,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
    pfile_writer.writerow(['Infosys',10,3430])
    pfile_writer.writerow(['UST', 15, 2430])