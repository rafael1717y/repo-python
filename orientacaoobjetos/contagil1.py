html = "<br> djfj rksk periculosidade"
#html = "<br> djfj rksk periculosidade --- adicional noturno"
#html = "periculosidad e inen"


class Siapenet:

    def __init__(self):
        pass

    def consultar_adicional(self):

        html = "<br> djfj rksk periculosidade"
        tipo_adic  = None

        if html.__contains__("periculosidade")  and html.__contains__("adicional noturno"):
            print("periculosidade e adicional noturno")
            tipo_adic = 1
            return html, tipo_adic

        elif html.__contains__("periculosidade")  and html.__contains__("indeniz estrategica"):
            print("periculosidade e indenizacao estrategica")
            tipo_adic = 2
            return html, tipo_adic


        elif html.__contains__("periculosidade"):
            print('periculosidade')
            tipo_adic = 3
            return html, tipo_adic

        else:
            print("é do tipo adicional noturno e periculosidade")
            tipo_adic = 4
            return html, tipo_adic


    def realizar_consulta(self, html, tipo_adic):
        print(html)
        print(tipo_adic)



siapenet = Siapenet()

html, tipo_adic = siapenet.consultar_adicional()
siapenet.realizar_consulta(html, tipo_adic)





"""
start = 2
qtd = 6

### colocar qtd mais 1....

for i in range(start, (qtd + 1)):
    print(i)
"""


