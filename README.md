# README.md

## Encãotrador

### Instruções para Executar o Sistema

1. **Pré-requisitos:**
   - Certifique-se de ter o Python instalado no seu computador.

2. **Configuração do Ambiente:**
   - Abra um terminal na pasta do projeto.
   - Instale as dependências necessárias para o servidor funcionar com o comando:
  
     pip install Flask flask-cors

3. **Execução do Servidor(Back End):**
   - Execute o servidor Flask com o comando:
     
     python main.py
     
   - Esse servidor ficará disponível em http://localhost:5000/.

4. **Execução do Front End:**
   - Após o servidor estar sendo executado, basta abrir o index.html e realizar suas buscas.

### Premissas Assumidas

1. **Formato de Data:**
   - O formato de data esperado é "YYYY-MM-DD" (exemplo: "2023-05-15").
  
2. **Exclusividade do projeto:**
   - Esse projeto foi desenvolvido pensando no problema apresentado do Eduardo, já que para outras pessoas as distâncias entre os petshops seriam diferentes, podendo levar a outros resultados.

### Decisões de Projeto

1. **Front End:**
   - Foram utilizados html, css e js já que foi liberado utilizar a tecnologia que eu me sentisse mais a vontade, e essas foram as tecnologias que eu mais utilizei quando necessário projetar um Front End.
   - Utilização do Bootstrap para o design responsivo.
   - Barra lateral com informações fixas sobre petshops próximos.
   - A entrada das informações foi dividida em 3 caixas de texto para facilitar a utilização do usuário.

3. **Back End:**
   - Implementação de um servidor Flask para lidar com as requisições.
   - Cálculo do melhor petshop com base no menor preço oferecido, levando a distância em consideração nos casos de empate.

4. **Comunicação entre Front end e Back end:**
   - Integração entre o frontend e backend é feita via AJAX usando jQuery.

### Outras Informações

- **Arquivos:**
  - `main.py`: Backend Flask.
  - `index.html`: Página principal com formulário e apresentação dos resultados.
  - `script.js`: Script jQuery para interação entre frontend e backend.

- **Observações:**
  - O código possui alguns comentários para facilitar a compreensão.

- **Autor:**
  - Vinícius Augusto Gomes de Oliveira
