from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
features_path = os.getenv("FEATURES_PATH")

df = pd.read_csv(features_path, encoding="latin-1")
print(df.columns, "\n")
#print(df.head())

grouped_df = df.groupby(df.gender)

fem_df = grouped_df.get_group("feminin")
mask_df = grouped_df.get_group("maskulin")
neut_df = grouped_df.get_group("Neutrum")

print("Femininum, 7 häufigste Anfänge:\n", fem_df.first_three.value_counts()[:7], "\n")
print("Maskulinum, 7 häufigste Anfänge:\n", mask_df.first_three.value_counts()[:7], "\n")
print("Neutrum, 7 häufigste Anfänge:\n", neut_df.first_three.value_counts()[:7], "\n")

print("Femininum, 7 häufigste Endungen:\n", fem_df.last_four.value_counts()[:7], "\n")
print("Maskulinum, 7 häufigste Endungen:\n", mask_df.last_four.value_counts()[:7], "\n")
print("Neutrum, 7 häufigste Endungen:\n", neut_df.last_four.value_counts()[:7], "\n")

print("Femininum, Vokal-Konsonant-Verhältnis:\n", fem_df.vc_ratio.value_counts(), "\n")
print("Maskulinum, Vokal-Konsonant-Verhältnis:\n", mask_df.vc_ratio.value_counts(), "\n")
print("Neutrum, Vokal-Konsonant-Verhältnis:\n", neut_df.vc_ratio.value_counts(), "\n")