# Program Menghitung Volume Balok dan Kubus

Dua skrip Python sederhana untuk menghitung volume balok dan kubus: satu bagian
dengan nilai tetap (*statis*), satu bagian yang meminta masukan pengguna (*dinamis*).
Dibuat sebagai latihan dasar: variabel, operasi aritmetika, dan `input()`.

## Isi repositori

| Berkas | Rumus | Nilai statis di dalam kode | Hasil |
|---|---|---|---|
| `Volume Balok.py` | V = panjang × lebar × tinggi | 20 × 7 × 10 | 1400 |
| `Volume Kubus.py` | V = sisi × sisi × sisi | 10 × 10 × 10 | 1000 |
| `main.py` | sama, versi rapi | — (lewat argumen) | lihat contoh di bawah |

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

## Versi rapi: `main.py`

Dua berkas di atas adalah arsip latihan awal dan tetap dibiarkan apa adanya. Versi yang
sudah dirapikan ada di `main.py`: fungsi terpisah, validasi masukan, kode keluar yang
jelas, dan bisa menerima angka desimal.

```bash
python3 main.py balok 20 7 10     # Volume balok (20 x 7 x 10) = 1400
python3 main.py kubus 10          # Volume kubus (10^3) = 1000
python3 main.py balok 2.5 4 1,2   # Volume balok (2.5 x 4 x 1.2) = 12
python3 main.py balok             # mode tanya-jawab
```

Aturan masukan di `main.py`:

- angka harus **lebih besar dari 0** — `0` dan `-5` ditolak
- menerima titik maupun koma desimal (`2.5` dan `2,5` sama)
- menolak teks, masukan kosong, dan nilai tak berhingga
- masukan buruk menghasilkan pesan jelas dan kode keluar `2`

Uji otomatis (11 uji, bawaan Python):

```bash
make test                              # 11 uji
python3 -m unittest discover -s tests -v   # sama, tanpa make
```

## Catatan

- Masukan dibaca dengan `int()`, sehingga **hanya menerima bilangan bulat**. Menulis `5.5` akan berhenti dengan `ValueError`; bila angka desimal diperlukan, ganti `int(...)` menjadi `float(...)`.
- Setiap berkas menjalankan dua bagian berurutan: bagian statis lebih dulu (langsung mencetak hasil), baru bagian dinamis (meminta masukan). Kalau hanya ingin bagian dinamisnya, hapus blok statis di atasnya.
- Belum ada validasi masukan: masukan kosong atau bukan angka akan menghasilkan error.
- Diuji dengan Python 3.14.

---

Repo ini dimulai sebagai latihan pertama Python, lalu dirapikan sebagai latihan menulis
kode yang bisa diuji: fungsi terpisah, validasi masukan, dan uji unit. Berkas latihan
aslinya sengaja tidak dihapus supaya perjalanannya kelihatan.
