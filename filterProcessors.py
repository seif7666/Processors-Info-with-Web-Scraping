from processors import Processor

# name = input("Enter name of Processor : ")
contents = None
with open('processors.txt', 'r') as file:
    contents = file.read()
    contents=contents.split('__'*100+'\n')

processors = []
for content in contents : 
    content = content.split('\n')
    name = " "
    name = name.join(content[0].split()[2:])
    # print('name is ',name)

    price = ' '
    price = price.join(content[1].split(' ')[3:])
    break