import  fractions   as  fc
import  numpy   as  np  
import  pandas  as  pd

############################################################
###-----------def_function_attack_and_dodge--------------###
############################################################
def table_attack_base_and_dodge( attack_init, dodge_init, probability_dice ):

    ###----------------Import_probability--------------------###
    tabla   =   pd.read_csv(
                    str(probability_dice),  # "probability/Probabilidad_3D6.dat",
                    delimiter   =   ";;",
                    header      =   None,
                    engine      =   "python"
                )

    tabla_x         =   np.array(tabla[0])
    tabla_y         =   np.array(tabla[1])
    sum_faces       =   [ int(i) for i in tabla_x ]     
    probability     =   [ float(fc.Fraction(i)) for i in tabla_y ]
    data_length_pro =   len(probability)


    ###---------------------list_dodge-----------------------###
    dodge           =   np.array([ i + dodge_init    for i   in  sum_faces ])

    ###-------------classification_attack_dodge--------------###

    attack_true     =   []
    attack_true_p   =   0

    attack_false    =   []
    attack_false_p  =   0

    relaunch        =   0
    relaunch_p      =   0

    for i   in  range(data_length_pro):
        
        ##------Damage_true------##
        if  attack_init > dodge[i]:
            attack_true.append(sum_faces[i])
            attack_true_p   =   attack_true_p   +   probability[i]

        ##-----Damage_false------##
        elif attack_init < dodge[i]:    
            attack_false.append(sum_faces[i])
            attack_false_p   =   attack_false_p   +   probability[i]

        ##-----Damage=dodge------##
        elif attack_init == dodge[i]:   
            relaunch    =   sum_faces[i]
            relaunch_p  =   probability[i]
    

    ###---------------contruction_table_result---------------###
    table_date      =   np.array([
                ["Attack true", str(np.array(attack_true)).replace("]","").replace("[",""), round(attack_true_p*100, 4)],
                ["Attack false", str(np.array(attack_false)).replace("]","").replace("[",""), round(attack_false_p*100, 4)],
                ["Relauch", relaunch, round(relaunch_p*100, 4)]
            ])

    table_date      =   pd.DataFrame(table_date, columns=[f"Dodge init = {dodge_init} ", "Sum of dice for dodge", "Probability (%)"])
    
    return  table_date


############################################################
###---------def_function_attack_neto_and_dodge-----------###
############################################################
def table_attack_neto_and_dodge( attack_init, dodge_init, p, probability_dice ):

    ###----------------Import_probability--------------------###
    tabla   =   pd.read_csv(
                    str(probability_dice),  # "probability/Probabilidad_3D6.dat"
                    delimiter   =   ";;",
                    header      =   None,
                    engine      =   "python"
                )

    tabla_x         =   np.array(tabla[0])
    tabla_y         =   np.array(tabla[1])
    sum_faces       =   [ int(i) for i in tabla_x ]     
    probability     =   [ float(fc.Fraction(i)) for i in tabla_y ]
    data_length_pro =   len(probability)


    ###---------------------list_attack----------------------###
    attack          =   np.array([ i + attack_init    for i   in  sum_faces ])

    ###-------------classification_attack_dodge--------------###

    table_attack    =   np.array([
                        str(round(probability[p]*100, 4)), 
                        str(sum_faces[p]), str(attack_init), 
                        str(attack[p])
                        ])
    
    table_attack    =   pd.DataFrame( 
                            [table_attack], columns=["Probability of Attack", "Sum of dice for attack", "Attack init", "Attack final"]
                        )
        

    return  table_attack


############################################################
###--------------def_function_length_data----------------###
############################################################
def length_data( probability_dice ):

    ###----------------Import_probability--------------------###
    tabla   =   pd.read_csv(
                    str(probability_dice),  # "probability/Probabilidad_3D6.dat"
                    delimiter   =   ";;",
                    header      =   None,
                    engine      =   "python"
                )

    tabla_x         =   np.array(tabla[0])
    tabla_y         =   np.array(tabla[1])
    data_length_pro =   len(tabla_y)

    return  data_length_pro


###------------------Testing program---------------------###
# print(table_attack_base_and_dodge(4,-1,"probability/Probabilidad_3D6.dat"))
# print(table_attack_neto_and_dodge(4,-1, 0,"probability/Probabilidad_3D6.dat"))
# print(length_data("probability/Probabilidad_3D6.dat"))


