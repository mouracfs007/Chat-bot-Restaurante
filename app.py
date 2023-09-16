import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, os nossos pratos de hoje são: File de Frango à parmegiana: R$15,00 / Bifé à milanesa R$18,00 / Escondidinho de frango: R$11,00 /Churrasquinho: R$20,00 / Massas: Lasanha ou Espaguete: R$8,00.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, Lasanha ou Espaguete são as promoções de hoje. Quer conferir os preços? digite: "1".{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, as formas de pagamento são: Dinheiro / Cartão de crédito ou débito / Pix / transferência bancária comum / cashback-eat [caso atinja o nível 100]{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}, fique ligado, pois aqui no Restaurante ComiMermo, temos várias promoções durante a semana e inclusive durante o ano. Com o sistema de "cashback-eat" nós trazemos à você cliente fiel, descontos, e até mesmo uma "troca" de cashback-eat por comida de forma totalmente gratuita, caso atinja o nível 100 de cashback-eat.{os.linesep}')
    else:
        print('Por favor, digite apenas 1, 2, 3 ou 4 para prosseguir com o atendimento !')

def start():
    # Apresentar o chatbot
    print('Olá! Bem-vindo ao Restaurante ComiMermo')
    # Pedir o nome da pessoa
    nome = input('Digite o seu nome: ')
    # Pedir o e-mail
    email = input('Digite o seu e-mail: ')
    
    while True:
        # Oferecer o menu de opções
        print(f'\n O que você gostaria de pedir hoje em nosso cardápio? \n {os.linesep} [1] - Consulte os nossos pratos de hoje!{os.linesep} [2] - Promoções de hoje ! {os.linesep} [3] - Consultar formas de pagamento {os.linesep} [4] - Saiba tudo sobre o cashback-eat para trocar por descontos')
        resposta = input('\n Digite o número da opção desejada (1, 2, 3 ou 4) ou digite "sair" para encerrar: ')
        
        if resposta.lower() == 'sair':
            break
        
        # Processar a resposta enviada
        processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()
