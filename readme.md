1. Matriks Pengukuran
   Matriks pengukuran adalah jenis matriks dengan indeks (i, j) yang merepresentasikan suatu titik koordinat. Setiap elemen dari matriks ini merepresentasikan hasil pengukuran pada suatu titik koordinat tertentu dan merupakan bilangan real atau tipe data float.
2. Matriks Satuan
   Selanjutnya adalah matriks satuan yang merupakan matriks dengan elemen bernilai hanya 0 atau 1. Setiap elemen matriks ini bertipe data integer.

> Machine Learning
> Akses Elemen Matriks

```
Jika kita ingin mengakses nilai 12 pada matriks di atas, nilai tersebut berada pada indeks baris ke-2 dan indeks kolom ke-1. Dalam pemrograman,
nilai tersebut bisa diasumsikan dengan "[2][1]" dengan nilai 2 adalah indeks atau nomor baris dan nilai 1 adalah indeks atau nomor kolom.
```

> Operasi Matriks pada Python

```
Operasi 1 matriks:
    - Menghitung total semua elemen matriks.
    - Mengalikan elemen matriks dengan konstanta.
    - Transpose matriks.
    - Inverse matriks.
    - Menentukan determinan, dan sebagainya.

Operasi 2 matriks:
    - Menambahkan dua matriks.
    - Mengalikan dua matriks.
    - Pembagian dua matriks, dan sebagainya.
```

> Object

```
    - umpamakan kelas adalah bentuk abstrak dari objek, layaknya cetakan atau blueprint. Saat kelas diwujudkan menjadi bentuk yang lebih nyata, proses ini disebut sebagai instansiasi. Itulah sebabnya objek disebut juga sebagai instance atau instance of the class.
```

> Atribut

```
 - jenis atribut kelas yang dapat dibagi, yaitu atribut kelas dan atribut objek atau instance.
    - Atribut kelas adalah jenis atribut yang secara otomatis terdefinisi dan menjadi bawaan kelas ketika instance dibuat berdasarkan kelas tersebut. Anda dapat menganggapnya sebagai nilai default atau bawaan dari kelas. Jika Anda membuat beberapa objek berdasarkan kelas yang memiliki jenis atribut ini, setiap objek akan memiliki atribut yang sama dengan nilai yang sama.
```

> Method

- Ada tiga jenis method
  - Metode dari object (object method).
  - Metode secara statis (static method).
  - Metode dari class (class method).

> Class Constructor

```
Pembangun kelas atau class constructor adalah sebuah fungsi khusus dalam Python yang digunakan untuk menentukan nilai awal atau kondisi awal dari suatu kelas. Dengan fungsi ini, saat kita melakukan proses instansiasi atau pembuatan objek baru, hal pertama yang dilakukan adalah memanggilnya terlebih dahulu.
```

- Example Code

```
{
    class Mobil:
        def __init__(self):
            self.warna = 'Merah'
}
```

- fungsi bernama "**init**" sebagai fungsi khusus untuk menjadi constructor. Selanjutnya, kita menggunakan parameter self, yakni sebuah kata kunci untuk merujuk pada objek yang sedang diproses saat ini.
