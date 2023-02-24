print("Checking Email is valid or not")

""" In the address example@mail.com, "example" is the email prefix, 
and "mail.com" is the email domain."""

# Acceptable email prefix formats
""" Allowed characters: letters (a-z), numbers, underscores, periods, and dashes.
An underscore, period, or dash must be followed by one or more letter or number. """

# Acceptable email domain formats
""" Allowed characters: letters, numbers, dashes.
The last portion of the domain must be at least two characters, for example: .com, .org, .cc"""

email = input("Enter the email address to check : ")


def validation(email):
  if (" " in email)== False:
     if ("@" in email) and (email.count("@")==1):
         domain_split = email.split("@")

         if len(domain_split) == 2:
             username, domain = domain_split
         else:
            return False


            dot_commercial=domain.split(".")

            if len(dot_commercial) == 2:
                  email_service, domain_name = dot_commercial

                  if len(domain_name) >= 2:
                    if email_service.isdigit() == False:
                      if username.isalpha():


                    elif (("." in username) or ("_" in username) or ("-" in username)):
                        if username[0].isalpha() == True:
                            if username[-1].isalnum() == True:
                                if "." in username:
                                    first_name, last_name = username.split(".")
                                    if first_name[-1].isalnum() == True:
                                        return True
                                    elif first_name[-1]==(".") or("_") or("_"):
                                        return False
                                    else:
                                        return False
                                elif "-" in username:
                                    first_name, last_name = username.split("-")
                                    if first_name[-1].isalnum() == True:
                                        return False
                                    elif first_name[-1]==(".") or("_") or("_"):
                                        return False
                                    else:
                                        return False
                                elif "_" in username:
                                    first_name, last_name = username.split("_")
                                    if first_name[-1].isalnum() == True:
                                        return False
                                    elif first_name[-1]==(".") or("_") or("_"):
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
     else:
        return False
  else:
     return False

print(validation(email))