# Composition


class Chocolate():

    def __init__(self):
        self.numberOfPiecesLeft = 10

    def eatPiece(self):
        self.numberOfPiecesLeft -= 1


class Child():

    def __init__(self, name):
        self.choc = Chocolate()
        self.name = name

    def eatXPiecesOfChocolate(self, x):
        for i in range(x):
            self.choc.eatPiece()
            print(f"""
You now have {getattr(self.choc, 'numberOfPiecesLeft')}
pieces of chocolate left.
                   """)


boy = Child(name='Wilson')
print(f"""
You start of with
{getattr(boy.choc, 'numberOfPiecesLeft')} pieces.""")
boy.eatXPiecesOfChocolate(x=4)
