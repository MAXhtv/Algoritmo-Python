import scipy
from scipy import stats
import numpy as np

matrix=np.array([[8,0,3,4,6],[5,6,1,8,9],[8,0,0,5,10]])
newuser=[8,0,2,3,0]

watchNewUser=[]

for n in newuser:
	if n > 0:
		watchNewUser.append(0)
		
	if n==0:
		watchNewUser.append(1)
print(watchNewUser)


nameSeries=['Round 6','A invocação do Mal','9 Desconhecidos', 'You','La Casa de Papel']

similarity=[0]*3
for i in range(0,3):
	temp=matrix[i, :]
	
	print(i, temp)
	
	tempUser=[t for n, t in zip(newuser, temp) if n !=0]
	tempnewuser=[n for n in newuser if n !=0]
	
	print('user: ',i)
	print(tempUser, tempnewuser)
	
	similarity[i]=scipy.stats.pearsonr(tempUser, tempnewuser)[0]
	
nota_peso=np.zeros((3,5))

for nUser in range(3):
	for nSeries in range(5):
		nota_peso[nUser][nSeries]=watchNewUser[nSeries]*matrix[nUser][nSeries]*similarity[nUser]

print(" ")
print(nota_peso)
print(" ")

notasAcumulent=np.sum(nota_peso.T,axis=1)
print(notasAcumulent)

temp_peso=nota_peso
temp_peso[nota_peso>0]=1
print(temp_peso)

temp_similaridade=np.zeros((3,5))
for nUser in range(3):
	for nSeries in range(5):
		temp_similaridade[nUser][nSeries]=temp_peso[nUser][nSeries]*similarity[nUser]
		
print(temp_similaridade)

similarityAcumulent=np.sum(temp_similaridade.T,axis=1)
print(similarityAcumulent)

notaEnd=[0]*5

for nSeries in range(5):
	if(similarityAcumulent[nSeries]>0):
		notaEnd[nSeries]=notasAcumulent[nSeries]/similarityAcumulent[nSeries]
		
	else:
		notaEnd[nSeries]=0
		
print(" ")
print(notaEnd)
print(" ")

nAssistidos=sum(watchNewUser)

notasOrdenByIndex=sorted(range(len(notaEnd)),key=notaEnd.__getitem__)[::-1][0:nAssistidos]
print(notasOrdenByIndex)

for i in notasOrdenByIndex:
	print(nameSeries[i],'nota:',notaEnd[i])

indiceMax=np.argmax([notaEnd[i] for i in notasOrdenByIndex])
recomendation=nameSeries[notasOrdenByIndex[indiceMax]]
print("\nO novo usuario deveria assistir: ",recomendation,"pois, provavelmente vai gostar mais.")