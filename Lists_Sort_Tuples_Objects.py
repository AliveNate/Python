

# ==============================================================
# Create a list
li = [9,1,8,2,7,3,6,4,5]


print('\n\nPrint out the original list.')
print('Original List:\t', li)


# Make new variable
print('\n\nWe need to make a new variable, and use the built in sort function.')
s_li = sorted(li)
print('Sorted List:\t', s_li)


print('\n\nWe can also sort without a new variable using:   li.sort()')
li.sort()
print('The original list after a specific sort:', li)
print('Note: the sort() function returns nothing, it just changes the original.')
print('Cannot use   s_li = li.sort()    because .sort() doesnt return anything.')


# ==============================================================
print('\n\nTo reverse the order of a sorted list.')
s_li = sorted(li, reverse = True)
print(s_li)


print('\nTo reverse the order of a sorted list, but inside the function')
li = [9,1,8,2,7,3,6,4,5]
print('Original list:\t', li)


li.sort(reverse=True)
print('Sorted list, with internal reverse.\t', li)


# ==============================================================
print('\n\n NOTE: the   .sort() only works with lists. ')
print('So   tup.sort()  is a NO. .sort() does not work on tuples.')
print('We must use the sort function instead.')


tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup)
print('Sorted Tuple\t', s_tup)
# ==============================================================


print('\n\nCan use the sort function for a dictionary also.')
di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print('Dict\t', s_di)
print('A sorted dictionary is auto sorted by the keys.')



# ==============================================================
li_N = [-6, 23, -5, 9, -4, 1, 2, 3]
print('\n\nThe original list:\t', li_N)
s_li_N = sorted(li_N)
print('The Sorted list: \t', s_li_N)


# Sort based on the absolute values
s_li_NAbs = sorted(li_N, key=abs)
print('List sorted by absolute values:\t', s_li_NAbs)
# ==============================================================


''' These class objects have different traits. We can sort based on each trait, but we need to create
seperate functions for that. We create 3 employees, then define 3 functions, technically all the exact same function:
def e_sort(emp):
    return emp.name
    That all you have to do is change the return piece to match the trait.
     Then:  s_employees = sorted(employees, key = e_sort)
you can see that the sort method used is a built in function but the sorts by the specific trait
that is returned from each employee that we have defined in our function. '''
# ==============================================================

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)



e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

print('\n\nPrint the employee list')
employees = [e2, e1, e3]
print(employees)


# ================
# ================
print('\n\nNow sort the list base on a certain attribute.')
print('Cannot just sort a object list, because it doesnt know what to sort based on.')
#   Won't work. Not sorting on anything
#   s_employees = sorted(employees)
print('We need a custom function to sort a object list.')
# define the function name, which returns the object name.
def e_sort(emp):
    return emp.name
# Tells that we are sorting the list of objects based on the return value(key)
# which we defined as the name
s_employees = sorted(employees, key = e_sort)
print(s_employees)
# ================


# -----------------------------------------------------
print('\nWe just sorted based on name, all we have to do is change that function to age, not name')
def e_sort(emp):
    return emp.age
s_employees = sorted(employees, key = e_sort)
print(s_employees)


# -----------------------------------------------------
print('\nWe just sorted based on age, all we have to do is change that function to salary, not age')
def e_sort(emp):
    return emp.salary
s_employees = sorted(employees, key = e_sort)
print(s_employees)


# -----------------------------------------------------
print('\nWe sorted on salary. Add reverse = True to the sorted method')
def e_sort(emp):
    return emp.salary
s_employees = sorted(employees, key = e_sort, reverse = True)
print(s_employees)
print('Remember this just sorted based on salary 70000, 80000, 90000, then reverse it.')
# -----------------------------------------------------


# ==============================================================

# ==============================================================


# ==============================================================

# ==============================================================


# ==============================================================

# ==============================================================


# ==============================================================