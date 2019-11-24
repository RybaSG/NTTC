class QAM64:
    
	St_Rest = {
		    0: 11, 1: 7, 2: 3, 3: 10, 4: 6, 5: 2, 6: 9, 7: 5, 
		    8: 1, 9: 8, 10: 4, 11: 0					
		}
	St_35 = {
		    0: 2, 1: 7, 2: 6, 3: 9, 4: 0, 5: 3, 6: 1, 7: 8, 
		    8: 4, 9: 11, 10: 5, 11: 10					
		}

	St_23 = {
		    0: 11, 1: 7, 2: 3, 3: 10, 4: 6, 5: 2, 6: 9, 7: 5, 
		    8: 1, 9: 8, 10: 4, 11: 0					
		}
	rates = {
		"2/3": St_23,
		"3/5": St_35,
		"rest": St_Rest
	    }
    
	N_FRAMES = 100
	N_MOD = 6        
	N_SUBSTREAMS = 12
	N_LDPC = 64800
	N_CELLS = N_LDPC/N_MOD
   
   

	def __init__(self, input_path , output_path , nLdpc ,  code_rate):
	
		rate=code_rate
		if( rate == ('1/2' or '3/4' or '4/5' or '5/6') ):
			rate="rest"
        
		self.N_LDPC = int(nLdpc)
		self.path = input_path
		self.output_path = output_path

		if(rate == "3/5" and self.N_LDPC == 16200 ):
			rate="2/3"

		self.N_CELLS = self.N_LDPC/self.N_MOD

		all_data = sci.loadmat(self.path)
		self.rate = self.rates[rate]
		self.inputData = np.array(all_data['v'])[0][0]
		self.output_data_check = np.array(all_data['y'])[0][0]
		self.output_data = np.zeros((int(self.N_LDPC/self.N_SUBSTREAMS), self.N_SUBSTREAMS, self.N_FRAMES), dtype = np.uint8)

    
	def demultiplex(self):
		for frameIndex in range(self.N_FRAMES):
			for bitIndex in range(self.N_LDPC):
				nStream = self.rate[bitIndex%self.N_SUBSTREAMS]
				mBitIndex = int(math.floor(bitIndex/self.N_SUBSTREAMS))
				bit = self.inputData[bitIndex][frameIndex]
				self.output_data[mBitIndex][nStream][frameIndex] = bit
		self.output_data = np.reshape(self.output_data, (int(self.N_LDPC/self.N_MOD), self.N_MOD, self.N_FRAMES))

	def checkResult(self):
		match = np.all(self.output_data_check == self.output_data)
		print(f"Match_{self.path}: {match}")

	def save(self):
		mat = {"y": self.output_data}
		sci.savemat(f"out_{self.output_path}", mat)

