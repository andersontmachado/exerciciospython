'''while True:
    t=int(input('Quer ver a tabuada de qual valor [0 para SAIR]: '))
    print('=-' * 30)
    if t == 0:#implementei o zero para sair,pois é nulo.
        break#vai parar quando digitar o zero
    for c in range(1,11):
        print(f'{t} x {c:2} = {t*c}')
print('PROGRAMA ENCERRADO')
...'''

opção=''
while True:
    t=int(input('Quer ver a tabuada de qual valor: '))
    print('='*35)
    for c in range(1,11):
        print(f'{t} x {c:2} = {t*c}')
    opção=str(input('Quer sair:[S/N]').strip().upper()[0])
    if opção == 'N':
        print('='*35)
    elif opção == 'S':
        print('Corno')
        break
print('FIM')
'''Esse programinha tentei fazer varias vezes algo da cabeça,consegui,ta funcionando..'''














