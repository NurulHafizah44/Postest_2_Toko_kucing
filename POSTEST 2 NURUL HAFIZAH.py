print("Selamat datang di 'SKY CATSHOP', selamat berbelanja!")
print("----------------------------------------------------")
data_produk = {
    'dry food': [
        ['whiskas', 'tuna, salmon,', '(1+ years),', '1 kg', 34000],
        ['bolt', 'tuna, salmon,', '(1+years),', '1kg', 24000],
        ['excel', 'tuna, salmon,', '(1+years),', '1kg', 27000]
    ],
    'wet food': [
        ['whiskas', 'tuna, salmon,', '(2-12 bulan), (1+ years)', '85 g', 6000],
        ['me-o', 'tuna, salmon,', '(2-12 bulan), (1+ years)', '80g', 7000],
        ['Life cat', 'tuna, salmon,', '(2-12 bulan), (1+ years)', '85 g', 6000]
    ],
    'perlengkapan lainnya': [
        ['Sisir,', 5000],
        ['Potong kuku kucing,', 10000],
        ['Tempat makan dan minum (2 in 1),', 15000],
        ['Mainan bulu ayam,', 7000],
        ['Kalung kucing,', 12000],
        ['Mainan squeeze(berbunyi),', 4000],
        ['Litter box S,', 15000],
        ['Litter box M,', 18000],
        ['Litter box L,', 25000]
    ]
}

akun = {
    'admin': 'admin',
    'pembeli': 'pembeli'
}

def tampil_produk():
    for kategori, produk in data_produk.items():
        print(f"\n{kategori.upper()}:")
        for idx, item in enumerate(produk, 1):
            detail_produk = ' '.join(str(detail) for detail in item)
            print(f"{idx}. {detail_produk}")


def admin_mode():
    while True:
        print("Selamat datang Admin Sky Catshop!")
        print("---------------------------------")
        tampil_produk()
        print("\n1. Tambah Produk\n2. Edit Produk\n3. Hapus Produk\n4. Kembali")
        pilihan = input("Pilih (1-4): ")

        if pilihan == '1':
            kategori = input("Masukkan kategori produk: ").lower()
            nama = input("Nama produk: ")
            detail = input("Detail produk (pisahkan dengan koma): ").split(',')
            detail = [d.strip() for d in detail]
            harga = int(input("Harga: "))
            data_produk[kategori].append([nama] + detail + [harga])

        elif pilihan == '2':
            kategori = input("Masukkan kategori produk yang ingin diedit: ").lower()
            no_produk = int(input("Nomor produk yang ingin diedit: "))
            item = data_produk[kategori][no_produk-1]
            print(f"Edit produk: {item}")
            item[0] = input("Nama baru: ")
            detail = input("Detail produk baru (pisahkan dengan koma): ").split(',')
            item[1:-1] = [d.strip() for d in detail]
            item[-1] = int(input("Harga baru: "))

        elif pilihan == '3':
            kategori = input("Masukkan kategori produk yang ingin dihapus: ").lower()
            no_produk = int(input("Nomor produk yang ingin dihapus: "))
            del data_produk[kategori][no_produk-1]

        elif pilihan == '4':
            break

def pembeli_mode():
    keranjang = []

    while True:
        print("Selamat datang pelanggan Sky Catshop!")
        print("-------------------------------------")
        tampil_produk()
        print("\n1. Tambah ke keranjang\n2. Lihat keranjang\n3. Checkout\n4. Kembali")
        pilihan = input("Pilih (1-4): ")

        if pilihan == '1':
            kategori = input("Pilih kategori: ").lower()
            no_produk = int(input("Nomor produk: "))
            qty = int(input("Jumlah: "))
            keranjang.append([kategori, no_produk, qty])

        elif pilihan == '2':
            total_harga = 0
            print("\nKeranjang:")
            for item in keranjang:
                kategori, no_produk, qty = item
                produk = data_produk[kategori][no_produk-1]
                print(f"{produk[0]} {qty} x {produk[-1]} = {qty*produk[-1]}")
                total_harga += qty*produk[-1]
            print(f"Total: {total_harga}")

        elif pilihan == '3':
            total_harga = 0
            print("\nCheckout:")
            for item in keranjang:
                kategori, no_produk, qty = item
                produk = data_produk[kategori][no_produk-1]
                print(f"{produk[0]} {qty} x {produk[-1]} = {qty*produk[-1]}")
                total_harga += qty*produk[-1]
            print(f"Total: {total_harga}")
            bayar = int(input("Bayar: "))
            if bayar >= total_harga:
                print(f"Kembali: {bayar - total_harga}")
                keranjang.clear()
                print("Terimakasih telah berbelanja dengan kami, silahkan datang kembali!")
            else:
                print("Uang tidak cukup")

        elif pilihan == '4':
            break

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in akun and akun[username] == password:
        if username == 'admin':
            return 'admin'
        elif username == 'pembeli':
            return 'pembeli'
    return None

def main():
    role = login()
    if role:
        if role == 'admin':
            admin_mode()
        elif role == 'pembeli':
            pembeli_mode()
    else:
        print("Login gagal.")

if __name__ == '__main__':
    main()