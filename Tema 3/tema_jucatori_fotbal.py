# Exerciții Opționale - grad de dificultate: Mediu spre
# greu (s-ar putea să ai nevoie de Google).
#
# 1. Ne imaginam o echipa de fotbal in timpul meciului. Sunt permise maxim 3 schimbari.
# - Declara o lista cu 5 jucatori: lista_jucatori_teren
# - Declara o lista cu 5 jucatori de rezerva: lista_jucatori_rezerva
# - Declara o lista goala cu jucatori scosi din teren: lista_jucatori_scosi
# - Schimbari_efectuate = joaca-te cu valori diferite ca sa vezi cum trec datele prin cod
# - SCHIMBARI_MAX va fi o constanta cu valoarea 3
# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie atunci:
# - Efectuam schimbarea daca jucatorul e in lista de rezerve si nu exista in jucatorii de pe
# teren
# - Stergem jucatorul scos din lista de teren si il adaugam in lista de jucatori scosi
# - Adaugam jucatorul intrat in lista de jucatori de pe teren si il scoatem din lista de jucatori
# de rezerva
# - Afisam pe ecran: a intrat x, a iesit y. Mai aveti z schimbari (inlocuiti x, y si z cu numele
# variabilelor voastre)
# Daca jucatorul pe care vrem sa il schimbam nu e in teren:
# - Afisati ‘nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# Altfel, afisati ecran: ‘mai aveti z schimbari’
# Google search hint: “how to check if item is in list python”

field_players = ['Messi', 'Higuain', 'Roberto Carlos', 'Ronaldo', 'Zidane']
reserve_players = ['Hagi', 'Popescu', 'Dumitrescu', 'Ilie', 'Petrescu' ]
players_out = [] #lista goala unde salvam jucatorii scosi
changes_made = 0 # variabila cu numarul de schimbari pe care le avem initial
CHANGES_MAX = 3 # variabila constanta

print(field_players)
print(reserve_players)

while changes_made < CHANGES_MAX:
    player_in = input("Enter the player who will enter the field: ")
    player_out = input("Enter the player who will leave the field: ")
    if player_out in field_players and player_in in reserve_players:
        field_players.remove(player_out)
        players_out.append(player_out)
        field_players.append(player_in)
        reserve_players.remove(player_in)
        changes_made += 1
        print(f"{player_in} entered, {player_out} let.You have {CHANGES_MAX-changes_made} substitution left.")
    elif player_out not in field_players:
        print(f"The substitution cannot be made because {player_out} is not on the field.")
    else:
        print(f"You have {CHANGES_MAX-changes_made} substition left ")

