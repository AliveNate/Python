
print(' Data is stored in c++ in what is a map. A dictionary in python is a map.')
print(' If you make a post on facebook it deeply looks like this:')
print('\t Facebook Post')
print('\t user_id = 209')
print('\t message = D5 E5 C5 C4 G4')
print('\t language = English')
print('\t datetime = 20230215T124231Z')
print('\t location = (44.590533, -104.715556)')


print('\n To store this in a map/Dictionary format: NEED BRACKETS ')
post = {"user_id": 209, "message": "D5 E5 C5 C4 G4", "language": 'English',
        "datetime": "20230215T124231Z", "location": "(44.590533, -104.715556)"}
print(' We have just created a dictionary call post.')
print(' The types inside are keys, and the corresponding pieces are values.')

print('\n Find the type (should be a dict)')
print('\t', type(post))


print('\n Create a new dict, partial from the first.')
print(' When you add new data you use flat brackets for key. Then assign value outside.')
post2 = dict(message = "SS Cotopaxi", language = "English")
print(post2)
print(' Add an element to the dict, both key/value')
post2["user_id"] = 209
post2["datetime"] = '234543621T124231Z'
print(post2)



print('\n\n Access the data in the dictionary.')
print(' To see a specific key in the dictionary:', '\t', post["message"])


print('\n\n Check if a key is actually in the dictionary:')
if 'location' in post2:
    print(post2['location'])
else:
    print('\t The key does not exist in this dictionary.')


print('------------------------\n Built in key checker is the   try:   function.')
try:
    print(post2['location'])
except KeyError:
    print('The post does not have a location.')




print('\n\n Another way to access data in a dictionary.')
dir(post2)
help(post2.get)
print(' The get function will either return the key value or return None')
loc_var = post2.get('location', None)
print('\t', loc_var)



print('\n\n A simple way to print all keys and values. Built in.')
for key in post.keys():
    value = post[key]
    print(key, '=', value)


print('\n\n pop is to pull the first item out. First out was last in.')
value = post.popitem()
print(value)

print('\n\n The dict before clear \n', post)
post.clear()
print(' The dict after clear. \n', post)



