import sys
import keyring
import getpass
import argparse
import xmpp

parser = argparse.ArgumentParser(prog='xmpp-notifier')
parser.add_argument('-u', required=True, help='login username')
parser.add_argument('-t', required=True, help='target username')
parser.add_argument('-m', required=True, help='message text')
parser.add_argument('-p', '--password', action="store_true", help='set password')
args = parser.parse_args()
if (args.password):
  keyring.set_password('uni-notifier', args.u, getpass.getpass('Password: '))

pwd = keyring.get_password('uni-notifier', args.u)
if pwd is None or pwd == '':
  sys.stderr.write('Invalid password\n')
  exit(1)

jid = xmpp.JID(args.u) 
client = xmpp.Client(jid.getDomain(), debug=[])
client.connect(server=('talk.google.com',5223))
client.auth(jid.getNode(), pwd, 'notifier')
#client.sendInitPresence()
message = xmpp.protocol.Message(args.t, args.m, typ='chat')
client.send(message)
