# Introduction 
Bulk add A records to AWS Route 53 DNS
---
# Requirements
* Python installed either using Python, PyCharm or VSCode or some other method of executing Python code
* An AWS acount
* API key and secret key from your Amazon AWS account. 
* CSV file saved in notepad do not use Excel as it will fail to import correctly
* route53 library `pip install route53`

* Zone ID of the domain you want to add records to. If you are unsure run the Get-Zone-ID.py first
---
# CSV File
|fqdn       | ip           
| ------------- |:-------------:|
| foo.bar.com.  | 127.0.0.1 
| foo2.bar.com. | 127.0.0.2    
| foo3.bar.com. | 127.0.0.3     

**Ensure the domains have a trailing period after them**

---

# Variables For Get-Zone-ID.py
The main variables are the following in both scripts

> "aws_access_key_id= ' '" - This is your AWS API key

> aws_secret_access_key='' - This is your secret key

The domain name (Zone) and the Zone ID will be shown

# Variables For Route53-A-Record.py
> "aws_access_key_id= ' '" - This is your AWS API key

> aws_secret_access_key='' - This is your secret key

> files = 'filename.csv' - Enter your CSV file name

>filepath = os.path.join('C:\\myfolder\\' - Location where to find the CSV file
