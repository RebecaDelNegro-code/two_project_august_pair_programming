'''
como fazer um bolo;
Bom para fazer um bolo, voce precisa de alguns ingredientes basicos, como farinha de trigo, ovos, leite, açucar,
cacau em po, fermento em po e manteiga. Primeniro, voce deve preaquecer o forno a 180 graus celsius. 
Em seguida, misture os ingredientes secos em uma tigela, em seguida coloque os ingredientes
liquidos e misture ate a massa do bolo ficar cremosa. Unte a forma que voce ira ultilizar  para fazer o bolo
em seguida coloque a forma no forno e espere o bolo ficar pronto entre 30 a 45 min. Apos o bolo ficar pronto
tire da forma e espere esfriare esta pronto.


'''
def fazer_bolo(tipo_bolo):
    print('🎂 Fazendo bolo - Sistema simples🎂')
    print('1. pegue os seguintes ingredientes')
    print('2. ovos, farinha de trigo, fermento em po, leite, açucar, cacau em po, fermento em po e manteiga ')
    print('3. pegue uma tigela e quebre o ovo')
    print('4. em seguida coloque todos os ingredientes secos e miesture')
    print('5. coloque os ingredientes liquidos')
    print('6. misture bem ate a massa fica cremosa')
    print('7. pegue uma forma e unte ela com margarina')
    print('8. coloque a massa na forma')
    print('9. coloque o bolo no forno em 180 graus celius')
    print('10. espere o bolo e em seguida tire da forma e pronto')

    if tipo_bolo.lower() == 'chocolate':
      resultado = 'bolo sabor chocolate'
    else:
      resultado = 'bolo sem sabor'
     
    return resultado  

meu_cafe = fazer_bolo('chocolate')
print(f'meu cafe esta: {meu_cafe}')