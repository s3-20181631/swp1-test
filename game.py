from guessme import UpDownNumber

sb = UpDownNumber()

def new_game(d):
	try:
		count = int(d.get('count', [''])[0])
	except:
		return {'code': 'error', 'msg': 'count not given'}

	sb.newgame(count)

	return {'code': 'success'}


def guess(d):
	try:
		guess = d.get('guess', [''])[0]
	except:
		return {'code': 'error', 'msg': 'wrong guess parameter'}

	result,trials = sb.guess(guess)

	return {'code': 'success', 'result': result, 'trials': trials}
