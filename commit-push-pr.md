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
