class Keyboard: 
  
  def __init__(self, language, connection):
    self.language = language
    self.connection = connection
  
  def definition(self): 
    print("Keyboard is an input device")
    
  def numer_of_keys(self): 
    print("There are 50 keys")
  
my_keyboard = Keyboard('English', 'wireless')
print(my_keyboard.language)
print(my_keyboard.connection)

class AboutMe:
  def __init__(self, name, address, occupation):
    self.name = name
    self.address = address
    self.occupation = occupation
    
  def talk(self):
     print(f"My name is {self.name}. I am from {self.address} and I am a {self.occupation}.")
    
    
tazrian_binte_mahfuz = AboutMe('Tazrian Binte Mahfuaz', 'Bangladesh', 'Student')
tazrian_binte_mahfuz.talk()
