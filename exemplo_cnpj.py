#!/usr/bin/python3

from ferramentas.valida_cnpj import Cnpj

CNPJ: bool = Cnpj.valida_cnpj('00000000000191')

print(CNPJ)

