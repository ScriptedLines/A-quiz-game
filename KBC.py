import random
kbc = {
    "Who wrote the famous play 'Romeo and Juliet'?": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Leo Tolstoy"],
    "Which is the largest ocean on Earth?": ["Pacific Ocean", "Indian Ocean", "Atlantic Ocean", "Arctic Ocean"],
    "What is the capital of Australia?": ["Canberra", "Sydney", "Melbourne", "Perth"],
    "Who discovered penicillin?": ["Alexander Fleming", "Marie Curie", "Louis Pasteur", "Isaac Newton"],
    "What is the chemical symbol for the element with atomic number 79?": ["Au", "Fe", "O", "Na"],
    "Who painted the Mona Lisa?": ["Leonardo da Vinci", "Vincent Van Gogh", "Pablo Picasso", "Claude Monet"],
    "What is the capital of Canada?": ["Ottawa", "Toronto", "Vancouver", "Montreal"],
    "Who is known as the Father of Computer Science?": ["Alan Turing", "Charles Babbage", "John von Neumann", "Ada Lovelace"],
    "What is the powerhouse of the cell?": ["Mitochondria", "Nucleus", "Ribosome", "Endoplasmic Reticulum"],
    "Who wrote 'War and Peace'?": ["Leo Tolstoy", "Fyodor Dostoevsky", "Anton Chekhov", "Vladimir Nabokov"],
    "What is the currency of Japan?": ["Yen", "Dollar", "Euro", "Pound"],
    "Who is the author of 'The Theory of Everything'?": ["Stephen Hawking", "Albert Einstein", "Isaac Newton", "Galileo Galilei"],
    "What is the highest mountain in the world?": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
    "Who is the current Secretary-General of the United Nations?": ["António Guterres", "Ban Ki-moon", "Kofi Annan", "Boutros Boutros-Ghali"],
    "What is the capital of Brazil?": ["Brasília", "Rio de Janeiro", "São Paulo", "Salvador"],
    "Who discovered the law of universal gravitation?": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Johannes Kepler"],
    "What is the chemical symbol for the element with atomic number 78?": ["Pt", "Au", "Ag", "Fe"],
    "Who painted 'The Starry Night'?": ["Vincent Van Gogh", "Pablo Picasso", "Claude Monet", "Leonardo da Vinci"],
    "What is the capital of Russia?": ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg"],
    "Who is known as the Mother of Modern Physics?": ["Marie Curie", "Rosalind Franklin", "Lise Meitner", "Chien-Shiung Wu"],
    "What is the powerhouse of the cell?": ["Mitochondria", "Nucleus", "Ribosome", "Endoplasmic Reticulum"],
    "Who wrote 'Pride and Prejudice'?": ["Jane Austen", "Emily Brontë", "Louisa May Alcott", "Virginia Woolf"],
    "What is the currency of India?": ["Rupee", "Dollar", "Euro", "Pound"],
    "Who is the author of 'A Brief History of Time'?": ["Stephen Hawking", "Albert Einstein", "Isaac Newton", "Galileo Galilei"],
    "What is the longest river in the world?": ["Nile", "Amazon", "Yangtze", "Mississippi"],
    "Who is the current Prime Minister of the United Kingdom?": ["Boris Johnson", "Theresa May", "David Cameron", "Gordon Brown"],
    "What is the capital of Germany?": ["Berlin", "Munich", "Hamburg", "Frankfurt"],
    "Who discovered the law of electromagnetic induction?": ["Michael Faraday", "James Clerk Maxwell", "André-Marie Ampère", "Georg Ohm"],
    "What is the chemical symbol for the element with atomic number 47?": ["Ag", "Au", "Fe", "Na"],
    "Who painted 'The Persistence of Memory'?": ["Salvador Dalí", "Pablo Picasso", "Vincent Van Gogh", "Claude Monet"]
}

l=list(kbc.keys())


money = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 70000000]
n=0


while True:
    a=random.choice(l)
    
    l.remove(a)
    options=list(kbc[a])
    random.shuffle(options)
    print(a)

   
    for i in options:
        print(i)
    ans=int(input("Answer:"))
    if options[ans-1]==kbc[a][0]:
        
        print("Correct Answer, You win", money[n])
        if n==14:
            print("YOOU HAVE WON THE GAME!")
            break
    
        n+=1
        print()
        print()
    
    else:
        print("Correct answer is",kbc[a][0])
        print("Sadly, YOU LOST IT!")
        if n==0:
            print("But you won NOTHING, great isnt it?")

        else:
            print("But you won", money[n-1])
        break
    



