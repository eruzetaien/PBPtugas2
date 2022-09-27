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
5. Membuat file respon HTML
  a. todolist, halaman utama berisi tabel todolist dari user
  b. login
  c. register
  d. create_task, halaman form untuk menambah task baru
6. Melakukan routing dengan memetakan fungsi view di file urls.py dalam folder todolist dan menambahkan alamat todolist pada file urls.py di folder project_django 

[Tugas 2](Tugas2.md)
[Tugas 3](Tugas3.md)
