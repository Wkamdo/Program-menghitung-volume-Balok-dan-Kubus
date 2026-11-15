#!/usr/bin/env python3
"""Hitung volume balok dan kubus.

Versi rapi dari latihan awal (lihat `Volume Balok.py` dan `Volume Kubus.py`,
yang tetap disimpan apa adanya sebagai arsip). Bedanya di sini: ada fungsi
terpisah, validasi masukan, kode keluar yang jelas, dan bisa menerima angka
desimal.

Contoh:
    python3 main.py balok 20 7 10      -> 1400
    python3 main.py kubus 10           -> 1000
    python3 main.py balok 2.5 4 1.2    -> 12
    python3 main.py kubus             -> mode tanya-jawab
"""
from __future__ import annotations

import argparse
import sys

BATAS_AKAL = 1e12  # nilai di atas ini hampir pasti salah ketik


class MasukanTidakValid(ValueError):
    """Nilai bukan angka positif yang masuk akal."""


def _bersihkan(teks: str) -> float:
    """Ubah teks jadi angka positif. Terima koma desimal (2,5) juga."""
    asli = teks.strip().replace(",", ".")
    try:
        nilai = float(asli)
    except ValueError:
        raise MasukanTidakValid(f"'{teks}' bukan angka")
    if nilai != nilai or nilai in (float("inf"), float("-inf")):
        raise MasukanTidakValid(f"'{teks}' bukan angka berhingga")
    if nilai <= 0:
        raise MasukanTidakValid(f"{teks} harus lebih besar dari 0")
    if nilai > BATAS_AKAL:
        raise MasukanTidakValid(f"{teks} terlalu besar (batas {BATAS_AKAL:g})")
    return nilai


def _tampil(nilai: float) -> str:
    """1400.0 -> '1400', 12.5 -> '12.5'."""
    return f"{nilai:g}"


def volume_balok(panjang: float, lebar: float, tinggi: float) -> float:
    """V = panjang x lebar x tinggi."""
    return panjang * lebar * tinggi


def volume_kubus(sisi: float) -> float:
    """V = sisi x sisi x sisi."""
    return sisi ** 3


def _tanya(label: str) -> float:
    while True:
        try:
            return _bersihkan(input(f"{label}: "))
        except MasukanTidakValid as e:
            print(f"  ! {e} — coba lagi")
        except EOFError:
            raise SystemExit("\nmasukan dihentikan")


def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        prog="main.py", description="Hitung volume balok dan kubus")
    sub = p.add_subparsers(dest="bangun")

    pb = sub.add_parser("balok", help="volume balok (p x l x t)")
    for nama in ("panjang", "lebar", "tinggi"):
        pb.add_argument(nama, nargs="?", type=_bersihkan)

    pk = sub.add_parser("kubus", help="volume kubus (s^3)")
    pk.add_argument("sisi", nargs="?", type=_bersihkan)

    a = p.parse_args(argv)
    try:
        if a.bangun == "balok":
            if a.panjang is None:
                v = volume_balok(_tanya("Panjang"), _tanya("Lebar"), _tanya("Tinggi"))
                print(f"Volume balok = {_tampil(v)}")
            else:
                v = volume_balok(a.panjang, a.lebar, a.tinggi)
                print(f"Volume balok ({_tampil(a.panjang)} x {_tampil(a.lebar)} x "
                      f"{_tampil(a.tinggi)}) = {_tampil(v)}")
        elif a.bangun == "kubus":
            if a.sisi is None:
                v = volume_kubus(_tanya("Sisi"))
                print(f"Volume kubus = {_tampil(v)}")
            else:
                v = volume_kubus(a.sisi)
                print(f"Volume kubus ({_tampil(a.sisi)}^3) = {_tampil(v)}")
        else:
            p.print_help()
            return 2
    except MasukanTidakValid as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
