"""
1) Import (make available to this program) all the code from the Python standard library module called webbrowser.

2) Import all the code from the Python standard library module called json.

3) Import only the urlopen function from the standard library module urllib.request.

4) A blank line, because we don’t want to feel crowded.

5) Print some initial text to your display.

6) Print a question about a URL, read what you type, and save it in a program variable called site.

7) Print another question, this time reading a year, month, and day, and then save it in a variable called era.

8) Construct a string variable called url to make the Wayback Machine look up its copy of the site and date that you typed.

9) Connect to the web server at that URL and request a particular web service.

10) Get the response data and assign to the variable contents.

11) Decode contents to a text string in JSON format, and assign to the variable text.

12) Convert text to data—Python data structures.

13) Error-checking: try to run the next four lines, and if any fail, run the last line of the program (after the except).

14) If we got back a match for this site and date, extract its value from a three-level Python dictionary. Notice that this line and the next two are indented. That’s how Python knows that they go with the preceding try line.

15) Print the URL that we found.

16) Print what will happen after the next line executes.

17) Display the URL we found in your web browser.

18) If anything failed in the previous four lines, Python jumps down to here.

19) If it failed, print a message and the site that we were looking for. This is indented because it should be run only if the preceding except line runs.
"""


import webbrowser
import json
from urllib.request import urlopen

print("Let's find an old website.")
site = input("Type a website URL: ")
era = input("Type a year, month and day, like 20150613: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data = json.loads(text)
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Found this copy: ", old_site)
    print("It should appear in your browser now.")
    webbrowser.open(old_site)
except:
    print("Sorry, no luck finding", site)