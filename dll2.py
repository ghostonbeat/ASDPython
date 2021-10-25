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
            print (' {} '.format(temp.nama_mhs))
            temp = temp.next

        temp = n
        while temp :
            print (' {} '.format(temp.nama_mhs))
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