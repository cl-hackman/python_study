
def user_profile_4_Ben(**x):  # python will store the multiple keyword arguments as a Dictionary 
    return (x["address"])


print(user_profile_4_Ben(yup="giveme5dollars", age=32, address="675 coster street apt 5 bronx NY", sex="M", school="Baruch College"))
# ["yup"] gives the value of a specific keyword argument in the dictionary (works like variables that you can access later)

