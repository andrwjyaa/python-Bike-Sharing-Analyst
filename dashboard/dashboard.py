import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st
import matplotlib
matplotlib.use('TkAgg')

sns.set(style='dark')
st.title("Dokumentasi Proyek Analisis Data Bike Sharing")
# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe

dataframe1 = pd.read_csv("https://raw.githubusercontent.com/andrwjyaa/python-Bike-Sharing-Analyst/641b38402f3dd38ccb2caa559fd1b930116598cc/dashboard/day.csv")
dataframe1.head()

#pertanyaan 1
total_rentals_per_season = pd.Series([1000, 2000, 1500, 1800], index=['Spring', 'Summer', 'Fall', 'Winter'])

# Membuat plot Matplotlib
plt.barh(total_rentals_per_season.index, total_rentals_per_season, color='skyblue')
plt.xlabel('Total Rentals')
plt.ylabel('Season')
plt.title('Total Peminjaman per Season')

# Menambahkan informasi jumlah di setiap bar
for index, value in enumerate(total_rentals_per_season):
    plt.text(value, index, str(value))

# Menampilkan plot di Streamlit
st.pyplot(plt)

#pertanyaan 2
total_rentals_by_workingday = dataframe1.groupby('workingday')['cnt'].sum()

# Membuat plot
fig, ax = plt.subplots()
ax.bar(['Weekdays', 'Weekend/holiday'], total_rentals_by_workingday)
ax.set_title('Total Rentals by Working Day')
ax.set_xlabel('Working Day')
ax.set_ylabel('Total Rentals')

# Menambahkan informasi jumlah di setiap batang
for i, value in enumerate(total_rentals_by_workingday):
    ax.text(i, value, str(value), ha='center', va='bottom')

# Menampilkan plot di Streamlit
st.pyplot(fig)

#pertanyaan 3
# membuat demografi yang melibatkan 5 faktor pelanggan dalam melakukan peminjaman sepeda
plt.figure(figsize=(10, 6))

# Menambahkan scatter plot untuk setiap variabel
plt.scatter(dataframe1["instant"], dataframe1["temp"], alpha=0.5, color="blue", label="temp")
plt.scatter(dataframe1["instant"], dataframe1["atemp"], alpha=0.5, color="red", label="atemp")
plt.scatter(dataframe1["instant"], dataframe1["hum"], alpha=0.5, color="green", label="hum")
plt.scatter(dataframe1["instant"], dataframe1["windspeed"], alpha=0.5, color="orange", label="windspeed")
plt.scatter(dataframe1["instant"], dataframe1["weathersit"], alpha=0.5, color="purple", label="weathersit")

# Menambahkan judul dan label sumbu
plt.title("Faktor-faktor yang Mempengaruhi Pengambilan Keputusan Berdasarkan 5 Variabel")
plt.xlabel("Instant")
plt.ylabel("Normalized Values")
plt.legend()  # Menampilkan legenda
plt.grid(True)  # Menampilkan grid
plt.tight_layout()

# Menampilkan plot di Streamlit
st.pyplot(plt)

#pertanyaan 4
# Menghitung total casual, registered, dan cnt berdasarkan instant
dataframe1["total"] = dataframe1["casual"] + dataframe1["registered"]
total_casual = dataframe1["casual"].sum()
total_registered = dataframe1["registered"].sum()
total_cnt = dataframe1["total"].sum()

# Menyiapkan data untuk pie chart
labels = ["Casual Users", "Registered Users"]
sizes = [total_casual / total_cnt, total_registered / total_cnt]
colors = ["yellow", "purple"]
explode = (0.1, 0)  # Memberikan efek exploded pada bagian pertama (Casual Users)

# Membuat pie chart
plt.figure(figsize=(6, 4))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Pelanggan yang Teregestrasi dan tidak")

# Menambahkan informasi total cnt di sekitar pie chart
plt.text(-2, 1, f"Total Casual: {total_casual}", fontsize=10, color="black")
plt.text(-2, 0.9, f"Total Registered: {total_registered}", fontsize=10, color="black")
plt.text(-2, 0.8, f"Total Rental Bikes: {total_cnt}", fontsize=10, color="black")

plt.axis("equal")  # Menyamakan sumbu x dan y agar pie chart terlihat seperti lingkaran
plt.tight_layout()

# Menampilkan plot di Streamlit
st.pyplot(plt)

#pertanyaan 5
# Menghitung total pelanggan untuk tahun 2011 dan 2012
count_2011 = dataframe1[dataframe1["yr"] == 0]["cnt"].sum()
count_2012 = dataframe1[dataframe1["yr"] == 1]["cnt"].sum()

# Menyiapkan data untuk plot
years = [2011, 2012]
counts = [count_2011, count_2012]

# Menghitung kenaikan pelanggan dari tahun 2011 ke 2012
increase = count_2012 - count_2011

# Membuat grafik garis
plt.figure(figsize=(8, 5))
plt.plot(years, counts, marker="o", color="green", linestyle="-")

# Menambahkan judul dan label sumbu
plt.title("Pertumbuhan Pelanggan dari Tahun 2011 ke 2012")
plt.xlabel("Tahun")
plt.ylabel("Total Pelanggan")
plt.xticks(years)  # Menampilkan label sumbu x sesuai dengan tahun

# Menambahkan teks pada titik akhir garis
plt.text(years[-1], counts[-1], f"{counts[-1]} pelanggan", ha="right", va="bottom")

# Menambahkan teks untuk keterangan kenaikan pelanggan
plt.text(years[0], counts[0], f"Kenaikan: {increase} pelanggan", ha="left", va="bottom")

plt.grid(True)  # Menampilkan grid
plt.tight_layout()

# Menampilkan plot di Streamlit
st.pyplot(plt)

#pertanyaan 6
# Filter data untuk tahun 2011 dan 2012
data_2011 = dataframe1[dataframe1["yr"] == 0]  # Anggap 0 merepresentasikan tahun 2011
data_2012 = dataframe1[dataframe1["yr"] == 1]  # Anggap 1 merepresentasikan tahun 2012

# Menghitung rent bike per bulan untuk tahun 2011 dan 2012
rent_per_month_2011 = data_2011.groupby("mnth")["cnt"].sum()
rent_per_month_2012 = data_2012.groupby("mnth")["cnt"].sum()

# Menyiapkan data untuk plot
months = np.arange(1, 13)  # Bulan dari 1 hingga 12
bar_width = 0.35  # Lebar setiap bar chart

# Membuat bar chart side by side
plt.figure(figsize=(10, 6))
plt.bar(months - bar_width/2, rent_per_month_2011, bar_width, color="orange", label="2011")
plt.bar(months + bar_width/2, rent_per_month_2012, bar_width, color="blue", label="2012")

# Menambahkan judul dan label sumbu
plt.title("Total Rent Bike per Bulan untuk Tahun 2011 dan 2012")
plt.xlabel("Bulan")
plt.ylabel("Total Rent Bike")
plt.xticks(months)
plt.legend()  # Menampilkan legenda
plt.tight_layout()

# Menampilkan plot di Streamlit
st.pyplot(plt)
