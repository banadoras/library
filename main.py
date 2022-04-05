class Smart_Phrase:
  number_of_smart_phrases = 0
  list_of_smart_phrases = []
  def __init__(self,title,info):
      self.title = title
      self.info = info
      Smart_Phrase.number_of_smart_phrases += 1
      Smart_Phrase.list_of_smart_phrases.append(self)



def sp_entry():
  while True:
    title = input("Enter smart phrase title: ")
    info = input("Enter info: ")
    Smart_Phrase(title,info)
    print(f"Number of Smart phrases: {Smart_Phrase.number_of_smart_phrases})")
    print("Do you want add more smart phrases?")
    answer = input()
    if answer == "y":
      continue
    else:
       break

def display_sp():
  for sp in Smart_Phrase.list_of_smart_phrases:
    print(sp.title)
    print(sp.info)
    print("")


while True:
  option = input("What do you want to do?\n-Enter smart phrase (press e)\n-Display smart phrases (press d)\n-Exit (press x)\n")
  if option == "e":
    sp_entry()
  elif option == "d":
    display_sp()
  else:
    break
  
      