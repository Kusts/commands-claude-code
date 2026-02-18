# Sub-Agentes para Claude Code

Uma coleção de sub-agentes especializados para uso com Claude Code, cada um projetado para tarefas específicas de desenvolvimento de software.

## Instalação

Para usar estes agentes no seu projeto, copie a pasta `agents` para `.claude/agents/` no seu projeto:

```bash
mkdir -p .claude/agents
cp agents/*.md .claude/agents/
```

## Arquitetura de 3 Camadas

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

## Princípios de Operação

### 1. Sempre opere com times de agentes
- Use Task tool para dividir tarefas complexas
- Agentes disponíveis: Explore, Plan, senior-software-engineer, fullstack-dev-specialist, security-code-reviewer, software-architect, documentation-sync-agent, e2e-testing-specialist, e mais

### 2. Use Skills quando agregarem valor
- Use a Skill tool para invocar skills especializadas
- O Claude Code deve usar skills automaticamente quando:
  - A tarefa match com uma skill disponível
  - A skill pode automatizar ou melhorar o fluxo
  - For necessário conhecimento especializado

**Skills disponíveis:**
| Skill | Descrição |
|-------|-----------|
| `/commit-push-pr` | Cria commit, push e PR no GitHub |
| `/code-quality-check` | Verificação de qualidade de código |
| `/design-principles` | Princípios de design |
| `/fullstack-dev` | Desenvolvimento fullstack |
| `/hero-visual-prompt-generator` | Geração de prompts visuais |
| `/landing-page-prd-architect` | Arquitetura de PRD |
| `/lisa-prompt-engineering` | Engenharia de prompts |
| `/long-running-agent` | Agente de longa duração |
| `/prd-brainstorm` | Brainstorming de PRD |
| `/ralph-prompt-builder` | Construtor de prompts |
| `/software-architecture` | Arquitetura de software |
| `/software-engineer` | Engenharia de software |
| `/sprint-context-generator` | Gerador de contexto de sprint |

### 3. Pensamento passo a passo
- Divida tarefas complexas em etapas sequenciais
- Valide cada passo antes de continuar
- Relate o progresso: "Executando etapa X/Y: [descrição]"

### 4. Memória persistente
- Salve soluções em `memory/solutions.md`
- Use o script `execution/memory_manager.py` para adicionar soluções
- Consulte a memória antes de resolver problemas recorrentes

---

## Estrutura de Diretórios

```
.claude/
├── agents/              # Sub-agentes especializados
├── commands/           # Comandos personalizados
├── skills/             # Skills do Claude Code
└── settings.local.json # Configurações locais

directives/             # SOPs em Markdown
execution/              # Scripts Python determinísticos
memory/                 # Memória persistente de soluções
.tmp/                   # Arquivos intermediários
CLAUDE.md              # Configurações globais (raiz do projeto)
```

---

## Agentes Disponíveis

### 1. Documentation Sync Agent (`documentation-sync-agent.md`)

**Cor:** Verde | **Modelo:** Opus

Agente especializado em manter a documentação do projeto sempre atualizada e sincronizada. Responsável por:

- Rastrear progresso de desenvolvimento
- Documentar bugs encontrados
- Registrar decisões arquiteturais (ADRs)
- Manter o mapa do codebase (`codebase-map.json`)
- Criar arquivos `CLAUDE.md` contextuais em diretórios importantes

**Quando usar:**
- Após completar implementação de features
- Quando bugs são encontrados e corrigidos
- Ao tomar decisões arquiteturais importantes
- Para entender a estrutura do projeto

---

### 2. E2E Testing Specialist (`e2e-testing-specialist.md`)

**Cor:** Rosa | **Modelo:** Opus

Especialista em testes end-to-end automatizados, detecção de bugs e validação de funcionalidades. Utiliza MCP Chrome DevTools ou Playwright para:

- Executar testes E2E completos
- Identificar e documentar falhas
- Criar planos de correção detalhados
- Validar fluxos de usuário críticos
- Testar responsividade e compatibilidade cross-browser

**Quando usar:**
- Após implementar novas features ou componentes
- Para reproduzir e documentar bugs
- Antes de releases (testes de regressão)
- Para validar fluxos críticos (autenticação, pagamentos)

---

### 3. Fullstack Dev Specialist (`fullstack-dev-specialist.md`)

**Cor:** Ciano | **Modelo:** Opus

Desenvolvedor fullstack experiente que implementa código real, funcional e consistente. Utiliza MCPs (Supabase, Context7, Serena) para:

- Entender contexto do projeto antes de codificar
- Implementar código personalizado para cada aplicação
- Seguir padrões e convenções existentes
- Integrar frontend, backend e banco de dados

**Quando usar:**
- Implementar features que envolvem frontend e backend
- Criar endpoints de API com integração de banco
- Integrar serviços de terceiros (webhooks, APIs)
- Implementar lógica funcional após aprovação de design

---

### 4. Security Code Reviewer (`security-code-reviewer.md`)

**Cor:** Amarelo | **Modelo:** Opus

Especialista em segurança de aplicações e revisão de código. Foco em:

