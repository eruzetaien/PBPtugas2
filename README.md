[Tugas 2](Tugas2.md)

Perbedaan antara html dengan xml dan json adalah fungsinya, html berfungsi untuk menampilkan data. Sedangkan, xml dan json berfungsi untuk menyimpan dan mengirim data. Html menggunakan tag yang sudah didefinisikan sebelumnya untuk struktur penulisannya.

<p> XML, sama seperti HTML, merupakan markup language, sehingga menggunakan tag dalam penulisannya dan lebih struktural. tidak seperti json yang penulisannya menggunakan pasangan name dan value sama seperti attribut objek di JavaScript seusuai namanya, JavaScript ObjectNotation. Kelebihan dari Json dibandingkan XML adalah JSON lebih ringan dan dapatmengirim data berupa array. Namun, dari segi keamanan, XML lebih unggul dibandingkan JSON. </p>

Data delivery penting dalam pengimplementasian sebuah platform karena
dengan itu lah pengguna dapat melihat konten-konten yang kita buat di sebuah
platform. Server mengirimkan data yang akan diterima dan ditampilkan ke pengguna

Langkah pengimplementasian tugas 3:
1. Membuat folder aplikasi bernama mywatchlist. langkah ini bisa dilakukan menggunakan fungsi startapp atau menyalin
folder aplikasi yang sudah pernah dibuat lalu memodifikasinya. 
2. Membuat sebuah class model yang saya beri nama Watchlist dengan attribut sesuai pemintaan pada tugas 3
3. Memanggil fungsi makemigrations dan migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
4. Membuat 10 objek dari class Watchlist di file berformat json pada folder fixtures, lalu memanggil fungsi loaddata
5. Membuat 3 fungsi pada file views.py yaitu, show_watchlist, show_watchlist_xml, show_watchlist_json. masing
masing akan menyajikan data dalam format html, xml, dan json.
6. Membuat file watchlist.html yang akan menjadi response yang ditampilkan untuk format html
7. Menambahkan 3 fungsi yang telah dibuat ke file urls.py pada folder aplikasi untuk memetakan fungsi yang akan dipanggil
berdasarkan alamat yang dituju. dan menambahkan file urls.py tersebut ke file urls.py yang ada pada folder proyek django.
8. Menambahkan kode "release: sh -c 'python manage.py migrate && python manage.py loaddata initial_watchlist_data.json'" agar
platform heroku dapat melakukan loaddata secara otomatis
9. Membuat class di file tests.py untuk melakukan testing, class berisi 3 fungsi akan mengecek apakah permintaan pengguna 
berhasil diterima, dipahami, dan diterima.
