# This script processes text using a Markov model

def generate_text(input_text, n=2):
    words = input_text.split()
    markov_chain = {}
    
    for i in range(len(words) - n):
        key = tuple(words[i:i+n])
        next_word = words[i+n]
        
        if key not in markov_chain:
            markov_chain[key] = []
        markov_chain[key].append(next_word)
    
    return markov_chain

# Example usage
sample_text = "This is a simple example of a Markov model based text generator."
markov_model = generate_text(sample_text)
print(markov_model)
