class TreeNode:
    def __init__(self, entry, id):
        self.left = None
        self.right = None
        self.entry = entry
        self.id = []
        self.id.append(id)


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.name = ""

    def TreeSize(self):
        return self.size

    def TreeFull(self):
        return 0

    def TreeEmpty(self):
        if self.root == None:
            return 1
        else:
            return 0

    def InsertNode(self, entry, id):
        pe = TreeNode(entry, id)
        if self.root is None:  # Zero nodes
            self.root = pe
        else:
            q = self.root
            while q != None:
                r = q
                if entry == q.entry:
                    q.id.append(id)
                    self.size = self.size + 1
                    return
                if entry < q.entry:
                    q = q.left
                else:
                    q = q.right
            if entry < r.entry:
                r.left = pe
            else:
                r.right = pe
        self.size = self.size + 1

    def TraverseTree(self, t):
        q = t
        if q is None:
            return
        print(str(q.entry) + ": " + str(q.id))
        self.TraverseTree(q.left)
        self.TraverseTree(q.right)

    def findNode(self, entry):
        if self.root is None:
            return -1
        q = self.root
        while q != None:
            if entry == q.entry:
                return q.id
            if entry < q.entry:
                q = q.left
            else:
                q = q.right
        return -1


t = Tree()
def upload(self):
        t.root = None
        # self.textBrowser.zoomIn(1)
        try:
            name = QFileDialog.getOpenFileNames()
            self.progressBar.setVisible(True)
            n = len(name[0])
            # print(n)
            self.progressBar.setMaximum(n)
            t.name = name
            for i in range(n):
                try:
                    with open(name[0][i], encoding='UTF-8')as f:
                        # f = open(name[0][i], encoding='UTF-8')
                        bio = f.read()
                        # print(f.read())
                        import re
                    for j in re.split(r'[;,.:)({}!?\s]\s*', bio):
                        j = j.replace(",", " ").replace(".", " ").replace(":", " ").replace("/", " ").replace("?",
                                                                                                              "").replace(
                            "!", " ").replace(";", " ").replace(")", " ").replace("(", " ").replace("{", " ").replace(
                            "}",
                            " ").replace(
                            "[", " ").replace("]", " ").replace('”', " ").replace('“', " ").replace("シ", " ").replace(
                            "し", " ").replace("...", " ")
                        # print(j.lower())
                        t.InsertNode(j.lower(), i + 1)
                        self.progressBar.setValue(i + 1)
                except:
                    print(i)
        finally:
            self.progressBar.setValue(n)
        # '''except:
        #     self.progressBar.setValue(False)
        #     self.progressBar.setVisible(False)
        #     self.lineEdit_2.clear()
        #     self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255);""border-color: rgb(255, 255, 127);")  # yellow
        #     self.lineEdit_2.setText("Invalid File")'''

    def search(self):
        self.progressBar.setVisible(False)
        self.textBrowser.clear()
        if t.root is None:
            self.lineEdit_2.clear()
            self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255);""border-color: rgb(255, 255, 127);")  # yellow
            self.lineEdit_2.setText("No Files Uploaded")
            return
        word = str(self.lineEdit.text())
        word = word.lower()
        found = t.findNode(word)
        if found == -1:  # word not found
            self.lineEdit_2.clear()
            self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255);""border-color: rgb(255, 255, 127);")  # yellow
            self.lineEdit_2.setText("Not Found")
        else:
            self.lineEdit_2.clear()
            self.lineEdit_2.setStyleSheet("border-color: rgb(48, 47, 47);")
            for i in range(100000):
                try:
                    with open(t.name[0][found[i] - 1], encoding="UTF-8")as f:
                        bio = f.read()
                    self.textBrowser.insertPlainText(
                        "Document " + "'" + t.name[0][found[i] - 1] + "'" + "\n\n" + bio + "\n")
                    self.textBrowser.insertPlainText(
                        "-----------------------------------------------------------------------------------------------------------------\n")
                    self.textBrowser.find(word)
                except:
                    return
