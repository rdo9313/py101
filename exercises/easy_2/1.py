def greetings(name, occupation):
    return f"Hello, {" ".join(name)}! Nice to have a {occupation["title"]} {occupation["occupation"]} around."

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.