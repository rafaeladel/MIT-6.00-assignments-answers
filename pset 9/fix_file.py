import re
old = open("shapes.txt", "r")
old_con = old.read()
old.close()

new_str = re.sub("\n","",old_con)

print new_str

another_str = re.sub("(\d)([a-zA-Z])", r"\1\n\2", new_str)

print another_str