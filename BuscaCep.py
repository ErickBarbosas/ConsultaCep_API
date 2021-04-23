import requests 
import os 

def main():
    print('*****************************************')
    print('*********      Consulta Cep     *********')
    print('*****************************************')
    print('\n')

    cep=input('Digite o CEP para consultar: ')

    if len(cep)!=8:
        print('Cep Invalido')
        exit()
        
    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    retorno = request.json()

    os.system('cls') or None
    if 'erro' not in retorno:

        print('\n\n\CEP Localizado Com Sucesso\n')
        print('CEP: {}'.format(retorno['cep']))
        print('Rua: {}'.format(retorno['logradouro']))
        print('Bairro: {}'.format(retorno['bairro']))
        print('Cidade: {}'.format(retorno['localidade']))
        print('UF: {}'.format(retorno['uf']))
        print('DDD: {}'.format(retorno['ddd']))
    else:
        print('\n\nCep Invalido\n\n')

    resposta = int(input('Deseja fazer uma Nova Busca?\n\n1-Sim\n2-Não\n\nR: '))

    if resposta == 1:
        main()
    else:
        exit()

if __name__ == '__main__':
    main()


