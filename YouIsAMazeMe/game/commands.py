import arcade
from game import constants
# import game.director

class Commands():
    def __init__(self, sprites):
        self.file = 'YouIsAMazeMe/game/run.py'
        self.sprites = sprites
        self.door = sprites['door'][0]

    def execute(self, sprites):
        print("Executing commands!")
        self.sprites = sprites
        self.boxes = sprites['boxes']
        self.box_order()
        
           
    def box_order(self):
        boxes = self.boxes
        search = None
        cmds = []
        searching = True
        for box in boxes:
            if box.get_type() == "start":
                original_x = box.center_x
                original_y = box.center_y
                search = original_x + constants.TILE_SIZE
                count = 0
                while searching:
                    count += 1
                    for box in boxes: 
                        end = "Nope!"                      
                        if box.center_x == search and box.center_y == original_y:
                            cmds.append(box.get_type())
                            end = box.get_type()
                            print(box.get_type())
                            search = box.center_x + constants.TILE_SIZE
                        if end == ")" or count == len(boxes):
                            searching = False
                if cmds == ['print(', 'door', ")"]:
                    print("A door.")
                    door = self.door
                    door.center_x = 704
                    door.center_y = 704
                if cmds == ['del(', 'door', ")"]:
                    print("Delete a door.")
                    door = self.door
                    door.center_x = constants.TILE_SIZE + constants.SCREEN_WIDTH
                    door.center_y = constants.TILE_SIZE + constants.SCREEN_HEIGHT