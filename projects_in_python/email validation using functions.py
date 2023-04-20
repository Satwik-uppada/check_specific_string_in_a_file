email = input("Enter the Email address: ")


def validation(email):
    if (" " in email) == False:
            if not email.islower():
                return False
            else:
                if ("@" in email) and (email.count("@") == 1):
                    email_split = email.split("@")
                    if len(email_split) == 2:
                        username, domain = email_split
                        if username.isalnum() == True:
                            if username[0].isalpha() == True:
                                if username[-1].isalnum() == True:
                                    dot_commercial = domain.split(".")
                                    if len(dot_commercial) == 2:
                                        email_service, domain_name = dot_commercial
                                        if len(domain_name) >= 2:
                                            if email_service.isdigit() == False:
                                                if email_service.isalpha() == True:
                                                    return True
                                                else:
                                                    return False
                                            else:
                                                return False
                                        else:
                                            return False
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        elif (("." in username) or ("_" in username) or ("-" in username)):
                            if username[-1].isalnum() and username[0].isalnum() == True:
                                if "." in username:
                                    first_name, last_name = username.split(".", 1)
                                    if first_name[-1].isalnum() and last_name[0].isalnum() == True:
                                        dot_commercial = domain.split(".")
                                        if len(dot_commercial) == 2:
                                            email_service, domain_name = dot_commercial
                                            if len(domain_name) >= 2:
                                                if email_service.isdigit() == False:
                                                    if email_service.isalpha() == True:
                                                        return True
                                                    else:
                                                        return False
                                                else:
                                                    return False
                                            else:
                                                return False
                                        else:
                                            return False
                                    elif (first_name[-1] or last_name[0] == (".") or ("_") or ("-")):
                                        return False
                                    else:
                                        return False
                                elif ("_" in username):
                                    first_name, last_name = username.split("_", 1)
                                    if first_name[-1].isalnum() and last_name[0].isalnum() == True:
                                        dot_commercial = domain.split(".")
                                        if len(dot_commercial) == 2:
                                            email_service, domain_name = dot_commercial
                                            if len(domain_name) >= 2:
                                                if email_service.isdigit() == False:
                                                    if email_service.isalpha() == True:
                                                        return True
                                                    else:
                                                        return False
                                                else:
                                                    return False
                                            else:
                                                return False
                                        else:
                                            return False
                                    elif (first_name[-1] or last_name[0] == (".") or ("_") or ("-")):
                                        return False
                                    else:
                                        return False
                                elif "-" in username:
                                    first_name, last_name = username.split("-", 1)
                                    if first_name[-1].isalnum() and last_name[0].isalnum() == True:
                                        dot_commercial = domain.split(".")
                                        if len(dot_commercial) == 2:
                                            email_service, domain_name = dot_commercial
                                            if len(domain_name) >= 2:
                                                if email_service.isdigit() == False:
                                                    if email_service.isalpha() == True:
                                                        return True
                                                    else:
                                                        return False
                                                else:
                                                    return False
                                            else:
                                                return False
                                        else:
                                            return False
                                    elif (first_name[-1] or last_name[0] == (".") or ("_") or ("-")):
                                        return False
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False

    else:
        return False


print(validation(email))