import pandas as pd
from sklearn.preprocessing import MinMaxScaler
df = pd.read_csv('C:\\Users\\hp\\OneDrive\\Desktop\\pandas_project\\myvenv\\Traffic_Forecasting_Project\\AI Projects\\top_30_mutual_funds.csv')
print(df.head())
print(df.describe())
print(df['category'].unique())

print(df.isnull().sum())

mean_returns_3yr = df['returns_3yr'].mean()
mean_returns_5yr = df['returns_5yr'].mean()
df['returns_3yr'].fillna(mean_returns_3yr, inplace=True)
df['returns_5yr'].fillna(mean_returns_5yr, inplace=True)
print(df.isnull().sum())
print(mean_returns_3yr, mean_returns_5yr)

columns_to_normalize = ['expense_ratio', 'returns_1yr', 'returns_3yr', 'returns_5yr', 
                        'sharpe', 'sortino', 'alpha', 'beta']
df[columns_to_normalize] = df[columns_to_normalize].replace('-', pd.NA).apply(pd.to_numeric)

scaler = MinMaxScaler()
df_normalized = pd.DataFrame(scaler.fit_transform(df[columns_to_normalize]), columns=columns_to_normalize)

# Adjust metrics where lower is better
df_normalized['expense_ratio'] = 1 - df_normalized['expense_ratio']
df_normalized['beta'] = 1 - df_normalized['beta']
print(df_normalized)

weights = {
    'expense_ratio': 0.2,
    'returns_1yr': 0.15,
    'returns_3yr': 0.15,
    'returns_5yr': 0.15,
    'sharpe': 0.1,
    'sortino': 0.1,
    'alpha': 0.1,
    'beta': 0.05
}

df_normalized['composite_score'] = sum(
    df_normalized[col] * weight for col, weight in weights.items()
)
df['composite_score'] = df_normalized['composite_score']

df['rank'] = df['composite_score'].rank(ascending=False)
df_sorted = df.sort_values(by='rank')
print(df_sorted)

df_top_30 = df_sorted.head(30)
df_top_30.to_csv('top_30_mutual_funds.csv', index=False)
print("Exported top 30 mutual funds to 'top_30_mutual_funds.csv'.")

