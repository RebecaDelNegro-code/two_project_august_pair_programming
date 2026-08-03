'''
javascript object notation (JSON) 
é um formato leve de troca de dados,
fácil para humanos lerem e escreverem,
e fácil para máquinas analisarem e
gerarem. Ele e baseado em um subconjunto
da linguagem de programaçâo JavaScript
mas é independente de linguagem, com muitos
idiomas de programaçâo incluindo código para
gerar e analisar JSON




'''

import json
import os

dados_brutos = """
Ivan Silva;40 anos;02899-000;947541;ivanpaulino@mail.com
Beatriz Vitoria;30 anos;057193-000;978786;beavitoria@mail.com
Eric Renan;17 anos;089880-100;98799;ericrenan@gmail.com
Miguel Mendes;17 anos;05861-260;976767;migueldiasmendes9@gmail.com
Carlos Pereira; 15 anos; 09876-000; 948867; carlospereira@gmail.com
Herique Augusto;17 anos;05857-030;96105;henriqueaugusto@mail.com
Otavio Sebastiao;14 anos;09731-000;976431;otaviosebastiao@mail.com
Yasmin Santos;17 anos;09876-000;971123;yasminssantos@gmail.com
Livia Giffony;14 anos;09162-0000;989123;liviagiffony@gmail.com
Sophia Neris;14 anos;05790410-000;998922;sophiasilva@mail.com
Anna Clara;14 anos;05799910-000;91478;annaclarasilva@mail.com
Nicole Mendes;14 anos;06357-000;897456;nicolemendea099@gmail.com
Nicollas Tegas;15 anos;048394-909;931841;nicollastegas@mail.com
Joao Vitor;15 anos;0579110; joaovitoralvesdecarvalho6@gmail.com
Luane Santana;17 anos;09752-000;976352;luanesantana@mail.com
Ivan Silva;40 anos;02899-000;947541;ivanpaulino@mail.com
Beatriz Vitoria;30 anos;057193-000;978786;beavitoria@mail.com
Gabriel Aquino;15 anos;09876-000;995899;kaiserhzx@gmail.com
Isabelly Marcelino;15 anos;05883-280;948630926;orlandoisabelly5@gmail.com
Filipe Luis;18 anos;09564-000;963263;filipeluissouzasilva100@gmail.com
Leonardo Sales Marques;14 anos;05867-000;940182;leozinnxd00@gmail.com
Gabriel Carvalho;18 anos;06789-000;94967;gabriel.c.silva74@gmail.com
Giovana Medeiros;15 anos;09876-000;988942;giiovana.medeiiros@gmail.com
Kauan Cavalcanti;16 anos;05757-110;923456;kauancavalcanti13@gmail.com
Maria Eduarda Verissimo;15 anos;05957-411;930172;mariaeverissimo24@gmail.com
Nicolas santana;19 anos;05795-010;980853;nicolasdml02@gmail.com
Arthur Cordeiro;15anos;04872-000;983945;arthur.spike2012@gmail.com
Rafael Aquino;15 anos;06742-000;998381;fritz.ff.cl4ud14@gmail.com
Gustavo Gonçalves;18 anos;04567-000;962127;gustavogoncalves0228@gmail.com
Lucas Prates;15 anos;05633-000;995804;luccas.pssilva@gmail.com
Victor Oliveira;17 anos;05866-110;991341;felixcandido50@gmail.com
Leandro Do Carmo;15 Anos;05792-000;994523;LeandroCarmoXav@gmail.com
Daniel de Jesus;15 anos;05792-000;978082;dandejesus74@gmail.com
Ellis de Oliveira;15anos;06775-300; 99815;ellisrosaoliveira@gmail.com
Manuella Andrade;15 anos;05498-450;998792;santsandrade0@gmail.com
Gustavo Silva;15 Anos;05795-300;gustavo000923.sme@gmail.com
Diogo Santos;17 anos,06099-000;diogosantos@mail.com
Yasmim Vitoria; 16 anos; 05792-050; mimvitoriasantossilva
Felipe mendes;15 anos;01529-230;felipemendes@mail.com
Livia Borelli;15 anos; 05791-080; liliborelli19@gmail.com
Nathanael Dias Cruz;15 anos;05763-420;nathanaeldias845@gmail.com
Ester Furukawa, 16 anos, 03991-000, esterfurukawa@gmail.com
Isaque da Silva Sena;15 anos;05763-490 isaquesena@mail.com
Pedro Henrique; 16 anos; 05851-290; pedroflausino949@gmail.com
Isabelly Silva Castelo;17 anos;00000-000;isabellysilva@mail.com
Maria Eduarda Mello; 16 anos;05129-376; dduda.rmello@gmail.com
Sarah Santos, 15 anos, 09658-000, sarahsantos@gmail.com
Matheus Santos; 15 anos; 12300-000; Matheussantos@mail.com
Igor Freitas; 15 anos;08965-876;igorgomes@gmail.com
Beatriz Araujo; 18 anos; 05762-000; beatrizsouzaaraujo173@gmail.com
Ivan Silva;40 anos;02899-000;947541;ivanpaulino@mail.com
Beatriz Vitoria;30 anos;057193-000;978786;beavitoria@mail.com
Eric Renan;17 anos;089880-100;98799;ericrenan@gmail.com
Miguel Mendes;17 anos;05861-260;976767;migueldiasmendes9@gmail.com
Carlos Pereira; 15 anos; 09876-000; 948867; carlospereira@gmail.com
Herique Augusto;17 anos;05857-030;96105;henriqueaugusto@mail.com
Otavio Sebastiao;14 anos;09731-000;976431;otaviosebastiao@mail.com
Yasmin Santos;17 anos;09876-000;971123;yasminssantos@gmail.com
Livia Giffony;14 anos;09162-0000;989123;liviagiffony@gmail.com
Sophia Neris;14 anos;05790410-000;998922;sophiasilva@mail.com
Anna Clara;14 anos;05799910-000;91478;annaclarasilva@mail.com
Nicole Mendes;14 anos;06357-000;897456;nicolemendea099@gmail.com
Nicollas Tegas;15 anos;048394-909;931841;nicollastegas@mail.com
Joao Vitor;15 anos;0579110; joaovitoralvesdecarvalho6@gmail.com
Luane Santana;17 anos;09752-000;976352;luanesantana@mail.com
"""

