print('Quizz de perguntas e respostas sobre os clubes brasileiros! Escolha a letra correta e no final verá sua nota!')
print()

respostas_certas = 0
quiz_clubes = {
    'Pergunta 1': {
        'pergunta': 'Qual foi o primeiro clube brasileiro a ganhar uma libertadores?',
        'respostas': {'a': 'Santos', 'b': 'Flamengo', 'c': 'Grêmio', 'd': 'São Paulo',},
        'resposta_certa': 'a',
    },
    'Pergunta 2': {
        'pergunta': 'Qual foi o primeiro clube brasileiro a ser tri campeão da libertadores?',
        'respostas': {'a': 'Santos', 'b': 'Palmeiras', 'c': 'São Paulo', 'd': 'Grêmio',},
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Qual clube do RJ foi o primeiro a ganhar Libertadores?',
        'respostas': {'a': 'Vasco', 'b': 'Fluminense', 'c': 'Botafogo', 'd': 'Flamengo',},
        'resposta_certa': 'd',
    },
    'Pergunta 4': {
        'pergunta': 'Quantos titulos na decada de 90 o Palmeiras ganhou?',
        'respostas': {'a': '10', 'b': '7', 'c': '9', 'd': '11',},
        'resposta_certa': 'c',
    },
    'Pergunta 5': {
        'pergunta': 'Qual clube revelou o Romario?',
        'respostas': {'a': 'Vasco', 'b': 'Fluminense', 'c': 'Flamengo', 'd': 'Olaria',},
        'resposta_certa': 'a',
    },
    'Pergunta 6': {
        'pergunta': 'Qual clube brasileiro tem a maior torcida?',
        'respostas': {'a': 'São Paulo', 'b': 'Flamengo', 'c': 'Corinthians', 'd': 'Vasco',},
        'resposta_certa': 'b',
    },
    'Pergunta 7': {
        'pergunta': 'Qual destes clubes nunca foi rebaixado?',
        'respostas': {'a': 'Internacional', 'b': 'Palmeiras', 'c': 'Corinthians', 'd': 'Santos',},
        'resposta_certa': 'd',
    },
    'Pergunta 8': {
        'pergunta': 'Quantos HatTrick Pelé fez em sua carreira?',
        'respostas': {'a': '95', 'b': '89', 'c': '92', 'd': '96',},
        'resposta_certa': 'c',
    },
}

for pergunta_chave, pergunta_valor in quiz_clubes.items():
    print(f'{pergunta_chave}: "{pergunta_valor["pergunta"]}"')
    print('')
    for resposta_chave, resposta_valor in pergunta_valor['respostas'].items():
        print(f'[{resposta_chave}]: {resposta_valor}')

    resposta = input('Escolha a letra correta: ')

    if resposta == pergunta_valor['resposta_certa']:
        print('Resposta certa!')
        respostas_certas += 1
    else:
        print('Resposta errada!')

    print()

qt_perguntas = len(quiz_clubes)
porcentagem_corretas = respostas_certas / qt_perguntas * 100

print(f'Você acertou {respostas_certas} perguntas.')
print(f'Você acertou {porcentagem_corretas:.1f}% no quizz') 

if porcentagem_corretas >= float(80):
    print('Nota A, Parabens!')
if porcentagem_corretas < float(80) and porcentagem_corretas >= float(60):
    print('Nota B')
if porcentagem_corretas < float(60) and porcentagem_corretas > float(30):
    print('Nota C')
if porcentagem_corretas <= float(30):
    print('Nota D, tá reprovado =(')