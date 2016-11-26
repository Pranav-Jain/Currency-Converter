import json
from urllib.request import urlopen

def exchange(currency_from, currency_to, amount_from):
	json_string=currency_response(currency_from, currency_to, amount_from)
	valid=has_error(json_string)
	if(valid=='True'):
		return('-1')
	else:
		parsed_json = json.loads(json_string)
		rhs = parsed_json['rhs']
		final_amount=before_space(rhs)
		return(float(final_amount))


def currency_response(currency_from, currency_to, amount_from):
	url='http://cs1110.cs.cornell.edu/2015fa/a1server.php?from=%s&to=%s&amt=%f' % (currency_from,currency_to,float(amount_from))
	json_string=urlopen(url).read().decode("utf-8")
	return(json_string)
	


def has_error(json_string):
	parsed_json = json.loads(json_string)
	if(parsed_json['lhs']==''):
		return('True')
	else:
		return('False')


def before_space(s):
	x = s.index(' ')
	return s[:x]


def after_space(s):
	x = s.index(' ')
	return s[x+1:]


if __name__ == '__main__':
	currency_from=input('Enter code of currency you want to change from: ')
	currency_to=input('Enter code of currency you want to change to: ')
	amount_from=float(input('Enter the amount: '))
	final_amount=exchange(currency_from, currency_to, amount_from)
	print(final_amount)


