try:
    num1 = int(input('Please enter number 1 '))
    num2 = int(input('Please enter number 2 '))
    result = num1/num2
    print(result)
except TypeError as err:
    print("Please provide only digits : ", err)
#handling multiple Exceptions
except ZeroDivisionError as err1:
    print('Please dont enter zero ', err1)
except ValueError as err:
    print('Please enter valid Input ', err)
except Exception as err:
    print('Handle all types of Exception ', err)
#else block will only execute when there is no Exception
else:
    print('Else block Execution')
#finally block - it will execute whatever the condition comes it will always execute
finally:
    print('Division Happened')


