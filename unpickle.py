import pickle

with open("/home/bombbom/Documents/Malware_Project/blocks/federated_model1.block","rb") as f:
	block = pickle.load(f)
	model = block.basemodel
	for keys, values in sorted(model.items()):
		with open("/home/bombbom/Documents/Malware_Project/blocks/federated_model1.txt","a") as f:
			f.write(str(keys) + ' ->>> '+ str(values) + '\n\n')
			f.close()



