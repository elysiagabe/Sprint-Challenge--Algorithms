'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case -- if string is less than 2, we can't find a match b/c we're looking for a string that has 2 characters
    if len(word) < 2:
        return 0
    
    else: 
        # recursive case
        # if first two letters are string 'th', increment count and then look at next letters after those 2
        if word[:2] == "th":
            return 1 + count_th(word[2:])
        # else look at the next letter
        else:
            return count_th(word[1:])

