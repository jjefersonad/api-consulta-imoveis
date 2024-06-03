import os
import sys
import csv
# Adicionar o diretório raiz do seu aplicativo ao caminho de busca de módulos
diretorio_app = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, diretorio_app)

# Agora você pode importar o módulo app
from app import create_app, db
from app.core.entities import Imovel

def importar_dados_csv(caminho_arquivo):
    try:
        app = create_app()
        with app.app_context():
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_csv:
                leitor_csv = csv.DictReader(arquivo_csv, delimiter=';')
                for linha in leitor_csv:
                    print(linha)
                    imovel = Imovel(
                        price=float(linha['price']),
                        condo=float(linha['condo']),
                        size=int(linha['size']),
                        rooms=int(linha['rooms']),
                        toilets=int(linha['toilets']),
                        suites=int(linha['suites']),
                        parking=bool(linha['parking']),
                        elevator=bool(linha['elevator']),
                        furnished=bool(linha['furnished']),
                        swimming_pool=bool(linha['swimming_pool']),
                        new=bool(linha['new']),
                        district=linha['district'],
                        negotiation_type=linha['negotiation_type'],
                        property_type=linha['property_type'],
                        latitude=float(linha['latitude']),
                        longitude=float(linha['longitude'])
                    )
                    db.session.add(imovel)
                
                db.session.commit()
                print("Dados importados com sucesso!")
    
    except Exception as e:
        print(f"Erro ao importar os dados do arquivo CSV: {e}")

if __name__ == "__main__":
    caminho_arquivo_csv = "./seeds/sao-paulo-properties-april-2019_sem_cabecalho.csv"
    importar_dados_csv(caminho_arquivo_csv)