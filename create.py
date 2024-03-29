#!C:/python
print("content-type: text/html; charset=utf-8\n")
print()
import cgi, os, view

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('practice/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'

print('''<!doctype html>
<html>
  <head>
    <title>WEB1 - Welcome</title>
    <meta charset="UTF-8">
  </head>

  <body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>
        {listStr}
    </ol>
    <a href="create.py">create</a>
    <form action="process_create.py" method="post">
        <p><input type="text" name="title" placeholder="title"></p>
        <p><textarea row="4" name="description" placeholder="description"></textarea></p>
        <p><input type="submit"></p>
    </form>
  </body>
</html>
'''.format(title=pageId, desc=description,  listStr=view.getList()))
