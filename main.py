# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name, template='Hello, <name>!'):

    greeting = template.replace('<name>', name)

    return greeting

def force(mass, body='earth'):

    # define dict with gravities of all bodies
    gravity = {
        'sun': 274.0,  
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6,
    }

    # Does body exist in dict
    if not (body in gravity):
        return False

    # Calculation F = m*g
    exerted_force = mass * gravity[body]

    return exerted_force

def pull(m1, m2, d):

    # Constant G
    G = 6.674e-11

    # Calculation
    grav_pull = G * ((m1 * m2) / d ** 2)

    return grav_pull

if __name__ == '__main__':
    pass