import os
import pickle
from OlympicGame import OlympicGame
from Competition import Competition
from OlympicGames import OlympicGames
from Competitions import Competitions
from Olympic_Competition import Olympic_Competition

class Menu(object):
    def draw(self):
        ol_cp_f = open('ol_cp_f.pickle', 'rb')
        ol_f = open('ol_f.pickle', 'rb')
        cp_f = open('cp_f.pickle', 'rb')
        ch = -1
        # ol_cp = Olympic_Competition()
        ol_cp = pickle.load(ol_cp_f)
        # ol = OlympicGames()
        ol = pickle.load(ol_f)
        # cp = Competitions()
        cp = pickle.load(cp_f)
        while ch != 7:
            ch = -1
            print("Welcome\n")
            print("Make your choise\n\n")
            print("1. Look database\n")
            print("2. Add Olympic Game\n")
            print("3. Add Competition\n")
            print("4. Delete Olympic Game\n")
            print("5. Delete Competition\n")
            print("6. Sort\n")
            print("7. Exit\n\n")
            try:
                ch = int(input())
            except Exception:
                print("Wrong!!!")
                os.system('cls')
            if ch == 1:
                i = 0
                while i <= ol_cp.getSize():
                    ids = ol_cp.getByID(i)
                    print(str(i) + ".")
                    ol.printById(ids[0])
                    cp.printById(ids[1])
                    print()
                    i += 1
                while ch != 0:
                    print("Press 0 to return\n")
                    try:
                        ch = int(input())
                    except Exception:
                        print("Wrong!!!\n")
            elif ch == 2:
                print("Input city\n")
                city = input()
                year = 0
                print("\nInput year\n")
                try:
                    year = int(input())
                except Exception:
                    print("\nError format\n")
                ogame = OlympicGame(year, city)
                ol.add(ogame)
                try:
                    ol_cp.add(ol.last_id, -1)
                except Exception as e:
                    print(e)

            elif ch == 3:
                print("Input type of competition\n")
                t_of_c = input()
                print("Input type of sports\n")
                t_of_s = input()
                new_cp = Competition(t_of_c, t_of_s)
                idx = cp.add(new_cp)
                print("To which Olympic Games you would like to add them?\n")
                print("Enter id")
                ch3 = -1
                while (ch3 < 0) or (ch3 > ol_cp.getSize()):
                    ch = -1
                    ol.print()
                    try:
                        ch3 = int(input())
                    except Exception:
                        print("Wrong!!!\n")
                fl = 0
                i = 0
                while i <= ol_cp.getSize():
                    if ch3 == ol_cp.omap[i]:
                        if ol_cp.cmap[i] == -1:
                            ol_cp.cmap[i] = idx
                            fl = 1
                            break
                    i += 1
                if fl == 0:
                    try:
                        ol_cp.add(ch3, idx)
                    except Exception as e:
                        print(e)
            elif ch == 4:
                print("Which one to delete?")
                ol.print()
                ch4 = -1
                while (ch4 < 0)or(ch4 > len(ol.olympicGames)):
                    try:
                        ch4 = int(input())
                    except Exception:
                        print("Try again!")
                try:
                    ol.delete(ch4)
                except Exception as e:
                    print(e)
                ol_cp.delete(ch4, -1)
                olist = ol.reindex()
                i = 0
                while i < len(ol_cp.omap):
                    for o_reindex in olist:
                        if ol_cp.omap[i] == o_reindex[0]:
                            ol_cp.omap[i] = o_reindex[1]
                    i += 1
            elif ch == 5:
                print("Which one to delete?")
                cp.print()
                ch5 = -1
                while (ch5 < 0) or (ch5 > len(cp.competitions)):
                    try:
                        ch5 = int(input())
                    except Exception:
                        print("Try again!")
                try:
                    cp.delete(ch5)
                except Exception as e:
                    print(e)
                ol_cp.delete(-1, ch5)
                clist = cp.reindex()
                i = 0
                while i < len(ol_cp.cmap):
                    for c_reindex in clist:
                        if ol_cp.cmap[i] == c_reindex[0]:
                            ol_cp.cmap[i] = c_reindex[1]
                    i += 1
            elif ch == 6:
                result = []
                for comp in cp.competitions:
                    if comp.type_of_competition == "Group":
                        result.append(comp.cid)
                presult = []
                i = 0
                while i < len(ol_cp.omap):
                    for idx in result:
                        if ol_cp.cmap[i] == idx:
                            presult.append(ol_cp.omap[i])
                    i += 1
                for ogame in ol.olympicGames:
                    for idx in presult:
                        if ogame.oid == idx:
                            ogame.print()

        ol_cp_f = open('ol_cp_f.pickle', 'wb')
        pickle.dump(ol_cp, ol_cp_f)
        ol_f = open('ol_f.pickle', 'wb')
        pickle.dump(ol, ol_f)
        cp_f = open('cp_f.pickle', 'wb')
        pickle.dump(cp, cp_f)

