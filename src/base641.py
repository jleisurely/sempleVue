# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import base64

with open("1.jpeg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

print(encoded_string)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
