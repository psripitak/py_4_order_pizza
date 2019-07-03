import cgi
import cgitb

# File: pizza.py
# Author: Pete Sripitak
# This program receives the submitted form from the webpage
# and compute the price of the pizza which is being ordered.

cgitb.enable()

print("Content-type: text/html\n\n")
print("""
<!DOCTYPE html>
<html>
    <head>
        <title>Project 4</title>
    </head>
    <body>
""")

form = cgi.FieldStorage()

#for e in form:
	#print('{0} = {1} <br />'.format(e, form[e].value))

formVals = {}
for key in list(form.keys()):
    formVals[key] = form[key].value
    #print(key)
    #print('<br />')

price = 0

if formVals['size'] == 'small':
	price = 10
elif formVals['size'] == 'medium':
	price = 13
elif formVals['size'] == 'large':
	price = 14

if formVals['crust'] == 'thick':
	price += 1
elif formVals['crust'] == 'chicago':
	price += 2

if 'anchovies' in formVals:
	formVals['anchovies'] = '<b>Added</b> anchovies'
	price += 1
else:
	formVals['anchovies'] = '<b>No</b> anchovies'
if 'pepperoni' in formVals:
	formVals['pepperoni'] = '<b>Added</b> pepperoni'
	price += 1
else:
	formVals['pepperoni'] = '<b>No</b> pepperoni'
if 'pineapple' in formVals:
	formVals['pineapple'] = '<b>Added</b> pineapple'
	price += 1
else:
	formVals['pineapple'] = '<b>No</b> pineapple'

formVals['price'] = price

print('<br />')
print('<div style="background-color:#EEEEEE;height:170px;width:500px;float:left;">')
s = """
<b><u>Your pizza has been ordered</u>.</b><br />
<b>It will be delivered to:</b> {address}.<br />
<b>Size:</b> {size}.<br />
<b>Crust:</b> {crust}.<br />
{anchovies}.<br />
{pepperoni}.<br />
{pineapple}.<br />
<b>Total cost:</b> ${price}.<br />
""".format(**formVals)
print(s)
print('</div>')
print('<br />')

print("""
    </body>
    </html>
""")
