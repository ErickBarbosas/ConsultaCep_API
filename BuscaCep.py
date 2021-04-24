import requests
import os

def main():
    os.system('cls') or None
    print('*****************************************')
    print('*********      Consulta Cep     *********')
    print('*****************************************')
    print('\n')

    cep=input('Digite o CEP para consultar: ')

    if len(cep)!=8:
        os.system('cls') or None
        print('Cep Invalido')
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    retorno = request.json()


    if 'erro' not in retorno:
        os.system('cls') or None
        print('****************************************')
        print('****** CEP Localizado Com Sucesso ******')
        print('****************************************\n')
        print(' CEP: {}'.format(retorno['cep']))
        print(' Rua: {}'.format(retorno['logradouro']))
        print(' Bairro: {}'.format(retorno['bairro']))
        print(' Cidade: {}'.format(retorno['localidade']))
        print(' UF: {}'.format(retorno['uf']))
        print(' DDD: {}'.format(retorno['ddd']))
        print('\n****************************************')
    else:
        os.system('cls') or None
        print('\n\nCep Invalido\n\n')

    resposta = int(input('\nDeseja fazer uma Nova Busca?\n\n1-Sim\n2-Não\n\nR: '))

    if resposta == 1:
        main()
    else:
        os.system('cls') or None
        exit()

if __name__ == '__main__':
    main()