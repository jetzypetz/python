class Trobble:
    def __init__(s, name, sex):
        s.name, s.sex = name, sex
        s.health, s.age, s.hunger = 10, 0, 0

    
    def __str__(s):
        return f'{s.name}: {s.sex}, health {s.health}, hunger {s.hunger}, age {s.age}'

    def next_turn(s):
        if s.health:
            s.age += 1
            s.hunger += s.age
            s.health -= s.hunger//20
            if s.health < 0:
                s.health = 0

    def feed(s):
        s.hunger -= 25
        if s.hunger < 0:
            s.hunger = 0

    def cure(s):
        s.health += 5
        if s.health > 10:
            s.health = 10

    def party(s):
        s.health += 2
        if s.health > 10:
            s.health = 10
        s.hunger += 4

    def is_alive(s):
        return bool(s.health>0)

def get_name():
    return input('Please give your new Trobble a name: ')

def get_sex():
    sex = None
    while sex is None:
        prompt = 'Is your new Trobble male or female? Type "m" or "f" to choose: '
        choice = input(prompt)
        if choice == 'm':
            sex = 'male'
        elif choice == 'f':
            sex = 'female'
    return sex

def get_action(actions):
    while True:
        prompt = f"Type one of {', '.join(actions.keys())} to perform the action, or stop to quit the game: "
        action_string = input(prompt)
        if action_string == 'stop':
            print('Thanks for having played with Trobbles!')
            return
        if action_string not in actions:
            print('Unknown action!')
        else:
            return actions[action_string]
        
def play():
    name = get_name()
    sex = get_sex()
    trobble = Trobble(name, sex)
    actions = {'feed': trobble.feed, 'cure': trobble.cure, 'party': trobble.party}
    while trobble.is_alive():
        print('You have one Trobble named ' + str(trobble))
        if not trobble.age % 10 and not trobble.age == 0:
            print(f'Happy Birthday {trobble.name}!')
            trobble.hunger -= 5
        action = get_action(actions)
        if action is None:
            return
        action()
        trobble.next_turn()
    print(f'Unfortunately, your Trobble {trobble.name} has died at the age of {trobble.age}')

def mate(t1, t2, kidname):
    if t1.sex != t2.sex and t1.age > 3 and t2.age > 3 and t1.health and t2.health:
        return Trobble(kidname, t1.sex)
    else:
        return None