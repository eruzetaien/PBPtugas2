# Tugas 5
## [Halaman Tugas](https://heshturia.herokuapp.com/todolist)

Perbedaan Inline, Internal, dan External CSS ada pada penempatannya, Inline CSS ditempatkan pada tag elemen tertentu, Internal CSS ditempatkan di dalam tag head HTML, dan External CSS ditempatkan di file yang berbeda dengan file HTML. Karena penempatan tersebut, inline CSS hanya bisa diterapkan untuk satu elemen tertentu saja, internal CSS dapat diterapkan pada banyak elemen menggunakan selector, tetapi terbatas hanya untuk satu halaman html. Sedangkan, external CSS dapat diterapkan untuk banyak halaman CSS 

Tag HTML :  
<head> untuk menyimpan metadata, dapat berisi tag <title> judul halaman, <style> inline CSS, <link> external CSS.
<body> untuk menyimpan data yang akan ditampilkan di halaman, dapat berisi tag :    
- Header dengan berbagai macam ukuran h1,h2, dst.  
- <p> untuk membuat paragraf  
- <br> untuk membuat garis baru (enter)  
- <img> untuk menampilkan gambar  
- <form> untuk mengumpulkan input pengguna  
- <a> untuk membuat link ke halaman tertentu  

Tipe tipe Selector 
1. Element selector, Melakukan styling pada tag html tertentu  
2. ID Selector,  Melakukan styling pada ID tertentu, ID pada file HTML harus unik, sehingga ID selector dapat digunakan untuk menggantikan fungsi inline CSS.  
3. Class Selector, Melakukan styling pada class tertentu, karena class tidak harus unik maka class selector dapat dimanfaatkan untuk melakukan styling pada tag html yang berbeda

Implementasi 
Untuk mempercantik halaman web saya menggunakan framework bootstrap. Beberapa untuk beberapa halaman seperti login dan register saya menggunakan template yang sudah tersedia di internet. Untuk menggunakan bootstrap, hanya perlu menambahkan style yang kita inginkan pada attribut class elemen tertentu, contohnya untuk memperbagus input berupa submit form kita dapat menambahkan class .btn dan .btn-primary, input tersebut akan secara otomatis melakukan styling seperti yang kita inginkan. beberapa class pada bootstrap dapat kita atur secara manual, seperti .d-flex .justify-content-center kita dapat melakukannya secara manual dengan attribut display dan justify-content pada css.  


# Tugas 4  
{% csrf_token %} pada elemen <form> berfungsi untuk membuat token yang akan digunakan untuk melakukan autentikasi pengguna. token akan selalu diperbarui ketika mengakses halaman. Jika kita tidak menyediakan kode tersebut, maka aplikasi kita berpotensi terkena serangan Cross Site Request Forgery (CSRF), dimana serangan tersebut akan memaksa pengguna untuk melakukan aksi yang tidak diinginkan, seperti mengganti password akun, secara tidak sadar

Untuk mebuat element form secara manual, kita perlu menggunakan tag <form> untuk menandakan kita sedang mengumpulkan input untuk dikirim ke server. Dalam tag <form> kita perlu mengisi atribut method (GET/POST) dan atribut action berisi alamat dimana data akan dikirim. Selanjutnya adalah membuat elemen <input> di dalam <form>, tipe dari elemnen input beragam, seperti text, radio button, checkbox, submit, dan, button.

ALur dari program tugas 4 ini dimulai dari request pengguna ke server, lalu server akan meresponnya dan menampilkan halaman html yang berisi form di dalamnya. Setelah itu, pengguna akan mengisi data pada form tersebut dan melakukan request sekali lagi lengkap dengan method dan alamat url tujuan tempat data akan dikirim. Pihak server akan menyimpan data dari pengguna ke database serta menggunakannya untuk memperbarui halaman html yang akan ditampilkan ke pengguna.

Langkah pengimplementasian tugas 4:  
1. Membuat folder aplikasi bernama todolist dengan menggunakan fungsi startapp 
2. Membuat sebuah class model Task dengan attribut sesuai pemintaan pada tugas 4
3. Memanggil fungsi makemigrations dan migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django.
4. Membuat fungsi pada file views   
  a. show_todolist, fungsi untuk halaman utama menampilkan semua task user  
  b. register, membuat akun user dengan menggunakan form django UserCreationForm()  
  c. login_user, menggunakan fungsi authenticate() untuk autentifikasi username dan password    
  d. logout_user, menggunakan fungsi logout() dari django, mengarahkan ke halaman login  
  e. create task, menggunakan form CreateTask() dari file forms.py, digunakan untuk membuat task baru, form berupa input text judul dan dekskripsi task  
  f. change_status, mengubah atribut is_finished pada objek Task  
  g. delete, menghapus objek task 
6. Meretriksi akses halaman utama, sehingga memerlukan login terlebih dahulu. dan menambahkan cookies, sehingga user tidak perlu login berulang kali ketika mengakses halaman
7. Membuat file respon HTML  
  a. todolist, halaman utama berisi tabel todolist dari user  
  b. login  
  c. register  
  d. create_task, halaman form untuk menambah task baru  
8. Melakukan routing dengan memetakan fungsi view di file urls.py dalam folder todolist dan menambahkan alamat todolist pada file urls.py di folder project_django   

[Tugas 2](Tugas2.md)
[Tugas 3](Tugas3.md)
