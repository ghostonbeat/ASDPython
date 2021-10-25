class node :
    def __init__(self, nama_mhs) :
        self.nama_mhs = nama_mhs
        self.next = None
        self.back = None

class link :
    def __init__(self) :
        self.first = None

    def cetak(self, n) :
        print('\nTraversal in forward direction')
        while n :
            print (' {} '.format(n.nama_mhs), end='')
            last = n
            n = n.next

        print('\nTraversal in reverse direction')
        while last :
            print (' {} '.format(last.nama_mhs), end='')
            last = last.back

if __name__ == '__main__' :
    list = link()

    list.first = node('Yanto')
    middle = node('Yuli')
    last = node('Katno')

    list.first.next = middle
    middle.back = list.first
    middle.next = last
    last.back = middle

    list.cetak(list.first)