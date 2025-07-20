import  numpy   as  np  
import  pandas  as  pd

############################################################
###-----------def_function_damage_and_dodge--------------###
############################################################
def table_damge_dodge( damage_init, dodge_init, probability_dice ):

    ###----------------Import_probability_3D6----------------###
    tabla   =   pd.read_csv(
                    str(probability_dice),  # "probability/Probabilidad_3D6.dat",
                    delimiter   =   ";;",
                    header      =   None,
                    engine      =   "python"
                )

    sum_faces       =   np.array(tabla[0]).reshape(-1,1).flatten()
    probability     =   np.array(tabla[1]).reshape(-1,1).flatten()
    data_length_pro =   len(probability)

    ###---------------------list_dodge-----------------------###
    dodge           =   np.array([ i + dodge_init    for i   in  sum_faces ])

    ###-------------classification_damage_dodge--------------###

    damage_true     =   []
    damage_true_p   =   0

    damage_false    =   []
    damage_false_p  =   0

    relaunch        =   0
    relaunch_p      =   0

    for i   in  range(data_length_pro):
        
        ##------Damage_true------##
        if  damage_init > dodge[i]:
            # print( str(damage_init) + " > " + str(dodge[i]) + " damage true" )
            damage_true.append(sum_faces[i])
            damage_true_p   =   damage_true_p   +   probability[i]

        ##-----Damage_false------##
        elif damage_init < dodge[i]:    
            # print( str(damage_init) + " < " + str(dodge[i]) + " damage false" )
            damage_false.append(sum_faces[i])
            damage_false_p   =   damage_false_p   +   probability[i]

        ##-----Damage=dodge------##
        elif damage_init == dodge[i]:   
            # print( str(damage_init) + " = " + str(dodge[i]) + " relaunch" )
            relaunch    =   sum_faces[i]
            relaunch_p  =   probability[i]


    ###---------------contruction_table_result---------------###
    table_date      =   np.array([
                ["Damage true", str(np.array(damage_true)).replace("]","").replace("[",""), round(damage_true_p*100, 4)],
                ["Damage false", str(np.array(damage_false)).replace("]","").replace("[",""), round(damage_false_p*100, 4)],
                ["Relauch", relaunch, round(relaunch_p*100, 4)]
            ])

    table_date      =   pd.DataFrame(table_date, columns=[" ", "Sum of dice", "Probability (%)"])


    return  table_date

###------------------Testing program---------------------###
# print(table_damge_dodge(4,-1,"probability/Probabilidad_3D6.dat"))