nome_arquivo = 'arquivos_jovens.json' 

def carrega_processa_dados():
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados

listas_dados = []
emails_dados = set()

for linha in dados_brutos.strip().split('\n'):
    partes = linha.split(',')
    continue

linha_limpa = linha.replace(',',';')
partes = [p.split() for p in linha_limpa.split(';') if p.strip()]

if len(partes) >= 4:
    emails = paartes[-1]  
     
      if email in emails_dados:
                continue
            emails_dados.add(email)

            aluno = {
                "Nome completo": partes[0],
                "idade": partes[1],
                "CEP": partes[2],
                "ResgMatr": partes[3] if len(partes) == 5 else "N/A",
                "E-Mail": email,
            }
            lista_dados.append(aluno)

    return lista_dados


def salvar_json(dados):
    """Salva a lista atualizada no arquivo JSON."""
    with open(NOME_ARQUIVO, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=2)


def cadastrar_novo_aluno(lista_alunos):
    """Permite a inserção interativa de novos alunos pelo usuário."""
    print("\n--- CADASTRO DE NOVO ALUNO ---")
    nome = input("Nome completo: ").strip()
    idade = input("Idade (ex: 15 anos): ").strip()
    cep = input("CEP: ").strip()
    resg_matr = input("ResgMatr : ").strip()
    email = input("E-Mail: ").strip()

    novo_aluno = {
        "Nome completo": nome,
        "idade": idade if "ano" in idade.lower() else f"{idade} anos",
        "CEP": cep,
        "ResgMatr": resg_matr if resg_matr else "N/A",
        "E-Mail": email,
    }

    lista_alunos.append(novo_aluno)
    salvar_json(lista_alunos)
    print(f"\n✅ {nome} cadastrado e salvo com sucesso em '{NOME_ARQUIVO}'!")























if __name__ == "__main__":
    aluno = carrega_processa_dados()
    salva_json(aluno)

    print(
        f"🎉 Base inicial carregada! Total de {len(aluno)} aluno aunicio processados."
    )

    while true:
        opção = input("\n deseja inserir um novo aluno? (s\n): ").strip().lower()
        if opção == "s":
            cadastrar_novo_aluno(aluno)
        elif opção == "n":
            print("\nEncerrando o programa. Todos os dados estao salvos no JSON!")
            break
        else:
            print("Opção invalida. Digite 's' para sim ou 'n' para não.")