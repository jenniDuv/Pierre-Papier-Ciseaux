import random
import inquirer

def initialize_game():
    questions = [
        inquirer.List('size',
                      message="Choisissez entre pierre, papier ou ciseaux ",
                      choices=['pierre', 'papier', 'ciseaux'],
                      ),
    ]
    choix = [
        inquirer.List('choix',
                      message="Souhaitez-vous jouer au jeu ?",
                      choices=['oui', 'non'],
                      ),
    ]
    return questions, choix, 0, 0

def get_choice_user(choix):
    answers_user = inquirer.prompt(choix)
    user_choice = answers_user["choix"]
    return user_choice

def get_choice_computer():
    return random.choice(['pierre', 'papier', 'ciseaux'])

def compare_choice(utilisateur_choix, ordinateur_choix):
    if utilisateur_choix == ordinateur_choix:
        return "Match nul!\n", 0, 0
    
    elif (utilisateur_choix == "pierre" and ordinateur_choix == "ciseaux") or \
        (utilisateur_choix == "papier" and ordinateur_choix == "pierre") or \
        (utilisateur_choix == "ciseaux" and ordinateur_choix == "papier"):
         return "Vous avez gagnez!\n", 2, 0
    else:
        return "Vous avez perdu!\n", 0, 2
    
def print_results(score_user, score_ordinateur):
    print("Votre score est de : " + str(score_user))
    print("Le score de l'ordinateur est de : " + str(score_ordinateur))
    
def main():
    questions, choix, score_user, score_ordinateur = initialize_game()
    user_choice = get_choice_user(choix)
    
    while score_user < 10 and score_ordinateur < 10 and user_choice == 'oui':
        answers = inquirer.prompt(questions)
        utilisateur_choix = answers["size"]
        ordinateur_choix = get_choice_computer()

        resultat, points_user, points_ordinateur = compare_choice(utilisateur_choix, ordinateur_choix)
        print(f"L'ordinateur a fait : {ordinateur_choix} et vous avez fait : {utilisateur_choix}")
        print(resultat)

        score_user += points_user
        score_ordinateur += points_ordinateur
        print_results(score_user, score_ordinateur)

        user_choice = get_choice_user(choix)
    
    if score_user >= 10:
        print("Félicitations, vous avez atteint 10 points et gagné le jeu !")
    elif score_ordinateur >= 10:
        print("L'ordinateur a atteint 10 points et a gagné le jeu !")
    else:
        print("Merci d'avoir joué !")

if __name__ == "__main__":
    main()