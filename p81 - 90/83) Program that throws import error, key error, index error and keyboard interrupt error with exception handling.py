import sys

# Import error handling
try:
    from functools import partial

except ImportError as msg1:
    print(msg1)
    print(sys.version)

finally:
    print('End1')


# Key error handling
emp_dict = {'Name': 'Jack', 'ID': 1}
try:
    emp_id = emp_dict['ID']
    print(emp_id)

    emp_role = emp_dict['Role']
    print(emp_role)

except KeyError as key_error_message:
    print('Key Not Found in Employee Dictionary:', key_error_message)

finally:
    print('End2')


# Index error handling
try:
    my_list = [3, 7, 9, 4, 6]
    print(my_list[6])

except IndexError as msg2:
    print(msg2)

finally:
    print('End3')


# Keyboard Interrupt error handling
try:
    x = input()
    print('Try using KeyboardInterrupt')

except KeyboardInterrupt:
    print('Caught KeyboardInterrupt')  # Interrupt the execution

else:
    print('No exceptions are caught')

finally:
    print('End4')
