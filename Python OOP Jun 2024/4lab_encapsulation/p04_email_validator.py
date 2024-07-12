class EmailValidator:
    def __init__(self, min_length, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        _name = email.split("@")[0]
        _mail = email.split("@")[1].split(".")[0]
        _domain = email.split(".")[-1]

        valid_name = self.__is_name_valid(_name)
        valid_mail = self.__is_mail_valid(_mail)
        valid_domain = self.__is_domain_valid(_domain)

        return valid_name and valid_mail and valid_domain


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
