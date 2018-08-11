class Calculator:
    def add(self,a,b):
        self.a = a
        self.b = b
        return self.a + self.b
    def sub(self,a,b):
        self.a = a
        self.b = b
        return self.a - self.b
    def mul(self,a,b):
        self.a = a
        self.b = b
        return self.a * self.b
    def div(self,a,b):
        self.a = a
        self.b = b
        return self.a / self.b
calc = Calculator()