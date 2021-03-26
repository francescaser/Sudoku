# risolutore.py

def risolvi(matrice): 
    ''' Funzione che abilita la selezione delle caselle vuote per l'inserimento della cifra/mossa,
        che controlla se la cifra inserita è valida -richiamando la funzione validata-,
        e che, se la cifra non dovesse essere valida, restituisce la cella vuota'''

    find = find_empty(matrice)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if validata(matrice, i, (row, col)):
            matrice[row][col] = i

            if risolvi(matrice):
                return True

            matrice[row][col] = 0

    return False


def validata(matrice, num, pos): 
    '''Funzione per il controllo di validità della mossa inserita su riga, colonna e box  '''

    # Verifica che nella riga non sia già presente il numero inserito
    for i in range(len(matrice[0])):
        if matrice[pos[0]][i] == num and pos[1] != i:
            return False

    # Verifica che nella colnna non sia già presente il numero inserito
    for i in range(len(matrice)):
        if matrice[i][pos[1]] == num and pos[0] != i:
            return False

    # Verifica che nel box 3x3 non sia già presente il numero inserito
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if matrice[i][j] == num and (i,j) != pos:
                return False

    return True

def find_empty(matrice):
    ''' Funzione per l'indivuazione delle caselle riempibili:
        restituisce la posizione della cella vuota '''
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j] == 0:
                return (i, j)  # riga, colonna

    return None
