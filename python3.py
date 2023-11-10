import csv
import socket
from csv import DictReader
from csv import DictWriter

# Input and output file paths (replace with your file paths)
input_file = "C:\\Users\\FejiroCornelius\\Desktop\\gamblingblocklist.csv"
output_file = "C:\\Users\\FejiroCornelius\\Desktop\\gamblingblocklist.csv"

# Function to resolve domain to IP address
def resolve_domain_to_ip(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.error:
        return "Not Found"

# Open the input and output CSV files
with open(input_file, 'r') as csv_input, open(output_file, 'w', newline='') as csv_output:
    # Create CSV reader and writer
    csv_reader = csv.DictReader(csv_input)
    fieldnames = csv_reader.fieldnames   # Add a new column for IP addresses
    # Write the column names in output csv file
    csv_writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
   

    # Process each row in the input CSV
    for row in csv_reader:
        domain = row['DomainName']  # Replace 'Domain' with your column name
        ip_address = resolve_domain_to_ip(domain)
        row['IP Address'] = ip_address
        csv_writer.writerow(row)

print("IP addresses added to the CSV file.")