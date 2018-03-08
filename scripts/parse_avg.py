import scipy.io
#
subject_list = ['Record_victim1', 'Record_victim2', 'Record_victim3',
				'Record_victim4', 'Record_victim5', 'Record_victim6',
				'Record_victim7', 'Record_victim8', 'Record_victim9',
				'Record_victim10', 'Record_victim11', 'Record_victim12',
				'Record_victim13', 'Record_victim14', 'Record_victim15',
				'Record_victim16', 'Record_victim17', 'Record_victim18',
				'Record_victim19', 'Record_victim20']


# initialize lists
num = [0] * 22
count = [0] * 22
avg = [0] * 22

file = open('parsed_avg/averages.txt','w+')

for subject in subject_list:

	# load the entire matlab data file
	mat = scipy.io.loadmat('copy_results/' + subject + '.mat')

	# load the relevant data
	data = (mat[subject])

	# Loop through data
	for row in data:

		left = row[1]
		right = row[2]

		# score value
		score = row[3]

		# If the score is negative, add that score to left image tabulation.
		if (score < 0):
			num[left] = num[left] + abs(score)
			count[left] = count[left] + 1
		elif (score == 0):
			num[left] = num[left] + abs(score)
			num[right] = num[right] + abs(score)
			count[left] = count[left] + 1
			count[right] = count[right] + 1
		else:
			num[right] = num[right] + abs(score)
			count[right] = count[right] + 1

for i in range(1,22):
	if (count[i] == 0):
		avg[i] = 0
	else:
		avg[i] = num[i] / count[i]
	file.write(str(i) + ': ' + str(avg[i]) + '\n')


file.close()
