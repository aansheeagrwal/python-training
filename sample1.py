print(7**4)

planet = "Earth"
diameter = 12742
print("The diameter of {} is {} kilometers.".format(planet,diameter))

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0])
print(lst[3][1][1])
print(lst)

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

print(d['k1'][3]['tricky'][3]['target'][3])

my_list = [1,2,3]
my_tuple = (1,2,3)

# create a function that grabs the email website domain from a string in the form
#user@domain.com

def domainGet(email):
    return email.split('@')[1]
print(domainGet('user@domain.com'))


# create a basic function that returns true if the word dog is present in the input string. dont worry about edge cases like a punctuation being attached to the word dog,but do account for capitalization.

def findDog(st):
    return 'dog' in st.lower().split()
print(findDog('Is there a dog here?'))

def countDog(st):
    count = 0
    for word in st.lower().split():
        if word == 'dog':
            count += 1
    return count
print(countDog('Dog : this dog run faster'))

# Use lambda expression and the filter() functon to filter out words from a list that don't start with the letter 's'.
seq = ['soup','dog','salad','cat','green']

print(list(filter(lambda word: word[0]=='s',seq)))


# you are driving a little too fast, and a police officer stops you. write a function to return one of three possible results:"No ticket",'Small ticket",or"Big ticket". if you speed is 60 or less the result is "No ticket",if speed is between 61 and 80 exclusive,the result is "Small Ticket". if speed is 81 or more, the result is "Big Ticket",Unless it is your birthday(encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases.

#tuple,list , dictionary, functional programming, one program for lazy execution

