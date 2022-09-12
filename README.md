![This is an image](/MVT Django.png/)
Sesuai namanya virtual environment adalah lingkungan virtual yang terisolasi, tertutup, dan tidak bisa diakses dari luar. Alasan kenapa menggunakan virtual environment
ini pada proyek django adalah untuk menjaga konsistensi modul-modul yang digunakan untuk membuat aplikasi. Misalnya, kita membuat aplikasi menggunakan django dan 
berjalan lancar di modul versi 1.9. Namun, ketika django merilis versi terbaru, misal 4.1, dan kita memperbarui modulnya. Ternyata aplikasi kita tidak dapat berjalan
di modul versi terbaru ini. Oleh karena itu, kita menggunakan virtual environment agar aplikasi kita bisa terus berjalan menggunakan modul-modul dengan versi yang 
sesuai yang ada di virtual environment kita. Aplikasi berbasis django tetap bisa berjalan di luar virtual environment apabila aplikasi kita masih sesuai dengan 
modul-modul yang ada secara global.
