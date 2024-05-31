class NameTooShortError(Exception):
    """Less than or equal to 4 length of name"""
    pass


class MustContainAtSymbolError(Exception):
    """No @ in the email"""
    pass


class InvalidDomainError(Exception):
    """Valid domains are .com, .bg, .net, .org"""
    pass


while True:
    email = input()
    if email == 'End':
        break
    name = email.split('@')[0]
    domain = email.split('.')[1]

    if len(name) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')

    # if email.count("@") != 1:
    #         raise MustContainAtSymbolError("Email must contain @")
    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')

    if domain not in ['com', 'bg', 'org', 'net']:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print('Email is valid')
