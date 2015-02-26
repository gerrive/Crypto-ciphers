__author__ = 'DeathScythe'

# Name: German A. Rivera De La Torre
# Description: using a key's multiple index we have n keys that we shift to in the lib
# then we grab the the key and shift the current letter then mod 26

class VigenereCypher:
	def __init__(self):
		self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	def encrypt(self, key, text):
		encrypt = []
		keyIndex = 0
		key = key.upper()

		for character in text:
			num = self.alphabet.find(character.upper())
			if num != -1:
				num = (self.alphabet.find(key[keyIndex]) + num) % len(self.alphabet) # encrypt 

				if character.isupper():
					encrypt.append(self.alphabet[num])
				elif character.islower():
					encrypt.append(self.alphabet[num].lower())

				keyIndex += 1

				if keyIndex == len(key):
					keyIndex = 0
			else:
				encrypt.append(character)

		return ''.join(encrypt)


	def decrypt(self, key, text):
		encrypt = []
		keyIndex = 0
		key = key.upper()

		for character in text:
			num = self.alphabet.find(character.upper())
			if num != -1:
				num = (num - self.alphabet.find(key[keyIndex])) % len(self.alphabet) # decrypt

				if character.isupper():
					encrypt.append(self.alphabet[num])
				elif character.islower():
					encrypt.append(self.alphabet[num].lower())

				keyIndex += 1

				if keyIndex == len(key):
					keyIndex = 0
			else:
				encrypt.append(character)

		return ''.join(encrypt)


start = VigenereCypher()
key = 'puertorro'
text = 'thehouseiseingsoldtonight'
encryted = start.encrypt(key, text)
print encryted
print start.decrypt(key, encryted)