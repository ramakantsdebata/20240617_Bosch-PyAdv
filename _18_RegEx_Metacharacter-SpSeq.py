import re

# . - Dot matches all the characters, except newlines... unless re.S is specified as a flag
# ^ - Matches at the beginnig of the line, not entire subject string.
# $ - Matches at the end of line, not entire subject string.

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% - the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

string2 = '''The Euro STOXX 600 index,
which tracks all stock markets across Europe including the FTSE, fell by 11.48% - the worst day since it launched in 1998.
The panic selling prompted by the coronavirus has wiped £2.7tn off
the value of STOXX 600 shares since its all-time peak on 19 February.'''

#region asterisk_plus_qmark
# res = re.findall(r"^the", string2, re.I|re.M)
# print(len(res), res)


# res = re.findall(r"\s(\w{2,})\W$", string2, re.M)
# print(res)

# #################################################################
# ## Quantifiers - * + ?
# ## * - Zero or more occurances of the preceeding pattern, such that it captures as many as possible; Greedy behaviour
# ## + - One or more occurances of the preceeding pattern, such that it captures as many as possible; Greedy behaviour
# ## ? - Zero or one occurance of the preceeding pattern, such that it captures as many as possible; Non-Greedy behaviour

# res = re.findall(r"\d\d\d*", string)
# print(res)

# res = re.findall(r"\d\d\d+", string)
# print(res)

# res = re.findall(r"\d\d\d?", string)
# print(res)

# res = re.findall(r"\d\d\d*?", string)
# print(res)

# res = re.findall(r"\d\d\d+?", string)
# print(res)

# res = re.findall(r"\d\d\d??", string)
# print(res)

# print( "-----------------------------------")

# res = re.findall(r"E.+", string)
# print(res)

# res = re.findall(r"E.+\s", string)
# print(res)

# res = re.findall(r"E.+?\s", string)
# print(res)

# res = re.findall(r"(E.*?)\s", string)
# print(res)
#endregion
######################################################################################

#region backslash
# ## Backslash - One of two things
# ##          1. Special Sequence - \A \b \B \w \W ....
# ##          2. Escape character - \( \) \[ \] \\ \. 

# res = re.findall(r"\d", string)
# print(res)

# res = re.findall(r"\.", string)
# print(res)
#endregion

## Square brackets - []
## Character class - [A-Z]  [a-z] [0-9]  [A-Za-z]
## Characgter set - [aeiou]

res = re.findall(r"[aeiou]", string)
print(res)
st = set(res)
print(True) if len(st) == 5 else print(False)
print("Count of a -->", res.count('a'))
print("Count of e -->", res.count('e'))
