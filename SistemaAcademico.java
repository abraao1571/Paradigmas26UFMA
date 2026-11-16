import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

// 1. Classe Modelo (Equivalente à AvaliacaoDisciplina em Python)
class AvaliacaoDisciplina {
    // Atributos privados (Encapsulamento rígido)
    private String aluno;
    private String disciplina;
    private List<Double> notas;

    // Construtor (Equivalente ao def __init__ em Python)
    public AvaliacaoDisciplina(String aluno, String disciplina, List<Double> notas) {
        this.aluno = aluno;
        this.disciplina = disciplina;
        // Cria uma cópia imutável da lista (Equivalente à tuple() do Python)
        this.notas = Collections.unmodifiableList(new ArrayList<>(notas));
    }

    // Getter (Equivalente ao @property em Python)
    public List<Double> getNotas() {
        return this.notas;
    }

    public double calcularMedia() {
        double soma = 0;
        for (double nota : this.notas) {
            soma += nota;
        }
        return soma / this.notas.size();
    }

    public String verificarStatus() {
        double media = calcularMedia();
        if (media >= 7) {
            return "aprovado";
        } else if (media >= 5) {
            return "reposição";
        }
        return "reprovado";
    }

    public String gerarClassificacao() {
        double media = calcularMedia();
        if (media >= 9) {
            return "muito boa";
        } else if (media >= 7) {
            return "boa";
        } else if (media >= 5) {
            return "regular";
        }
        return "insuficiente";
    }

    public void exibirResumo() {
        System.out.println("aluno: " + this.aluno);
        System.out.println("disciplina: " + this.disciplina);
        System.out.printf("media: %.2f%n", calcularMedia());
        System.out.println("classificacao: " + gerarClassificacao());
        System.out.println("situacao: " + verificarStatus());
    }
}

// 2. Classe Gerenciadora e Execução (Equivalente à SistemaAcademico em Python)
public class SistemaAcademico {
    private List<AvaliacaoDisciplina> historico;
    private Scanner scanner;

    public SistemaAcademico() {
        this.historico = new ArrayList<>();
        this.scanner = new Scanner(System.in);
    }

    private List<Double> lerNotas(int quantidade) {
        List<Double> notas = new ArrayList<>();
        for (int i = 0; i < quantidade; i++) {
            System.out.print("digite a nota " + (i + 1) + ": ");
            double nota = scanner.nextDouble();
            notas.add(nota);
        }
        scanner.nextLine(); // Limpa o buffer do teclado após ler números
        return notas;
    }

    public void cadastrarDisciplina() {
        System.out.print("digite o nome do aluno: ");
        String aluno = scanner.nextLine();

        System.out.print("digite o nome da disciplina: ");
        String disciplina = scanner.nextLine();

        System.out.print("digite a quantidade de notas: ");
        int quantidade = scanner.nextInt();

        while (quantidade < 2 || quantidade > 10) {
            System.out.println("digite entre 2 a 10");
            System.out.print("digite novamente: ");
            quantidade = scanner.nextInt();
        }

        List<Double> notas = lerNotas(quantidade);

        // Criação do objeto (Instanciação com a palavra-chave 'new')
        AvaliacaoDisciplina avaliacao = new AvaliacaoDisciplina(aluno, disciplina, notas);
        this.historico.add(avaliacao);

        System.out.println("\n- resultado -");
        avaliacao.exibirResumo();
    }

    public void consultarHistorico() {
        if (this.historico.isEmpty()) {
            System.out.println("\nainda nao existem disciplinas cadastradas.");
            return;
        }

        System.out.println("\n- historico -");
        for (AvaliacaoDisciplina avaliacao : this.historico) {
            System.out.println();
            avaliacao.exibirResumo();
        }
    }

    public void executar() {
        int opcao = 0;
        while (opcao != 3) {
            System.out.println("\n- sistema academico -");
            System.out.println("1. cadastrar disciplina");
            System.out.println("2. consultar historico");
            System.out.println("3. sair");

            System.out.print("escolha uma opcao: ");
            opcao = scanner.nextInt();
            scanner.nextLine(); // Limpa o buffer do teclado

            if (opcao == 1) {
                cadastrarDisciplina();
            } else if (opcao == 2) {
                consultarHistorico();
            } else if (opcao == 3) {
                System.out.println("\nfim");
            } else {
                System.out.println("\ninvalido");
            }
        }
    }

    // Ponto de entrada obrigatório do Java (Equivalente ao if __name__ == "__main__":)
    public static void main(String[] args) {
        SistemaAcademico sistema = new SistemaAcademico();
        sistema.executar();
    }
}