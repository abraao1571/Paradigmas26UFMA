#include <stdio.h>

int main() {
    float notas[50];        // vetor para guardar as notas
    int i, qtd_aprovados = 0;
    float soma = 0, media, maior, menor;
    int qtd_alunos = 5;     // teste com 5 alunos (pode mudar para 50)

    // Entrada das notas
    for (i = 0; i < qtd_alunos; i++) {
        printf("Digite a nota do aluno %d: ", i + 1);
        scanf("%f", &notas[i]);

        soma += notas[i]; // acumula a soma das notas
    }

    // Inicializa maior e menor com a primeira nota
    maior = menor = notas[0];

    // Processamento
    for (i = 0; i < qtd_alunos; i++) {
        if (notas[i] >= 6.0) {   // critério de aprovação
            qtd_aprovados++;
        }

        if (notas[i] > maior) {  // verifica maior nota
            maior = notas[i];
        }

        if (notas[i] < menor) {  // verifica menor nota
            menor = notas[i];
        }
    }

    media = soma / qtd_alunos; // calcula média

    // Saída
    printf("\n--- RESULTADOS ---\n");
    printf("Media da turma: %.2f\n", media);
    printf("Quantidade de aprovados: %d\n", qtd_aprovados);
    printf("Maior nota: %.2f\n", maior);
    printf("Menor nota: %.2f\n", menor);

    return 0;
}
