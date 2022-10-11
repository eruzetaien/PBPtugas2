# Tugas 6
## [Halaman Tugas](https://heshturia.herokuapp.com/todolist)


Perbedaan dari asynchronous programming dengan synchronous programming adalah bagaimana alur berjalannya dari program-program. Pada synchronous ketika program/kode sedang di jalankan, maka program selanjutnya harus menunggu program sebelumnya selesai untuk bisa dijalankan, permintaan klien akan diblokir untuk memastikan tidak ada program yang berjalan bersamaan. Sedangkan pada asynchronous program tidak perlu menunggu program sebelumnya selesai untuk bisa dijalankan, program-program di asynchronous bisa berjalan secara serentak, sehingga asynchronous lebih cepat dibanding asynchronous. Perbandingannya dapat dilihat dari ilustrasi berikut yang berasal dari situs medium.com.  
![Asynch vs Synch](https://miro.medium.com/proxy/1*V5syja2casc0gCuu9zKV5g.png))  

Event-Driven Programming adalah sebuah pardigma dimana alur program ditentukan oleh suatu event / peristiwa, contoh dari event pada tugas ini adalah tombol add ditekan. Selain komponen event, terdapat pula komponen event handler, yakni komponen yang bertugas melakukan sesuatu ketika terjadi event, contoh dari tugas ini adalah fungsi delete_task yang menjadi event handler ketika tombol delete ditekan. Objek-objek pada paradigma ini bisa berkomunikasi satu sama lain, contoh dari tugas ini adalah ketika tombol add ditekan, maka modal form akan muncul dan ketika tombol close ditekan modal tersebut akan segera hilang. Selain itu, alur program pada Event-Driven Programming berjalan secara loop sambil menunggu terjadinya event. 

Penerapan asynchronous programming pada AJAX adalah kita dapat membuat request secara asynchronous yang berbeda dengan request utama yang biasa kita lakukan ketika me-reload halaman web. Sehingga, dengan request AJAX tersebut, kita dapat menerima response HTML secara asynchronous tanpa perlu mereload keseluruhan halaman.

Implementasi dari tugas ini adalah :  
1. Membuat view untuk mengembalikan seluruh data objek task dalam bentuk JSON.  
2. Data-data tersebut akan digunakan untuk menyusun HTML menggunakan request GET dari ajax, sehingga seluruh objek bisa tampil di halaman web  
3. Membuat request POST ajax dari data form pada modal untuk membuat fitur add task tanpa perlu me-reload halaman page  
4. Melakukan request GET kembali setelah melakukan POST untuk mengupdate halaman web setelah task baru ditambahkan  
5. Membuat fungsi event handler untuk menghapus dan mengubah status task, kedua fungsi ini memerlukan paramater berupa ID objek task yang akan diproses  
6. Lakukan request GET tiap pemanggilan fungsi tersebut untuk mengupdate halaman.
