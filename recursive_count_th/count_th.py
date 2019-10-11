'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# def count_th(word):
#     count = 0
#     if "th" in word:
#         count = word.count("th")
#         return count
#     else:
#         return count

i = 0
count = 0


def count_th(words):
    global i
    global count

    i = words.find("th", i, len(words)-1) + 1
    count += 1
    # need to work on if statement; if th is not at end of string, count will be plus 1
    if i > 0 and (len(words)-1)-i > 1:
        count_th(words)
    return count

# string = "abcthxyz"
# print(count_th(string))
