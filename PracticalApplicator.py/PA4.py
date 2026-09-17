import re

def clean_text(html):
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', html)

    # Collapse spaces, tabs and newlines
    text = re.sub(r'\s+', ' ', text)

    return text.strip()

html = """
<p>Hello   World!</p>
<div>Welcome    to Python.</div>
"""

print(clean_text(html))
# output:
# Hello World! Welcome to Python.