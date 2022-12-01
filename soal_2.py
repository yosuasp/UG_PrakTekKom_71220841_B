def funPalindrome(lmao):
    ispalindrome = 'Yes' if lmao == lmao[::-1] else 'No'
    return f'{ispalindrome}\nJika Dibalik: {lmao[::-1]}'

kata = input('Masukkan kata:')
print(funPalindrome(kata))
