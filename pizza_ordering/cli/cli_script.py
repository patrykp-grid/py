import argparse
import requests

parser = argparse.ArgumentParser(description='Pizza Ordering CLI')
parser.add_argument('command', help='Command to run', choices=['list_menu', 'create_order', 'check_order', 'cancel_order', 'add_pizza'])
parser.add_argument('--order_id', help='Order ID')
parser.add_argument('--pizza_id', help='Pizza ID')
parser.add_argument('--address', help='Delivery address')
parser.add_argument('--name', help='Pizza name')
parser.add_argument('--description', help='Pizza description')
parser.add_argument('--price', type=float, help='Pizza price')
parser.add_argument('--admin_token', help='Admin token for authorization')

args = parser.parse_args()

# CLI functions to interact with API
def list_menu():
    response = requests.get('http://localhost:8000/menu/')
    print(response.json())

def create_order(pizza_id, address):
    data = {"pizza_id": pizza_id, "address": address}
    response = requests.post('http://localhost:8000/order/', json=data)
    print(response.json())

def check_order(order_id):
    response = requests.get(f'http://localhost:8000/order/{order_id}')
    print(response.json())

def cancel_order(order_id):
    response = requests.delete(f'http://localhost:8000/order/{order_id}')
    print(response.json())

def add_pizza(name, description, price, admin_token):
    headers = {'Authorization': admin_token}
    data = {"name": name, "description": description, "price": price}
    response = requests.post('http://localhost:8000/menu/add/', json=data, headers=headers)
    print(response.json())

# CLI Command Execution
if args.command == 'list_menu':
    list_menu()
elif args.command == 'create_order':
    if args.pizza_id and args.address:
        create_order(args.pizza_id, args.address)
    else:
        print("Error: --pizza_id and --address are required for create_order command.")
elif args.command == 'check_order':
    if args.order_id:
        check_order(args.order_id)
    else:
        print("Error: --order_id is required for check_order command.")
elif args.command == 'cancel_order':
    if args.order_id:
        cancel_order(args.order_id, args.admin_token)
    else:
        print("Error: --order_id is required for cancel_order command.")
elif args.command == 'add_pizza':
    if args.name and args.description and args.price and args.admin_token:
        add_pizza(args.name, args.description, args.price, args.admin_token)
    else:
        print("Error: --name, --description, --price, and --admin_token are required for add_pizza command.")
else:
    print("Error: Unknown command.")