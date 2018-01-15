import os

for filename in os.listdir("./sona"):
    print(filename)
    path = "./sona/" + filename
    file = open(path, "r")
    print file.read()
    print "-----"
