#!C:/python

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form["description"].value

opened_file = open('practice/'+pageId, 'w')
opened_file.write(description)
opened_file.close()

os.rename('practice/'+pageId, 'practice/'+title)

#Redirection
print("Location: index.py?id="+title)
print()
