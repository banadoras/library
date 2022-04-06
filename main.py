import json

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
    print(f"Smart phrase added, current number of Smart phrases: {Smart_Phrase.number_of_smart_phrases}")
    print("Do you want add more smart phrases? y=yes n=no")
    answer = input()
    if answer == "y":
      continue
    else:
       break

def display_sp(l):
  print("-----------------------------------------------------------------------")
  print("Smart Phrases:")
  for sp in l:
    print(f"{l.index(sp) + 1}-{sp.title}")
    print(f"  {sp.info}")
  if len(l) < 1:
    print("No smart phrases avalaible")
  else:
    print("-----------------------------------------------------------------------")
    print(f"Number of smart phrases: {len(l) }")
  print("")

def save_sp(sp):
  try:
    f = open("smartPhrases.txt","w")
    for p in sp:
      f.write(f"{sp.index(p) + 1}-{p.title}\n  {p.info}\n")
    f.close()
    json_object = json.dumps([ob.__dict__ for ob in sp])
    with open("smartPhrases.json","w") as sp_json:
     sp_json.write(json_object)
  except:
    print("Could not save file")
  else:
    print("File saved!")
  finally:
    print("Thank you!")


def load_sp():
  with open("smartPhrases.json","r") as sp_json:
    l = json.load(sp_json)
    for sp in l:
      Smart_Phrase(sp["title"],sp["info"])

def run_prog():
  load_sp()
  while True:
    option = input("What do you want to do?\n-Enter smart phrase (press e)\n-Display smart phrases (press d)\n-Look up smart phrase (press f)\n-Save smart phrases to file (press s)\n-Exit (press x)\n")
    if option == "e":
      sp_entry()
    elif option == "d":
      display_sp(Smart_Phrase.list_of_smart_phrases)
    elif option == "s":
      save_sp(Smart_Phrase.list_of_smart_phrases)
    elif option == "f":
      find_sp(Smart_Phrase.list_of_smart_phrases)
    else:
      s = input("Are you sure you want to exit? Did you save added smart phrases? y=yes n=no\n" )
      if s == "y":
        break
      else:
        #save_sp(Smart_Phrase.list_of_smart_phrases)
        continue

def find_sp(sp_list):
  w = input("Search smart phrases: ")
  filtered = []
  for sp in sp_list:
    if sp.title.lower().find(w.lower()) != -1:
      filtered.append(sp)
  display_sp(filtered)
  
run_prog()
      