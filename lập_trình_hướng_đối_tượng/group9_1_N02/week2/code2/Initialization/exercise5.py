class Dog:
    def bark(self, sound=None):
        if sound is None:
            print("Woof!")
        elif isinstance(sound, int):
            print("Bark " * sound)
        elif isinstance(sound, float):
            print("Howl!")
        elif isinstance(sound, str):
            print(f"{sound}!")
        else:
            print("Unknown sound")

def showInfo():
    dog = Dog()
    dog.bark()
    dog.bark(3)
    dog.bark(2.5)
    dog.bark("Growl")
    dog.bark([1, 2, 3])

if __name__ == "__main__":
    showInfo()
