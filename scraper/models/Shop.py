class Shop:

    def __init__(self, name, url, data):
        self.name = name
        self.url = url
        self.data = [data]

    def setName(self, name):
        self.name = name

    def setURL(self, url):
        self.url = url

    # def addData(self, data):
    #     self.data.append(data)

    def getName(self):
        return self.name

    def getURL(self):
        return self.url
