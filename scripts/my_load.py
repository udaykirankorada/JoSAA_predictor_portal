import sqlite3
import pandas as pd


file_path = "C:/Users/91630/OneDrive - Indian Institute of Technology Guwahati/Desktop/django/JoSAA/my_data_table/all_IITs_filtered_16_to_23.csv"
df = pd.read_csv(file_path, low_memory=False)


connection = sqlite3.connect('db.sqlite3')


cursor = connection.cursor()
cursor.execute('''
DROP TABLE IF EXISTS MainApp_data
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS MainApp_data (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    institute TEXT,
    Branch TEXT,
    Category TEXT,
    Gender TEXT,
    Opening_rank INTEGER,
    Closing_rank INTEGER,
    year INTEGER,
    round INTEGER
)
''')


df.to_sql('MainApp_data', connection, if_exists='replace', index=False)


connection.commit()


connection.close()
