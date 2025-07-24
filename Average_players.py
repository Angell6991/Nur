import  numpy   as  np
import  pandas  as  pd

numbers_players     =   int(input("Numero de jugadores en la mesa: "))

attack  =   []
dodge   =   []
damage  =   []
life    =   []
players =   []

print("")
for i   in  range(numbers_players):
    attack.append(int(input(f"Ataque jugador {i+1}:")))

print("")
for i   in  range(numbers_players):
    dodge.append(int(input(f"Esquivar jugador {i+1}:")))

print("")
for i   in  range(numbers_players):
    damage.append(int(input(f"Daño jugador {i+1}:")))

print("")
   
for i   in  range(numbers_players):
    life.append(int(input(f"Vida jugador {i+1}:")))
    players.append(f"Player {i+1}")


sum_attack  =   0
sum_dodge   =   0
sum_damage  =   0
sum_life    =   0


for i   in  range(numbers_players):
        
    sum_attack  =   sum_attack  +   attack[i]
    sum_dodge   =   sum_dodge   +   dodge[i]
    sum_damage  =   sum_damage  +   damage[i]
    sum_life    =   sum_life    +   life[i]


attack_pro  =   sum_attack/numbers_players
attack.append(attack_pro)

dodge_pro   =   sum_dodge/numbers_players
dodge.append(dodge_pro)

damage_pro  =   sum_damage/numbers_players 
damage.append(damage_pro)

life_pro    =   sum_life/numbers_players
life.append(life_pro)

players.append("Player prom")


table   =   [players, attack, dodge, damage, life]
table   =   pd.DataFrame({ 
                'Player': players,
                'Attack': attack,
                'Dodge': dodge,
                'Damage': damage,
                'Life': life
            })


###############################################################
###-------------write_in_document_markdown------------------###
###############################################################
with    open(f"Number_player_{numbers_players}.md", "w")   as  f:
    f.write(table.to_markdown(index=False))

###---------------------------------------------------------###
# with    open(f"Tabla_attack[{attack_init}]_dodge[{dodge_init}].md", "w")   as  f:
#     f.write("Daño: " + str(damage_init) + "\n" + "\n" + "Esquivar: " + str(dodge_init) + "\n" + "\n")
#     f.write(table_result.to_markdown(index=False))


