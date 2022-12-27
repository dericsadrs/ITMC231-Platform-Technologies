class Emmet:

    #initialize parameters
    def __init__(self,raw,finalOutput = "", malformedChecker = True, listOfTags = ['div','span','p','nav']):
        self.raw = raw
        self.finalOutput = finalOutput
        self.malformedChekcer = malformedChecker
        self.listOfTags = listOfTags

    def emmetAbbrevations(self):
        child = self.raw.split('+')
        for htmlTags in child:
            parent = htmlTags.split('>')
            for item in range(len(parent)):
                if parent[item] in self.listOfTags:
                     self.finalOutput+= "\t" * item+'<{}>'.format(parent[item]) + "\n"
                else:
                    self.malformedChekcer = False
            for itemForReverse in range (len(parent)-1,-1,-1):
                self.finalOutput+="\t" * itemForReverse + "</{}>".format(parent[itemForReverse])+"\n"

    def __str__(self):
        self.emmetAbbrevations() # calls the emmetAbbrevations Function
        if self.malformedChekcer == True: 
            return self.finalOutput
        else:
            return "Unrecognized Abbreviation"
