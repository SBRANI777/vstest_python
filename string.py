str1="Virat@kohli.banglore"
f_name=str1[:str1.find("@")]
s_name=str1[str1.find("@")+1:str1.find(".")]
t_name=str1[str1.find(".")+1:]
print(f_name)
print(s_name)
print(t_name)


