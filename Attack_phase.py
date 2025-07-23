import matplotlib
matplotlib.use("TkAgg") 

import  modules.points_p1_p2    as  ppp
import  matplotlib.pyplot   as  plt
import  matplotlib.colors   as  pcolor
import  numpy   as  np


##############################################################
###-------------------input_data---------------------------###
##############################################################

attack_init     =   4 #int(input("Ataque: "))
dodge_init      =   -1 #int(input("Esquivar: "))


##############################################################
###-------------------organize_data------------------------###
##############################################################

###--------------------import_data-------------------------###
length_dat          =   int(ppp.length_data("modules/probability/Probabilidad_3D6.dat"))
table_attack        =   ppp.table_palyer_01(attack_init, "modules/probability/Probabilidad_3D6.dat")

###-------------------graph_axis_x-------------------------###
faces_attack        =   [table_attack.iloc[i,0] for i in range(length_dat)]
faces_attack        =   np.array(faces_attack)

###-------------------graph_axis_y-------------------------###
probability_attack  =   [table_attack.iloc[i,1] for i in range(length_dat)]
probability_attack  =   np.array(probability_attack)

###--------list_attack_true_false_and_relaunch-------------###
list_attack_true        =   []
list_attack_false       =   []
list_attack_relaunch    =   []

for i   in range(length_dat):
    list_of_tables  =   0
    list_of_tables  =   ppp.table_palyer_02(
                            dodge_init, 
                            table_attack.iloc[i,2], 
                            "modules/probability/Probabilidad_3D6.dat"
                        )
    list_attack_true.append(float(list_of_tables.iloc[0,2]))
    list_attack_false.append(float(list_of_tables.iloc[1,2]))
    list_attack_relaunch.append(float(list_of_tables.iloc[2,2]))

list_attack_true        =   np.array(list_attack_true)
list_attack_false       =   np.array(list_attack_false)
list_attack_relaunch    =   np.array(list_attack_relaunch)


##############################################################
###---------------------plot_graph-------------------------###
##############################################################

# Degradado hacia "#1D1D1D" hacia "#00CCDE"
list_color  =   [round(list_attack_true[i]*100, 4) for i in range(length_dat)] 
colormap    =   pcolor.LinearSegmentedColormap.from_list("custom_cmap", ["#1D1D1D", "#00CCDE"])  

plt.figure(facecolor="#1D1D1D")
plt.grid(True, linestyle="dashed", color="#696969", alpha=0.5, zorder=1)
scatter     =   plt.scatter(
                    faces_attack, 
                    probability_attack,
                    c=list_color, 
                    cmap=colormap, 
                    s=50, 
                    zorder=2
                )

cbar = plt.colorbar(scatter)
cbar.set_label("Attack true P(%)", color="#5AEDA3", fontsize= "13")
cbar.ax.tick_params(labelcolor="#5AEDA3")

for i in range(length_dat):
    plt.text(
            faces_attack[i], 
            probability_attack[i], 
            f'{list_color[i]}%', 
            fontsize=7, va='bottom',  ha='center', 
            color="#ffffff"
    )


plt.xlabel("Possibilities in the dice", color="#5AEDA3", fontsize= "13")
plt.xticks(faces_attack,color="#5AEDA3")

plt.ylabel("Attack probability (%)", color="#5AEDA3", fontsize="13")
plt.yticks(probability_attack, [ str(round(probability_attack[i]*100,4)) for i in range(length_dat) ], color="#5AEDA3")

plt.title(f"Attack True \n attack: {attack_init} vs dodge: {dodge_init}", color="#5AEDA3", fontsize="14")

plt.gca().set_facecolor("#353535")

plt.show()  # plt.savefig("grafica.pdf") plt.savefig("grafica.png")





###############################################################
###-------------write_in_document_markdown------------------###
###############################################################
# with    open(f"Tabla_attack[{attack_init}]_dodge[{dodge_init}].md", "w")   as  f:
#     f.write("Daño: " + str(damage_init) + "\n" + "\n" + "Esquivar: " + str(dodge_init) + "\n" + "\n")
#     f.write(table_result.to_markdown(index=False))


