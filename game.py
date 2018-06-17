from guessme.py import guess

sb = guess()

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

	result = sb.guess(guess)
	trials = sb.trials()

	return {'code': 'success', 'result': result, 'trials': trials}
