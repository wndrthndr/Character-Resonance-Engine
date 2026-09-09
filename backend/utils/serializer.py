TRAIT_LABELS = [
    "Aggressive",
    "Analytical",
    "Humorous",
    "Leader",
    "Disciplined",
    "Moral",
    "Adaptive",
    "Strategic",
    "Calm",
    "Bold",
    "Resilient",
    "Visionary"
]

def get_stats(trait_vector):
    if not trait_vector or len(trait_vector) < 12:
        return {}

    return {
        "combat": round((trait_vector[0] + trait_vector[10]) / 2, 2),
        "intelligence": round((trait_vector[1] + trait_vector[9]) / 2, 2),
        "resolve": round((trait_vector[3] + trait_vector[5]) / 2, 2),
        "influence": round((trait_vector[4] + trait_vector[7]) / 2, 2),
        "adaptability": round((trait_vector[2] + trait_vector[11]) / 2, 2),
        "morality": round((trait_vector[6] + trait_vector[8]) / 2, 2),
    }

def vector_to_traits(vector):
    paired = list(zip(TRAIT_LABELS, vector))

    # sort by strength
    paired.sort(key=lambda x: x[1], reverse=True)

    # take top 4
    return [trait for trait, _ in paired[:4]]


def serialize_character(character, franchise):
    return {
        "name": character.name,
        "tagline": character.tagline,
        "desc": character.desc,
        "image": character.image,
        "franchise": franchise,

        "stats": get_stats(character.trait_vector),

        # 🔥 NEW
        "traits": vector_to_traits(character.trait_vector),

        "geometry": character.geometry
    }

def get_top_traits(vector):
    trait_map = [
        "Strategist",        # 0
        "Intellectual",      # 1
        "Rebel",             # 2
        "Disciplined",       # 3
        "Empathetic",        # 4
        "Leader",            # 5
        "Risk Taker",        # 6
        "Calm & Wise",       # 7
        "Aggressive",        # 8
        "Lone Wolf",         # 9
        "Protector",         # 10
        "Visionary"          # 11
    ]

    paired = list(zip(trait_map, vector))
    paired.sort(key=lambda x: x[1], reverse=True)

    return [trait for trait, _ in paired[:3]]