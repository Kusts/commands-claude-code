# Commit, Push, and Open PR

## Name
commit-push-pr

## Trigger
`/commit-push-pr`

## Description
Automaticamente faz commit de todas as mudanças, faz push para o repositório remoto e abre um Pull Request.

## Usage
```
/commit-push-pr [branch-name] [pr-title]
```

### Parameters
- `branch-name` (optional): Nome da branch. Se não especificado, usa a branch atual
- `pr-title` (optional): Título do Pull Request. Se não especificado, gera automaticamente a partir do último commit

### Examples
```bash
/commit-push-pr
# Usa a branch atual e gera título automático

/commit-push-pr feature/new-feature "Add new authentication system"
# Especifica branch e título do PR
```

## Actions
1. **Verifica o status do Git**
```bash
   git status
```

2. **Faz commit das mudanças**
```bash
   git add .
   git commit -m "[Commit message gerado automaticamente]"
```

3. **Faz push para o repositório remoto**
```bash
   git push origin [branch-name]
```

4. **Abre um Pull Request**
```bash
   # Usando GitHub CLI (gh)
   gh pr create --title "[PR Title]" --body "Auto-generated PR" --web
```

## Full Script
```bash
#!/bin/bash

# Cores para output
GREEN='\\033[0;32m'
BLUE='\\033[0;34m'
NC='\\033[0m' # No Color

echo -e "${BLUE}📋 Verificando status do Git...${NC}"
git status

echo -e "${BLUE}📝 Adicionando e fazendo commit...${NC}"
git add .
git commit -m "chore: update code changes"

echo -e "${BLUE}🚀 Fazendo push para o repositório...${NC}"
git push origin $(git rev-parse --abbrev-ref HEAD)

echo -e "${BLUE}🔗 Abrindo Pull Request...${NC}"
gh pr create --fill --web

echo -e "${GREEN}✅ Commit, push e PR abertos com sucesso!${NC}"
```

## Alternativa: Para Repositórios GitLab
```bash
#!/bin/bash

echo "📋 Verificando status do Git..."
git status

echo "📝 Adicionando e fazendo commit..."
git add .
git commit -m "chore: update code changes"

echo "🚀 Fazendo push para o repositório..."
git push origin $(git rev-parse --abbrev-ref HEAD)

echo "🔗 Abrindo Merge Request..."
glab mr create --fill --web

echo "✅ Commit, push e MR abertos com sucesso!"
```

---

## **Como Salvar no Claude Code:**

### **Passo 1: Acesse o Claude Code**
- Abra seu repositório no [claude.ai/code](https://claude.ai/code)

### **Passo 2: Crie a pasta de comandos (se não existir)**
```bash
mkdir -p .claude/commands
```

### **Passo 3: Crie o arquivo do comando**
- Crie um novo arquivo chamado `commit-push-pr.md` em `.claude/commands/`

### **Passo 4: Cole o conteúdo acima**
- Copie o conteúdo do comando acima para esse arquivo

### **Passo 5: Faça commit e salve**
```bash
git add .claude/commands/commit-push-pr.md
git commit -m "feat: add commit-push-pr command"
git push
```

### **Passo 6: Configure permissões (opcional)**
Se você quer que o Claude execute o comando sem pedir permissão, adicione ao `.claude/settings.json`:
```json
{
  "permissions": {
    "bash": {
      "allowed": [
        "git add",
        "git commit",
        "git push",
        "git status",
        "git rev-parse",
        "gh pr create",
        "glab mr create"
      ]
    }
  }
}
```

---

## **Uso no Claude Code:**

Quando estiver trabalhando no Claude Code, você pode simplesmente digitar:
