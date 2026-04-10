class IMCService:
    @staticmethod
    def calcular_imc(altura:float,peso:float) -> dict:
        if altura <= 0 or peso <= 0:
            raise ValueError("Altura e peso devem ser maiores que zero.")
        imc = peso / (altura * altura)
        if imc < 18.5:
            classificacao = 'Abaixo do peso'
        elif imc < 24.9:
            classificacao = 'Peso normal'
        elif imc < 29.9:
            classificacao = 'Sobrepeso'
        else:
            classificacao = 'Obesidade'
        resultado={
            'imc': round(imc, 2),
            'classificacao': classificacao
        }
        return resultado