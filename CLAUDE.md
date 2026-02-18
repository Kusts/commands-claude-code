# 🤖 Arquitetura Global do Claude Code

> **Versão:** 2.0 | **Data:** 2026-02-18

Este arquivo define o padrão operacional para todas as sessões de desenvolvimento.

---

## 📐 Arquitetura de 3 Camadas

### Camada 1: Diretiva (O que fazer)
- **Local:** `directives/*.md`
- SOPs em Markdown com objetivo, entradas, ferramentas, saídas e edge cases
- Definir "o que fazer" em linguagem natural

### Camada 2: Orquestração (Decisão)
- **Você (Task tool)** - Roteamento inteligente entre agentes
- Dividir tarefas complexas em partes menores
- Lidar com erros e atualizar diretivas

### Camada 3: Execução (Trabalho)
- **Local:** `execution/*.py`
- Scripts determinísticos em Python
- APIs, banco de dados, operações de arquivos

---

## ⚡ Princípios Fundamentais

### 1. Times de Agentes (SEMPRE)
Para **toda tarefa complexa**, use o Task tool com agentes especializados:

| Agente | Uso |
|--------|-----|
| `Explore` | Explorar codebase, encontrar arquivos |
| `Plan` | Planejar implementação |
| `senior-software-engineer` | Implementação, refatoração, code review |
| `fullstack-dev-specialist` | Features fullstack com MCPs |
| `security-code-reviewer` | Análise de vulnerabilidades |
| `software-architect` | Arquitetura de sistemas |
| `documentation-sync-agent` | Documentação sincronizada |
| `e2e-testing-specialist` | Testes automatizados |
| `devops-engineer` | CI/CD, infraestrutura |
| `database-engineer` | Modelagem, queries |
| `mobile-developer` | Apps iOS/Android |
| `performance-tuning-specialist` | Otimização |
| `api-integration-specialist` | APIs e webhooks |
| `data-analytics-engineer` | Dashboards, analytics |
| `ui-designer` | Design de interfaces |

### 2. Skills Disponíveis (QUANDO AGREGAR)
Use a **Skill tool** para invocar skills especializadas. O Claude Code deve usar skills automaticamente quando:
- A tarefa matches com uma skill disponível
- A skill pode automatizar ou melhorar o fluxo de trabalho
- For necessário conhecimento especializado (engenharia de prompts, arquitetura, etc.)

**Skills disponíveis:**
| Skill | Descrição |
|-------|-----------|
| `/commit-push-pr` | Cria commit, push e PR no GitHub |
| `/code-quality-check` | Verificação de qualidade de código |
| `/design-principles` | Princípios de design |
| `/fullstack-dev` | Desenvolvimento fullstack |
| `/hero-visual-prompt-generator` | Geração de prompts visuais |
| `/landing-page-prd-architect` | Arquitetura de PRD para landing pages |
| `/lisa-prompt-engineering` | Engenharia de prompts |
| `/long-running-agent` | Agente de longa duração |
| `/prd-brainstorm` | Brainstorming de PRD |
| `/ralph-prompt-builder` | Construtor de prompts |
| `/software-architecture` | Arquitetura de software |
| `/software-engineer` | Engenharia de software |
| `/sprint-context-generator` | Gerador de contexto de sprint |

### 3. Pensamento Passo a Passo
Para qualquer tarefa não-trivial:
```
1. Analisar o problema
2. Dividir em etapas menores
3. Executar uma etapa por vez
4. Validar antes de continuar
5. Relatar progresso
```

### 4. Comunicação Resumida
**Formato obrigatório:**
- Início: "Iniciando [tarefa]..."
- Progresso: "Etapa X/Y: [descrição breve]"
- Conclusão: "[Resultado em 1-2 linhas]"

### 5. Memória Persistente
**Sempre salvar soluções em `memory/solutions.md`:**
- Problema encontrado
- Solução aplicada
- Tags para futura consulta

**Script utilitário:** `python execution/memory_manager.py add "problema" "solução" "tags"`

---

## 🔄 Workflow Padrão

```
┌─────────────────────────────────────────────────────────┐
│  1. ANALISAR                                           │
│     → Entender o problema/tarefa                       │
│     → Verificar memória para soluções anteriores       │
└─────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│  2. PLANEJAR                                           │
│     → Usar agente Explore para entender contexto       │
│     → Dividir em etapas menores                        │
│     → Identificar agentes necessários                  │
└─────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│  3. EXECUTAR                                            │
│     → Usar scripts determinísticos (execution/)       │
│     → Aplicar pensamento passo a passo                 │
│     → Relatar cada etapa                               │
└─────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│  4. DOCUMENTAR                                         │
│     → Salvar aprendizados em memory/solutions.md       │
│     → Atualizar diretivas se necessário                │
└─────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│  5. RELATAR                                             │
│     → Resumo em 1-2 linhas                             │
│     → Próximos passos se houver                        │
└─────────────────────────────────────────────────────────┘
```

---

## 🛠️ Estrutura de Diretórios

```
.claude/
├── agents/              # 15+ agentes especializados
├── commands/           # Comandos personalizados
├── skills/             # Skills (ex: commit-push-pr)
└── settings.local Configurações locais.json #

directives/             # SOPs reutilizáveis
execution/              # Scripts Python
memory/
├── solutions.md        # Banco de soluções
└── patterns.md         # Padrões recorrentes
.tmp/                   # Arquivos temporários
```

---

## 🔧 MCPs Obrigatórios

Sempre use estes MCPs quando disponíveis:
- **MCP Supabase** - Operações de banco de dados
- **MCP Playwright** - Testes E2E e validação de UI
- **MCP Sequential-Thinking** - Raciocínio complexo

---

## 🔁 Self-Annealing

Quando algo quebrar:
1. **Analisar** - Ler erro e stack trace
2. **Corrigir** - Ajustar script
3. **Testar** - Verificar se funcionou
4. **Documentar** - Salvar solução na memória
5. **Atualizar** - Melhorar diretiva se necessário

---

## 📋 Checklist de Qualidade

Antes de considerar qualquer tarefa completa:
- [ ] Código compila/executa sem erros
- [ ] Testes existentes passam
- [ ] Novos testes para nova funcionalidade
- [ ] Segue padrões do projeto
- [ ] Sem vulnerabilidades de segurança
- [ ] Performance aceitável
- [ ] Error handling adequado
- [ ] Documentação atualizada

---

## ⚠️ Restrições Importantes

- **NUNCA** implemente features fora do escopo sem aprovação
- **SEMPRE** use agentes para tarefas complexas
- **SEMPRE** salve soluções na memória
- **SEMPRE** relate progresso resumidamente
- Mantenha foco na tarefa atual
- Em dúvida, pergunte antes de prosseguir

---

**Este arquivo é carregado automaticamente em cada sessão.**
