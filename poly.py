class network:

  def cable(self): print('I am the cable')
  def router(self):print('I am the router')
  def switch(self): print('I am the switch')
  def wifi(self): print('I am wireless router, cable does not mater')

class tokenRing(network):
  
  def cable(self): print('I am a token Ring network cable')
  def router(self): print('I am a token Ring network router')
  def switch(self): print('I am a token Ring network switch')

class ethernet(network):

  def cable(self): print('I am an ethernet cable')
  def router(self): print('I am an ethernet router')
  def wifi(self): print('I am wifi for mac only')

def main():

  windows=tokenRing()
  mac=ethernet()

  #windows.cable()
  #mac.cable()

  for obj in (windows,mac):
    obj.cable()
    obj.router()
    obj.wifi()

main()

