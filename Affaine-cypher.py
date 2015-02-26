__author__ = 'DeathScythe'

# Name: German A. Rivera De La Torre
# Description: we take a sting and then shifted n times KeyA and then add keyB
#

class AddativeCyhpher:
	def __init__(self):
		self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
						 't', 'u', 'v', 'w', 'x', 'y', 'z']

	def encrypt(self, text, keyA, keyB):
		shift = []
		newLetter = []

		for x in text:
			newIndex = (keyA*self.alphabet.index(x) + keyB) % len(self.alphabet) # encrypts
			shift.append(newIndex)

		for x in shift:
			newLetter.append(self.alphabet[x])

		return ''.join(newLetter)

	def decryptKey(self, key):
		""" THis finds the inverse of a when key times x is equal to 1 """
		for x in range(len(self.alphabet)):
			if (key * x) % len(self.alphabet) == 1:
				return x

	def decrypt(self, text, keyA, keyB):
		shift = []
		newLetter = []

		inverseKeyA = self.decryptKey(keyA)

		for x in text:
			newIndex = inverseKeyA * (self.alphabet.index(x) - keyB) % len(self.alphabet) # decrypts
			shift.append(newIndex)

		for x in shift:
			newLetter.append(self.alphabet[x])

		return ''.join(newLetter)


start = AddativeCyhpher()

keyA = 15
keyB = 20

encrypt = start.encrypt('thisisanexample', keyA, keyB)
print 'Encrypt:', encrypt
decrypt = start.decrypt(encrypt, keyA, keyB)
print 'Decrypt:', decrypt


