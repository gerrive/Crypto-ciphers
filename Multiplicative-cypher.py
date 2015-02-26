__author__ = 'DeathScythe'

# Name: German A. Rivera De La Torre
# Description: we take a sting and then shifted n times by multiplicative of the key

class MultiplicativeCyhpher:
	def __init__(self):
		self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
						 't', 'u', 'v', 'w', 'x', 'y', 'z']

	def encrypt(self, text, key):
			""" encrypt the text by shifting the letter by a multiplactive of key """
		shift = []
		newLetter = []

		for x in text:
			newIndex = (self.alphabet.index(x) * key) % len(self.alphabet)
			shift.append(newIndex)

		for x in shift:
			newLetter.append(self.alphabet[x])
		return ''.join(newLetter)

	def decryptKey(self, key):
		""" THis finds the inverse of a when key times x is equal to 1 """
		for x in range(len(self.alphabet)):
			if (key * x) % len(self.alphabet) == 1:
				return x


	def decrypt(self, text, key):
		""" we decrypt the key finding the inverse of key then multiply the letter by the inverse key"""
		shift = []
		newLetter = []
		dercyptKey = self.decryptKey(key)

		for x in text:
			newIndex = (self.alphabet.index(x) * dercyptKey) % len(self.alphabet)
			shift.append(newIndex)

		for x in shift:
			newLetter.append(self.alphabet[x])

		return ''.join(newLetter)


start = MultiplicativeCyhpher()

key = 15

encrypt = start.encrypt('thisisanexample', key)
print 'Encrypt:', encrypt
decrypt = start.decrypt(encrypt, key)
print 'Decrypt:', decrypt
