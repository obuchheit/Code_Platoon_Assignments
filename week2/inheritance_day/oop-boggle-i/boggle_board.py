import random

class BoggleBoard:
  boggle_dice = {
    'die1': [' A ', ' A ', ' E ', ' E ', ' G ', ' N '],
    'die2': [' E ', ' L ', ' R ', ' T ', ' T ', ' Y '],
    'die3': [' A ', ' O ', ' O ', ' T ', ' T ', ' W '],
    'die4': [' A ', ' B ', ' B ', ' J ', ' O ', ' O '],
    'die5': [' E ', ' H ', ' R ', ' T ', ' V ', ' W '],
    'die6': [' C ', ' I ', ' M ', ' O ', ' T ', ' U '],
    'die7': [' D ', ' I ', ' S ', ' T ', ' T ', ' Y '],
    'die8': [' E ', ' I ', ' O ', ' S ', ' S ', ' T'],
    'die9': [' D ', ' E ', ' L ', ' R ', ' V ', ' Y '],
    'die10': [' A ', ' C ', ' H ', ' O ', ' P ', ' S '],
    'die11': [' H ', ' I ', ' M ', ' N ', ' Qu', ' U '],
    'die12': [' E ', ' E ', ' I ', ' N ', ' S ', ' U '],
    'die13': [' E ', ' E ', ' G ', ' H ', ' N ', ' W '],
    'die14': [' A ', ' F ', ' F ', ' K ', ' P ', ' S '],
    'die15': [' H ', ' L ', ' N ', ' N ', ' R ', ' Z '],
    'die16': [' D ', ' E ', ' I ', ' L ', ' R ', ' X ']
  }
  
  def __init__(self):
    print("____")
    print("____")
    print("____")
    print("____")
    
  def shake(self):
    str1 = ''
    str2 = ''
    str3 = ''
    str4 = ''
    
    for i, value in enumerate(BoggleBoard.boggle_dice.values()):
      random_number = random.randint(0, 5)

      if i < 4:
        str1 += value[random_number]
      elif 4 <= i < 8:
        str2 += value[random_number]
      elif 8 <= i < 12:
        str3 += value[random_number]
      else:
        str4 += value[random_number]

    print(str1)
    print(str2)
    print(str3)
    print(str4)
      
test = BoggleBoard()
test.shake()