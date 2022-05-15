def demander_reponse_numerique_utilisateur(min, max):
  reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") : ")
  try:
    reponse_int = int(reponse_str)
    if min<= reponse_int <= max:
      return reponse_int
    print ("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
  except:
    print("ERREUR : Veuillez rentrer uniquement des chiffres")
  return demander_reponse_numerique_utilisateur(min,max)

def poser_question(question):
  choix = question[1]
  bonne_reponse = question[2]

  print("  " + question[0])
  for i in range(len(choix)):
    print("  ", i+1, "-", choix[i])

  print()
  resultat_reponse_correcte = False
  reponse_int = demander_reponse_numerique_utilisateur(1, len(choix))
  
  if choix[reponse_int-1].lower() == bonne_reponse.lower():
    print("Bonne réponse")
    resultat_reponse_correcte = True
  else:
    print("Mauvaise réponse")
  print()
  return resultat_reponse_correcte

def lancer_questionnaire(questionnaire):
  score = 0
  for question in questionnaire:
    if poser_question(question):
      score += 1 
  print("Score :", score)

question1 = ("Quelle est la capitale de la Hongrie ?", ("Vienne", "Budapest", "Bratislava", "Zagreb"), "Budapest")
question2 = ("Quelle est la capitale de la Pologne ?", ("Prague", "Kiev", "Varsovie", "Ostrava"), "Varsovie")
question3 = ("Quelle est la capitale de l'Autriche ?", ("Vienne", "Budapest", "Strasbourg", "Salzbourg"), "Vienne")
question4 = ("Quelle est la capitale de la Bulgarie ?", ("Bucarest", "Sofia", "Tirana", "Pristina"), "Sofia")
question5 = ("Quelle est la capitale de la Lituanie ?", ("Vilnius", "Riga", "Tallinn", "Helsinki", "la réponse D"), "Vilnius")
question6 = ("En quelle année ont été rédigés les droits de l'homme ?", ("1715", "1781", "1789", "1792"), "1789")
question7 = ("En quelle année a été fondée l'URSS ?", ("1921", "1922", "1933", "1945"), "1922")
question8 = ("En quelle année a pris fin la dernière guerre froide ?", ("1975", "1989", "1991", "2002"), "1991")
question9 = ("Au cours de quel mois a eu lieu l'invasion de l'Ukraine?", ("décembre 2021", "janvier 2022", "février 2022", "mars 2022", "avril 2022"), "février 2022")
question10 = ("Depuis quelle année se déroule la guerre du Donbass ?", ("2010", "2012", "2014", "2016", "2018", "2020", "2022"), "2022")
questionnaire = (question1, question2, question3, question4, question5, question6, question7, question8, question9, question10)
lancer_questionnaire(questionnaire)