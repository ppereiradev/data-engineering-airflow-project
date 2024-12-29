import pandas as pd

df = pd.read_csv("/airflow-core/data/raw/data.csv")

# Nome da tabela
table_name = "person"

# Geração do SQL
sql_statements = []
sql_statements.append(f"INSERT INTO {table_name} (name, age, street, city, state, zip, lng, lat) VALUES")

for i, row in df.iterrows():
    values = ', '.join(
        f"'{value}'" if isinstance(value, str) else str(value)
        for value in row
    )
    sql_statements.append(f"({values}),")

# Remove a última vírgula e adiciona um ponto e vírgula
sql_statements[-1] = sql_statements[-1][:-1] + ';'

# Salva o SQL em um arquivo
output_file = "/airflow-core/dags/sql/populate_person_table.sql"
with open(output_file, "w") as f:
    f.write('\n'.join(sql_statements))

print(f"Arquivo SQL salvo como {output_file}")
