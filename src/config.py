class OptionConfig:
	def __init__(self, file='../config/config.txt'):
		self.time = 3
		self.rounds = 1
		self.video = 2
		self.music = 1
		self.sound = 2
		self.keysP1 = [32]*10
		self.keysP2 = [32]*10
		try:
			self.loadconfig(file)
		except Exception as e:
			print("Error: unable to load config !!!")
			raise e


	def loadconfig(self, file):
		with open(file, encoding='utf-8') as f_obj:
			for line in f_obj:
				line.lower()
				if line.find('time=') != -1:
					self.time = int(line.strip('time='))
				if line.find('rounds=') != -1:
					self.rounds = int(line.strip('rounds='))
				if line.find('video=') != -1:
					self.video = int(int(line.strip('video=')))
				if line.find('sound=') != -1:
					self.sound = int(line.strip('sound='))
				if line.find('music=') != -1:
					self.music = int(line.strip('music='))
				if line.find('keysP1=') != -1:
					keys = line.strip('keysP1=').split('/')
					keys.remove('\n')
					for i in range(len(keys)):
				   		keys[i]=int(keys[i])
					self.keysP1 = keys
				if line.find('keysP2=') != -1:
					keys = line.strip('keysP2=').split('/')
					keys.remove('\n')
					for i in range(len(keys)):
						keys[i]=int(keys[i])
					self.keysP2 = keys


	def saveconfig(self, file):
		pass

if __name__ == '__main__':
	con = OptionConfig()
	print('done')