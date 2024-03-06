import random
import string

print("This is Grace's Password Generator")
print("Press 'Enter' to generate password.")
input()

#list of things
adjective_list = ["big", "small", "happy", "sad", "fast", "slow", "loud", "quiet", "bright", "dark", "hot", "cold", "hard", "soft", "tall", "short", "thin", "thick", "old", "young", "rich", "poor", "clean", "dirty", "smooth", "rough", "light", "heavy", "empty", "full", "wide", "narrow", "empty", "full", "deep", "shallow", "smooth", "rough", "free", "busy", "calm", "chaotic", "brave", "fearful", "strong", "weak", "kind", "cruel", "simple", "complex", "plain", "fancy", "good", "bad", "new", "old", "fresh", "stale", "loud", "quiet", "wild", "tame", "bright", "dull", "clean", "dirty", "smooth", "rough", "empty", "full", "deep", "shallow", "wide", "narrow", "strong", "weak", "tasty", "bland", "simple", "complex", "calm", "chaotic", "brave", "fearful", "happy", "sad", "fast", "slow", "rich", "poor", "hot", "cold", "bright", "dark", "tall", "short", "thin", "thick", "old", "young", "clean", "dirty", "soft", "hard", "free", "busy", "plain", "fancy", "good", "bad", "new", "old", "fresh", "stale", "wild", "tame", "kind", "cruel", "light", "heavy", "simple", "complex", "empty", "full", "smooth", "rough", "loud", "quiet", "bright", "dark", "calm", "chaotic", "brave", "fearful", "strong", "weak", "wide", "narrow", "clean", "dirty", "deep", "shallow", "free", "busy", "plain", "fancy", "good", "bad", "new", "old", "fresh", "stale", "soft", "hard", "tasty", "bland", "simple", "complex", "plain", "fancy", "rich", "poor", "bright", "dark", "happy", "sad", "fast", "slow", "tall", "short", "thin", "thick", "old", "young", "clean", "dirty", "smooth", "rough", "light", "heavy", "empty", "full", "wide", "narrow", "deep", "shallow", "strong", "weak", "kind", "cruel", "simple", "complex", "plain", "fancy", "good", "bad", "new", "old", "fresh", "stale", "loud", "quiet", "wild", "tame", "bright", "dull", "clean", "dirty", "smooth", "rough", "empty", "full", "deep", "shallow", "wide", "narrow", "strong", "weak", "tasty", "bland"]
verb_list =["accepts", "achieves", "acts", "adapts", "adds", "adjusts", "admires", "admits", "adopts", "affirms","agrees", "alarms", "aligns", "allows", "analyzes", "apologizes", "applies", "appreciates", "approves", "argues","ascends", "asks", "asserts", "assumes", "attaches", "attracts", "avoids", "balances", "barks", "bears","believes", "belongs", "bends", "binds", "blames", "boasts", "borrows", "breathes", "builds", "bursts",
    "calculates", "captures", "cares", "carries", "changes", "charges", "chases", "cheers", "chooses", "claims",
    "cleans", "climbs", "closes", "collects", "combines", "comforts", "commands", "communicates", "compares", "complains",
    "completes", "concludes", "confesses", "confirms", "connects", "considers", "constructs", "contemplates", "controls", "cooks",
    "coordinates", "corrects", "counts", "creates", "criticizes", "crosses", "cuts", "damages", "dances", "dares",
    "decreases", "defends", "defines", "delays", "delights", "delivers", "depends", "describes", "desires", "destroys",
    "detects", "develops", "disagrees", "disappears", "discovers", "discusses", "divides", "dominates", "doubts", "drafts",
    "drives", "drops", "drowns", "earns", "edits", "educates", "elevates", "embraces", "emerges", "employs",
    "enables", "encourages", "ends", "enjoys", "enters", "establishes", "evaluates", "exclaims", "exercises", "exists",
    "expands", "expects", "explains", "explores", "expresses", "faces", "fails", "fears", "feeds", "feels",
    "finds", "finishes", "fixes", "follows", "forgets", "forgives", "forms", "frees", "fulfills", "gathers",
    "generates", "gives", "glows", "goes", "grabs", "greets", "grows", "guides", "hails", "handles",
    "hangs", "happens", "harms", "hates", "hears", "helps", "hides", "highlights", "hopes", "hugs",
    "identifies", "ignores", "imagines", "implements", "improves", "includes", "incorporates", "indicates", "infuses", "inherits",
    "initiates", "inspires", "integrates", "intends", "interacts", "interprets", "interviews", "introduces", "invents", "invests",
    "invites", "involves", "isolates", "jumps", "justifies", "keeps", "kicks", "kisses", "knows", "laughs",
    "leads", "learns", "leaves", "lends", "lets", "lights", "listens", "lives", "looks", "loves",
    "maintains", "manages", "measures", "meets", "melds", "mentions", "merges", "misses", "mixes", "modifies",
    "monitors", "motivates", "moves", "navigates", "needs", "negotiates", "notices", "nurtures", "obeys", "observes",
    "obtains", "occurs", "offers", "opposes", "organizes", "overcomes", "owns", "pays", "perceives", "performs",
    "permits", "persuades", "photographs", "picks", "plans", "plays", "pleases", "plugs", "possesses", "prevents",
    "proclaims", "produces", "progresses", "promises", "proposes", "protects", "provides", "pursues", "questions", "quotes",
    "races", "reacts", "reads", "realizes", "recommends", "reflects", "refuses", "regrets", "relaxes", "relies",
    "remembers", "removes", "repairs", "repeats", "replaces", "represents", "requests", "rescues", "resides", "respects",
    "rests", "retires", "returns", "reveals", "revolves", "rides", "rises", "rocks", "rolls", "runs",
    "satisfies", "saves", "scares", "schedules", "seeks", "sees", "selects", "sells", "sends", "senses",
    "separates", "sets", "settles", "shakes", "shares", "shifts", "shoots", "shows", "shuts", "sings",
    "sits", "slides", "smiles", "solves", "speaks", "speeds", "spends", "spins", "spreads", "stands",
    "starts", "stays", "steps", "stirs", "stops", "strives", "studies", "succeeds", "suffers", "suggests",
    "surprises", "survives", "swims", "takes", "talks", "teaches", "tells", "tests", "thinks", "throws",
    "touches", "travels", "tries", "trusts", "turns", "understands", "unites", "uses", "values", "verifies",
    "visits", "voices", "waits", "walks", "watches", "wears", "welcomes", "whispers", "wins", "works",
    "worries", "writes", "yells"]
