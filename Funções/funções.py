# Criando funções usando outras funções

# Funções com número variável de argumentos
def printVarInfo( arg1, *vartuple ):
    # Imprimindo o valor do primeiro argumento
    print("O parâmetro passado foi: ", arg1)

    # Imprimindo o valor do segundo argumento
    for item in vartuple:
        print("O parâmetro passado foi: ", item)
    return;
 # Fazendo chamada à função usando apenas 1 argumento
printVarInfo(10)

printVarInfo('Chocolate', 'Morango', 'Banana')
