---
description: Cria commit, faz push e cria pull request
---

Crie um commit das mudanças atuais, faça push para o remote e crie uma pull request.

Siga estes passos:

1. **Verificar status**: Execute `git status` e `git diff` para ver as mudanças

2. **Criar commit**: Adicione os arquivos modificados e crie um commit com mensagem descritiva terminando com:
   ```
   Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
   ```

3. **Fazer push**: Execute `git push -u origin <branch>` para enviar as mudanças

4. **Criar PR**: Use `gh pr create` para criar uma pull request com:
   - Título curto e descritivo (max 70 caracteres)
   - Corpo com:
     - ## Summary (2-3 bullet points)
     - ## Test plan (checklist)
     - Footer com emoji gerado pelo Claude Code
