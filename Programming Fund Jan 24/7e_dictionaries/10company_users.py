user_data = input()
companies = {}

while user_data != 'End':
    company_name, username = user_data.split(' -> ')

    if company_name not in companies:
        companies[company_name] = [username]
    elif company_name in companies and username not in companies[company_name]:
        companies[company_name].append(username)

    user_data = input()

for company, employees in companies.items():
    print(company)
    print('--', '\n-- '.join(employees))
