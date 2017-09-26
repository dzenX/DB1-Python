from OlympicGame import OlympicGame
from Competition import Competition
from OlympicGames import OlympicGames
from Competitions import Competitions
from Olympic_Competition import Olympic_Competition
from Menu import Menu


# Greetings here
print("Welcome\n\n")

# Test of class Competition
c1 = Competition("Group", "Swimming")
# c1.print()
c2 = Competition("Individual", "Jogging")
# c2.print()
c3 = Competition("Group", "Basketball")
# EOT of Competition

# Test of class OlympicGame
o1 = OlympicGame(2012, "London")
# o1.print()
o2 = OlympicGame(2010, "Gavana")
# o2.print()
o3 = OlympicGame(2008, "Gonduras")
# 03.print()
# EOT of OlympicGame

# Test of class OlympicGames
og1 = OlympicGames()
og1.add(o1)
og1.add(o2)
og1.add(o3)
og1.print()
og1.delete(1)
og1.print()
# EOT of OlympicGames

# Test of class Competitions
cs1 = Competitions()
cs1.add(c1)
cs1.add(c2)
cs1.add(c3)
cs1.print()
cs1.delete(2)
cs1.print()
# EOT of Competitions

# Test of class O_C
oc = Olympic_Competition()
oc.add(1, 1)
oc.add(1, 2)
print(oc.getByID(1))
oc.delete(0, 2)
print(oc.getByID(0))
# EOT of O_C

# Menu
main = Menu()
main.draw()
# EOC

