# regex library re for the pattern recognition methods for scraping
# skills: regex and pattern recognition
# Library: re, pyperclip

# pyperclip to allow you to store data on the clipboard
# so that you can copy (to load the data) and paste (to export the output)

# To run:
# Copy string/text into the clipboard 
# run the code
# paste result into desired word doc or text file. 


import re, pyperclip

# 1) Create a regex for phone numbers


# setting these are the variations for phone number
# 1234 -232- 2321, 232- 9343, (232) 234-0000. 434-0000 ext 22422, ext.12345, x12343

phoneRegex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))?            # area code (optional)
(\s|-)            # first separator
\d\d\d            # first 3 digits
-            # separator
\d\d\d\d   # last 4 charaters
(((ext(\.)?\s)|x)      # extension word-part ( optional)      
(\d{2.5}))?            # extension number-part (optional)
)
''', re.VERBOSE) 

# 2) Create a regex for email addresses
emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+        # name part
@        # @ symbol
[a-zA-Z0-9_.+]+        # domain name type

''', re.VERBOSE)



# 3) Get the text off the clipboard ( you should have copied some text using 'copy' CNTL+C)
# as a example you can CNTL + C any amount of text from the PDF into the clipboard

text = pyperclip.paste()
text = directory
# 4) Extract the email/phone from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)


# 5) Copy the extracted email/phone to the clipboard

allPhoneNumbers = []
for phoneNumber in extractedPhone:
     allPhoneNumbers.append(phoneNumber[0])
        

# 6) Join all the phone number and emails into a long string delimited by newline

results = '\n'.join(allPhoneNumbers) +'\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)


