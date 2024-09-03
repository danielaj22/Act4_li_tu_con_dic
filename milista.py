# ejemplo de uso de lista 
misnovios= ["agripino", "anastacio", "mario"]
misnumeros=["666", "777","10"]
# mostrando mis novios 
print(misnovios)
# mostrando mis numeros raros 
print(misnumeros)
print("-----accediendo a los elemnetos de la lista------")
print(misnovios[-2])
if "melanie" in misnovios:
  print("si, 'melanie' esta en la lista de mis novios")
else:
  print("chale no eres mi novio")
print("numero de novios")
Nnovios=len(misnovios)
print(f"numero de novios = {Nnovios}")
print("ciclo for en listas")
posicion=0
for medianaranja in misnovios:
  print(posicion," ",medianaranja)
  posicion=posicion+1