- Análise OWASP Top 10
- Identificação de vulnerabilidades (SQL Injection, XSS, etc.)
- Auditoria de autenticação e autorização
- Análise de práticas criptográficas
- Criação de planos de remediação

**Quando usar:**
- Após implementar código sensível à segurança
- Ao criar sistemas de autenticação
- Para endpoints de API que manipulam dados sensíveis
- Antes de deploy para produção
- Auditorias gerais de segurança

---

### 5. Senior Software Engineer (`senior-software-engineer.md`)

**Cor:** Azul | **Modelo:** Opus

Engenheiro de software sênior com 15+ anos de experiência. Especializado em:

- Implementação de features full-stack
- Código de qualidade de produção
- Correção de bugs complexos
- Refatoração seguindo SOLID
- Criação de testes automatizados
- Code reviews detalhados

**Quando usar:**
- Implementar novas features
- Corrigir bugs complexos (memory leaks, race conditions)
- Refatorar código seguindo boas práticas
- Criar testes unitários e de integração
- Revisar pull requests

---

### 6. Software Architect (`software-architect.md`)

**Cor:** Vermelho | **Modelo:** Opus

Arquiteto de software sênior especializado em sistemas de alta escala. Responsável por:

- Identificar gargalos de infraestrutura
- Analisar problemas de escalabilidade
- Avaliar segurança e resiliência
- Documentar decisões arquiteturais (ADRs)
- Definir métricas e SLIs/SLOs

**Quando usar:**
- Antes de homologação/produção
- Ao planejar features de alta escala
- Quando há problemas de performance
- Para decisões arquiteturais importantes
- Migrações de infraestrutura

---

## Mais Agentes Disponíveis

### 7. DevOps Engineer (`devops-engineer.md`)

Agente especializado em DevOps, CI/CD, infraestrutura como código, containerização e orquestração.

**Quando usar:**
- Configurar pipelines de CI/CD
- Gerenciar infraestrutura na nuvem
- Criar configurações Docker/Kubernetes
- Automatizar deployments
- Configurar monitoramento e alertas

---

### 8. Database Engineer (`database-engineer.md`)

Agente especializado em engenharia de banco de dados, modelagem de dados, otimização de queries e administração de databases.

**Quando usar:**
- Projetar esquemas de banco de dados
- Otimizar queries lentas
- Criar migrations
- Configurar índices
- Resolver problemas de performance

---

### 9. Mobile Developer (`mobile-developer.md`)

Agente especializado em desenvolvimento mobile para iOS e Android.

**Quando usar:**
- Criar aplicativos mobile
- Implementar features mobile
- Otimizar performance mobile
- Integrar com APIs nativas
- Configurar builds e deployments de apps

---

### 10. Performance Tuning Specialist (`performance-tuning-specialist.md`)

Agente especializado em otimização de performance, profiling e tuning de aplicações.

**Quando usar:**
- Aplicações estão lentas
- Otimizar queries
- Reduzir tempo de carregamento
- Otimizar uso de memória
- Resolver problemas de escalabilidade

---

### 11. API Integration Specialist (`api-integration-specialist.md`)

Agente especializado em design e implementação de APIs, integrações de terceiros e contratos de API.

**Quando usar:**
- Projetar APIs REST ou GraphQL
- Integrar com serviços externos
- Definir contratos de API
- Configurar webhooks
- Implementar autenticação de APIs

---

### 12. Data Analytics Engineer (`data-analytics-engineer.md`)

Agente especializado em engenharia de dados, analytics, business intelligence e pipelines de dados.

**Quando usar:**
- Criar dashboards
- Configurar pipelines de dados
- Implementar analytics
- Processar dados em tempo real
- Criar relatórios

---

### 13. UI Designer (`ui-designer.md`)

Agente especializado em design de interfaces, sistemas de design e experiência do usuário.

**Quando usar:**
- Criar componentes visuais
- Definir sistemas de design
- Projetar layouts
- Criar wireframes
- Padronizar estilos

---

### 14. System Planner Architect (`system-planner-architect.md`)

Agente especializado em planejamento estratégico, arquitetura de sistemas e engenharia de software.

**Quando usar:**
- Iniciar novos projetos do zero
- Arquitetar sistemas completos
- Planejar roadmaps técnicos
- Transformar requisitos em arquitetura
- Analisar viabilidade técnica

---

## MCPs Recomendados

Para melhor funcionamento dos agentes, recomenda-se configurar:

- **MCP Supabase** - Para operações de banco de dados
- **MCP Playwright** - Para testes E2E e validação de UI
- **MCP Sequential-Thinking** - Para raciocínio complexo

---

## Self-Annealing

Quando algo quebrar:
1. Corrija o script
2. Atualize a memória com a solução
3. Atualize a diretiva relevante
4. Teste novamente

---

## Como Usar

Os agentes são invocados automaticamente pelo Claude Code quando o contexto é apropriado. Você também pode solicitar explicitamente:

```
Use o agente security-code-reviewer para analisar este código
Use o agente fullstack-dev-specialist para implementar a feature de login
Use o agente e2e-testing-specialist para testar o fluxo de checkout
```

---

## Licença

MIT

---

Desenvolvido por [Made in Low Code](https://github.com/madeinlowcode)
