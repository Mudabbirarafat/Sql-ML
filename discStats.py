import pandas as pd

df = pd.read_csv(r"C:\Users\MUDABBIR\Downloads\housing.csv")

print("\nDescriptive statistics for numerical columns:")
print(df.describe())

print("\nDescriptive statistics for all columns (including categorical):")
print(df.describe(include='all'))

if 'ocean_proximity' in df.columns:
    print("\nValue counts for ocean_proximity:")
    print(df['ocean_proximity'].value_counts())

if 'median_house_value' in df.columns:
    print("\nIndividual statistics for 'median_house_value':")
    print(f"Mean: {df['median_house_value'].mean():.2f}")
    print(f"Median: {df['median_house_value'].median():.2f}")
    print(f"Mode: {df['median_house_value'].mode()[0]:.2f}")
    print(f"Standard Deviation: {df['median_house_value'].std():.2f}")

if 'housing_median_age' in df.columns:
    print("\nIndividual statistics for 'housing_median_age':")
    print(f"Mean: {df['housing_median_age'].mean():.2f}")
    print(f"Median: {df['housing_median_age'].median():.2f}")
    print(f"Mode: {df['housing_median_age'].mode()[0]:.2f}")