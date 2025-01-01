# SCOOPE  

SCOOPE é um simulador de microscópio virtual desenvolvido como uma aplicação web.  

## Funcionalidades  
- **Navegação entre estruturas:** explore diferentes regiões das amostras com facilidade.  
- **Imagens reais em alta ampliação:** imagens de microscopia eletrônica capturadas diretamente de amostras reais.  
- **Identificação de estruturas:** ferramentas para destacar e identificar partes importantes das imagens.  

## Parcerias  
Este projeto foi desenvolvido em parceria com:  
- **Universidade Estadual de Londrina (UEL)**  
- **Laboratório de Embriologia**  
- **Departamento de Ciência da Computação**  

As imagens de microscopia eletrônica foram produzidas e fornecidas pelo Laboratório de Embriologia da UEL, garantindo alta qualidade e realismo.  

## Tecnologias utilizadas  
- **Backend:** Django  
- **Frontend:** HTML, CSS e JavaScript  
- **Banco de Dados:** [Especifique o banco utilizado, ex.: PostgreSQL, SQLite, etc.]  
- **Outras tecnologias:** [Liste bibliotecas ou ferramentas específicas usadas no projeto, se houver.]  

## Como executar o projeto  
1. Clone este repositório
2. 	Crie um ambiente virtual e ative-o:

python -m venv venv  
source venv/bin/activate  # No Windows: venv\Scripts\activate  


	3.	Instale as dependências:

pip install -r requirements.txt  


	4.	Configure o banco de dados:

python manage.py migrate  


	5.	Execute o servidor de desenvolvimento:

python manage.py runserver  


	6.	Acesse o aplicativo no navegador em:

http://127.0.0.1:8000  