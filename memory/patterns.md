# Padrões Recorrentes

Registre padrões que se repetem em múltiplos projetos.

---

## Padrões de Código

### Estrutura de API REST
- `GET /resources` → listar
- `GET /resources/:id` → detalhar
- `POST /resources` → criar
- `PUT /resources/:id` → atualizar
- `DELETE /resources/:id` → excluir

### Error Handling
```python
try:
    # operação
except SpecificException as e:
    logger.error(f"Contexto: {e}")
    raise CustomException("mensagem", details)
```

### Validação de Entrada
- Sempre validar na camada de API
- Usar schemas (Pydantic, Zod)
- Retornar 400 para dados inválidos

---

## Padrões de Testes

### AAA Pattern
```
Arrange → Act → Assert
```

### Testes de Integração
- Mockar serviços externos
- Usar banco de testes
- Limpar estado entre testes

---

## Padrões de Git

### Conventional Commits
- `feat:` nova feature
- `fix:` correção de bug
- `docs:` documentação
- `refactor:` refatoração
- `test:` testes
- `chore:` tarefas

---

## Boas Práticas

### Código Limpo
- Funções < 20 linhas
- Nomes descritivos
- DRY - Don't Repeat Yourself
- KISS - Keep It Simple

### Segurança
- Nunca expor credenciais
- Sanitizar inputs
- Usar HTTPS
- Principle of Least Privilege
