class node :
    def __init__(self, nama_mhs) :
        self.nama_mhs = nama_mhs
        self.next = None

def cetak(n) :
    temp = n
    while temp :
        print (' {} '.format(temp.nama_mhs), end='')
        temp = temp.next

    print('')

if __name__ == '__main__' :
    first = node('Yanto')
    middle = node('Yuli')
    last = node('Katno')

    first.next = middle
    middle.next = last

    cetak(first)