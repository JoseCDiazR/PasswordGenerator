def generate_pass(limit:int , nick:str):
    password = ""
    while nick not in password:
        for i in range(1,(limit+1)):
            password +=str(i)  
    return password 
