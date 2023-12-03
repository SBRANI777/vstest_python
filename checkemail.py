#checking emails of faculty or studentsemais
emails=[]
s_email="@stdent.com"
f_email="@faculty.com"
n=int(input("enter the number of emails"))
for i in range(n):
    name=input("enter the email name")
    if name.endswith("@student.com"):
        emails.append(name)
print(emails)
if len(emails)==n:
    print("all the emials are of students")
else:
    print("there are faculty mails also exist")

