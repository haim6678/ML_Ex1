import sys
import numpy as np

def calcBool(example, hypo):
	result = 1
	count = 0
	for binaryNum in example:
		if (hypo[count]):
			result *= binaryNum
		if (hypo[len(example)] + count):
			result *= not (binaryNum)
		if (result == 0):
			break
		count = count + 1
	return result

def reCalcHypo(hypo, instance):
	newHypo = hypo[:]
	for x in range(0, len(instance)):
		if (instance[x] == 1):
			newHypo[len(instance) + x] = 0
		elif (instance[x] == 0):
			newHypo[x] = 0

	return newHypo


def writeHypoToFile(hypo):
	answer = []
	with open('test.txt', 'w') as file:
		for x in range(0, len(hypo) / 2):
			if (hypo[x] == 1):
				answer.append ('X' + str(x + 1) )
			elif (hypo[x + len(hypo) / 2] == 1):
				answer.append('Not (X' + str(x + 1)+')')
		finalAnswer = ",".join(answer)
		file.writelines(finalAnswer)

def main():
	# declare variables
	predictionVec = []
	hypothesis = []

	# get training data
	e = sys.argv[1]
	dataSet = np.loadtxt(e, dtype=int)
	vectorLen = len(dataSet[0]) - 1
	trainingX, trainingY = dataSet[:, :vectorLen], dataSet[:, vectorLen]

	# create initial hypothesis
	for x in range(0, vectorLen * 2):
		hypothesis.append(1)

	# calc the final hypothesis
	count = 0
	# print trainingX
	for instance_t in trainingX:
		if ((trainingY[count] == 1) and (calcBool(instance_t, hypothesis) == 0)):
			hypothesis = reCalcHypo(hypothesis, instance_t)
		count = count + 1

	writeHypoToFile(hypothesis)

if __name__ == "__main__":
	main()
