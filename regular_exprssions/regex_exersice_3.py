import re
### 1. Extract Email Addresses
sample_text="You can reach out to john.doe@example.com or jane.smith123@work-mail.org. Don't contact john.doe@example.com again."

# patter_email = re.compile(r'\b[a-zA-Z0-9]+\.[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}\b|\b[a-zA-Z0-9]+\.[a-zA-Z0-9]+@[a-zA-Z0-9]+-[a-zA-Z0-9]+\.+[a-zA-Z]{3}\b')
patter_email = re.compile(r'\b[a-z0-9.]+@[a-z0-9-]+\.[a-z]+\b')
print(patter_email.findall(sample_text))

### 2. Extract Dates in Multiple Formats
sample_text2="The project 922-129-2341 started on 2023-03-15 and will end by 15/07/2024. Another important date is 12-12-2023."

patter_date = re.compile(r'\b\d{4}-\d{2}-\d{2}\b|\b\d{2}/\d{2}/\d{4}\b|\b\d{2}-\d{2}-\d{4}\b')
print(patter_date.findall(sample_text2))

### 3. : Write a regex pattern to extract all URLs from the text.
sample_text3="Visit name:luminar our website at https://www.example.com for more details. You can also check our blog at http://blog.example.org."

patter_url = re.compile(r'\bhttps?://[a-z]+\.[a-z]+\.[a-z]+\b')
print(patter_url.findall(sample_text3))

### 4. : Write a regex pattern to extract phone numbers in formats like (123) 456-7890, +1-123-456-7890, and 123-456-7890.
sample_text4="For support, call us at (123) 456-7890 or +1-123-456-7890. You can also reach out to 123-456-7890."

patter_phone = re.compile(r'[0-9()]+ \d+-\d+|\+\d+-\d+-\d+-\d+|\d+-\d+-\d+')
print(patter_phone.findall(sample_text4))

### 5. : Write a regex pattern to extract monetary amounts in formats like $1,234.56 and €50.00.
sample_text5="The total cost is $1,234.56, and the discount is €50.00. Your final amount to pay is $1,184.56."
patter_money = re.compile(r'[$€][\d,]+\.[\d]+')
print(patter_money.findall(sample_text5))
