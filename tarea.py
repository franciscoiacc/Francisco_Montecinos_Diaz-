def calcular_costo_estudios(nombre_paciente):
 
  costo_estudio_nutricion = 10000
  costo_estudio_estetica = 5000
 
  cantidad_estudio_nutricion = int(input(f"{nombre_paciente}, ingrese la cantidad de estudios de nutrición: "))
  cantidad_estudio_estetica = int(input(f"{nombre_paciente}, ingrese la cantidad de estudios de estética: "))
 
  costo_total_sin_descuento = (cantidad_estudio_nutricion * costo_estudio_nutricion) + \
  (cantidad_estudio_estetica * costo_estudio_estetica)
 
  descuento = 0
  if costo_total_sin_descuento > 80000:
    descuento = costo_total_sin_descuento * 0.20
    costo_total_con_descuento = costo_total_sin_descuento - descuento
  else:
    costo_total_con_descuento = costo_total_sin_descuento

  return {
      "nombre": nombre_paciente,
      "estudios_nutricion": cantidad_estudio_nutricion,
      "estudios_estetica": cantidad_estudio_estetica,
      "costo_sin_descuento": costo_total_sin_descuento,
      "descuento": descuento,
      "costo_final": costo_total_con_descuento
  }

cantidad_pacientes = int(input("Ingrese la cantidad de pacientes a atender: "))

for paciente in range(cantidad_pacientes):
  nombre_paciente = input(f"Ingrese el nombre del paciente {paciente + 1}: ")
  informacion_paciente = calcular_costo_estudios(nombre_paciente)
 
  print(f"\nInformación de {informacion_paciente['nombre']}:")
  print(f"Estudios Nutrición: {informacion_paciente['estudios_nutricion']}")
  print(f"Estudios Estética: {informacion_paciente['estudios_estetica']}")
  print(f"Costo sin descuento: ${informacion_paciente['costo_sin_descuento']}")
  print(f"Descuento: ${informacion_paciente['descuento']}")
  print(f"Costo final: ${informacion_paciente['costo_final']}")