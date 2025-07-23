import  fractions   as  fc
import  numpy   as  np  
import  pandas  as  pd

############################################################
###-------------def_function_for_palyer_01---------------###
############################################################
def table_palyer_01( point_init, probability_dice ):

    ###----------------Import_probability--------------------###
    tabla   =   pd.read_csv(
                    str(probability_dice),  # "probability/Probabilidad_3D6.dat",
                    delimiter   =   ";;",
                    header      =   None,
                    engine      =   "python"
                )

    tabla_x         =   np.array(tabla[0])
    tabla_y         =   np.array(tabla[1])
    sum_faces       =   np.array([ int(i) for i in tabla_x ])     
    probability     =   np.array([ float(fc.Fraction(i)) for i in tabla_y ])
    data_length_pro =   len(probability)
   
    ###------------list_sum_face_plus_point_init-------------###
    sum_faces_plus_point_init   =   np.array([ i + point_init    for i   in  sum_faces ])

    ###---------Construction_table_the_probability-----------###
    table_player_01 =   np.array([sum_faces, probability, sum_faces_plus_point_init])
    table_player_01 =   pd.DataFrame({
                            "sum_faces": sum_faces, 
                            "probability": probability, 
                            "sum_faces_plus_point_init": sum_faces_plus_point_init
                        })    

    return  table_player_01


############################################################
###-------------def_function_for_palyer_02---------------###
############################################################
def table_palyer_02( point_init, points_player_01, probability_dice ):

    ###----------------Import_probability--------------------###
    tabla   =   pd.read_csv(
                    str(probability_dice),  # "probability/Probabilidad_3D6.dat",
                    delimiter   =   ";;",
                    header      =   None,
                    engine      =   "python"
                )

    tabla_x         =   np.array(tabla[0])
    tabla_y         =   np.array(tabla[1])
    sum_faces       =   np.array([ int(i) for i in tabla_x ])     
    probability     =   np.array([ float(fc.Fraction(i)) for i in tabla_y ])
    data_length_pro =   len(probability)

    ###------------list_sum_face_plus_point_init-------------###
    sum_faces_plus_point_init   =   np.array([ i + point_init    for i   in  sum_faces ])

    ###----------classification_probability_win--------------###
    win_true     =   []
    win_true_p   =   0

    win_false    =   []
    win_false_p  =   0

    relaunch        =   0
    relaunch_p      =   0

    for i   in  range(data_length_pro):
        
        ##--------Win_true_player_01-------##
        if  points_player_01 > sum_faces_plus_point_init[i]:
            win_true.append(sum_faces[i])
            win_true_p   =   win_true_p   +   probability[i]

        ##-----Damage_false_player_01------##
        elif points_player_01 < sum_faces_plus_point_init[i]:    
            win_false.append(sum_faces[i])
            win_false_p   =   win_false_p   +   probability[i]

        ##----------Damage=dodge-----------##
        elif points_player_01 == sum_faces_plus_point_init[i]:   
            relaunch    =   sum_faces[i]
            relaunch_p  =   probability[i]
    
    ###---------------contruction_table_result---------------###
    table_player_02 =   np.array([
                            ["Win true P_01", str(np.array(win_true)).replace("]","").replace("[",""), round(win_true_p, 4)],
                            ["Win false P_01", str(np.array(win_false)).replace("]","").replace("[",""), round(win_false_p, 4)],
                            ["Relauch", relaunch, round(relaunch_p, 4)]
                        ])

    table_player_02  =   pd.DataFrame(table_player_02, columns=[" ", "Sum of dice for dodge", "Probability"])
    
    return  table_player_02


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
# print(table_palyer_01(4, "probability/Probabilidad_3D6.dat"))
# print(table_palyer_02(-1 ,4 , "probability/Probabilidad_3D6.dat"))
# print(length_data("probability/Probabilidad_3D6.dat"))


