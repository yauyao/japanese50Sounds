class Question(object):
    def __int__(self):
        super(Question,self).__init__()

    def getQuestion(self):
        return self._question

    def setQuestion(self,question):
        self._question = question

    def getAnswer(self):
        return self._answer

    def setAnswer(self,answer):
        self._answer = answer