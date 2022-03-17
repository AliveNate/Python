
print('\n\n')
print(' Below is generally described as a, Try/Except block.')
print(' The title is incorrect here. It will throw an error. --> f = open(,text.txts,)')
print(' We dont want a client to see the python error. Too Complicated.')
print(' We want them so see our error which is simpler')
print('\n\n')


print(' We try to run code, and if it throws an exception, it will display ours instead of pythons.')
print(' The Exception header below, will catch many different specific exceptions. ')
try:
    f = open('Try_Except_ExeptionsXXXX.txt')
except Exception:
    print('\tSorry, this file does not exist. Error!')
# else:
#     pass
# finally:
#     pass



print('\n\n')
print(' The Exception header below, will catch many different specific exceptions. ')
print(' Unlike the ex. above, the txt file here is true, but the bad_var doesnt mean anything.')
print(' Just an example that it will catch different exceptions, regardless. ')
try:
    f = open('Try_Except_Exeptions.txt')
    var = bad_var
except Exception:
    print('\tSorry, this file does not exist. Error!')



print('\n\n')
print(' There are specific exceptions: Ex.  FileNotFoundError ')
try:
    f = open('Try_Except_Exeptions.txts')
#    var = bad_var
except FileNotFoundError:
    print('\tThe file was not found.')
    print(' We are using FileNotFoundError and it catches the file not found.')
    print(' But if the file is there, and there is another error, it will give the complicated python error.')



print('\n\n')
print(' There are specific exceptions: Ex.  FileNotFoundError ')
try:
    f = open('Try_Except_Exeptions.txt')
    var = bad_var
except FileNotFoundError:
    print('\tThe file was not found.')
except Exception:
    print('\t General Exception')
print(' You can add numerous exceptions. Put the more specific at the top.')




print('\n\n')
print(' You can use   e   for a list of exceptions.')
print(' Use   e  as below and it will specify automatically which exception it hit.')
try:
    f = open('Try_Except_ExeptionsXXX.txt')
    var = bad_var
except FileNotFoundError as e:
    print('\t',e)
except Exception as e:
    print('\t',e)



print('\n\n')
print(' The else clause, runs code if the try clause doesnt raise an exception.')
try:
    f = open('Try_Except_Exeptions.txt')
except FileNotFoundError as e:
    print('\t',e)
except Exception as e:
    print('\t',e)
else:
    print(f.read())
    f.close()
# finally:
#     pass




print('\n\n')
print(' The finally clause, runs code regardless if theres an exception.')
try:
    f = open('Try_Except_Exeptions.txt')
except FileNotFoundError as e:
    print('\t',e)
except Exception as e:
    print('\t',e)
else:
    print(f.read())
    f.close()
finally:
    print("\t Executing the finally, finally. Just to be sure the file is closed??")




print('\n\n')
print(' Last. We can raise/create our own specific exception in the try clause.')
try:
    f = open('corrupt_file.txt')
    if f.name == "corrupt_file.txt":
        raise Exception
except FileNotFoundError as e:
    print('\t', e)
except Exception as e:
    print('\t', e)
else:
    print(f.read())
    f.close()
finally:
    print("\t Executing the finally, finally. Use to be sure the file is closed??")
