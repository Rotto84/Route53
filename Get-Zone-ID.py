# This script lists the domains and corrisponding zone IDs
import route53

#Login To AWS
conn = route53.connect(
    aws_access_key_id='YOUR ACCESS KEY HERE',
    aws_secret_access_key='YOUR SECRET KEY HERE',
)

for zone in conn.list_hosted_zones():
    print('Domain Name:' + " " + zone.name)
    print('Zone ID:' + " " + zone.id)
    print ('\n')

