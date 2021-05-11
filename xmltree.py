

class XMLTREE:
    count = 0
    def __init__(self, tag):
        self.tag = tag
        self.text = None
        self.child = []

def addelement(root,data):
    if root == None:
            return None


    n = XMLTREE(data)
    root.child.append(n)

    return root

def addsubelement(root, data):

    for i in range(len(root.child)):
        if root.child[i].tag == "ADD":
            n = XMLTREE(data)
            root.child[i].child.append(n)

    return root














root = XMLTREE("measure")
addelement(root, "ADD")
addsubelement(root, "metadata")

print(root.child[0].child[0].tag)
print(root.child[0].tag)




