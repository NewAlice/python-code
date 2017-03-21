class mailData:

	def sendMail(self):
		print("sending mail")
	def fwdMail(self):
		print("fwd mail")
	def ccMail(self):
		print("cc mail")

def main():
	
	myMail=mailData()
	myMail.sendMail()
	myMail.fwdMail()
	myMail.ccMail()

main()

		