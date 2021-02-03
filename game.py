from models.calcular import Calcular
from time import sleep


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int):
    print('='*30)
    dificuldade: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        print('Você ganhou ', end='')
        if dificuldade == 1:
            pontos += 1
            print('1 ponto')
        elif dificuldade == 2:
            pontos += 2
            print('2 pontos')
        elif dificuldade == 3:
            pontos += 4
            print('4 pontos')
        elif dificuldade == 4:
            pontos += 8
            print('8 pontos')
        print(f'Agora você tem ', end='')
    else:
        print(f'Você ainda tem ', end='')
    if pontos == 1:
        print(f'1 ponto')
    else:
        print(f'{pontos} pontos')

    while True:

        continuar: int = int(input('Deseja continuar o jogo? [1 - sim, 0 - não] '))

        if continuar == 1:
            jogar(pontos)
            break
        elif continuar == 0:
            print()
            print(f'Você fez ', end='')
            if 1 <= pontos < 5:
                print(f'apenas 1 ponto\nVamos lá! Você é melhor do que isso!')
            elif pontos == 0:
                print(f'0 pontos\nNão desanime! Tente de novo!')
            else:
                print(f'{pontos} pontos!')
                if 5 <= pontos < 15:
                    print('Parabéns!! Você conquistou uma medalha de BRONZE!')
                    print('Continue jogando para melhorar sua colocação!')
                elif 15 <= pontos <= 25:
                    print('PARABÉNS!!! Você conquistou uma medalha de PRATA!')
                    print('Será que consegue chegar ao ouro?')
                elif pontos > 25:
                    print('UAU!!! VOCÊ CONSEGUIU A COLOCAÇÃO DE OURO!!!')
                    print('MEUS PARABÉNS!!! VOCÊ É UM ÁS DA MATEMÁTICA!')
            print()
            print('Até a próxima!')
            break
        else:
            print('\033[31mOpção inválida!\033[m')
            sleep(1)


if __name__ == '__main__':
    main()