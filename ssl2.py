class node :
    def __init__(self, nama_mhs) :
        self.nama_mhs = nama_mhs
        self.next = None

class link :
    def __init__(self) :
        self.first = None

    def cetak(self) :
        temp = self.first
        while temp :
            print (' {} '.format(temp.nama_mhs), end='')
            temp = temp.next

        print('')

if __name__ == '__main__' :
    list = link()

    list.first = node('Yanto')
    middle = node('Yuli')
    last = node('Katno')

    list.first.next = middle
    middle.next = last

    list.cetak()