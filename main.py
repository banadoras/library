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
  print("-----------------------------------------------------------------------")
  print("Smart Phrases:")
  for sp in Smart_Phrase.list_of_smart_phrases:
    print(f"{Smart_Phrase.list_of_smart_phrases.index(sp) + 1}-{sp.title}")
    print(f"  {sp.info}")
  if len(Smart_Phrase.list_of_smart_phrases) < 1:
    print("No smart phrases avalaible")
  else:
    print("-----------------------------------------------------------------------")
    print(f"Number of smart phrases: {len(Smart_Phrase.list_of_smart_phrases) }")
  print("")

def save_sp(sp):
  try:
    f = open("smartPhrases.txt","a")
    for p in sp:
      print(p)
      f.write(f"{sp.index(p) + 1}-{p.title}\n  {p.info}\n")
    f.close()
  except:
    print("Could not save file")
  else:
    print("File saved!")
  finally:
    print("Thank you!")

def run_prog():
  while True:
    option = input("What do you want to do?\n-Enter smart phrase (press e)\n-Display smart phrases (press d)\n-Save smart phrases to file (press s)\n-Exit (press x)\n")
    if option == "e":
      sp_entry()
    elif option == "d":
      display_sp()
    elif option == "s":
      save_sp(Smart_Phrase.list_of_smart_phrases)
    else:
      break

run_prog()
      