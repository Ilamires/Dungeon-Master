def CreateRooms():
    Room1 = [['Mount', 'Empty', 'Empty', 'Chest', 'Empty', 'Enemy', 'Potion', 'Empty', 'Empty'],
             ['Mount', 'Empty', 'Empty', 'Empty', 'Mount', 'Mount', 'Empty', 'Empty', 'Empty'],
             ['Mount', 'Empty', 'Empty', 'Enemy', 'Empty', 'Empty', 'Mount', 'Mount', 'Mount'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Mount', 'Empty', 'Enemy', 'Empty', 'Exit'],
             ['Mount', 'Empty', 'Empty', 'Empty', 'Mount', 'Empty', 'Mount', 'Mount', 'Mount'],
             ['Mount', 'Empty', 'Mount', 'Empty', 'Empty', 'Mount', 'Empty', 'Enemy', 'Empty'],
             ['Mount', 'Empty', 'Mount', 'Mount', 'Empty', 'Empty', 'Empty', 'Mount', 'Empty']]

    Room2 = [['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Enemy', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Mount', 'Mount', 'Mount', 'Mount', 'Mount', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Mount', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Mount', 'Mount', 'Mount', 'Mount', 'Mount', 'Exit'],
             ['Empty', 'Mount', 'Empty', 'Mount', 'Enemy', 'Potion', 'Mount', 'Mount', 'Mount'],
             ['Empty', 'Mount', 'Mount', 'Mount', 'Empty', 'Enemy', 'Empty', 'Mount', 'Chest'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Enemy']]

    Room3 = [['Enemy', 'Enemy', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Enemy', 'Empty'],
             ['Mount', 'Mount', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Mount', 'Enemy'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Mount', 'Mount', 'Mount', 'Chest'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Enemy', 'Exit'],
             ['Mount', 'Mount', 'Empty', 'Mount', 'Mount', 'Mount', 'Mount', 'Mount', 'Potion'],
             ['Mount', 'Mount', 'Empty', 'Empty', 'Empty', 'Enemy', 'Potion', 'Empty', 'Enemy'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Mount', 'Mount', 'Empty']]

    Room4 = [['Chest', 'Enemy', 'Empty', 'Enemy', 'Empty', 'Empty', 'Mount', 'Mount', 'Mount'],
             ['Potion', 'Mount', 'Mount', 'Mount', 'Mount', 'Empty', 'Enemy', 'Empty', 'Empty'],
             ['Mount', 'Mount', 'Mount', 'Empty', 'Empty', 'Empty', 'Mount', 'Empty', 'Enemy'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Mount', 'Enemy', 'Exit'],
             ['Mount', 'Empty', 'Empty', 'Mount', 'Mount', 'Empty', 'Mount', 'Mount', 'Empty'],
             ['Mount', 'Empty', 'Empty', 'Empty', 'Mount', 'Mount', 'Mount', 'Mount', 'Empty'],
             ['Mount', 'Empty', 'Empty', 'Empty', 'Empty', 'Potion', 'Empty', 'Empty', 'Empty']]

    Room5 = [['Empty', 'Mount', 'Empty', 'Mount', 'Mount', 'Mount', 'Empty', 'Mount', 'Mount'],
             ['Empty', 'Mount', 'Enemy', 'Mount', 'Mount', 'Empty', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Mount', 'Enemy', 'Mount', 'Mount', 'Empty', 'Mount', 'Mount', 'Empty'],
             ['Empty', 'Enemy', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Enemy', 'Exit'],
             ['Empty', 'Mount', 'Enemy', 'Mount', 'Mount', 'Mount', 'Mount', 'Empty', 'Mount'],
             ['Empty', 'Mount', 'Empty', 'Mount', 'Mount', 'Chest', 'Mount', 'Empty', 'Mount'],
             ['Empty', 'Mount', 'Empty', 'Potion', 'Mount', 'Enemy', 'Empty', 'Empty', 'Mount']]

    Room6 = [['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Exit'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty']]
    Room7 = [['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Exit'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty']]
    Room8 = [['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Exit'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty']]
    Room9 = [['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Exit'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
             ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty']]
    Room10 = [['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Exit'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty']]
    Room11 = [['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Exit'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty']]
    Room12 = [['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Exit'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty']]
    Room13 = [['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Exit'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty']]
    Room14 = [['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Exit'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty']]
    Room15 = [['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Exit'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty']]
    Room16 = [['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Exit'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
              ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty']]
    # return [Room1, Room2, Room3, Room4, Room5, Room6, Room7, Room8,
    #        Room9, Room10, Room11, Room12, Room13, Room14, Room15, Room16]
    return [Room1, Room2, Room3, Room4,Room5]
