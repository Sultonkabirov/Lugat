keys=["uzb","rus","eng"]
print(keys[0])
list = [
    {
        "uzb": "salom",
        "rus":"привет",
        "eng":"hello"
    },
    {
        "uzb": "mushuk",
        "rus":"кошка",
        "eng":"cat"
    },
    {
        "uzb":"kompyuter",
        "rus":"компьютер",
        "eng":"computer"
    }
]

langs = {
            "uzb": "O'zbek tili",
            "rus": "Rus tili",
            "eng": "Ingliz tili"
        }


while True:
    word = input("Enter word: ")
    lang = input("Which language: ")

    word = word.lower().strip()
    lang = lang.lower().strip()

    for lang_dict in list:
        for key, value in lang_dict.items():
            if lang_dict[key] == word:
                print(lang_dict[lang])

    soz=input("Yangi so'z kiritasizmi :").lower()
    if soz=="ha":
        s={}

        lang =  input("Qaysi tildagi so'zni qo'shasiz ? (uzb , rus , eng): ").lower().strip()
        word = input(f"{langs[lang]} uchun so'z kiriting: ").lower().strip()
        s[lang] = word
        lang =  input("Qaysi tildagi so'zni qo'shasiz ? ").lower().strip()
        word = input(f"{langs[lang]} uchun so'z kiriting: ").lower().strip()
        s[lang] = word   
        lang =  input("Qaysi tildagi so'zni qo'shasiz ? (uzb , rus , eng): ").lower().strip()
        word = input(f"{langs[lang]} uchun so'z kiriting: ").lower().strip()    
        s[lang] = word 
        list.append(s)
    else:
        break