noun_list = ["apple", "banana", "cat", "dog", "elephant", "fish", "guitar", "hat", "kerfuffle", "jacket", "kangaroo", "lamp", "moon", "notebook", "orange", "penguin", "quilt", "robot", "sun", "tree", "umbrella", "violin", "watermelon", "xylophone", "yogurt", "zebra", "airplane", "ball", "camera", "dolphin", "envelope", "flower", "globe", "hammer", "island", "jigsaw", "kite", "lemon", "mailbox", "necklace", "ocean", "piano", "quill", "rocket", "socks", "telephone", "unicorn", "volcano", "wallet", "xylograph", "yardstick", "zeppelin", "accordion", "bicycle", "candle", "dinosaur", "easel", "fireplace", "giraffe", "hamburger", "igloo", "jungle", "keyboard", "leopard", "magnifier", "nail", "octopus", "paintbrush", "quokka", "radiator", "saxophone", "telescope", "umbrella", "velvet", "wagon", "xylograph", "yarn", "zipper", "astronaut", "ballet", "carousel", "dragon", "eclipse", "flamingo", "giraffe", "harmonica", "igloo", "jellyfish", "kangaroo", "lighthouse", "marathon", "nebula", "opera", "puzzle", "quasar", "rattlesnake", "skyscraper", "trampoline", "umbrella", "volcano", "whale", "xylophone", "yoga", "zeppelin", "abacus", "beehive", "caterpillar", "daffodil", "elephant", "flute", "gazelle", "honeycomb", "iguana", "jigsaw", "koala", "lighthouse", "marzipan", "nectar", "oasis", "parachute", "quinoa", "rhubarb", "sandbox", "tambourine", "ukulele", "vase", "waffle", "xerox", "yodel", "zamboni"]
adverb_list = ["abnormally", "beautifully", "carefully", "dangerously", "eagerly", "frequently", "gracefully", "hastily", "innocently", "jovially", "keenly", "lazily", "merrily", "nervously", "obnoxiously", "politely", "quickly", "rudely", "swiftly", "tensely", "urgently", "vivaciously", "wisely", "yearningly", "zealously", "absurdly", "bashfully", "cheerfully", "daintily", "elegantly", "famously", "grumpily", "hungrily", "intently", "joyfully", "kookily", "loudly", "meekly", "naturally", "optimistically", "playfully", "quirkily", "rapidly", "safely", "timidly", "uniquely", "vividly", "wholly", "xenophobically", "yearly", "zestfully", "accidentally", "boldly", "cautiously", "daringly", "enthusiastically", "furiously", "gracelessly", "hungrily", "intensely", "jovially", "kookily", "lazily", "mindfully", "naturally", "obviously", "playfully", "quickly", "rudely", "silently", "tactfully", "urgently", "vibrantly", "wildly", "xenophobically", "youthfully", "zealously", "angrily", "briskly", "carefully", "doubtfully", "eagerly", "fondly", "gracefully", "hungrily", "inquisitively", "jovially", "kookily", "lazily", "mindfully", "nervously", "optimistically", "pensively", "quickly", "rudely", "softly", "tensely", "urgently", "vibrantly", "warmly", "xenophobically", "yearningly", "zestfully", "anxiously", "briskly", "curiously", "dramatically", "earnestly", "frantically", "gleefully", "hungrily", "intently", "jovially", "keenly", "lazily", "mindfully", "nervously", "obnoxiously", "politely", "quickly", "rudely", "softly", "tensely", "urgently", "vibrantly", "warmly", "xenophobically", "youthfully", "zealously"]
# US Presidents list with their birth years
us_presidents = {
    "George Washington": 1732, "John Adams": 1735, "Thomas Jefferson": 1743, "James Madison": 1751,
    "James Monroe": 1758, "John Quincy Adams": 1767, "Andrew Jackson": 1767, "Martin Van Buren": 1782,
    "William Henry Harrison": 1773, "John Tyler": 1790, "James K. Polk": 1795, "Zachary Taylor": 1784,
    "Millard Fillmore": 1800, "Franklin Pierce": 1804, "James Buchanan": 1791, "Abraham Lincoln": 1809,
    "Andrew Johnson": 1808, "Ulysses S. Grant": 1822, "Rutherford B. Hayes": 1822, "James A. Garfield": 1831,
    "Chester A. Arthur": 1829, "Grover Cleveland": 1837, "Benjamin Harrison": 1833,
    "William McKinley": 1843, "Theodore Roosevelt": 1858, "William Howard Taft": 1857, "Woodrow Wilson": 1856,
    "Warren G. Harding": 1865, "Calvin Coolidge": 1872, "Herbert Hoover": 1874, "Franklin D. Roosevelt": 1882,
    "Harry S. Truman": 1884, "Dwight D. Eisenhower": 1890, "John F. Kennedy": 1917, "Lyndon B. Johnson": 1908,
    "Richard Nixon": 1913, "Gerald Ford": 1913, "Jimmy Carter": 1924, "Ronald Reagan": 1911, "George H.W. Bush": 1924,
    "Bill Clinton": 1946, "George W. Bush": 1946, "Barack Obama": 1961, "Donald Trump": 1946, "Joe Biden": 1942,
}

