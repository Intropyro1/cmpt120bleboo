#Old McDonald.py
#This program Gives the lyrics to old Mcdonald song

def main():
  for a,n in [("cow","moo"), ("pig", "oink"), ("horse", "nay"), ("sheep", "baa"), ("chicken", "cluck")]:
    verse(a, n)
    print()

def verse(animal, noise):
  refrain1()
  had(animal)
  withx(noise)
  refrain1()

def refrain1():
  print("Old MacDonald had a farm," ,eieio())

def eieio():
  return ("Ee-igh, Ee-igh, Oh!")

def had(animal):
  print("And on that farm he had a", animal+",", eieio())

def withx(noise):
  noisecomma = noise + ","
  noise2 = noisecomma + " "+noise
  print("With a", noise2, "here and a", noise2, "there.")
  print("Here a", noisecomma, "there a", noisecomma,"\neverywhere a", noise2+".")

main()
