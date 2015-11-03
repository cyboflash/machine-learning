import numpy

def q2():
  print 10*'=', 'q2', 10*'='
  querry = numpy.array([1,3,2,1,2,1,1])
  querry = querry / numpy.linalg.norm(querry)
  corpus = {1 : numpy.array([7,0,2,1,0,0,1]),
            2 : numpy.array([1,7,0,0,2,0,1]),
            3 : numpy.array([1,0,0,0,7,1,2]),
            4 : numpy.array([0,2,0,0,7,1,1])}

  similarity = {}
  max_v = 0
  max_k = -1
  for k, v in corpus.items():
    v = v / numpy.linalg.norm(v)
    v *= querry
    v = numpy.sum(v)
    similarity[k] = v
    if v > max_v:
      max_v = v
      max_k = k

  print similarity
  print max_k, max_v

def main():
  q2()

if '__main__' == __name__:
  main()
