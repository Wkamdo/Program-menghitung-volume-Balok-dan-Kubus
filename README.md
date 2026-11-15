# Program Menghitung Volume Balok dan Kubus

Dua skrip Python sederhana untuk menghitung volume balok dan kubus: satu bagian
dengan nilai tetap (*statis*), satu bagian yang meminta masukan pengguna (*dinamis*).
Dibuat sebagai latihan dasar: variabel, operasi aritmetika, dan `input()`.

## Isi repositori

| Berkas | Rumus | Nilai statis di dalam kode | Hasil |
|---|---|---|---|
| `Volume Balok.py` | V = panjang × lebar × tinggi | 20 × 7 × 10 | 1400 |
| `Volume Kubus.py` | V = sisi × sisi × sisi | 10 × 10 × 10 | 1000 |

## Cara menjalankan

Nama berkas memuat spasi, jadi perlu tanda kutip:

```bash
python3 "Volume Balok.py"
python3 "Volume Kubus.py"
```

Contoh sesi nyata untuk balok (masukan 5, 3, 2):

```
1400
Masukkan Nilai Panjang : 5
Masukkan Nilai Lebar : 3
Masukkan Nilai Tinggi : 2
30
```

Baris `1400` adalah hasil bagian statis, lalu `30` adalah hasil perhitungan dari masukan.

## Catatan

- Masukan dibaca dengan `int()`, sehingga **hanya menerima bilangan bulat**. Menulis `5.5` akan berhenti dengan `ValueError`; bila angka desimal diperlukan, ganti `int(...)` menjadi `float(...)`.
- Setiap berkas menjalankan dua bagian berurutan: bagian statis lebih dulu (langsung mencetak hasil), baru bagian dinamis (meminta masukan). Kalau hanya ingin bagian dinamisnya, hapus blok statis di atasnya.
- Belum ada validasi masukan: masukan kosong atau bukan angka akan menghasilkan error.
- Diuji dengan Python 3.14.

---

Repositori ini arsip latihan awal. Versi yang lebih rapi akan memakai fungsi
(`def volume_balok(p, l, t)`), penanganan kesalahan masukan, dan satu berkas `main.py`
yang memilih bangun ruang melalui argumen — tapi untuk latihan pertama, yang penting
sudah jalan.
