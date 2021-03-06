class node :
    def __init__(self, nama_mhs) :
        self.nama_mhs = nama_mhs
        self.next = None
        self.back = None

def cetak(m, n) :
    temp = m
    print('\nTraversal in forward direction')
    while temp :
        print (' {} '.format(temp.nama_mhs), end='')
        temp = temp.next

    print('')

    temp = n
    print('\nTraversal in reverse direction')
    while temp :
        print (' {} '.format(temp.nama_mhs), end='')
        temp = temp.back

if __name__ == '__main__' :
    first = node('Yanto')
    middle = node('Yuli')
    last = node('Katno')

    first.next = middle
    middle.back = first
    middle.next = last
    last.back = middle

    cetak(first, last)