print("the first question")
x = [ [5,2,3], [10,8,9] ] 
studentss = [
{'first_name':  'Michael', 'last_name' : 'Jordan'},
{'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1]=[15,8,9]
print(x) 

studentss[0]['last_name']='Bryant'
print(studentss)

sports_directory['soccer']=['Andres', 'Ronaldo', 'Rooney']
print(sports_directory)

z[0]['y']=30
print(z)

print("the second question")
students = [
{'first_name':  'Michael', 'last_name' : 'Jordan'},
{'first_name' : 'John', 'last_name' : 'Rosales'},
{'first_name' : 'Mark', 'last_name' : 'Guillen'},
{'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(students):
    for student in students:
        output = f"first_name - {student['first_name']}, last_name - {student['last_name']}"
        print(output)
iterateDictionary(students)


print("second method")
def iterateDictionaryy(students):
    for student in students:
        output = []
        for key, value in student.items():
            output.append(f"{key} - {value}")
        print(", ".join(output))
iterateDictionaryy(students)


print("third question")
def iterateDictionary2(key, list):
  for student in list:
    print (student[key])

iterateDictionary2('last_name',students)


print("fourth question")
dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
  nblocation=len(dojo['locations'])
  nbinstrctors=len(dojo['instructors'])
  print(f"{nblocation}  location")
  for val in dojo['locations']:
    print(val)
  print(f"{nbinstrctors}  instructors")
  for val in dojo['instructors']:
    print(val)

printInfo(dojo)