while True: 
    
    ran_adjective = random.choice(adjective_list)
    ran_verb = random.choice(verb_list)
    ran_noun = random.choice(noun_list)
    ran_adverb = random.choice(adverb_list)

    # Create a sentence without spaces
    sentence = f"{ran_adjective}{ran_noun}{ran_verb}{ran_adverb}"

    # Extract the first letter of each word
    initials = "".join(word[0] for word in [ran_adjective, ran_noun, ran_verb, ran_adverb])

    # Morse code dictionary
    morse_code_dict = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
        'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
        'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
        'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
        'z': '--..'
    }

    # Translate initials to Morse code
    morse_code = ''.join(morse_code_dict[letter] for letter in initials.lower())

    # 4 digit no.
    def generate_random_4_digit_number():
        # Generate a random 4-digit number with zeros in the 1-thousands place
        random_number = random.randint(0000, 9999)
        return format(random_number, '04d')
    ran_number = generate_random_4_digit_number()

    #USpresidents
    # Function to get initials from a name
    def get_initials(name):
        return '.'.join(word[0] for word in name.split())


    # Randomly choose a US president
    chosen_president = random.choice(list(us_presidents.keys()))

    # Get the president's initials
    president_initials = get_initials(chosen_president)

    # Get the president's birth year
    president_birth_year = us_presidents[chosen_president]

    #Random Symbol
    def generate_random_symbol():
        symbols = string.punctuation.replace('.', '')  # Exclude period to avoid confusion
        return random.choice(symbols)
    rs1 = generate_random_symbol()
    rs2 = generate_random_symbol()

    # Print the result
    print(f"{president_initials}.{president_birth_year}{sentence}{morse_code}{ran_number}{rs1}{rs2}")
    input()
