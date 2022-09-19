[Tugas 2 PBP](https://heshturia.herokuapp.com/katalog/)
![MVT Django](https://github.com/eruzetaien/PBPtugas2/blob/e14a970fbd4eede404ebfd8cbb182b7eff8683d0/MVT%20Django.png)

Sesuai namanya virtual environment adalah lingkungan virtual yang terisolasi, tertutup, dan tidak bisa diakses dari luar. Alasan kenapa menggunakan virtual environment
ini pada proyek django adalah untuk menjaga konsistensi modul-modul yang digunakan untuk membuat aplikasi. Misalnya, kita membuat aplikasi menggunakan django dan 
berjalan lancar di modul versi 1.9. Namun, ketika django merilis versi terbaru, misal 4.1, dan kita memperbarui modulnya. Ternyata aplikasi kita tidak dapat berjalan
di modul versi terbaru ini. Oleh karena itu, kita menggunakan virtual environment agar aplikasi kita bisa terus berjalan menggunakan modul-modul dengan versi yang 
sesuai yang ada di virtual environment kita. Aplikasi berbasis django tetap bisa berjalan di luar virtual environment apabila aplikasi kita masih sesuai dengan 
modul-modul yang ada secara global.


Pada tugas kali ini saya membuat fungsi di file views.py yang bernama show_katalog yang dapat mengambil data dari model dengan mengimport class CatalogItem dari file 
models.py. Lalu dengan fungsi render, data model tersebut akan dikirim dalam bentuk dictioanry bernama context dan dipetakan ke template. Setelah itu, fungsi tersebut 
akan mengembalikan file html yang akan ditampilkan di browser. Setelah membuat fungsi di file views, tahap selanjutnya adalah membuat routing pada file urls.py dengan 
menambahkan elemen baru berupa path katalog pada list urlpatterns. Hal ini dilakukan untuk mencocokan url yang ada pada list tersebut dengan url yang diminta oleh user. 
Jika cocok dengan aplikasi katalog, maka akan dipanggil fungsi show_katalog yang telah dibuat.
Tahap terakhir adalah melakukan deployment ke Heroku. Untuk melakukannya,perlu menambahkan dua secret pada repository GitHub, yang pertama HEROKU_API_KEY sebagai namanya
dan API key dari Heroku yang dapat ditemukan di Account Setting sebagai valuenya. Yang kedua HEROKU_APP_NAME sebagai namanyadan nama aplikasi heroku sebagai valuenya.
Setelah itu aplikasi akan otomatis di-deploy ke Heroku jika file yang diperlukan seperti Procfile dan dpl.yml sudah tersedia dan setting.py pada proyek django telah 
dikonfigurasi.
