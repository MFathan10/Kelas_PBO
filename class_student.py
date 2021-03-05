class student:
    """A class representing a student"""
    jumlah_student = 0

    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        student.jumlah_student = 1

    def tampilkan_jumlah(self):
        print("Total student :", student.jumlah_student)

    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("Umur :", self.umur)

# Membuat objek pertama dari kelas Karyawan
student1 = student("Muhammad Fathan Mubina", 19)

student1.tampilkan_profil()

print("Total student :", student.jumlah_student)