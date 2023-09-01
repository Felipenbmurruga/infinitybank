from banco import obterConta, banco

def transferir(contaOrig: int,contaDes: int, valor: float) -> None:
    contaOrigem = obterConta(contaOrig)
    contaDestino = obterConta(contaDes)
    if contaOrigem and contaDestino:
        if contaOrigem['saldo'] >= valor:
            contaOrigem['saldo'] -=valor
            contaDestino['saldo'] +=valor
        else:
            print('Saldo Insuficiente!')
    else:
        print('Uma ou mais contas não existem!')

if __name__ == "__main__":
    transferir(1,2,159.99)
    print(banco)