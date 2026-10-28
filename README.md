# BloxGen Multi-Key Client

Klien CLI sederhana untuk memilih salah satu API key yang disimpan di `.env`.
Setiap kali dijalankan, program hanya mengirim **satu** request generate setelah konfirmasi.
Program tidak merotasi key otomatis, tidak mencetak API key, password, atau cookie.

## Instalasi (Windows)

1. Instal Python 3.10+.
2. Buka terminal di folder ini.
3. Jalankan:

   ```powershell
   py -m pip install -r requirements.txt
   ```

4. Isi `.env`:

   ```dotenv
   BLOXGEN_API_KEY_1=API_KEY_PERTAMA
   BLOXGEN_API_KEY_2=API_KEY_KEDUA
   BLOXGEN_API_KEY_3=API_KEY_KETIGA
   ```

5. Jalankan:

   ```powershell
   py main.py
   ```

6. Pilih nomor key, tipe yang didukung, lalu konfirmasi request.

## Catatan

- Endpoint berdasarkan dokumentasi yang diberikan: `https://core.bloxgen.net/api/generate`.
- Contoh payload: `{"apiKey": "...", "type": "alt"}`.
- Untuk tipe selain `alt`, masukkan identifier persis seperti yang ditentukan dokumentasi resmi. Jika tidak yakin, tes dengan `alt` terlebih dahulu.
- `.env` berisi rahasia. Jangan unggah atau kirim file itu ke orang lain.
