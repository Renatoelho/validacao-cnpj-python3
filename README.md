# Validação de CNPJ - Python 3 

Essa solução facilita a validação de um ou vários CNPJs, isso é útil para analisar uma base de clientes PJ para identificar CNPJs cadastrados de maneira equivocada ou para qualquer outra finalidade onde seja necessário saber se o CNPJ é válido ou não. 

Temos uma função chamada **ValidaCNPJ** dentro do módulo [**ferramentas**](ferramentas/__init__.py), para utilizar essa funcionalidade é necessário importar o módulo ````ferramentas```` no seu código principal, chamar a função ````ValidaCNPJ```` e passar como parâmetro uma string de números com 11 posições, lembre-se de adicionar os zeros à esquerda. 

A função retornará ````True```` para um CNPJ válido ou ````False````.

### Exemplo:

[Exemplo_CNPJ.py](Exemplo_CNPJ.py)

```python
#!/usr/bin/python3

from ferramentas import ValidaCNPJ

CNPJ = ValidaCNPJ('00000000000191')

print(CNPJ)

# >>> True
```

Essa função pode ser utilizada para validações pontuais ou ser implementada em uma solução mais robusta para tratar bases com milhões de CNPJs.

### Licença:
[Leia sobre a licença aplicada a esse Software.](LICENSE)

**Referências:**  <br/><font size="1">Macoratti.net, **Algoritmo de Validação do CNPJ.** Disponível em: <http://www.macoratti.net/alg_CNPJ.htm>. Acesso em: 01 nov. 2021.  <br/></font>
