## 1. Introduction ##

import pandas as pd
hn=pd.read_csv("hacker_news.csv")


## 2. The Regular Expression Module ##

import re

titles = hn["title"].tolist()
python_mentions=0
pattern="[pP]ython"
for s in titles:
    if re.search(pattern,s):
        python_mentions+=1
print(python_mentions)

## 3. Counting Matches with pandas Methods ##

pattern = '[Pp]ython'
titles=hn["title"]
python_mentions=pd.Series(titles).str.contains(pattern).sum()

## 4. Using Regular Expressions to Select Data ##

titles = hn['title']
ruby_titles=titles[pd.Series(titles).str.contains("[Rr]uby")]


## 5. Quantifiers ##

# The `titles` variable is available from
# the previous screens
email_bool=pd.Series(titles).str.contains("e-?mail")
email_count=email_bool.sum()
email_titles=titles[email_bool]

## 6. Character Classes ##

pattern="\[\w+\]"
tag_titles=pd.Series(titles).str.contains(pattern)
tag_count=tag_titles.sum()

## 7. Accessing the Matching Text with Capture Groups ##

pattern = r"\[(\w+)\]"
tag_freq=pd.Series(titles).str.extract(pattern).value_counts()


## 8. Negative Character Classes ##

def first_10_matches(pattern):
    """
    Return the first 10 story titles that match
    the provided regular expression
    """
    all_matches = titles[titles.str.contains(pattern)]
    first_10 = all_matches.head(10)
    return first_10
pattern="[Jj]ava[^Ss]"
java_titles=titles[titles.str.contains(pattern)]

## 9. Word Boundaries ##

java_titles=titles[titles.str.contains(r"\b[Jj]ava\b")]

## 10. Matching at the Start and End of Strings ##



pattern = r"^\[(\w+)\]"
beginning_count=titles.str.contains(pattern).sum()

pattern1=r"\[(\w+)\]$"
ending_count=titles.str.contains(pattern1).sum()


## 11. Challenge: Using Flags to Modify Regex Patterns ##

import re

email_tests = pd.Series(['email', 'Email', 'e Mail', 'e mail', 'E-mail',
              'e-mail', 'eMail', 'E-Mail', 'EMAIL', 'emails', 'Emails',
              'E-Mails'])
email_mentions=titles.str.contains(r"\be[\-\s]?mails?\b", flags=re.I).sum()