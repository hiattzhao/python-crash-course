filename = 'file_read.txt'

#read the entire file
with open(filename) as file_object:
  contents = file_object.read()
  print(contents)

#read file line by line
with open(filename) as file_object:
  for line in file_object:
    print(line.rstrip())

#make list of lines from file
with open(filename) as file_object:
  lines = file_object.readlines()

for line in lines:
  print(line.rstrip())

#replace
with open(filename) as file_object:
  for line in file_object:
    print(line.replace('Python', 'C').rstrip())

#write to file
write_to_filename = 'file_write.txt'
guest = input('What is your name (press "q" to quit)? ')
with open(write_to_filename, 'w') as file_object:
  file_object.write(guest)

#while loop to write to file
write_to_filename_with_while = 'file_write_while.txt'
with open(write_to_filename_with_while, 'a') as file_object:
  while True:
    name = input('What is your name (press "q" to quit)? ')
    print(name)
    file_object.write(name + '\n')
    repeat = input('Ask another guest ("y/n")? ')
    if repeat == 'n':
      break