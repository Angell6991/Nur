import matplotlib
matplotlib.use("TkAgg") 

import  modules.points_p1_p2    as  ppp
import  matplotlib.pyplot   as  plt
import  matplotlib.colors   as  pcolor
import  numpy   as  np


##############################################################
###-------------------Def_functions------------------------###
##############################################################


def graph_attack_and_dodge( attack_init, dodge_init ):
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
    prob_attack_100     =   [ round(probability_attack[i]*100,4) for i in range(length_dat) ]

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

    ###--------------color_and_degraded_list-------------------###
    list_color_true     =   [round(list_attack_true[i]*100, 4) for i in range(length_dat)] 
    colormap_true       =   pcolor.LinearSegmentedColormap.from_list("custom_cmap", ["#1D1D1D", "#00CCDE"])  
    
    list_color_false    =   [round(list_attack_false[i]*100, 4) for i in range(length_dat)] 
    colormap_false      =   pcolor.LinearSegmentedColormap.from_list("custom_cmap", ["#1D1D1D", "#E53681"])
    
    list_color_relaunch =   [round(list_attack_relaunch[i]*100, 4) for i in range(length_dat)] 
    colormap_relaunch   =   pcolor.LinearSegmentedColormap.from_list("custom_cmap", ["#1D1D1D", "#9370db"])
    ###------Degradado_hacia_"#1D1D1D"_hacia_"#00CCDE"---------###

    ###-----------building_the_inside_graphic_part-------------###
    fig, axs    =   plt.subplots(3, 1, figsize=(10, 15), facecolor="#1D1D1D")

    scatter_0   =   axs[0].scatter(
            faces_attack, prob_attack_100, 
            zorder=2,
            c=list_color_true, 
            cmap=colormap_true, 
            s=50
            )
    scatter_1   =   axs[1].scatter(
            faces_attack, prob_attack_100, 
            zorder=2,
            c=list_color_false, 
            cmap=colormap_false, 
            s=50
            )
    scatter_2   =   axs[2].scatter(
            faces_attack, prob_attack_100, 
            zorder=2,
            c=list_color_relaunch, 
            cmap=colormap_relaunch, 
            s=50
            )

    ###-------------parameters_for_axis_x_and_y----------------###
    for i in range(3):
        axs[i].grid(True, linestyle="dashed", color="#696969", alpha=0.5, zorder=1)
        axs[i].set_facecolor("#353535")
        axs[i].grid(True, linestyle="dashed", color="#ffffff", alpha=0.5)
        axs[i].set_xlabel("Possibilities in the dice", color="#5AEDA3")
        axs[i].set_ylabel("Attack probability (%)", color="#5AEDA3")
        axs[i].xaxis.label.set_color("#5AEDA3")
        axs[i].yaxis.label.set_color("#5AEDA3")
        axs[i].tick_params(axis="x", colors='#5AEDA3')
        axs[i].tick_params(axis="y", colors='#5AEDA3')
        axs[i].xaxis.label.set_size(13)
        axs[i].yaxis.label.set_size(13)  
        axs[i].set_xticks(faces_attack)
        axs[i].set_yticks([ round(probability_attack[i]*100,4) for i in range(length_dat) ])
        axs[i].set_title(f"Attack: {attack_init} vs Dodge: {dodge_init}", color="#5AEDA3", fontsize="14")
    
    plt.tight_layout() 

    ###---------------add_text_point_in_plt--------------------###
    for i in range(length_dat):
        axs[0].text(
                faces_attack[i], 
                prob_attack_100[i], 
                f'{list_color_true[i]}%', 
                fontsize=7, va='bottom',  ha='center', 
                color="#ffffff"
        )

    for i in range(length_dat):
        axs[1].text(
                faces_attack[i], 
                prob_attack_100[i], 
                f'{list_color_false[i]}%', 
                fontsize=7, va='bottom',  ha='center', 
                color="#ffffff"
        )

    for i in range(length_dat):
        axs[2].text(
                faces_attack[i], 
                prob_attack_100[i], 
                f'{list_color_relaunch[i]}%', 
                fontsize=7, va='bottom',  ha='center', 
                color="#ffffff"
        )

    ###----------------------sidebar---------------------------###
    cbar0 = plt.colorbar(scatter_0)  # Para el primer scatter
    cbar1 = plt.colorbar(scatter_1)  # Para el segundo scatter
    cbar2 = plt.colorbar(scatter_2)  # Para el tercer scatter

    # Configurar etiquetas y colores
    cbar0.set_label("Attack true P(%)", color="#5AEDA3", fontsize=13)
    cbar1.set_label("Attack false P(%)", color="#5AEDA3", fontsize=13)
    cbar2.set_label("Attack relauch P(%)", color="#5AEDA3", fontsize=13)

    # Establecer el color de los ticks
    cbar0.ax.tick_params(labelcolor="#5AEDA3")  # Para la barra de color 0
    cbar1.ax.tick_params(labelcolor="#5AEDA3")  # Para la barra de color 1
    cbar2.ax.tick_params(labelcolor="#5AEDA3")  # Para la barra de color 2

    ###--------------------show_graph--------------------------###
    # return  plt.savefig("grafica.pdf") 
    # return  plt.show()
    return  plt.savefig("graph_attack.png", dpi=300, bbox_inches="tight")


###------------------Texting_program-----------------------###
# graph_attack_and_dodge(4,-1);


##############################################################
###-------------------Using_program------------------------###
##############################################################
print("Calculo de probabilidad de exito del ataque en base á los puntos de ataque y esquivar")
atttack_init    =   int(input("Ataque: "))
dodge_init      =   int(input("Esquivar: "))
graph_attack_and_dodge(atttack_init,dodge_init)


