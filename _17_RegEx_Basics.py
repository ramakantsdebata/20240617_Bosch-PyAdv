import re

'''
string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
    including the FTSE, fell by 11.48% - the worst day since it launched in 1998. \
    The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
    of STOXX 600 shares since its all-time peak on 19 February."
'''

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% - the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

pattern = r"c:\Users\temp\newfile.txt"
print(pattern)

#region Commented
# sPattern = r"\d{3}"
# print(f"String Pattern--> [{type(sPattern)}], [{sPattern}]")

# rePattern = re.compile(sPattern)
# print(f"RE Pattern--> [{type(rePattern)}], [{rePattern}]")


#################################################################

# res = re.findall(rePattern, string)
# print(f"Res --> {type(res)}, {res}")

# res = re.findall(sPattern, string)
# print(f"Res --> {type(res)}, {res}")

#################################################################

# ## search() - Looks for a match and stops when it finds the first match. That is produced as the result.

# s = r"\d{3}"

# res = re.search(s, string)
# print(res)

# s = r"\w{3}"
# res = re.match(s, string)
# print(res)
# print(res.span())


###################################################################

## Match - This attempts to find a match starting from the beginning of the string.

# s = r"\d{3}"
# res = re.match(s, string)
# print(res)

###################################################################
## Fullmatch - Matches the entire string for a given pattern
## - . - matches everything bu the newline


# # print(len(string))
# s = r".{285}"
# res = re.fullmatch(s, string)
# print(res)


###################################################################
# ## Split - KLike the str.split(); However, it can accept patterns as well, unlike the str.split()

# res = string.split(' ')
# print(type(res), res)

# res = re.split(r"\s", string)
# print(type(res), res)

##################################################################
# ## Sub - Substitute a pattern with a giver string-replacement

# s = r"[A-Z]{2,}"
# res = re.sub(s, "INDEX", string, 2)
# print(type(res), res)

# ## Subn
# res = re.subn(s, "INDEX", string, 2)
# print(type(res), res)
# print(f"Made {res[1]} replacements")

#################################################################
## Groups, Group
#endregion

# s = r".+\s(.+ex).+(\d\d\s.+)."
# res = re.search(s, string)
# print(type(res), res)
# print(res.groups())
# print(res.group(1))
# print(res.group(2))
# print(res.group(0))
# print(res.group())
# print(res.group(1, 2))

# print(res.span(1))
# print(res.start(1), res.end(1))
# print(string[res.start(2) : res.end(2)])

# res = re.findall(s, string)
# print(res)


string2 = "The Euro STOXX 600 index,\nwhich tracks all stock markets across Europe including the FTSE, fell by 11.48% - the worst day since it launched in 1998.\nThe panic selling prompted by the coronavirus has wiped £2.7tn off \nthe value of STOXX 600 shares since its all-time peak on 19 February."

# re.I - IgnoreCase (performs a case insensitive search)
# re.M - Multiline; Enable multiline operations
# re.S - DotAll - The metacharacter '.' matches everything, including newline.
# re.X - Verbose
# Combine the flags with the OR operator --> flags = re.I | re.M | re.S | re.X

# res = re.findall(r"the", string, re.I)
# res = re.findall(r"the", string, re.I)
# print(len(res), res)

# res = re.findall(r"^the", string2, re.I|re.M)
# print(len(res), res)

# res = re.findall(r".+", string2, re.S)
# print(len(res), res)


res = re.search(r'''.+\s        # Beginning part of the string (ignore this part)
                (.+ex)          # a word ending with 'ex', and prepended by a whitespace
                .+              # Bunch of characters in the middle
                (\d\d\s.+)      # date that we want to see
                .               # The last character(anytype)''', string, re.X)
print(res.groups())