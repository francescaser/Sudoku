import numpy as np
import random

#CREAZIONE MATRICE
sudoku=np.array([[1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6],[2,3,1,6,4,5,8,9,7],[5,6,4,9,7,8,2,3,1],[8,9,7,3,1,2,5,6,4],[3,1,2,5,6,4,9,7,8],[6,4,5,8,9,7,3,1,2],[9,7,8,2,3,1,6,4,5]])
print(sudoku)

#RANDOMIZZAZIONE 
for i in range(81): #numero di volte che desidero cambiare i valori nelle celle

    val1=random.randint(1,9)    #generazione random di un valore tra 1 e 9
    val2=random.randint(1,9)

    for i in range(0,9):        # entro nella riga
        for j in range(0,9):    # entro nella colonna

            if sudoku[i][j]==val2:  
                sudoku[i][j]=val1
                
            elif sudoku[i][j]==val1:
                sudoku[i][j]=val2
print(sudoku)                    #stampa a video


###############COPERTUTA 38 CELLE - livello facile####################
import copy

sudokuCopy = copy.deepcopy(sudoku)
h=0
while h<43:
    for i in range(0,9): 
        for j in range(0,9):
            condizione=random.choice([True,False])
                      
            if sudoku[i][j]!=0 and condizione==True:
                if h<43:
                    sudoku[i][j]=0
                    h+=1
                
print(sudoku)

#####################INSERIMENTO POSIZIONE MOSSA
cont=0
while cont<43:
    iMossa=int(input('Inserire indice di riga '))
    jMossa=int(input('Inserire indice di colonna '))
    
    if (sudoku[iMossa][jMossa]!=0):
        print('ERREORE! Poszione già occupata')
        
    else:
        mossa=input('Inserire il numero')
        if mossa==sudokuCopy[iMossa][jMossa]:
            sudoku[iMossa][jMossa]=mossa
            cont+=1
            print(sudoku)
        else:
            print('Mossa errata')
print('Hai vinto')
        
        