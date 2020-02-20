#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
name = form.getvalue("user_name")

greeting = """
<!DOCTYPE html>
<h1>Hello %s!</h1>
"""%name

print(greeting)
