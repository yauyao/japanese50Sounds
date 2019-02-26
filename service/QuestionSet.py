from model.Question import Question


def initQuestionSet():
    questions = []

    questionSet = ["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ"]
    answerSet = ["a","i","u","e","o","ka","ki","ku","ke","ko","sa","si","su","se","so"]

    for index in range(len(questionSet)):
        elemnet = Question()
        elemnet.setQuestion(questionSet[index])
        elemnet.setAnswer(answerSet[index])
        questions.append(elemnet)

    return questions

# if __name__ == '__main__':
#     list = initQuestionSet()
#     target = random.choice(list)
#     print( "請告訴我『 " + target.getQuestion() +" 』的讀音")
#     userAnswer = input("請輸入答案:")
#
#     if userAnswer == target.getAnswer() :
#         print("答對了")
#     else:
#         print("答錯了")