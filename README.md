# Pertemuan 13 - Debugging dan Testing
- Nama : Tantri Widya Solehati
- NIM : 2225250114
- Kelas : 3F
## Kasus
Program digunakan untuk:
1. Menghitung rata-rata nilai mahasiswa.
2. Menentukan status kelulusan berdasarkan nilai.
3. Menentukan nilai tertinggi dalam sebuah daftar nilai.
Pada versi awal program ditemukan beberapa bug logika yang menyebabkan hasil perhitungan tidak sesuai dengan yang diharapkan. Proses debugging dilakukan menggunakan tracing, test case, dan pengujian ulang (retest).
## Test Case

| ID | Target | Input | Expected | Actual Awal | Status Awal |
|----|---------|--------|----------|-------------|-------------|
| T1 | hitung_rata_rata | [80,60,90,70] | 75.0 | 60.0 | FAIL |
| T2 | hitung_rata_rata | [100,80] | 90.0 | 36.0 | FAIL |
| T3 | hitung_rata_rata | [] | 0 | Error/ZeroDivisionError | FAIL |
| T4 | status | 60 | Lulus | Tidak lulus | FAIL |
| T5 | status | 59 | Tidak lulus | Tidak lulus | PASS |
| T6 | status | 61 | Lulus | Lulus | PASS |
| T7 | nilai_tertinggi | [80,60,90,70] | 90 | 0 | FAIL |
| T8 | nilai_tertinggi | [100] | 100 | 0 | FAIL |
| T9 | nilai_tertinggi | [] | None | Error | FAIL |

## Bug Report

### Perhitungan Rata-rata Salah

**Gejala**

Nilai rata-rata salah ketika jumlah data bukan 5.

**Contoh**

```python
[80, 60, 90, 70]
```

Expected:

```text
75.0
```

Actual:

```text
60.0
```

**Lokasi**

```python
return sum(nilai) / 5
```

**Akar Penyebab**

Program selalu membagi total dengan angka 5 meskipun jumlah data dapat berbeda.

**Perbaikan**

```python
return sum(nilai) / len(nilai)
```

Ditambah validasi list kosong:

```python
if len(nilai) == 0:
    return 0
```

---

### Batas Kelulusan Salah

**Gejala**

Nilai 60 dianggap tidak lulus.

**Contoh**

```python
status(60)
```

Expected:

```text
Lulus
```

Actual:

```text
Tidak lulus
```

**Lokasi**

```python
if nilai > 60
```

**Akar Penyebab**

Operator `>` tidak memasukkan nilai tepat 60 ke kategori lulus.

**Perbaikan**

```python
if nilai >= 60
```

---

### Nilai Tertinggi Tidak Ditemukan

**Gejala**

Program gagal menemukan nilai terbesar.

**Contoh**

```python
[80, 60, 90, 70]
```

Expected:

```text
90
```

Actual:

```text
0
```

**Lokasi**

```python
tertinggi = 0

for x in nilai:
    if x < tertinggi:
        tertinggi = x
```

**Akar Penyebab**

- Nilai awal tertinggi tidak diambil dari data.
- Operator pembanding menggunakan `<`, sehingga logika pencarian maksimum salah.

**Perbaikan**

```python
tertinggi = nilai[0]

for x in nilai[1:]:
    if x > tertinggi:
        tertinggi = x
```

Ditambah validasi:

```python
if len(nilai) == 0:
    return None
```
## Retest

| ID | Expected | Actual Setelah Perbaikan | Status |
|----|----------|--------------------------|---------|
| T1 | 75.0 | 75.0 | PASS |
| T2 | 90.0 | 90.0 | PASS |
| T3 | 0 | 0 | PASS |
| T4 | Lulus | Lulus | PASS |
| T5 | Tidak lulus | Tidak lulus | PASS |
| T6 | Lulus | Lulus | PASS |
| T7 | 90 | 90 | PASS |
| T8 | 100 | 100 | PASS |
| T9 | None | None | PASS |

---

## Hasil Program

Output:

```text
Rata-rata: 75.0
Status 60: Lulus
Tertinggi: 90
```
## Cara Menjalankan
```bash
python3 praktik/praktik_4_debugging.py
```
## Refleksi
Pada praktik ini saya mempelajari bahwa program yang dapat dijalankan belum tentu menghasilkan output yang benar. Teknik yang paling membantu adalah membuat test case batas, melakukan tracing variabel, dan membandingkan expected result dengan actual result. Dengan debugging yang sistematis, bug dapat ditemukan berdasarkan bukti, bukan tebakan. Selain itu, retest penting dilakukan untuk memastikan bahwa perbaikan tidak menimbulkan bug baru pada bagian program lainnya.