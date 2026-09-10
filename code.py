print ("Hello, World!")

# hey guys im just getting started
def greet(name):
    return f"Hello, {name}!"

print(greet("Matthias"))

#guys i just learned about Regex in Python!

import re

text = "Meetings are on 2026-09-10, 2025-12-31, and 26-01-01. Ignore 2026-9-5 and 2026-123-45."

answer = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", text)

#sortin a tuple without using sorted() function

my_tuple = (5, 2, 9, 1, 7)

# Convert to list, sort, then convert back to tuple

my_list = [x for x in my_tuple]
my_list.sort()
sorted_tuple = tuple(my_list)