""" EUcsatlakozas.txt
Ausztria;1995.01.01
"""


with open ("EUcsatlakozas.txt" , "r" , encoding = "latin2") as f:
  lista = []
  for sor in f:
    lista.append(sor.strip().split(";"))


#3.feladat   
eu_államok_száma_2018 = len(lista)

print(f'3.feladat; EU tagállamainak száma : {eu_államok_száma_2018}db ')

#4.feladat     
számláló = 0
for orszag , datum in lista:
  if datum[0:4] == "2007":
    számláló += 1
print(f'4.feladat: 2007-ben {számláló} ország csatlakozott' )

#5.feladat
for orszag , datum in lista:
  if orszag == "Magyarország":
    print(f'5feladat: Mgyarország cstlakozásának dátuma: {datum}')


#6.feladat
számláló = 0

for orszag , datum in lista:
  if datum[5:7] == "05" :
    számláló += 1

if számláló > 0 :
  print("6.feladat: Májusban volt csatlakozás!")

else:
  ("6.feladat: Májusban nem volt csatlakozás!")

#7.feladat
utolsó_dátum = ""
for orszag, datum in lista:
  if utolsó_dátum < datum:
    utolsó_dátum = datum
    utolsó_orszag = orszag
print(f'7.feladat: Legutoljára csatlakozott ország : {utolsó_orzság}')

cnt = collections.Counter()
for orszag , datum in lista:
  cnt[datum[0:4]] += 1
print('8.feladat: Statisztika')
for év, darab in cnt.items():
  print(f'   {év} - {darab} ország')
