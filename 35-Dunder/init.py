class CountFromBy:
    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incr = i
    def increase(self) -> None:
        self.val += self.incr
    def __repr__(self) -> str:
        return('Nasz obiekt v:'+str(self.val)+' i:'+str(self.incr))

g = CountFromBy(100,10)

print(g.incr)
g.increase()
print(g)


