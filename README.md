# Data Engineering Airflow Project

Este é um projeto de Data Engineering utilizando **Apache Airflow** para orquestrar pipelines de dados, PostgreSQL para armazenar dados, e diversos scripts para ingestão, transformação e carregamento de dados no banco.

## Estrutura de Diretórios

A estrutura de diretórios do projeto é a seguinte:

```bash
data-engineering-airflow-project/
│
├── dags/                        # Definições de DAGs do Airflow
│   ├── __init__.py
│   ├── data_extraction.py       # DAG para extração de dados
│   ├── data_transformation.py   # DAG para transformação de dados
│   └── data_loading.py          # DAG para carregamento de dados no PostgreSQL
│
├── scripts/                     # Scripts auxiliares
│   ├── __init__.py
│   ├── data_ingestion/          # Scripts de ingestão de dados
│   │   ├── source_1.py
│   │   └── source_2.py
│   ├── data_transformation/     # Scripts de transformação de dados
│   │   ├── transform_1.py
│   │   └── transform_2.py
│   └── data_loading/            # Scripts de carregamento de dados no PostgreSQL
│       ├── load_data.py
│       └── utils.py             # Funções auxiliares para conexão ao PostgreSQL
│
├── airflow/                     # Arquivos e configurações específicos do Airflow
│   ├── Dockerfile               # Arquivo para construir o container do Airflow
│   ├── docker-compose.yml       # Arquivo para orquestrar os containers
│   ├── requirements.txt         # Dependências do Airflow e outras dependências
│   └── entrypoint.sh            # Script de inicialização do container
│
├── config/                      # Arquivos de configuração
│   ├── airflow.cfg              # Configurações do Airflow (se não usar configurações padrão)
│   └── postgres_config.yml      # Configuração de acesso ao PostgreSQL
│
├── data/                        # Diretórios para dados temporários e logs
│   ├── raw/                     # Dados brutos (antes de qualquer transformação)
│   ├── processed/               # Dados já processados
│   └── logs/                    # Logs gerados pelos DAGs do Airflow
│
├── tests/                       # Testes automatizados
│   ├── __init__.py
│   ├── test_data_ingestion.py   # Testes para scripts de ingestão de dados
│   ├── test_data_transformation.py # Testes para transformação de dados
│   └── test_data_loading.py      # Testes para o carregamento de dados no PostgreSQL
│
├── env-sample/                  # Arquivos com variáveis de ambiente
│   ├── airflow-core.env-sample
│   ├── airflow-postgres.env-sample   #
│   └── warehouse-postgres.env-sample #
│
├── .gitignore                   # Ignora arquivos temporários e dados sensíveis
├── airflow.env                  # Variáveis de ambiente para o Airflow (ex: senhas, chaves de API)
└── README.md                    # Documentação sobre o projeto
```

## Descrição dos Componentes

### `dags/`

Contém as definições dos DAGs do Airflow, que orquestram os pipelines de dados:

- **`data_ingestion.py`**: DAG para ingestão de dados de fontes externas (APIs, arquivos CSV, bancos de dados externos, etc.).
- **`data_transformation.py`**: DAG para a transformação dos dados, incluindo limpeza, agregação e enriquecimento.
- **`data_loading.py`**: DAG para carregar os dados no banco de dados PostgreSQL.

### `scripts/`

Scripts auxiliares que são executados dentro dos DAGs. Eles são responsáveis por diferentes etapas do pipeline de dados:

- **`data_ingestion/`**: Scripts para ingerir dados de diversas fontes.
- **`data_transformation/`**: Scripts para transformação e processamento dos dados.
- **`data_loading/`**: Scripts para carregar os dados no PostgreSQL, incluindo a conexão ao banco.

### `airflow/`

Contém a configuração e arquivos necessários para executar o Airflow, como o `Dockerfile`, `docker-compose.yml`, `requirements.txt`, e o script de inicialização `entrypoint.sh`.

- **`Dockerfile`**: Arquivo para construir a imagem Docker do Airflow com as dependências necessárias.
- **`docker-compose.yml`**: Arquivo para orquestrar os containers Docker, incluindo o Airflow e o PostgreSQL.
- **`requirements.txt`**: Lista de dependências do Airflow e outras bibliotecas Python necessárias.
- **`entrypoint.sh`**: Script que é executado na inicialização do container, configurando o Airflow e criando o usuário administrativo.

### `config/`

Contém os arquivos de configuração:

- **`airflow.cfg`**: Arquivo de configuração do Airflow (se você optar por não usar as configurações padrão).
- **`postgres_config.yml`**: Arquivo de configuração para conexão ao banco PostgreSQL.

### `data/`

Contém dados temporários e logs gerados pelos DAGs:

- **`raw/`**: Dados não processados que foram ingeridos.
- **`processed/`**: Dados transformados e prontos para serem carregados.
- **`logs/`**: Logs gerados pelo Airflow durante a execução dos DAGs.

### `tests/`

Contém os testes automatizados para garantir que os scripts e DAGs funcionem corretamente:

- **`test_data_ingestion.py`**: Testes para garantir que os scripts de ingestão de dados estão funcionando.
- **`test_data_transformation.py`**: Testes para as transformações realizadas nos dados.
- **`test_data_loading.py`**: Testes para garantir que os dados estão sendo carregados corretamente no PostgreSQL.

### Arquivos Importantes

- **`.gitignore`**: Para evitar o versionamento de arquivos temporários, logs e dados sensíveis.
- **`airflow.env`**: Arquivo de variáveis de ambiente, onde você pode definir senhas, credenciais e outras configurações sensíveis.
- **`README.md`**: Este arquivo, contendo a documentação do projeto.

## Como Rodar o Projeto

Para rodar o projeto, basta seguir os seguintes passos:

1. **Configuração do Docker**:
   - Certifique-se de ter o Docker e o Docker Compose instalados.
   - No diretório principal do projeto, execute o seguinte comando para construir as imagens Docker e iniciar os containers:
     ```bash
     docker-compose up --build
     ```

2. **Acessar o Airflow**:
   - Após a execução dos containers, o Airflow estará disponível no navegador, acessível por:
     - `http://localhost:8080`

3. **Variáveis de Ambiente**:
   - Defina as variáveis de ambiente necessárias no arquivo `.env` para configurar o Airflow e o PostgreSQL.

4. **Executando os Pipelines**:
   - Após a inicialização do Airflow, você pode acionar os DAGs a partir da interface web.

## Contribuição

Se você deseja contribuir com o projeto, siga as etapas abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para a sua feature (`git checkout -b minha-feature`).
3. Realize as alterações e adicione os testes necessários.
4. Faça um commit das suas alterações (`git commit -am 'Adiciona nova feature'`).
5. Envie para o repositório remoto (`git push origin minha-feature`).
6. Crie um pull request para revisão.

## Licença

Este projeto é licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
