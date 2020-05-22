def resume_detection(_classes):
    


detected_word = "слово"  #after one word was recognised, this variable holds it
phrase = "Макс, "

classes_2 = ["включи", "включить", "выключи", "выключить", "следующий", "предыдущий",
    "следующая", "предыдущая", "вперед", "назад", "убери", "убавь", "прибавь", "сделай", "измени"]
classes_3 = ["свет", "основной", "дополнительный", "аудио", "аудиосистему", "музыку", "медиасистему", "свет"]
if (detected_word == "Макс"):
    classes = classes_2
    phrase = phrase + detected_word + " "
    resume_detection()#запуск сетки на следующее слово
elif (detected_word == "включи" or detected_word == "выключи" or detected_word == "включить" or detected_word == "выключить"):
    classes = classes_3
    phrase = phrase + detected_word + " "
    resume_detection()
elif (detected_word == "следующий" or detected_word == "предыдующий" or detected_word == "следующая" or detected_word == "предыдующая"):
    classes = ["трек", "песня"]
    phrase = phrase + detected_word + " "
    resume_detection()
elif (detected_word == "вперед" or detected_word == "назад"):
    phrase = phrase + detected_word + " "
    restart_detection()
elif (detected_word == "убери"):
    phrase = phrase + detected_word + " с паузы"
    restart_detection()
elif (detected_word == "убавь" or detected_word == "прибавь"):
    phrase = phrase + detected_word + " громкость"
    restart_detection()
elif (detected_word == "сделай"):
    classes = ["потише","погромче"]
    phrase = phrase + detected_word
    restart_detection()
elif (detected_word == "измени"):
    phrase = phrase + detected_word + " голос"
    restart_detection()



