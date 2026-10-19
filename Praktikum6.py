import tkinter as tk

# ---------- Fungsi ----------
def hasil_prediksi():
    # Apapun input yang diberikan, hasilnya selalu Teknologi Informasi
    label_hasil.config(text="Teknologi Informasi")


# ---------- Jendela Utama ----------
root = tk.Tk()
root.title("Prediksi Prodi Pilihan")
root.geometry("480x470")
root.resizable(False, False)
root.configure(bg="#f0f4f8")

# ---------- Label Judul ----------
label_judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 16, "bold"),
    bg="#f0f4f8",
    fg="#1f3a5f",
)
label_judul.pack(pady=(20, 10))

# ---------- Frame Input (10 nilai mata pelajaran) ----------
frame_input = tk.Frame(root, bg="#f0f4f8")
frame_input.pack(pady=10)

mapel = [
    "Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia",
    "Biologi", "Ekonomi", "Geografi", "Sejarah", "Sosiologi",
]

entries = []
for i, nama in enumerate(mapel):
    kolom = (i // 5) * 2      # 5 baris per kolom -> 2 kolom
    baris = i % 5
    tk.Label(frame_input, text=nama + ":", font=("Arial", 10),
            bg="#f0f4f8", anchor="e", width=16).grid(
        row=baris, column=kolom, padx=(10, 4), pady=6, sticky="e")
    e = tk.Entry(frame_input, width=8, justify="center", font=("Arial", 10))
    e.grid(row=baris, column=kolom + 1, padx=(0, 15), pady=6)
    entries.append(e)

# ---------- Button ----------
btn_prediksi = tk.Button(
    root,
    text="Hasil Prediksi",
    font=("Arial", 11, "bold"),
    bg="#2e7d32",
    fg="white",
    padx=20,
    pady=6,
    command=hasil_prediksi,
)
btn_prediksi.pack(pady=15)

# ---------- Label Luaran Hasil Prediksi ----------
label_hasil = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#ffffff",
    fg="#c62828",
    width=30,
    height=2,
    relief="groove",
)
label_hasil.pack(pady=5)

root.mainloop()