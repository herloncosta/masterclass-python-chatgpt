### Configuração de Ambiente Python VSCode

1. Crie uma pasta .vscode e adicione o arquivo settings.json.

```
/.vscode
  | settings.json
```

Dentro do arquivo adicione o código a seguir:

```
{
  "code-runner.executorMap": {
    "python": "python -u",
  }
}
```

### Indicação de Extensão:

- **autopep8**: Auxilia na formatação do código, seguindo a padronização definida pela PEP 8.
