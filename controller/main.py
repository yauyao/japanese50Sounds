import random
from service.QuestionSet import initQuestionSet

if __name__ == '__main__':
    list = initQuestionSet()
    target = random.choice(list)
    print( "請告訴我『 " + target.getQuestion() +" 』的讀音")
    userAnswer = input("請輸入答案:")

    if userAnswer.strip() == target.getAnswer() :
        print("答對了")
    else:
        print("答錯了，題目是「"+target.getQuestion()+"」,答案是「"+target.getAnswer()+"」,你的回答是「"+userAnswer+"」")