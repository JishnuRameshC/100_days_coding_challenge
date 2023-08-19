def username(fname,lname):
    if fname == "" or lname == "":
        print('dont let it blank')
    return f"{fname.title()}  {lname.title()}"

print(username(input('enter first name  :  '),input("enter last name  :  ")))