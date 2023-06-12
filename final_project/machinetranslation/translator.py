from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    my_translator = MyMemoryTranslator("en", "fr")
    frenchText = my_translator.tranlsate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    my_translator = MyMemoryTranslator("fr", "en")
    englishText = my_translator.translate(frenchText)
    return englishText
