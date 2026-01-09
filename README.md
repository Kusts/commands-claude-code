# commands-claude-code
Comandos que utilizo para evitar tarefas repetitivas

# /commit-push-pr

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

1. ✅ Fazer commit de todas as mudanças
2. ✅ Fazer push para o repositório
3. ✅ Abrir um Pull Request automaticamente

**Dica:** Você pode personalizar a mensagem de commit editando a flag `-m "chore: update code changes"` para algo mais específico como `"feat: add new authentication"`.


# /deep-verify

## **Como Salvar**
1. Crie a pasta: `mkdir -p .claude/commands`
2. Crie o arquivo: `.claude/commands/deep-verify.md`
3. Cole o conteúdo acima
4. Faça commit: `git add .claude/ && git commit -m "feat: add deep-verify command"`

**Pronto!** Agora você pode usar `/deep-verify` no Claude Code quando precisar de verificações complexas. 🚀
