x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].  
x[1][0] = 15

# How would you change the last_name of the first student from 'Jordan' to "Bryant"?
students[0]['last_name'] = "Bryant"

# For the sports_directory, how would you change 'Messi' to 'Andres'?
sports_directory['soccer'][0] = 'Andres'

# For x, how would you change the value 20 to 30?
z[0]['y'] = 30


# 2. Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value.  For example, given the following list:
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary( students ):
    for s in students:
        print("{} - {} - {} - {}".format(list(s.keys())[0], s.get("first_name"),list(s.keys())[1], s.get("last_name")))
iterateDictionary(students)

# for i in range(len(students)):
    #     z = ""
        # for x,y in  students[i].items():
        #     z += students[i][x]
        #     z += " - "
        #     z += students[i][y]
        # print z

# 3. Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.  For example, iterateDictionary2('first_name', students) should output

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iteratedictionaries2( students, key):
    for i in range(len(students)):
        print(students[i][key])
iteratedictionaries2(students, 'first_name')

#4 Create a function that prints the name of each location and also how many locations the Dojo currently has.  Have the function also print the name of each instructor and how many instructors the Dojo currently has.  For example, printDojoInfo(dojo) should output

dojo = {
   'location': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printDojoInfo(dojo):
    for i in 'location':
        sum = 0
        sum = sum + i
        print (sum)
    return
printDojoInfo(dojo)



def two_lists_dict(diction):
    for key, data in diction.items():
        num = 1
        print key
        for value in data:
            print str(num) + " - " + value["first_name"].upper() + " " + value["last_name"].upper() + " - " + str(len(value["first_name"] + value["last_name"]))
            num = num + 1
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
two_lists_dict(users)