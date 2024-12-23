import random

words = [
    {"french": "bonjour", "english": "hello"},
    {"french": "au revoir", "english": "goodbye"},
    {"french": "merci", "english": "thank you"},
    {"french": "s'il vous plaît", "english": "please"},
    {"french": "oui", "english": "yes"},
    {"french": "non", "english": "no"},
    {"french": "homme", "english": "man"},
    {"french": "femme", "english": "woman"},
    {"french": "enfant", "english": "child"},
    {"french": "chat", "english": "cat"},
    {"french": "chien", "english": "dog"},
    {"french": "ami", "english": "friend"},
    {"french": "maison", "english": "house"},
    {"french": "voiture", "english": "car"},
    {"french": "livre", "english": "book"},
    {"french": "école", "english": "school"},
    {"french": "professeur", "english": "teacher"},
    {"french": "étudiant", "english": "student"},
    {"french": "ville", "english": "city"},
    {"french": "pays", "english": "country"},
    {"french": "eau", "english": "water"},
    {"french": "nourriture", "english": "food"},
    {"french": "argent", "english": "money"},
    {"french": "heure", "english": "hour"},
    {"french": "jour", "english": "day"},
    {"french": "semaine", "english": "week"},
    {"french": "mois", "english": "month"},
    {"french": "année", "english": "year"},
    {"french": "temps", "english": "time"},
    {"french": "hiver", "english": "winter"},
    {"french": "printemps", "english": "spring"},
    {"french": "été", "english": "summer"},
    {"french": "automne", "english": "autumn"},
    {"french": "rouge", "english": "red"},
    {"french": "bleu", "english": "blue"},
    {"french": "vert", "english": "green"},
    {"french": "noir", "english": "black"},
    {"french": "blanc", "english": "white"},
    {"french": "jaune", "english": "yellow"},
    {"french": "orange", "english": "orange"},
    {"french": "manger", "english": "to eat"},
    {"french": "boire", "english": "to drink"},
    {"french": "aller", "english": "to go"},
    {"french": "venir", "english": "to come"},
    {"french": "parler", "english": "to speak"},
    {"french": "écouter", "english": "to listen"},
    {"french": "voir", "english": "to see"},
    {"french": "regarder", "english": "to watch"},
    {"french": "acheter", "english": "to buy"},
    {"french": "vendre", "english": "to sell"},
    {"french": "travailler", "english": "to work"},
    {"french": "jouer", "english": "to play"},
    {"french": "vivre", "english": "to live"},
    {"french": "aimer", "english": "to love"},
    {"french": "savoir", "english": "to know"},
    {"french": "penser", "english": "to think"},
    {"french": "comprendre", "english": "to understand"},
    {"french": "courir", "english": "to run"},
    {"french": "marcher", "english": "to walk"},
    {"french": "dormir", "english": "to sleep"},
    {"french": "réveiller", "english": "to wake up"},
    {"french": "écrire", "english": "to write"},
    {"french": "lire", "english": "to read"},
    {"french": "ouvrir", "english": "to open"},
    {"french": "fermer", "english": "to close"},
    {"french": "prendre", "english": "to take"},
    {"french": "donner", "english": "to give"},
    {"french": "demander", "english": "to ask"},
    {"french": "répondre", "english": "to answer"},
    {"french": "aider", "english": "to help"},
    {"french": "porter", "english": "to carry"},
    {"french": "chercher", "english": "to search"},
    {"french": "trouver", "english": "to find"},
    {"french": "attendre", "english": "to wait"},
    {"french": "commencer", "english": "to start"},
    {"french": "finir", "english": "to finish"},
    {"french": "mère", "english": "mother"},
    {"french": "père", "english": "father"},
    {"french": "frère", "english": "brother"},
    {"french": "sœur", "english": "sister"},
    {"french": "famille", "english": "family"},
    {"french": "lundi", "english": "Monday"},
    {"french": "mardi", "english": "Tuesday"},
    {"french": "mercredi", "english": "Wednesday"},
    {"french": "jeudi", "english": "Thursday"},
    {"french": "vendredi", "english": "Friday"},
    {"french": "samedi", "english": "Saturday"},
    {"french": "dimanche", "english": "Sunday"},
    {"french": "matin", "english": "morning"},
    {"french": "après-midi", "english": "afternoon"},
    {"french": "soir", "english": "evening"},
    {"french": "nuit", "english": "night"},
    {"french": "petit", "english": "small"},
    {"french": "grand", "english": "big"},
    {"french": "jeune", "english": "young"},
    {"french": "vieux", "english": "old"},
]


def quiz_user(words):
    random.shuffle(words)
    score = 0

    for word in words:
        print(f"What is the meaning of {word['french']}")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word["english"].lower()

        if user_answer == correct_answer:
            print("Correct Answer!")
            score += 1
        elif user_answer == "quit":
            break
            print(f"You have scored {score} in quiz.")
        else:
            print("Wrong Answer!")
            print(f"The right answer is {correct_answer}\n")
            score -= 1

    print(f"You have scored {score} in quiz.")


def main():
    print("--------------------Welcome to Bingo--------------------")
    print("----------------A Language Learning App-----------------")
    input("\nEnter to start the quiz:")
    quiz_user(words)


main()
