
Inventory_List = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inv):
    print(f'Inventory:')
    for key, value in inv.items():
        total = sum(inv.values())
        print(f'{value} {key}')
    print(f'Total: {total} items')
        
display_inventory(Inventory_List)
