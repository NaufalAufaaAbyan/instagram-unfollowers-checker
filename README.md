# Pengecek Unfollowers Instagram

Ini adalah aplikasi web sederhana yang dibangun dengan Flask yang memungkinkan Anda untuk memeriksa unfollowers Instagram Anda dan pengguna yang tidak Anda ikuti kembali. Aplikasi ini memuat data dari file JSON dan menampilkan hasilnya dalam antarmuka yang ramah pengguna.

## Fitur

- Menampilkan jumlah total pengguna yang Anda ikuti.
- Menampilkan jumlah total pengikut Anda.
- Menampilkan jumlah pengguna yang tidak mengikuti Anda kembali.
- Menampilkan jumlah pengguna yang tidak Anda ikuti kembali.
- Menampilkan daftar pengguna yang tidak mengikuti Anda kembali.
- Menampilkan daftar pengguna yang tidak Anda ikuti kembali.

## Struktur Proyek

- `files_json/`: Folder yang berisi file JSON dengan data followers dan following.
- `main.py`: File aplikasi Flask utama.
- `static/styles.css`: CSS kustom untuk styling aplikasi.
- `templates/index.html`: Template HTML untuk menampilkan hasil.

## Persyaratan

- Python 3.x
- Flask

## Instalasi

1. Clone repositori ini:
    ```sh
    git clone https://github.com/NaufalAufaaAbyan/instagram-unfollowers-checker.git
    cd instagram-unfollowers-checker
    ```

2. Instal dependensi yang diperlukan:
    ```sh
    pip install flask
    ```

3. Salin file followers_1.json dan following.json Anda ke dalam folder `files_json`.

## Cara Menjalankan

1. Jalankan aplikasi Flask:
    ```sh
    python main.py
    ```

2. Buka browser web Anda dan pergi ke `http://127.0.0.1:5000/` untuk melihat aplikasi.

## Catatan

Kode ini mungkin tidak sepenuhnya akurat, jadi tolong periksa lagi data followers dan following Anda. Jika Anda mengalami masalah, silakan modifikasi kode sesuai kebutuhan Anda.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT.

## Hak Cipta

Copyright © 2025 Naufal Aufaa Abyan

## Kontribusi

Kontribusi sangat diterima! Jika Anda memiliki saran atau perbaikan, silakan buat pull request atau buka issue.


============================================================================


# Instagram Unfollowers Checker

This is a simple web application built with Flask that allows you to check your Instagram unfollowers and users you don't follow back. The application loads data from JSON files and displays the results in a user-friendly interface.

## Features

- Display the total number of users you follow.
- Display the total number of your followers.
- Display the number of users who don't follow you back.
- Display the number of users you don't follow back.
- Display a list of users who don't follow you back.
- Display a list of users you don't follow back.

## Project Structure

- `files_json/`: Folder containing JSON files with followers and following data.
- `main.py`: Main Flask application file.
- `static/styles.css`: Custom CSS for styling the application.
- `templates/index.html`: HTML template for rendering the results.

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/NaufalAufaaAbyan/instagram-unfollowers-checker.git
    cd instagram-unfollowers-checker
    ```

2. Install the required dependencies:
    ```sh
    pip install flask
    ```

3. Copy the followers_1.json and following.json files into the `files_json` folder

## How to Run

1. Run the Flask application:
    ```sh
    python main.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to view the application.

## Note

This code may not be fully accurate, so please double-check your followers and following data. If you encounter any issues, feel free to modify the code to suit your needs.

## License

This project is licensed under the MIT License.

## Contribution

Contributions are welcome! If you have suggestions or improvements, please create a pull request or open an issue.
