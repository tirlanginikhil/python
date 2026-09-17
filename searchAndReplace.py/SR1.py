import re

def redact_emails(text):
    return re.sub(r'[\w.-]+@[\w.-]+\.\w+', '[EMAIL HIDDEN]', text)

text = "Contact john@gmail.com or ram123@yahoo.com"
print(redact_emails(text))
# output:
# Contact [EMAIL HIDDEN] or [EMAIL HIDDEN]