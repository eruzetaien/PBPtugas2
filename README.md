### Halaman Tugas 3 :
[HTML](https://heshturia.herokuapp.com/mywatchlist/html/)  
[XML](https://heshturia.herokuapp.com/mywatchlist/xml/)  
[JSON](https://heshturia.herokuapp.com/mywatchlist/json/)  

Perbedaan antara html dengan xml dan json adalah fokus fungsinya, html fokus pada bagaimana data ditampilkan di halaman. Sedangkan, xml dan json berfokus untuk menyimpan dan mengirim data saja. Html menggunakan tag yang sudah didefinisikan sebelumnya untuk struktur penulisannya.

XML, sama seperti HTML, merupakan markup language, sehingga menggunakan tag dalam penulisannya dan lebih struktural. tidak seperti json yang penulisannya menggunakan pasangan name dan value sama seperti attribut objek di JavaScript seusuai namanya, JavaScript ObjectNotation. Kelebihan dari Json dibandingkan XML adalah JSON lebih ringan dan dapatmengirim data berupa array. Namun, dari segi keamanan, XML lebih unggul dibandingkan JSON.

Data delivery penting dalam pengimplementasian sebuah platform karenadengan itu lah pengguna dapat melihat konten-konten yang kita buat di sebuah platform. Server mengirimkan data yang akan diterima dan ditampilkan ke pengguna, yang terpenting dari data delivery adalah pengguna tidak perlu memuat halaman penuh untuk menerima suatu data, sehingga waktu akses dan bandwith bisa diminimalisir.


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

#### Screenshoot Postman
##### HTML
[HTML Postman](https://github.com/eruzetaien/PBPtugas2/blob/main/ImgTugas3/SS_HTML_postman.png)
##### XML
[XML Postman](https://github.com/eruzetaien/PBPtugas2/blob/main/ImgTugas3/SS_XML_postman.png)
##### JSON
[JSON Postman](https://github.com/eruzetaien/PBPtugas2/blob/main/ImgTugas3/SS_JSON_postman.png)

[Tugas 2](Tugas2.md)
