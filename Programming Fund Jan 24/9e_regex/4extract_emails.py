import re

text = input()

pattern = r'(?:^| )((([a-zA-Z0-9]+)[a-zA-Z0-9-._]*)@([a-zA-Z-]+)\.([a-zA-Z-._]+))\b'
matches = re.finditer(pattern, text)
for match in matches:
    print(match.group())


# import re
#
# sentence = input()
# pattern = r"\s((([a-z0-9]+)[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
# extracted_emails = re.findall(pattern, sentence)
# for extracted_email in extracted_emails:
#     print(extracted_email[0])
