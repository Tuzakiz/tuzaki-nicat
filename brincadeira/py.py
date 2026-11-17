import os

DUAL = ""
KNOWLEDGE = ""
CONECTIVO = ""
RESPOSTA = 1
EX = ''
while RESPOSTA == 1:
 os.system("cls")
 print("RESPONDE")
 GAJO = str(input("QUEM SERIA O GAJO? \nSeria "))


 if GAJO.lower() == "gemini": DUAL, KNOWLEDGE, CONECTIVO, RESPOSTA = False, 'capacidade', True, 0
 elif GAJO.strip() == "":
      RESPOSTA = 1
 else: DUAL, KNOWLEDGE, CONECTIVO, EX, RESPOSTA = True, 'problemas', False, ' 0', 0


print(f"gajo se achas fixes{', porém ' if CONECTIVO == True else ' mas válido es, póis '}{'não ' if DUAL == False else ''}possuis{EX}", KNOWLEDGE, "de escrever")