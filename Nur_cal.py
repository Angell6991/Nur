import  modules.damage_and_dodge    as  dad

###-------------------input_data---------------------------###
print("Calculo de probabilidad para esquivar en base al daño")
damage_init     =   int(input("Daño: "))
dodge_init      =   int(input("Esquivar: "))
table_result    =   dad.table_damge_dodge(damage_init, dodge_init, "modules/probability/Probabilidad_3D6.dat")

###-------------------write_result-------------------------###
with    open("Tabla_result.md", "w")   as  f:
    f.write("Daño: " + str(damage_init) + "\n" + "\n" + "Esquivar: " + str(dodge_init) + "\n" + "\n")
    f.write(table_result.to_markdown(index=False))


