givn_strng = 'green-red-yellow-black-white'

print('The string before modification = ', givn_strng)

wordsLis = givn_strng.split('-')
wordsLis.sort()
resultwords = '-'.join(wordsLis)

print('The string after modification = ', resultwords)