def countLines(name):
    return len(name.readlines())

def countChar(name):
    name.seek(0)
    return len(name.read())

def test(name):
    tmp = open(name, 'r')
    return countLines(tmp), countChar(tmp)

if __name__ == "__main__":
    print(test('expercise/mymod.py'))