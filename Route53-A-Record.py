# This script adds A records to a domain of your choice hosted on Amazon Route 53
import csv
import route53
import os

files = ['arecordimport.csv']

# Connect to AWS
conn = route53.connect(
    aws_access_key_id='YOUR_KEY_HERE',
    aws_secret_access_key='YOUR_SECRET_KEY_HERE',
)

zone = conn.get_hosted_zone_by_id('ZONE_ID_HERE')

for filename in files:
    filepath = os.path.join('C:\\PATH_TO_CSV_HERE', filename)
    print(filepath)
    with open(filepath) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['fqdn']
            value = row['ip']
            print('Adding url: ' + name)
            print('Binding to: ' + value)


            change_info = zone.create_a_record(
                # Must be FQDN
                name=name,
                # A list of IP address entries, in the case fo an A record.
                values=[value],
            )

print ('Everything has completed successfully!')




