class Animal:
    def speak(self):
        print("Animal speaks")

class Bird(Animal):
    def speak(self):
        print("Tweet Tweet!")

my_bird = Bird()
my_bird.speak()
