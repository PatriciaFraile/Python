import pandas as pd
from seaborn import load_dataset

datos = {'name':['Marc-André ter Stegen'
, 'Iñaki Peña', 'Joao Cancelo', 'Alejandro Balde','Ronald Araujo','Gavi','Pedri','Fermin Lopez','Sergio Roberto',
'Robert Lewandowksi','Raphinha','Vitor Roque','Joao Felix','Xavi Hernandez'],
'positions':['GoalKeepers','GoalKeepers','Defenders','Defenders','Defenders','Midfields','Midfields','Midfields','Midfields','Forwards','Forwards',
             'Forwards','Forwards','Coaching Staff']}

base = pd.DataFrame(datos)

find = "GoalKeepers"
goalKeepers =  base[base['positions']==find]
print(goalKeepers)

find2 = "Defenders"
defenders =  base[base['positions']==find2]
print(defenders)

find3 = "Midfields"
midfields =  base[base['positions']==find3]
print(midfields)

find4 = "Forwards"
forwards =  base[base['positions']==find4]
print(forwards)

find5 = "Coaching Staff"
coaching =  base[base['positions']==find5]
print(coaching)


writer = pd.ExcelWriter('players.xlsx')

base.to_excel(writer,sheet_name='player', index= False)

goalKeepers.to_excel(writer,sheet_name='player', startrow=1, startcol=len(base.columns)+1, index=False)

defenders.to_excel(writer,sheet_name='player', startrow=1, startcol=len(base.columns)+4, index=False)

midfields.to_excel(writer,sheet_name='player', startrow=1, startcol=len(base.columns)+7, index=False)

forwards.to_excel(writer,sheet_name='player', startrow=1, startcol=len(base.columns)+10, index=False)

coaching.to_excel(writer,sheet_name='player', startrow=1, startcol=len(base.columns)+13, index=False)



writer.close()