import time
state = 0
config_alarme = '1748'
aciona_buzzer= False
def obter_hora_atual_string():
    tempo_local = time.localtime()
    hora = tempo_local.tm_hour
    minuto = tempo_local.tm_min
    return f"{hora:02d}{minuto:02d}"
    hora1 = str(hora) 
    minuto1 = str(minuto)

print(hora1 + ":"+ minuto1)
if aciona_buzzer ==True:
    print("buzer bip bip bip")

print("alarme configurado para"+config_alarme)

while True:
    if state == 0:
        hora_ataual= obter_hora_atual_string()
        if hora_ataual == config_alarme:
            aciona_buzzer= True
    else:
        aciona_buzzer= False
def sleep()
