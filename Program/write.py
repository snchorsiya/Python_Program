# Read the file and store all line in list
# Reverse the list
# Write the list back to file

with open('test.txt', 'r') as reader:
    content = reader.readlines()  # [abc, ads, sdsd, addd]
    reversed(content)  # [sdsd, ads, addd, abc]
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
