months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]

print(months)
months.append("Aug")
print(months)
months.pop()
print(months)
months.insert(0, "Dec")
print(months)

#iteration
for month in months:
    print(f"{month}, 2025")

#name
fullname = 'Dynneal Antonio' 
name = list(fullname)
print(name)

for i in name[0 : 7]:
    print(i)

name.reverse()
print(name)