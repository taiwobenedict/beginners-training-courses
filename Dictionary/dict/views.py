from django.shortcuts import render


dictionary = [
    {
        "slug_index":     "all-A",
        "slug_meaning":   "meaning",
        "index":          'A',
        "abaddon":        "The destroyer, or angel of the bottomless pit; - the same as Apollyon and Asmodeus",
        "aba":            "A loose sleeveless outer garment made from aba cloth; worn by Arabs",
        "abacinate":      "Blind by holding a red-hot metal plate before someone's eyes",
        "abridge":        "Reduce in scope while retaining essential elements",
    },
    {
        "slug_index":     "all-B",
        "slug_meaning":   "meaning",
        "index":          'B',
        "backhoe":        "An excavator whose shovel bucket is attached to a hinged boom and is drawn backward to move earth",
        "backing":        "Pick one person to give support and approval to in a particular role",
        "backup":         "A musical part (vocal or instrumental) that supports or provides background for other musical parts",
        "back off":      "Move backwards from a certain position",
    },
    {
        "slug_index":     "all-C",
        "slug_meaning":   "meaning",
        "index":          'C',
        "centigrade":     "Of or relating to a temperature scale on which the freezing point of water is 0 degrees and the boiling point of water is 100 degrees",
        "centile":        "(statistics) any of the 99 numbered points that divide an ordered set of scores into 100 parts each of which contains one-hundredth of the total",
        "central":        "In or near a center or constituting a center; the inner area",
        "Central Africa": "A landlocked country in central Africa; formerly under French control; became independent in 1960",
    },
]


def get_letters(letters):
    return letters["index"]

ordered_words = sorted(dictionary, key=get_letters)

def homepage(request):
    return render(request, "dict/homepage.html", {
        
    })


def index(request):
    return render(request, "dict/index.html", {
        "index": ordered_words
    })


def all_words(request):
    ordered_words = sorted(dictionary, key=get_letters)
    list_of_words = []
    
    for dict in ordered_words:
        count = 0
        for word in dict:
            count += 1
            if 4 > count:
                pass
            else:
                list_of_words.append(word)

    return render(request, "dict/all_words.html", {
        "all_words": list_of_words
    })


def letter_collection(request, letter):
    each_letter = list(next(word for word in dictionary if word['slug_index']== letter))
    return render(request, "dict/letter_collection.html", {
        "each_letter": each_letter[3:]
    })
    

def meaning(request, meaning):
    ordered_words = sorted(dictionary, key=get_letters)
    for word in ordered_words:
        for key in word:
            if key == meaning:
                word_meaning = word[key]
                return render(request, "dict/meanning.html", {
                    'word_meaning':word_meaning,
                    "word": key
                })
