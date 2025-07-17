import random
try:
    import keyboard
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "keyboard"])
    import keyboard

global start
start = True
key_pressed = False
item_pressed = False
item_pressed2= False
item_pressed3 = False
skip_pressed = False
k_skip_pressed = False
item_pressed4 = False
phone = []
phone_position = 0
random_phone = 0
shells_len = 0
item_pressed5 = False
player_score = 0
key_pressed2 = False

my_items1 = ['beer', 'glass', 'inverter', 'phone', 'cigarette']
real_item = []

heart = 3

#player first item setting
for _ in range(5):
    real_item2 = random.choice(my_items1)
    real_item.append(real_item2)



# restart

def restart():
    global skip_pressed
    global start
    while start == False:
        if keyboard.is_pressed('a') and not skip_pressed:
            start = True
            skip_pressed = True
        if not keyboard.is_pressed('a'):
            skip_pressed = False

# shell setting          
range_value = int(random.randint(4, 6))
    
shells = ['공포탄'] * range_value
    
random_value2 = random.randint(1, 6)
    
for _ in range(random_value2):
    random_value = random.randint(0, range_value - 1)
    shells[random_value] = '실탄'

bullet = shells.count('실탄')
blank_bullet = shells.count('공포탄')

print(f"실탄: {bullet}")
print(f"공포탄: {blank_bullet}")

first_bullet = shells[0]

 

#commend

def shoot():
    global start
    global heart
    if start == True:
        if keyboard.is_pressed('s'):
            if shells[0] == '공포탄':
                print("survived")
            if shells[0] == '실탄':
                print("hit")
                heart = heart - 1
                print(f"your heart is {heart}")
            del shells[0]
            start = False

            if len(shells) == 0:
                reset_shells()
                player_item_setting()

def shell_check():
    print(random_phone)
    print(shells)
    if shells[random_phone] == '공포탄':
        print(f"{random_phone + 1}번째 탄에 공포탄이 있습니다")
    elif shells[random_phone] == '실탄' :
        print(f"{random_phone + 1}번째 탄에 실탄이 있습니다")
  


def item_use():
    global start
    global my_items1
    global real_item
    global range_value
    global random_value
    global shells
    global item_pressed
    global item_pressed3
    global item_pressed2
    global first_bullet
    global item_pressed4
    global phone
    global phone_position
    global random_phone
    global shells_len
    global item_pressed5
    global heart
    
    if start == True:
        if keyboard.is_pressed('a') and keyboard.is_pressed('1') and not item_pressed:
            if 'beer' in real_item:  
                real_item.remove('beer')
                first_bullet = shells[0]
                print(f"shell was {first_bullet}")
                del shells[0]
                item_pressed = True
        if not keyboard.is_pressed('a') and not keyboard.is_pressed('1'):
            item_pressed = False

        if keyboard.is_pressed('a') and keyboard.is_pressed('2') and not item_pressed2:
            if 'glass' in real_item:  
                real_item.remove('glass')
                first_bullet = shells[0]
                print(f"shell is {first_bullet}.")
                item_pressed2 = True
        if not keyboard.is_pressed('a') and not keyboard.is_pressed('2'):
            item_pressed2 = False

        if keyboard.is_pressed('a') and keyboard.is_pressed('3') and not item_pressed3:
            if 'inverter' in real_item:  
                real_item.remove('inverter')
                if shells[0] == '공포탄':
                    shells[0] = '실탄'
                else: 
                    if shells[0] == '실탄':
                        shells[0] = '공포탄'
                print("shell changed")
                item_pressed3 = True
        if not keyboard.is_pressed('a') or not keyboard.is_pressed('3'):
            item_pressed3 = False
                
        if keyboard.is_pressed('a') and keyboard.is_pressed('4') and not item_pressed4:
            if 'phone' in real_item: 
                real_item.remove('phone')
                shells_len = len(shells)
                random_phone = random.randint(0, shells_len - 1)
                shell_check()
                item_pressed4 = True
        if not keyboard.is_pressed('a') or not keyboard.is_pressed('4'):
            item_pressed4 = False


        if keyboard.is_pressed('a') and keyboard.is_pressed('5') and not item_pressed5:
            if 'cigarette' in real_item: 
                real_item.remove('cigarette')
                if heart < 3:
                    heart += 1
                    print("Using cigarette...")
                elif heart >= 3:
                    print("I'm feel exhausted..")
                    real_item.append("cigarette")
                item_pressed5 = True
        if not keyboard.is_pressed('a') or not keyboard.is_pressed('5'):
            item_pressed5 = False

def turn_skip():
    global start
    global shells
    global heart
    global k_skip_pressed

    if start == True:
        if keyboard.is_pressed('k') and not k_skip_pressed:
            if shells[0] == '실탄':
                print("실탄 eliminated")
            elif shells[0] == '공포탄':
                print("공포탄 eliminated")
                heart = heart - 1
                print(f"your heart is {heart}")
            k_skip_pressed = True
            del shells[0]
            start = False
        if not keyboard.is_pressed('k'):
            k_skip_pressed = False
        

           

def show_my_item():
    global real_item
    global key_pressed

    
    if keyboard.is_pressed('i') and not key_pressed:
        print(real_item)
        key_pressed = True
    if not keyboard.is_pressed('i') and key_pressed:
        key_pressed = False

def item_tutorial():
    global key_pressed2
    
    if keyboard.is_pressed('t') and not key_pressed2:
        print("a + ? / 1 = beer, 2 = glass, 3 = inverter, 4 = phone, 5 = cigarette")
        key_pressed2 = True
    if not keyboard.is_pressed('t') and key_pressed2:
        key_pressed2 = False

def reset_shells():
    global start
    global my_items1
    global real_item
    global range_value
    global random_value
    global shells
    global bullet
    global blank_bullet
    global player_score

    range_value = int(random.randint(4, 6))
    
    shells = ['공포탄'] * range_value

    player_score += 100
    
    random_value2 = random.randint(1, 7)
    
    for _ in range(random_value2):
        random_value = random.randint(0, range_value - 1)
        shells[random_value] = '실탄'

    bullet = shells.count('실탄')
    blank_bullet = shells.count('공포탄')
    
    print(f"실탄: {bullet}")
    print(f"공포탄: {blank_bullet}")

    print("shells reloaded")
    

def player_item_setting():
    for _ in range(3):
        real_item2 = random.choice(my_items1)
        real_item.append(real_item2)


# game start
while True:
    shoot()
    item_use()
    restart()
    turn_skip()
    show_my_item()
    item_tutorial()

    if heart == 0:
        print(f"Your score is {player_score}.")
        print("Game Over")
        break

    if len(shells) == 0:
                reset_shells()
                player_item_setting()
