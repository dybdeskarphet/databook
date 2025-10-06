# %% [markdown]
# # Başlangıç

# Kütüphanelerimizi aktaralım.

# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

# %% [markdown]
# Sonrasında ise veri tabanımızla alakalı hazırlıklarımızı yapalım.

# %%
matplotlib.use("TkAgg")
df = pd.read_csv("data/IMBD.csv")

# %% [markdown]
# Film süresi ile alakalı veriyi _... min_ `string` veri tipinden, analiz yaparken kullanabileceğimiz bir `float` tablosuna dönüştürelim.

# %%
df["duration"] = df["duration"].str.replace(" min", "", regex=False).astype(float)
df["year_start"] = df["year"].str.extract(r"(\d{4})").fillna(0).astype(int)
df = df[~df["year_start"].isin([0])]
df["decade"] = (df["year_start"] // 10) * 10
print(df["decade"])

# %% [markdown]
# Filmin çıktığı yılı tanımlayalım. Sonrasında ise filmin çıkış yılı ve iMDB oyu arasındaki bağlantıyı görelim.

# %%
year_avg = df.groupby("decade")["rating"].mean().reset_index()
year_rating_fig, year_rating_ax = plt.subplots(figsize=[6, 4])
year_rating_ax.plot(year_avg["decade"], year_avg["rating"])
plt.show()
