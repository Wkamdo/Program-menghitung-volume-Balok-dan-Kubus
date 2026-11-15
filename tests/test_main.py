#!/usr/bin/env python3
"""Uji main.py dengan unittest bawaan Python.

Jalankan:  python3 -m unittest discover -s tests -v
"""
import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import main  # noqa: E402


class UjiPerhitungan(unittest.TestCase):
    def test_balok(self):
        self.assertEqual(main.volume_balok(20, 7, 10), 1400)

    def test_kubus(self):
        self.assertEqual(main.volume_kubus(10), 1000)

    def test_desimal(self):
        self.assertAlmostEqual(main.volume_balok(2.5, 4, 1.2), 12.0)


class UjiMasukan(unittest.TestCase):
    def test_tolak_nol_dan_negatif(self):
        for buruk in ("0", "-3", "0,0"):
            with self.assertRaises(main.MasukanTidakValid):
                main._bersihkan(buruk)

    def test_tolak_bukan_angka(self):
        for buruk in ("abc", "", "5x"):
            with self.assertRaises(main.MasukanTidakValid):
                main._bersihkan(buruk)

    def test_terima_koma_desimal(self):
        self.assertEqual(main._bersihkan("2,5"), 2.5)

    def test_tolak_kebesaran(self):
        with self.assertRaises(main.MasukanTidakValid):
            main._bersihkan("1e13")


class UjiCLI(unittest.TestCase):
    def _jalan(self, *argv):
        buf = io.StringIO()
        with redirect_stdout(buf):
            kode = main.main(list(argv))
        return kode, buf.getvalue()

    def test_balok_lewat_argumen(self):
        kode, keluaran = self._jalan("balok", "20", "7", "10")
        self.assertEqual(kode, 0)
        self.assertIn("= 1400", keluaran)

    def test_kubus_lewat_argumen(self):
        kode, keluaran = self._jalan("kubus", "10")
        self.assertEqual(kode, 0)
        self.assertIn("= 1000", keluaran)

    def test_masukan_buruk_keluar_kode_2(self):
        with self.assertRaises(SystemExit) as cm:
            main.main(["kubus", "-5"])
        self.assertEqual(cm.exception.code, 2)

    def test_tanpa_subperintah_memberi_bantuan(self):
        kode, keluaran = self._jalan()
        self.assertEqual(kode, 2)
        self.assertIn("usage", keluaran.lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
