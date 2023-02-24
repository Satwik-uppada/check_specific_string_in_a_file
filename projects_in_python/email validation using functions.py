email=input("enter the email:")
def validation(email):
    if ("@" in email):
        domain_split=email.split("@")
        domain_part_validation(domain_split)
        domain_validation()


    else:
        return False

def domain_part_validation(domain_split):
     if len(domain_split)==2:
         username,domain=domain_split
         return domain,username
     else:
        return False

def domain_validation(domain):
    dot_commercial=domain.split(".")
    if len(dot_commercial)==2:
        email_service,domain_name=dot_commercial
    else:
        return False

