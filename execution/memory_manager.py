"""
Script utilitário para gerenciar a memória persistente.
Uso: python execution/memory_manager.py <comando> [args]

Comandos:
  add <problema> <solução> <tags>
  search <termo>
  list
  patterns
"""
import os
import sys
from datetime import datetime

BASE_DIR = os.path.join(os.path.dirname(__file__), '..')
MEMORY_DIR = os.path.join(BASE_DIR, 'memory')
SOLUTIONS_FILE = os.path.join(MEMORY_DIR, 'solutions.md')
PATTERNS_FILE = os.path.join(MEMORY_DIR, 'patterns.md')


def ensure_memory_dir():
    """Garante que o diretório de memória existe."""
    if not os.path.exists(MEMORY_DIR):
        os.makedirs(MEMORY_DIR)


def read_file(filepath):
    """Lê o conteúdo de um arquivo."""
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return None


def write_file(filepath, content):
    """Escreve conteúdo em um arquivo."""
    ensure_memory_dir()
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def add_solution(problem, solution, tags):
    """Adiciona uma nova solução à memória."""
    ensure_memory_dir()
    date = datetime.now().strftime("%Y-%m-%d")

    new_entry = f"""### Solução - {date}

**Problema:** {problem}

**Solução:** {solution}

**Tags:** {tags}

---

"""

    content = read_file(SOLUTIONS_FILE)

    # Se não existe, cria estrutura base
    if not content:
        content = "# Memória Persistente de Soluções\n\n## Como usar\nSalve soluções, padrões e aprendizados que podem ser reutilizados futuramente.\n\n---\n\n## Soluções Salvas\n"

    # Insere após o header "## Soluções Salvas"
    header = "## Soluções Salvas\n"
    if header in content:
        content = content.replace(header, header + new_entry)
    else:
        content += new_entry

    write_file(SOLUTIONS_FILE, content)
    print(f"✓ Solução adicionada: {tags}")


def search_memory(query):
    """Busca soluções na memória."""
    content = read_file(SOLUTIONS_FILE)

    if not content:
        print("Memória vazia. Nenhuma solução salva ainda.")
        return

    lines = content.split('\n')
    found = False

    print(f"\nResultados para '{query}':")
    print("-" * 50)

    for i, line in enumerate(lines):
        if query.lower() in line.lower():
            # Mostrar contexto ao redor
            start = max(0, i - 2)
            end = min(len(lines), i + 3)

            for j in range(start, end):
                marker = ">>>" if j == i else "   "
                print(f"{marker} {lines[j]}")

            print()
            found = True

    if not found:
        print(f"Nenhuma solução encontrada para '{query}'")


def list_solutions():
    """Lista todas as soluções."""
    content = read_file(SOLUTIONS_FILE)

    if not content:
        print("Memória vazia.")
        return

    print(content)


def show_patterns():
    """Mostra os padrões recorrentes."""
    content = read_file(PTERNS_FILE)

    if not content:
        print("Arquivo de padrões não encontrado.")
        print(f"Crie em: {PATTERNS_FILE}")
        return

    print(content)


def main():
    if len(sys.argv) < 2:
        print("Uso: python memory_manager.py <comando> [args]")
        print("Comandos:")
        print("  add <problema> <solução> <tags>")
        print("  search <termo>")
        print("  list")
        print("  patterns")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 5:
            print("Uso: python memory_manager.py add <problema> <solução> <tags>")
            print("Exemplo: python memory_manager.py add 'API lenta' 'Adicionado cache Redis' '#api #performance'")
            return
        # Juntar argumentos como string
        problem = sys.argv[2]
        solution = sys.argv[3]
        tags = sys.argv[4]
        add_solution(problem, solution, tags)

    elif command == "search":
        if len(sys.argv) < 3:
            print("Uso: python memory_manager.py search <termo>")
            return
        search_memory(sys.argv[2])

    elif command == "list":
        list_solutions()

    elif command == "patterns":
        show_patterns()

    else:
        print(f"Comando desconhecido: {command}")


if __name__ == "__main__":
    main()
