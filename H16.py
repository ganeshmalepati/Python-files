# import os
# print(os.listdir())

name=input("Enter your name: ")
date=input("Enter your date: ")
template='''
Dear <name>,
Your are selected
<date>
'''
print(template.replace('<name>', name).replace('<date>', date))