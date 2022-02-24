# Validação de CNPJ - Python 3 

Essa solução facilita a validação de um ou vários CNPJs, isso é útil para analisar uma base de clientes PJ, para identificar CNPJs cadastrados de maneira equivocada ou para qualquer outra finalidade onde seja necessário saber se o CNPJ é válido ou não. 

Temos um método chamado **valida_cnpj**, dentro da classe **Cnpj**. Para utilizar essa funcionalidade é necessário importar o módulo ````ferramentas```` no seu código principal, chamar o método ````valida_cnpj```` e passar como parâmetro uma string de números com 14 posições. Lembre-se de adicionar os zeros à esquerda. 

O método retornará ````True```` para um CNPJ válido ou ````False````.

### Exemplo:

[exemplo_cnpj.py](exemplo_cnpj.py)

```python
#!/usr/bin/python3

from ferramentas.valida_cnpj import Cnpj

CNPJ = Cnpj.valida_cnpj('00000000000191')

print(CNPJ)

# >>> True
```

Essa função pode ser utilizada para validações pontuais ou ser implementada em uma solução mais robusta, para tratar bases com milhões de CNPJs.

### Licença:
[Leia sobre a licença aplicada a esse Software.](LICENSE)

**Referências:**  <br/><font size="1">Macoratti.net, **Algoritmo de Validação do CNPJ.** Disponível em: <http://www.macoratti.net/alg_CNPJ.htm>. Acesso em: 01 nov. 2021.  <br/></font>
