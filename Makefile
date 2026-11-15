.PHONY: test run lint

test:            ## jalankan uji unit (stdlib, tanpa dependensi)
	python3 -m unittest discover -s tests -v

run:             ## contoh pemakaian: make run A="balok 20 7 10"
	python3 main.py $(A)

lint:            ## cek sintaks semua berkas Python
	python3 -m py_compile main.py "Volume Balok.py" "Volume Kubus.py" tests/test_main.py
