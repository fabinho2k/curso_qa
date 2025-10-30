alunos = {
    1001: {"nome": "Ana Silva", "idade": 20},
    1002: {"nome": "Bruno Santos", "idade": 22},
    1003: {"nome": "Carlos Oliveira", "idade": 19},
    1004: {"nome": "Daniela Costa", "idade": 21},
    1005: {"nome": "Eduardo Souza", "idade": 23},
    1006: {"nome": "Fernanda Lima", "idade": 20},
    1007: {"nome": "Gabriel Alves", "idade": 18},
    1008: {"nome": "Helena Pereira", "idade": 22},
    1009: {"nome": "Igor Rodrigues", "idade": 21},
    1010: {"nome": "Juliana Ferreira", "idade": 19},
    1011: {"nome": "Kevin Martins", "idade": 24},
    1012: {"nome": "Larissa Gomes", "idade": 20},
    1013: {"nome": "Marcelo Ribeiro", "idade": 23},
    1014: {"nome": "Natália Cardoso", "idade": 21},
    1015: {"nome": "Otávio Barbosa", "idade": 22},
    1016: {"nome": "Paula Araújo", "idade": 19},
    1017: {"nome": "Rafael Dias", "idade": 20},
    1018: {"nome": "Sabrina Castro", "idade": 18},
    1019: {"nome": "Thiago Moreira", "idade": 23},
    1020: {"nome": "Vanessa Rocha", "idade": 21},
    1021: {"nome": "Wagner Cunha", "idade": 22},
    1022: {"nome": "Yasmin Mendes", "idade": 20},
    1023: {"nome": "André Vieira", "idade": 24},
    1024: {"nome": "Beatriz Soares", "idade": 19},
    1025: {"nome": "Caio Monteiro", "idade": 21},
    1026: {"nome": "Débora Freitas", "idade": 23},
    1027: {"nome": "Enzo Carvalho", "idade": 18},
    1028: {"nome": "Flávia Batista", "idade": 22},
    1029: {"nome": "Gustavo Nunes", "idade": 20},
    1030: {"nome": "Isabela Campos", "idade": 21},
    1031: {"nome": "João Ramos", "idade": 19},
    1032: {"nome": "Kamila Correia", "idade": 23},
    1033: {"nome": "Leonardo Pinto", "idade": 22},
    1034: {"nome": "Mariana Teixeira", "idade": 20},
    1035: {"nome": "Nicolas Azevedo", "idade": 24},
    1036: {"nome": "Olivia Borges", "idade": 18},
    1037: {"nome": "Pedro Melo", "idade": 21},
    1038: {"nome": "Rafaela Lopes", "idade": 19},
    1039: {"nome": "Samuel Rezende", "idade": 23},
    1040: {"nome": "Tatiana Macedo", "idade": 22},
    1041: {"nome": "Ulisses Farias", "idade": 20},
    1042: {"nome": "Vitória Moura", "idade": 21},
    1043: {"nome": "William Gonçalves", "idade": 19},
    1044: {"nome": "Xuxa Tavares", "idade": 24},
    1045: {"nome": "Yuri Nascimento", "idade": 23},
    1046: {"nome": "Zélia Duarte", "idade": 20},
    1047: {"nome": "Arthur Fonseca", "idade": 18},
    1048: {"nome": "Bianca Aragão", "idade": 22},
    1049: {"nome": "Cauã Miranda", "idade": 21},
    1050: {"nome": "Diana Siqueira", "idade": 19}
}

grupo_azul = []
grupo_amarelo = []

for matricula, dados in alunos.items():
    if matricula % 2 == 0:
        grupo_azul.append(dados)
    else:

        grupo_amarelo.append(dados)

print(grupo_amarelo)
print(grupo_azul)