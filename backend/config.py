from typing import Dict, List
from models import VectorCharacterProfile

ARCHETYPE_TAGS = [
    "DIRECT_FORCE", "CALCULATED_MIND", "CHAOTIC_FLOW", "SACRED_DUTY", 
    "UNBOUND_AMBITION", "EMPATHETIC_BOND", "MYSTIC_UNIVERSE", "SHADOW_OPERATIVE", 
    "SOVEREIGN_REBEL", "BENEVOLENT_RULER", "RECKLESS_AVENGER", "STAGNANT_ANCHOR"
]

NUM_TAGS = len(ARCHETYPE_TAGS)

FRANCHISE_VECTOR_REGISTRY: Dict[str, List[VectorCharacterProfile]] = {
    "marvel": [
        VectorCharacterProfile(name="Iron Man", tagline="The Armored Avenger", desc="A visionary strategist.",image="/characters/marvel/ironman.png", geometry={"color": "#E09E8C"}, trait_vector=[0.5, 1.0, 0.6, 0.2, 0.8, 0.4, 0.1, 0.3, 0.4, 0.8, 0.2, 0.1]),
        VectorCharacterProfile(name="Captain America", tagline="The First Avenger", desc="An unshakeable moral compass.",image="/characters/marvel/cap.png", geometry={"color": "#A98CE0"}, trait_vector=[0.8, 0.3, 0.1, 1.0, 0.1, 0.9, 0.1, 0.2, 0.7, 0.6, 0.1, 0.3]),
        VectorCharacterProfile(name="Thor", tagline="God of Thunder", desc="A powerful warrior.",image="/characters/marvel/thor.png", geometry={"color": "#FFD700"}, trait_vector=[1.0, 0.2, 0.5, 0.6, 0.3, 0.7, 0.4, 0.1, 0.5, 0.6, 0.8, 0.1]),
        VectorCharacterProfile(name="Spider-Man", tagline="Friendly Neighborhood Hero", desc="Quick wit and acrobatic flow.",image="/characters/marvel/spiderman.png", geometry={"color": "#FF4500"}, trait_vector=[0.4, 0.7, 0.9, 0.4, 0.1, 1.0, 0.0, 0.2, 0.3, 0.2, 0.1, 0.6]),
        VectorCharacterProfile(name="Black Widow", tagline="The Master Spy", desc="Calculated and precise.", geometry={"color": "#333333"}, trait_vector=[0.5, 0.8, 0.3, 0.6, 0.2, 0.5, 0.0, 1.0, 0.4, 0.3, 0.3, 0.4])
    ],
    "kung_fu_panda": [
        VectorCharacterProfile(name="Po", tagline="The Dragon Warrior", desc="Fluid soul and humor.", geometry={"color": "#DFBA73"}, trait_vector=[0.6, 0.2, 1.0, 0.5, 0.1, 1.0, 0.9, 0.1, 0.6, 0.4, 0.2, 0.3]),
        VectorCharacterProfile(name="Tigress", tagline="Leader of the Furious Five", desc="Driven by raw perfection.", geometry={"color": "#E08C8C"}, trait_vector=[1.0, 0.5, 0.1, 0.9, 0.4, 0.6, 0.4, 0.3, 0.3, 0.5, 0.5, 0.4]),
        VectorCharacterProfile(name="Shifu", tagline="Master of the Jade Palace", desc="Disciplined and strategic.", geometry={"color": "#8CBBE0"}, trait_vector=[0.5, 0.8, 0.3, 1.0, 0.3, 0.6, 0.7, 0.4, 0.2, 0.8, 0.3, 0.7]),
        VectorCharacterProfile(name="Oogway", tagline="Founder of Kung Fu", desc="Aligned with cosmic flow.", geometry={"color": "#8CE0A8"}, trait_vector=[0.4, 0.6, 0.6, 0.8, 0.1, 0.7, 1.0, 0.2, 0.4, 0.9, 0.0, 0.9]),
        VectorCharacterProfile(name="Tai Lung", tagline="The Snow Leopard", desc="Driven by unbridled ambition.", geometry={"color": "#A0522D"}, trait_vector=[1.0, 0.6, 0.2, 0.5, 0.9, 0.2, 0.3, 0.4, 0.9, 0.3, 1.0, 0.1])
    ],
    "avatar": [
    VectorCharacterProfile(
        name="Aang",
        tagline="The Last Airbender",
        desc="Playful spirit carrying impossible responsibility.",
        image="/characters/avatar/aang.png",
        geometry={"color": "#7FD8FF"},
        trait_vector=[
            0.45,  # DIRECT_FORCE
            0.55,  # CALCULATED_MIND
            0.95,  # CHAOTIC_FLOW
            0.95,  # SACRED_DUTY
            0.10,  # UNBOUND_AMBITION
            1.00,  # EMPATHETIC_BOND
            0.95,  # MYSTIC_UNIVERSE
            0.10,  # SHADOW_OPERATIVE
            0.75,  # SOVEREIGN_REBEL
            0.80,  # BENEVOLENT_RULER
            0.10,  # RECKLESS_AVENGER
            0.30,  # STAGNANT_ANCHOR
        ]
    ),

    VectorCharacterProfile(
        name="Zuko",
        tagline="The Banished Prince",
        desc="A relentless search for identity.",
        image="/characters/avatar/zuko.png",
        geometry={"color": "#E07A5F"},
        trait_vector=[ 0.85,0.65,0.45,0.85,0.75,0.70,0.30,0.35,0.80,0.75,0.90,0.20,
        ]
    ),

    VectorCharacterProfile(
        name="Katara",
        tagline="Master Waterbender",
        desc="Compassion guided by conviction.",
        image="/characters/avatar/katara.png",
        geometry={"color": "#5DADE2"},
        trait_vector=[
            0.65,
            0.70,
            0.45,
            0.90,
            0.20,
            1.00,
            0.55,
            0.15,
            0.45,
            0.85,
            0.35,
            0.55,
        ]
    ),

    VectorCharacterProfile(
        name="Toph",
        tagline="The Blind Bandit",
        desc="Absolute confidence and independence.",
        image="/characters/avatar/toph.png",
        geometry={"color": "#8BC34A"},
        trait_vector=[
            0.95,
            0.60,
            0.80,
            0.40,
            0.55,
            0.55,
            0.20,
            0.15,
            0.95,
            0.25,
            0.60,
            0.05,
        ]
    ),

    VectorCharacterProfile(
        name="Iroh",
        tagline="The Dragon of the West",
        desc="Wisdom without domination.",
        image="/characters/avatar/iroh.png",
        geometry={"color": "#C68642"},
        trait_vector=[
            0.55,
            0.90,
            0.45,
            0.95,
            0.10,
            1.00,
            1.00,
            0.10,
            0.30,
            1.00,
            0.05,
            0.95,
        ]
    )
    ],
    "dc": [
    VectorCharacterProfile(
        name="Batman",
        tagline="The Dark Knight",
        desc="Preparation above all else.",
        image="/characters/dc/batman.png",
        geometry={"color": "#4B5563"},
        trait_vector=[
            0.70,
            1.00,
            0.15,
            0.95,
            0.45,
            0.35,
            0.20,
            1.00,
            0.60,
            0.65,
            0.55,
            0.90,
        ],stats={
        "combat":94,
        "intelligence":100,
        "resolve":100,
        "influence":90,
        "adaptability":84,
        "morality":90
    }
    ),

    VectorCharacterProfile(
        name="Superman",
        tagline="The Man of Steel",
        desc="Power restrained by compassion.",
        image="/characters/dc/superman.png",
        geometry={"color": "#3B82F6"},
        trait_vector=[
            1.00,
            0.65,
            0.25,
            1.00,
            0.10,
            1.00,
            0.35,
            0.10,
            0.35,
            1.00,
            0.10,
            0.70,
        ]
    ),

    VectorCharacterProfile(
        name="Wonder Woman",
        tagline="Amazon Warrior",
        desc="Truth, honor, and decisive action.",
        image="/characters/dc/wonderwoman.png",
        geometry={"color": "#D4AF37"},
        trait_vector=[
            0.95,
            0.75,
            0.40,
            1.00,
            0.20,
            0.90,
            0.55,
            0.10,
            0.60,
            0.95,
            0.30,
            0.55,
        ]
    ),

    VectorCharacterProfile(
        name="The Flash",
        tagline="The Fastest Man Alive",
        desc="Optimism moving faster than doubt.",
        image="/characters/dc/flash.png",
        geometry={"color": "#E53935"},
        trait_vector=[
            0.65,
            0.65,
            1.00,
            0.70,
            0.15,
            0.95,
            0.15,
            0.10,
            0.45,
            0.55,
            0.20,
            0.20,
        ]
    ),

    VectorCharacterProfile(
        name="Joker",
        tagline="The Clown Prince of Crime",
        desc="Chaos without restraint.",
        image="/characters/dc/joker.png",
        geometry={"color": "#8E44AD"},
        trait_vector=[
            0.40,
            0.80,
            1.00,
            0.00,
            0.90,
            0.00,
            0.05,
            0.95,
            1.00,
            0.00,
            1.00,
            0.00,
        ]
    )
],
}