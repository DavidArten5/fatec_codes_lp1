import time
state = 0
config_alarme = '1214'
def obter_hora_atual_string():
    tempo_local = time.localtime()
    hora = tempo_local.tm_hour
    minuto = tempo_local.tm_min
    return f"{hora:02d}:{minuto:02d}"


print(obter_hora_atual_string()) 
 print("buzer bip bip bip")
print("alarme configurado para"+config_alarme)

while True:
    if state == 0:
        print(obter_hora_atual_string())              
time.sleep(360)   