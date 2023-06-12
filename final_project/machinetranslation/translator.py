from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    e2f_translator = MyMemoryTranslator("en", "fr")
    frenchText = e2f_translator.translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    f2e_translator = MyMemoryTranslator("fr", "en")
    englishText = f2e_translator.translate(frenchText)
    return englishText
