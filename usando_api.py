import requests
import json
import pyodbc


class api_cep:
    cep = None
    address = {}
    def set_cep(self, cep_input):
        self.cep = cep_input

    def set_endereco(self):
        try:
            address_data = requests.get("https://viacep.com.br/ws/{}/json/".format(self.cep))
            self.address = address_data.json()
            address_data.close()
        except:
            print("Erro ao buscar endereço")
            self.address = None

    def get_endereco(self):
        return self.address

    def mostrar_endereco(self):
        if 'erro' not in self.address:
            print("CEP: {}\nRUA: {}\nBAIRRO: {}\nCIDADE: {}\nUF: {}\n".format(self.address['cep'],
                                                                              self.address['logradouro'],
                                                                              self.address['bairro'],
                                                                              self.address['localidade'],
                                                                              self.address['uf']))
        else:
            print("{} CEP Invalido\n".format(self.cep))


if __name__ == '__main__':
    option = 1
    objCep = api_cep()
    while option:
        print("\t=>Consulta CEP<=\n")
        cep_input = input("Digite o CEP sem traços ")
        if len(cep_input) != 8:
            print("Quantidade de dígitos invalidos\n")
            continue

        objCep.set_cep(cep_input)

        objCep.set_endereco()
        if objCep.get_endereco() is not None:
            objCep.mostrar_endereco()
        option = int(input("Deseja realizar uma nova consulta?\n1 - Sim\n0 - Não\n"))
    print("Processo Finalizado")
    exit(0)
