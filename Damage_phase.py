import matplotlib
matplotlib.use("TkAgg") 

import  modules.points_p1_p2    as  ppp
import  matplotlib.pyplot   as  plt
import  matplotlib.colors   as  pcolor
import  numpy   as  np


##############################################################
###-------------------Def_functions------------------------###
##############################################################


def graph_damage_and_life( damage_init, life_init, number_dice ):
    ##############################################################
    ###-------------------organize_data------------------------###
    ##############################################################
    
    direction_proba     =   f"modules/probability/Probabilidad_{number_dice}D6.dat"

    ###--------------------import_data-------------------------###
    length_dat          =   int(ppp.length_data(str(direction_proba)))
    table_damage        =   ppp.table_palyer_01(damage_init, str(direction_proba))

    ###-------------------graph_axis_x-------------------------###
    faces_damage        =   [table_damage.iloc[i,0] for i in range(length_dat)]
    faces_damage        =   np.array(faces_damage)

    ###-------------------graph_axis_y-------------------------###
    probability_damage  =   [table_damage.iloc[i,1] for i in range(length_dat)]
    probability_damage  =   np.array(probability_damage)
    prob_damage_100     =   np.array([round(probability_damage[i]*100, 4) for i in range(length_dat)])

    ###--------------shift_probability_list--------------------###
    list_shift          =   np.array([int(life_init/table_damage.iloc[i,2]) for i in range(length_dat)])
    ##############################################################
    ###---------------------plot_graph-------------------------###
    ##############################################################

    ###--------------color_and_degraded_list-------------------###
    list_color  =   [list_shift[i]  for i in range(length_dat)] 
    colormap    =   pcolor.LinearSegmentedColormap.from_list("custom_cmap", ["#1D1D1D", "#ffa500"])  
    ###------Degradado_hacia_"#1D1D1D"_hacia_"#00CCDE"---------###
    
    ###-----------building_the_inside_graphic_part-------------###
    plt.figure(facecolor="#1D1D1D", figsize=(7, 4))
    plt.title(f"Damage: {damage_init} vs Life: {life_init}", color="#5AEDA3", fontsize="14")
    plt.gca().set_facecolor("#353535")
    plt.grid(True, linestyle="dashed", color="#696969", alpha=0.5, zorder=1)
    scatter     =   plt.scatter(
                        faces_damage, 
                        prob_damage_100,
                        c=list_color, 
                        cmap=colormap, 
                        s=50, 
                        zorder=2,
                    )

    ###-------------parameters_for_axis_x_and_y----------------###
    plt.xlabel("Possibilities in the dice", color="#5AEDA3", fontsize= "13")
    plt.xticks(faces_damage,color="#5AEDA3")

    plt.ylabel("Damage probability (%)", color="#5AEDA3", fontsize="13")
    plt.yticks(prob_damage_100, color="#5AEDA3")

    ###---------------add_text_point_in_plt--------------------###
    for i in range(length_dat):
        plt.text(
                faces_damage[i], 
                prob_damage_100[i], 
                f"{list_shift[i]}", 
                fontsize=7, va='bottom',  ha='center', 
                color="#ffffff"
        )

    ###----------------------sidebar---------------------------###
    cbar = plt.colorbar(scatter)
    cbar.set_label("Life shifts", color="#5AEDA3", fontsize= "13")
    cbar.ax.tick_params(labelcolor="#5AEDA3")
 
    ###--------------------show_graph--------------------------###
    # plt.savefig("grafica.pdf") 
    plt.savefig("graph_damage.png", dpi=300, bbox_inches="tight")
    # return  plt.show()


###------------------Texting_program-----------------------###
# graph_damage_and_life(4,4,3);


##############################################################
###-------------------Using_program------------------------###
##############################################################
print("Calculo de duracion de turnos en base á los puntos de daño y vida")
dice            =   int(input("Cantidad de dados a lanzar 1-9: "))
damage_init     =   int(input("Daño: "))
life_init       =   int(input("Vida: "))
graph_damage_and_life(damage_init, life_init, dice)


