import requests

BASE_URL_POST = "https://calculadora-fxpc.onrender.com/operation"
BASE_URL_GET = "https://calculadora-fxpc.onrender.com/operations"


def listar_operacoes():
    #Recebe as informações da API
    response = requests.get(BASE_URL_GET)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao listar operações: {response.status_code}")

def realizar_operacao(op, num1, num2):
    #Realiza alguma das 4 operações da API
    url = f"{BASE_URL_POST}/{op}/{num1}/{num2}"
    response = requests.post(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao realizar operação {op}: {response.status_code}")

def main():
    try:
        # Listar operações disponíveis
        opcoes = listar_operacoes()
        print("Operações disponíveis:")
        for op in opcoes.get('operations'):
            print(op.get('name'))
    
        num1 = 10
        num2 = 5
        print("Resultado das operações utilizando {} e {}".format(num1, num2))
        
        #Executa todos os métodos disponíveis
        op = "soma"
        resultado = realizar_operacao(op, num1, num2)
        print(f"Resultado da operação {op}: {resultado.get('result')}")

        op = "subtracao"
        resultado = realizar_operacao(op, num1, num2)
        print(f"Resultado da operação {op}: {resultado.get('result')}")

        op = "multiplicacao"
        resultado = realizar_operacao(op, num1, num2)
        print(f"Resultado da operação {op}: {resultado.get('result')}")
        
        op = "divisao"
        resultado = realizar_operacao(op, num1, num2)
        print(f"Resultado da operação {op}: {resultado.get('result')}")
        

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()