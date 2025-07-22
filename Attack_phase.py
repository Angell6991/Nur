import  modules.attack_and_dodge    as  ad


###-------------------input_data---------------------------###
print("Calculo de probabilidad para esquivar en base al ataque")
attack_init     =   int(input("Ataque: "))
dodge_init      =   int(input("Esquivar: "))


###-------------------write_result-------------------------###

with    open(f"Tabla_attack[{attack_init}]_dodge[{dodge_init}].md", "w")   as  f:

    for i   in range(ad.length_data("modules/probability/Probabilidad_3D6.dat")):

        attack_table    =   0
        dodge_table     =   0

        attack_table    =   ad.table_attack_neto_and_dodge(attack_init, dodge_init, i, "modules/probability/Probabilidad_3D6.dat")
        attack_neto     =   int(attack_table.iloc[0, 3])
        dodge_table     =   ad.table_attack_base_and_dodge(attack_neto, dodge_init, "modules/probability/Probabilidad_3D6.dat")


        f.write(attack_table.to_markdown(index=False))
        f.write("\n" + "\n")
        f.write(dodge_table.to_markdown(index=False))
        f.write("\n" + "\n" + "\n")


###---------------------------------------------------------###
# with    open(f"Tabla_attack[{attack_init}]_dodge[{dodge_init}].md", "w")   as  f:
#     f.write("Daño: " + str(damage_init) + "\n" + "\n" + "Esquivar: " + str(dodge_init) + "\n" + "\n")
#     f.write(table_result.to_markdown(index=False))


