import csv
import classes

# Function to read CSV file and yield rows
def read_csv(file_name):
    with open(file_name, "r") as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        header = next(reader)
        for row in reader:
            yield row

def write_objects_to_csv(file_name, header_list, objects):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(header_list)
        for obj in objects:
            writer.writerow(obj.get_attributes())

# Lists to store data
customer_codes = []
invoices = []
invoiceItems = []
customers = []

# Counters for creating unique object names
custCount = 0
invCount = 0
invItemCount = 0

# Read customer codes from CUSTOMER_SAMPLE.CSV
with open("CUSTOMER_SAMPLE.CSV", 'r') as customer_sample:
    csvreader = csv.reader(customer_sample, delimiter=',', quotechar='"')
    header = next(csvreader)
    for row in csvreader:
        customer_codes.append(str(row[0]))

# Create Customer objects from CUSTOMER.CSV
for row in read_csv("CUSTOMER.CSV"):
    if row[0] in customer_codes:
        customerObject = classes.Customer(row[0], row[1], row[2])
        customers.append(customerObject)
        custCount += 1

# Create Invoice objects from INVOICE.CSV
for row in read_csv("INVOICE.CSV"):
    if row[0] in customer_codes:
        invoiceObject = classes.Invoice(row[0], row[1], row[2], row[3])
        invoices.append(invoiceObject)
        invCount += 1

# Create InvoiceItem objects from INVOICE_ITEM.CSV
for row in read_csv("INVOICE_ITEM.CSV"):
    for invoice in invoices:
        if row[0] == invoice.invoice_code:
            invoiceItemObject = classes.InvoiceItem(row[0], row[1], row[2], row[3])
            invoiceItems.append(invoiceItemObject)
            invItemCount += 1

# Write Customer objects to NEW_CUSTOMER.csv
write_objects_to_csv('NEW_CUSTOMER.csv', classes.Customer.get_headerList(), customers)

# Write Invoice objects to NEW_INVOICE.csv
write_objects_to_csv('NEW_INVOICE.csv', classes.Invoice.get_headerList(), invoices)

# Write InvoiceItem objects to NEW_INVOICE_ITEM.csv
write_objects_to_csv('NEW_INVOICE_ITEM.csv', classes.InvoiceItem.get_headerList(), invoiceItems)