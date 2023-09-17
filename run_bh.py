import subprocess
import time
import os
from multiprocessing import Process

def jalankan_skrip(nama_skrip, direktori):
    os.chdir(direktori)  
    subprocess.call(['python', nama_skrip])

def main():
    skrip = [
        {'nama': 'Honkai3rd.py', 'direktori': "./Honkai3rd"}
    ]
    jeda_waktu = 43 * 24 * 60 * 60  

    while True:
        processes = []

        for skrip_info in skrip:
            nama_skrip = skrip_info['nama']
            direktori = skrip_info['direktori']

            print(f"Menjalankan skrip: {nama_skrip}")
            process = Process(target=jalankan_skrip, args=(nama_skrip, direktori))
            process.start()
            processes.append(process)

        for process in processes:
            process.join()

        print(f"Menunggu {jeda_waktu} detik sebelum menjalankan skrip berikutnya.")
        time.sleep(jeda_waktu)

if __name__ == '__main__':
    main()
