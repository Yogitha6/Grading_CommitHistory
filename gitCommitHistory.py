from github import Github

def generateUserList(filename):
    Users = []
    f = open(filename,'r')
    f.readline()
    for line in f:
        data = line.split(",")
        Users.append(data[0].strip())
        #print(data[2])
    f.close()
    print "Users list is %s" %Users
    return Users
	
generateUserList("C:\\New folder\\users.txt")