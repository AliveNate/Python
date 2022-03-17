print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')

print('\n We have to specify why we are opening this file. Read, write, appending, or both R/W')
print(' You include a comma, then:  r   or   w   or   a   or   r+    in quotes. ')
#   Just to read the file
f = open('file_ReadFrom.txt', 'r')
print('\n We just opened the file, and are printing the name of the file. ')
print('\t', f.name)
print('\n We can print the mode that we just opened the file for = ')
print(f.mode)
print('\n Note: You always have to close a file.')
f.close()

'''
We have to specify why we are opening this file. Read, write, appending, or both R/W
 You include a comma, then:  r   or   w   or   a   or   r+    in quotes. 

 We just opened the file, and are printing the name of the file. 
	 file_ReadFrom.txt

 We can print the mode that we just opened the file for = 
r

 Note: You always have to close a file.
'''

print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')

print(' The open that we did above, is simple but can lead to problems. Another way below.')
print(' This with way, will auto close after we are done to prevent leaks. ')
print(' Open the file to read, set full contents to variable. Print variable')
with open('file_ReadFrom.txt', 'r') as f:
    f_contents = f.read()
    print('\n f_contents = \n', f_contents)

print(' Note: This is fine for a small file, but is not good for a large one.')

'''
 The open that we did above, is simple but can lead to problems. Another way below.
 This with way, will auto close after we are done to prevent leaks. 
 Open the file to read, set full contents to variable. Print variable

 f_contents = 
 1) This is a test file!
2) With multiple lines of data…
3) Third line
4) Fourth line
5) Fifth line
6) Sixth line
7) Seventh line
8) Eighth line
9) Nineth line
10) Tenth line
 Note: This is fine for a small file, but is not good for a large one.
'''

print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')

print(' We can read line by line. It looks strange ')
print(' Reads each line, and places each as a new element in list.')
with open('file_ReadFrom.txt', 'r') as f:
    f_contents = f.readlines()
    print(f_contents)

'''
 We can read line by line. It looks strange 
 Reads each line, and places each as a new element in list.
['1) This is a test file!\n', '2) With multiple lines of data…\n', '3) Third line\n', '4) Fourth line\n', '5) Fifth line\n', '6) Sixth line\n', '7) Seventh line\n', '8) Eighth line\n', '9) Nineth line\n', '10) Tenth line']

'''


print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')

print(' We can read individual line.    ')
print(' Reads each line, and places each as a new element in list.')
with open('file_ReadFrom.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents)

    f_contents = f.readline()
    print(f_contents)
print(' This auto includes a line. To prevent, use end=''')

with open('file_ReadFrom.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents, end='')

    f_contents = f.readline()
    print(f_contents, end='')

'''
 We can read individual line.    
 Reads each line, and places each as a new element in list.
1) This is a test file!

2) With multiple lines of data…

 This auto includes a line. To prevent, use end=
1) This is a test file!
2) With multiple lines of data…

'''

print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')

print(' This is efficient. Read a line, print it out. Repeat.')
with open('file_ReadFrom.txt', 'r') as f:
    for line in f:
        print(line, end='')

'''
 This is efficient. Read a line, print it out. Repeat.
1) This is a test file!
2) With multiple lines of data…
3) Third line
4) Fourth line
5) Fifth line
6) Sixth line
7) Seventh line
8) Eighth line
9) Nineth line
10) Tenth line
'''

print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')

print(' This read the first 100 characters in and prints them out. ')
with open('file_ReadFrom.txt', 'r') as f:
    f_contents = f.read(100)
    print(f_contents, end='')

'''
 This read the first 100 characters in and prints them out. 
1) This is a test file!
2) With multiple lines of data…
3) Third line
4) Fourth line
5) Fifth line
6

'''


print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')

print('This will be an iterative loop. Grab the first 100 chars. Include a while loop.')
print(' The while loop checks if the contents is greater than 0, if so it prints. Gets the next')
print(' Because we get the next in the loop, it will stop if the next is not > 0')
print(' This will go until the end of the file.')

with open('file_ReadFrom.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)

'''
1) This is a test file!
2) With multiple lines of data…
3) Third line
4) Fourth line
5) Fifth line
6) Sixth line
7) Seventh line
8) Eighth line
9) Nineth line
10) Tenth line
'''


print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')

print(' This is the same as above, but you can see that our read of 10 chars is noted.')
print(' After we get through 10 chars, it prints a *')
with open('file_ReadFrom.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)

'''
 This is the same as above, but you can see that our read of 10 chars is noted.
 After we get through 10 chars, it prints a *
1) This is* a test fi*le!
2) Wit*h multiple* lines of *data…
3) T*hird line
*4) Fourth *line
5) Fi*fth line
6*) Sixth li*ne
7) Seve*nth line
8*) Eighth l*ine
9) Nin*eth line
1*0) Tenth l*ine*
'''


print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('     Step 1 -> read 10 char')
with open('file_ReadFrom.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

print('\n=====')
print('     Step 2 -> read 10 char twice i.e. 20')
with open('file_ReadFrom.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f_contents = f.read(size_to_read)
    print(f_contents, end='')

print('\n=====')
print('     Step 3 -> read 10 char twice i.e. 20')
with open('file_ReadFrom.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents)
    print('\t This shows that we can read 10 chars twice, but read from anywhere.')
    print('\t Here we used f.seek(0) in between to start from the beginning AGAIN.')

'''
=====================================================
     Step 1 -> read 10 char
1) This is
=====
     Step 2 -> read 10 char twice i.e. 20
1) This is a test fi
=====
     Step 3 -> read 10 char twice i.e. 20
1) This is1) This is
	 This shows that we can read 10 chars twice, but read from anywhere.
	 Here we used f.seek(0) in between to start from the beginning AGAIN.
'''
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')
print('\n\n=====================================================')

print('\n\nConfirm the file is close? = \t', f.closed)
'''
Confirm the file is close? = 	 True
'''