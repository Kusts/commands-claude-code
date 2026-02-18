"""
Script para executar diretivas do Claude Code.
Uso: python execution/directive_runner.py <diretiva> [args]
"""
import os
import sys
import importlib.util

DIRECTIVES_DIR = os.path.join(os.path.dirname(__file__), '..', 'directives')


def list_directives():
    """Lista todas as diretivas disponíveis."""
    print("Diretivas disponíveis:")
    print("-" * 40)

    if not os.path.exists(DIRECTIVES_DIR):
        print("Diretório de diretivas não encontrado.")
        return

    for file in os.listdir(DIRECTIVES_DIR):
        if file.endswith('.md'):
            name = file.replace('.md', '')
            print(f"  - {name}")


def read_directive(name):
    """Lê o conteúdo de uma diretiva."""
    path = os.path.join(DIRECTIVES_DIR, f"{name}.md")

    if not os.path.exists(path):
        print(f"Diretiva '{name}' não encontrada.")
        return None

    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def execute_directive(name):
    """Executa uma diretiva (apenas exibe as instruções)."""
    content = read_directive(name)

    if content:
        print(f"\n=== DIRETIVA: {name} ===\n")
        print(content)
    else:
        print(f"Diretiva '{name}' não encontrada.")
        print("\nUse: python directive_runner.py list")
        print("     python directive_runner.py <nome>")


def main():
    if len(sys.argv) < 2:
        print("Uso: python directive_runner.py <comando> [args]")
        print("Comandos:")
        print("  list              - Lista diretivas disponíveis")
        print("  <nome>            - Executa uma diretiva")
        return

    command = sys.argv[1]

    if command == "list":
        list_directives()
    else:
        execute_directive(command)


if __name__ == "__main__":
    main()
