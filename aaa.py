def sakas_vienadi(teksts):
  teksts= teksts.lower().split()

  if teksts[0][0]==teksts[1][0]:
    return True
  else:
    return False

print(sakas_vienadi("Liela Lama"))
print(sakas_vienadi("Maza Lama"))

