#set the status as False initally
status = False

languages = ['Java', 'Python' ,'C#' ,'Ruby']

for ele in languages:
    #if the language is Found then the condition will be executed
    if ele == 'Ruby':
        status = True
        print('Python found')
        break
    else:
        print('Language still searching')

#if found set the status as True
if status:
    print('Status set to True')
else:
    print('Sorry could not find')


