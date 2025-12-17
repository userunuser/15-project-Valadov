import pandas as pd

# Загрузка данных
df = pd.read_csv('winequality-red.csv', sep=';')

# Базовая информация
print(f"Размер датасета: {df.shape}")
print(f"\nПервые 5 строк:")
print(df.head())
print(f"\nИнформация о столбцах:")
print(df.info())
print(f"\nСтатистика по числовым признакам:")
print(df.describe())
print(f"\nЦелевая переменная 'quality':")
print(f"Уникальные значения: {sorted(df['quality'].unique())}")
print(f"Распределение классов:")
print(df['quality'].value_counts().sort_index())