import sys
import os
def topological_sort(graph_mk_prasyarat):
    """ Meminta input graph, mengeluarkan order matkul yang bisa diambil berupa list """
    order_diambil = []
    while True:
        graph_mk_prasyarat, mk_diambil = ambil_matkul(graph_mk_prasyarat)
        order_diambil.append(mk_diambil)
        if not (graph_mk_prasyarat):
            break    
    return order_diambil
    
def ambil_matkul(graph_mk_prasyarat):
    """ Meminta input graph, mengeluarkan graph baru tanpa matkul yang diambil, dan matkul yang diambil list"""
    yg_diambil = []
    new_graph_mk_prasyarat = graph_mk_prasyarat.copy()
    for mk,prasyarat in graph_mk_prasyarat.items():
        if len(prasyarat) == 0:
            new_graph_mk_prasyarat = hapus_mk_dan_prasyarat(new_graph_mk_prasyarat,mk)
            yg_diambil.append(mk)
        
    return new_graph_mk_prasyarat, yg_diambil

def hapus_mk_dan_prasyarat(graph_mk_prasyarat,mk):
    """ Menghapus matkul dari graph"""
    graph_mk_prasyarat.pop(mk)
    for matkul,prasyarat in graph_mk_prasyarat.items():
        if mk in prasyarat:
            prasyarat = [x for x in prasyarat if x!=mk]
            graph_mk_prasyarat[matkul] = prasyarat
    return graph_mk_prasyarat

def keluaran(order):
    """ fungsi output """
    romawi = ['I','II','III','IV','V','VI','VII','VIII']
    print ("Urutan mata kuliah yang dapat diambil :")
    order = [", ".join(x) for x in order]
    for i in range(min(len(order),8)):
        print ("SEMESTER {:<3}  : {}".format(romawi[i],str(order[i])))
    if len(order)>8:
        print("Matkul lainnya tidak dapat diambil dalam 8 semester")

def clean(line):
    """ fungsi membersihkan input """
    line = line.split(",")
    line = [x.strip(" \n,.") for x in line]
    return line[0], line[1:]


if __name__ == "__main__":
    graph = {}
    path = "./test/"
    namafile = sys.argv[1]
    with open(os.path.join(path,namafile), "r") as f:
        for line in f:
            mk, prasyarat = clean(line)
            graph[mk] = prasyarat
        f.close()
    order = topological_sort(graph)
    keluaran(order)
    