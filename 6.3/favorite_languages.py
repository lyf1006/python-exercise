favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
person_rolled = ['jen', 'jhon', 'edward', 'lucy', 'jack']

for per in person_rolled:
    if per in favorite_languages.keys():
        print(per+",thank you for taking our roll.")
    else:
        print(per+" ,please take our roll!")