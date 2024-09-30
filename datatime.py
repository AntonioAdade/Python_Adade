from datetime import date, datetime, time

data = date(2024, 9, 30)
print(data)
print(date.today())

data_hora = datetime(2024, 9, 30)
print(data_hora)
print(datetime.today())

hora = time(14)
print(hora)
print()
print("########################################")

###################################################
#funcção deltatime

from datetime import datetime, timedelta, date, time

#pequeno = 30
#medio = 45
#grande = 60
#data_entrada = datetime.now()
#
#
#print("""
#      
#      digite uma opção abaixo para escolher o tipo de carro
#      [P] Carro pequeno
#      [M] Carro medio
#      [G] Carro grande
#       
#      """)
#
#tipo_carro = str(input("digite sua opção aqui: "))
#
#if tipo_carro == "p":
#    data_estimada = data_entrada + timedelta(minutes=pequeno)
#    print(f"o carro chegou {data_entrada} e ficará pronto as {data_estimada}")
#elif tipo_carro == "m":
#    data_estimada = data_entrada + timedelta(minutes=pequeno)
#    print(f"o carro chegou {data_entrada} e ficará pronto as {data_estimada}")
#else:
#    data_estimada = data_entrada + timedelta(minutes=pequeno)
#    print(f"o carro chegou {data_entrada} e ficará pronto as {data_estimada}")

#########################################################################
#manipulando data a partir de hora

print(date.today() - timedelta(days=1))

resultado = datetime(2024, 9, 30, 16, 2, 0) - timedelta(hours=1)
print(resultado.time()) #o atributo .time serve para retornar apenas as horas da função datetime. Vale para o atributo de data.
print()
print("######################################################")

data_hora_atual = datetime.now()
data_hora_str = "2024-9-30 16:19"
mascara_ptbr = "%d/%m/%Y"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr)) #converte um input formato datetime para outra forma de apresentação.

data_convertida = datetime.strptime(data_hora_str, mascara_en) #converte uma string da data em formato datetime. A mascara precisa ser igual a tipo a ser convertido
print(data_convertida)
print("##################################################################")
print()

#######################################################################
#trabalhando com timezone e biblioteca pytz

import pytz
from datetime import datetime

data2 = datetime.now(pytz.timezone("Europe/Oslo"))
print(data2)

print("####################")

#######################################################################
#trabalhando com timezone sem biblioteca pytz

from datetime import datetime, timedelta, timezone


hora_sp = datetime.now(timezone(timedelta(hours=-3)))
hora_oslo = datetime.now(timezone(timedelta(hours=2)))

print(hora_sp)
print(hora_oslo)

