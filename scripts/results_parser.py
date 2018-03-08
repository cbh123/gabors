import scipy.io

subject_list = ['Record_victim1', 'Record_victim2', 'Record_victim3',
				'Record_victim4', 'Record_victim5', 'Record_victim6',
				'Record_victim7', 'Record_victim8', 'Record_victim9',
				'Record_victim10', 'Record_victim11', 'Record_victim12',
				'Record_victim13', 'Record_victim14', 'Record_victim15',
				'Record_victim16', 'Record_victim17', 'Record_victim18',
				'Record_victim19', 'Record_victim20']

for subject in subject_list:

	# load the entire matlab data file
	mat = scipy.io.loadmat('copy_results/' + subject + '.mat')

	file = open('parsed_data/parsed_' + subject + '.txt','w+')

	# load the relevant data
	data = (mat[subject])

	# create dictionary
	d = {}

	# Loop through data
	for row in data:

		# create comparison response pair
		comparison = row[1],row[2]

		# alter responses to -1, 0, 1
		response = row[3]
		if (response <= -1):
			response = -1
		elif (response >= 1):
			response = 1
		elif (response == 0):
			response = 0

		# add to dictionary
		d[comparison] = response
		file.write(str(comparison) + ': ' + str(response) + '\n')

	file.close()
