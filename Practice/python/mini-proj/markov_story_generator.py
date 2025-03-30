import random

class MarkovChain:
    def __init__(self):
        self.model = {}

    def train(self, text, n=2):
        words = text.split()
        for i in range(len(words) - n):
            key = tuple(words[i:i+n])
            next_word = words[i + n]
            if key not in self.model:
                self.model[key] = []
            self.model[key].append(next_word)

    def generate(self, size=50):
        seed = random.choice(list(self.model.keys()))
        output = list(seed)
        for _ in range(size):
            next_words = self.model.get(tuple(output[-2:]), None)
            if not next_words:
                break
            output.append(random.choice(next_words))
        return ' '.join(output)

# Example usage
if __name__ == "__main__":
    input_text = """
    Once upon a time in a faraway land, there lived a brave warrior. He roamed the forests, battled dragons, and protected the innocent. People from distant lands came to seek his help...
    """
    mc = MarkovChain()
    mc.train(input_text)
    print("Generated Story:\n", mc.generate(60))
