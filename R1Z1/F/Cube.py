def find_missing_card(placed_cards, bounds):
    for x in range(bounds['min_x'], bounds['max_x'] + 1):
        for y in range(bounds['min_y'], bounds['max_y'] + 1):
            for z in range(bounds['min_z'], bounds['max_z'] + 1):
                
                if not is_cube_covered(x, y, z, placed_cards):
                    
                    return (x, y, z)
    return None

def is_cube_covered(x, y, z, placed_cards):
    
    faces = [
        (x, y, z, 'xy'),  
        (x, y, z + 1, 'xy'),  
        (x, y, z, 'yz'),  
        (x + 1, y, z, 'yz'),  
        (x, y, z, 'xz'),  
        (x, y + 1, z, 'xz')  
    ]
    return all((fx, fy, fz, plane) in placed_cards for fx, fy, fz, plane in faces)

def solve():
    
    n = int(input())
    
    placed_cards = set()
    bounds = {'min_x': float('inf'), 'max_x': float('-inf'),
              'min_y': float('inf'), 'max_y': float('-inf'),
              'min_z': float('inf'), 'max_z': float('-inf')}
    
    
    for _ in range(n):
        x, y, z, plane = input().split()
        x, y, z = int(x), int(y), int(z)
        
        
        placed_cards.add((x, y, z, plane))
        
        
        bounds['min_x'] = min(bounds['min_x'], x)
        bounds['max_x'] = max(bounds['max_x'], x)
        bounds['min_y'] = min(bounds['min_y'], y)
        bounds['max_y'] = max(bounds['max_y'], y)
        bounds['min_z'] = min(bounds['min_z'], z)
        bounds['max_z'] = max(bounds['max_z'], z)
    
    
    missing_card = find_missing_card(placed_cards, bounds)
    
    if missing_card:
        
        x, y, z = missing_card
        print(f"{x} {y} {z} xy")
    else:
        
        volume = (bounds['max_x'] - bounds['min_x'] + 1) * \
                 (bounds['max_y'] - bounds['min_y'] + 1) * \
                 (bounds['max_z'] - bounds['min_z'] + 1)
        print(volume)

