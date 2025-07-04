
jogadores = []

while True:
    nome = input('Nome: ')
    partidas = int(input('Partidas: '))
    gols = []

    for i in range(partidas):
        gols.append(int(input(f'  Gols no jogo {i+1}: ')))

    jogadores.append([nome, gols])

    if input('Mais? (s/n): ') != 's':
        break

for i, j in enumerate(jogadores):
    print(f'{i} - {j[0]} - Total: {sum(j[1])} gols')

while True:
    i = int(input('Ver detalhes de qual jogador? (-1 sai): '))
    if i == -1:
        break
    if i < len(jogadores):
        print(f'Jogador: {jogadores[i][0]}')
        for n, g in enumerate(jogadores[i][1]):
            print(f'  Jogo {n+1}: {g} gols')

