name= input("What is your name? ")

greeting = """
<!DOCTYPE html>
<h1>Hello %s</h1>
"""%name

b= open("username.html", "w")
b.write(greeting)
b.close()
