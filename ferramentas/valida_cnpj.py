# -*- coding: utf-8 -*-

__version__ = '1.0.0'


class Cnpj:
    def valida_cnpj(num: str) -> bool:
        if len(num) == 14:
            radical: list = list(num)[:-2]
            dv: list = list(num)[-2:]

            # Calculando DV 1
            try:
                index_cal: int = 0
                lista_cal: list = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
                soma1: int = 0
                for x in radical:
                    soma1 = soma1 + (lista_cal[index_cal] * int(x))
                    index_cal = index_cal + 1
                calc_dv_1: int = soma1 % 11
                if calc_dv_1 < 2:
                    dv_1: int = 0
                else:
                    dv_1 = 11 - calc_dv_1

                # Calculando DV 2
                try:
                    index_cal = 0
                    lista_cal = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
                    soma2: int = 0
                    radical.append(str(dv_1))
                    for x in radical:
                        soma2 = soma2 + (lista_cal[index_cal] * int(x))
                        index_cal = index_cal + 1
                    calc_dv_2: int = soma2 % 11
                    if calc_dv_2 < 2:
                        dv_2: int = 0
                    else:
                        dv_2 = 11 - calc_dv_2

                    # Teste CNPJ válido?

                    try:
                        if ''.join(dv).strip() == str(dv_1)+str(dv_2).strip():
                            return True
                        else:
                            return False

                    except Exception:

                        return False

                except Exception:

                    return False

            except Exception:

                return False

        else:

            return False
