__author__ = 'DeathScythe'

# Name: German A. Rivera De La Torre
# Description: we take a sting and then shifted n times depending on the key
#

class AddativeCyhpher:
	def __init__(self):
		self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
						 't', 'u', 'v', 'w', 'x', 'y', 'z']

	def encrypt(self, text, key):
		text = text.replace(' ', '')
		shift = [] 		# index shift
		newLetter = [] 	#  the new letter generated

		for x in text:
			newIndex = (self.alphabet.index(x) + key) % len(self.alphabet) # shifts the key to encrypt
			shift.append(newIndex)

		for x in shift:
			newLetter.append(self.alphabet[x])

		return ''.join(newLetter)

	def decrypt(self, text, key):
		text = text.replace(' ', '')
		shift = []
		newLetter = []

		for x in text:
			newIndex = self.alphabet.index(x) - key % len(self.alphabet) # shifts the key to decrypts
			shift.append(newIndex)

		for x in shift:
			newLetter.append(self.alphabet[x])

		return ''.join(newLetter)


start = AddativeCyhpher()

key = 20

encrypt = start.encrypt('thisisanexample', key)
print 'Encrypt:', encrypt
decrypt = start.decrypt(encrypt, key)
print 'Decrypt:', decrypt
