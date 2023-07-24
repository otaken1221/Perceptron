import sys


class Parceptron:
    def __init__(self, X, p, w):
      self.X = X
      self.p = p
      self.w = w
      self.c = 1

    def g(self, x):
      g=0
      for i in range(len(x)-1):
        g += self.w[i] * x[i]

      return g

    def X_first(self, X):
      for x in X:
        x.insert(0, 1)

      return X

    def train(self):
      w_dash = self.w
      self.X = self.X_first(self.X)
      while(True):
        flag = False
        for x in self.X:
          g = self.g(x)
          if x[-1] == 1:
            if g <= 0:
              w_dash[0] += self.p * x[0]
              w_dash[1] += self.p * x[1]
              w_dash[2] += self.p * x[2]
              w_dash[3] += self.p * x[3]
              self.w = w_dash    
              flag = True

          elif x[-1] == 2:
            if g >= 0:
              w_dash[0] -= self.p * x[0]
              w_dash[1] -= self.p * x[1]
              w_dash[2] -= self.p * x[2]
              w_dash[3] -= self.p * x[3]
              self.w = w_dash  
              flag = True

          print(f"epoch={self.c}, class={x[-1]}, x={x}, w={self.w}, g={g} w_dash={w_dash}")

        if flag:
            self.c += 1
            print()
            print("================================================================================================")
            print()

        else:
          print()
          print(f"w={self.w}, epoch={self.c}")
          sys.exit()

if __name__ == '__main__':
  X = [[13,5,10,1],
      [8,2,-7,1],
      [18,8,1,1],
      [2,5,5,2],
      [2,7,-1,2],
      [9,7,2,2]
      ]
  p = 1
  w = [1,1,1,1]
  parceptron = Parceptron(X, p, w)
  parceptron.train()