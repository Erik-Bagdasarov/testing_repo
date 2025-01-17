file = open('test.txt', 'a')
file.write("hello world")
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
file.writelines(lines)
file.close()