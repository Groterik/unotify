import sys
import argparse
import requests

try:
  requests.packages.urllib3.disable_warnings()
except:
  pass

parser = argparse.ArgumentParser(prog='telegram-notifier')
parser.add_argument('-u', '--user', required=True, help='bot token id')
parser.add_argument('-t', '--to', required=True, help='target chat id')
parser.add_argument('-m', '--message', required=True, help='message text')
parser.add_argument('-c', '--check', action="store_true", help='check token')
parser.add_argument('-p', '--print-updates', action="store_true", help='fetch and print incoming bot updates')
args = parser.parse_args()

token = args.user
chat_id = args.to

if args.check:
  response = requests.post(
    url='https://api.telegram.org/bot{0}/getMe'.format(token)
).json()
  print response
  exit(0)

if args.print_updates:
  response = requests.post(
    url='https://api.telegram.org/bot{0}/getUpdates'.format(token),
    data={'offset': 0}
).json()
  print response
  exit(0)

response = requests.post(
    url='https://api.telegram.org/bot{0}/sendMessage'.format(token),
    data={'chat_id': chat_id, 'text': args.message}
).json()

if not response['ok']:
  sys.stderr.write('Error: ' + str(response))
  exit(1)
