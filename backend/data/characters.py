from models import VectorCharacterProfile, Behavior


# ==========================================================
# MARVEL CHARACTER PROFILES
#


# Trait order:
# ACTION
# ANALYTICAL
# EMPATHETIC
# JUSTICE_DRIVEN
# AMBITIOUS
# CREATIVE
# LOYAL
# DISCIPLINED
# HUMOROUS
# CURIOUS
# PRAGMATIC
# REBELLIOUS


MARVEL_CHARACTERS = [

    # ======================================================
    # IRON MAN
    # ======================================================

    VectorCharacterProfile(
        name="Iron-Man",
        tagline="Genius, billionaire, and reluctant savior.",
        desc="A brilliant inventor who turns intelligence, ego, improvisation, and ambition into his greatest weapons.",
        image="/characters/marvel/ironman.png",
        geometry={"color": "#C62828"},
        behaviors=[
            Behavior.ANALYTICAL,
            Behavior.CREATIVE,
            Behavior.AMBITIOUS
        ],
        trait_vector=[
            0.68, 1.00, 0.28, 0.42,
            0.92, 1.00, 0.48, 0.55,
            0.82, 0.88, 0.86, 0.68
        ]
    ),

    # ======================================================
    # CAPTAIN AMERICA
    # ======================================================

    VectorCharacterProfile(
        name="Captain America",
        tagline="The soldier who never stops believing.",
        desc="A disciplined idealist whose courage, loyalty, and moral conviction remain steady when everything else changes.",
        image="/characters/marvel/cap.png",
        geometry={"color": "#3B5998"},
        behaviors=[
            Behavior.JUSTICE_DRIVEN,
            Behavior.LOYAL,
            Behavior.DISCIPLINED
        ],
        trait_vector=[
            0.86, 0.48, 0.76, 1.00,
            0.34, 0.28, 1.00, 0.98,
            0.34, 0.42, 0.58, 0.22
        ]
    ),

    # ======================================================
    # THOR
    # ======================================================

    VectorCharacterProfile(
        name="Thor",
        tagline="God of Thunder, king of second chances.",
        desc="A powerful warrior whose pride matures into humility, responsibility, loyalty, and genuine compassion.",
        image="/characters/marvel/thor.png",
        geometry={"color": "#2E4C6D"},
        behaviors=[
            Behavior.ACTION,
            Behavior.LOYAL,
            Behavior.JUSTICE_DRIVEN
        ],
        trait_vector=[
            1.00, 0.28, 0.64, 0.78,
            0.62, 0.30, 0.96, 0.68,
            0.92, 0.30, 0.48, 0.38
        ]
    ),

    # ======================================================
    # HULK
    # ======================================================

    VectorCharacterProfile(
        name="Hulk",
        tagline="The strongest rage wrapped around a gentle mind.",
        desc="A deeply conflicted powerhouse whose destructive instincts exist alongside Bruce Banner's intelligence, vulnerability, and compassion.",
        image="/characters/marvel/hulk.png",
        geometry={"color": "#2E7D32"},
        behaviors=[
            Behavior.ACTION,
            Behavior.EMPATHETIC,
            Behavior.ANALYTICAL
        ],
        trait_vector=[
            1.00, 0.58, 0.82, 0.38,
            0.16, 0.28, 0.68, 0.24,
            0.28, 0.46, 0.30, 0.62
        ]
    ),

    # ======================================================
    # BLACK WIDOW
    # ======================================================

    VectorCharacterProfile(
        name="Black Widow",
        tagline="Every secret has a price she's already paid.",
        desc="A highly trained spy who relies on preparation, deception, adaptability, pragmatism, and a loyalty she rarely displays openly.",
        image="/characters/marvel/black_widow.png",
        geometry={"color": "#4A0404"},
        behaviors=[
            Behavior.ANALYTICAL,
            Behavior.PRAGMATIC,
            Behavior.DISCIPLINED
        ],
        trait_vector=[
            0.72, 0.96, 0.48, 0.62,
            0.42, 0.38, 0.78, 0.96,
            0.24, 0.70, 1.00, 0.46
        ]
    ),

    # ======================================================
    # SPIDER-MAN
    # ======================================================

    VectorCharacterProfile(
        name="Spider-Man",
        tagline="Great power, greater guilt, best one-liners.",
        desc="An empathetic young hero who balances responsibility with curiosity, humor, improvisation, and an instinct to help others.",
        image="/characters/marvel/spiderman.png",
        geometry={"color": "#D32F2F"},
        behaviors=[
            Behavior.EMPATHETIC,
            Behavior.LOYAL,
            Behavior.HUMOROUS
        ],
        trait_vector=[
            0.76, 0.58, 1.00, 0.88,
            0.24, 0.72, 0.94, 0.42,
            1.00, 0.92, 0.42, 0.54
        ]
    ),

    # ======================================================
    # DOCTOR STRANGE
    # ======================================================

    VectorCharacterProfile(
        name="Doctor Strange",
        tagline="He bent time to save everyone but himself.",
        desc="A highly analytical seeker whose relentless pursuit of knowledge develops into discipline, responsibility, and unconventional problem-solving.",
        image="/characters/marvel/doctor_strange.png",
        geometry={"color": "#6A1B9A"},
        behaviors=[
            Behavior.ANALYTICAL,
            Behavior.CURIOUS,
            Behavior.CREATIVE
        ],
        trait_vector=[
            0.38, 1.00, 0.38, 0.68,
            0.62, 0.76, 0.32, 0.94,
            0.30, 1.00, 0.72, 0.42
        ]
    ),

    # ======================================================
    # LOKI
    # ======================================================

    VectorCharacterProfile(
        name="Loki",
        tagline="The god of mischief, allergic to being ordinary.",
        desc="A brilliant manipulator driven by insecurity, ambition, identity, cleverness, and a refusal to accept the role others give him.",
        image="/characters/marvel/loki.png",
        geometry={"color": "#1B5E20"},
        behaviors=[
            Behavior.CREATIVE,
            Behavior.REBELLIOUS,
            Behavior.AMBITIOUS
        ],
        trait_vector=[
            0.42, 0.84, 0.30, 0.18,
            0.90, 1.00, 0.38, 0.42,
            0.72, 0.86, 0.66, 1.00
        ]
    ),

    # ======================================================
    # THANOS
    # ======================================================

    VectorCharacterProfile(
        name="Thanos",
        tagline="Balance, by any means necessary.",
        desc="A ruthless ideologue whose immense ambition is matched by extraordinary patience, conviction, discipline, and pragmatic calculation.",
        image="/characters/marvel/thanos.png",
        geometry={"color": "#4E342E"},
        behaviors=[
            Behavior.AMBITIOUS,
            Behavior.DISCIPLINED,
            Behavior.PRAGMATIC
        ],
        trait_vector=[
            0.76, 0.70, 0.08, 0.74,
            1.00, 0.16, 0.12, 1.00,
            0.08, 0.30, 1.00, 0.42
        ]
    ),

    # ======================================================
    # DEADPOOL
    # ======================================================

    VectorCharacterProfile(
        name="Deadpool",
        tagline="Chaos with a katana and a punchline.",
        desc="An unpredictable mercenary who hides pain behind relentless humor, improvisation, violence, and deliberate chaos.",
        image="/characters/marvel/deadpool.png",
        geometry={"color": "#8E0000"},
        behaviors=[
            Behavior.HUMOROUS,
            Behavior.REBELLIOUS,
            Behavior.CREATIVE
        ],
        trait_vector=[
            0.92, 0.26, 0.52, 0.18,
            0.28, 0.94, 0.64, 0.20,
            1.00, 0.64, 0.48, 1.00
        ]
    ),

    # ======================================================
    # MOON KNIGHT
    # ======================================================

    VectorCharacterProfile(
        name="Moon Knight",
        tagline="Many faces, one broken vow to protect.",
        desc="A relentless and psychologically complex protector whose violence, conviction, and unconventional morality drive him forward.",
        image="/characters/marvel/moon_knight.png",
        geometry={"color": "#B0BEC5"},
        behaviors=[
            Behavior.ACTION,
            Behavior.JUSTICE_DRIVEN,
            Behavior.REBELLIOUS
        ],
        trait_vector=[
            1.00, 0.34, 0.34, 0.82,
            0.26, 0.30, 0.58, 0.46,
            0.20, 0.38, 0.68, 0.98
        ]
    ),

    # ======================================================
    # WOLVERINE
    # ======================================================

    VectorCharacterProfile(
        name="Wolverine",
        tagline="A healing wound that never stops fighting.",
        desc="A fiercely independent survivor whose ferocity hides deep loyalty, instinctive compassion, stubbornness, and a long memory of pain.",
        image="/characters/marvel/wolverine.png",
        geometry={"color": "#F9A825"},
        behaviors=[
            Behavior.ACTION,
            Behavior.LOYAL,
            Behavior.REBELLIOUS
        ],
        trait_vector=[
            1.00, 0.22, 0.58, 0.62,
            0.24, 0.18, 0.98, 0.52,
            0.38, 0.24, 0.72, 0.96
        ]
    ),

    # ======================================================
    # SCARLET WITCH
    # ======================================================

    VectorCharacterProfile(
        name="Scarlet Witch",
        tagline="Grief given the power to rewrite worlds.",
        desc="An extraordinarily powerful and emotionally driven woman whose love, grief, imagination, and desperation can reshape reality itself.",
        image="/characters/marvel/scarlet_witch.png",
        geometry={"color": "#B71C1C"},
        behaviors=[
            Behavior.EMPATHETIC,
            Behavior.CREATIVE,
            Behavior.AMBITIOUS
        ],
        trait_vector=[
            0.54, 0.48, 1.00, 0.44,
            0.58, 1.00, 0.94, 0.24,
            0.22, 0.72, 0.28, 0.62
        ]
    ),

    # ======================================================
    # KILLMONGER
    # ======================================================

    VectorCharacterProfile(
        name="Killmonger",
        tagline="A prince exiled, returning to burn the throne.",
        desc="A brilliant and ruthless revolutionary whose ambition, tactical thinking, anger, and conviction turn personal pain into ideology.",
        image="/characters/marvel/killmonger.png",
        geometry={"color": "#212121"},
        behaviors=[
            Behavior.AMBITIOUS,
            Behavior.REBELLIOUS,
            Behavior.ACTION
        ],
        trait_vector=[
            0.96, 0.62, 0.18, 0.48,
            1.00, 0.38, 0.22, 0.76,
            0.16, 0.48, 0.86, 1.00
        ]
    ),

    # ======================================================
    # VENOM
    # ======================================================

    VectorCharacterProfile(
        name="Venom",
        tagline="A monster that decided to be a hero anyway.",
        desc="A volatile antihero whose violent instincts are tempered by attachment, loyalty, humor, and a growing desire to protect the innocent.",
        image="/characters/marvel/venom.png",
        geometry={"color": "#1A1A1A"},
        behaviors=[
            Behavior.ACTION,
            Behavior.HUMOROUS,
            Behavior.LOYAL
        ],
        trait_vector=[
            0.98, 0.18, 0.72, 0.34,
            0.20, 0.46, 1.00, 0.18,
            0.88, 0.28, 0.52, 0.84
        ]
    ),
]

# ==========================================================
# AVATAR: THE LAST AIRBENDER CHARACTER PROFILES
#
# Trait order:
# 0 ACTION
# 1 ANALYTICAL
# 2 EMPATHETIC
# 3 JUSTICE_DRIVEN
# 4 AMBITIOUS
# 5 CREATIVE
# 6 LOYAL
# 7 DISCIPLINED
# 8 HUMOROUS
# 9 CURIOUS
# 10 PRAGMATIC
# 11 REBELLIOUS




# ==========================================================
# ATLA CHARACTER PROFILES
#
# IMPORTANT:
# - These values are comparative CHARACTER SIGNATURES, not
#   objective power levels.
# - The scores are deliberately calibrated so that characters
#   who are commonly compared within ATLA retain sensible
#   relationships.
# - "ACTION" remains the existing schema dimension; it should
#   NOT be interpreted as raw bending/combat power.
# ==========================================================

ATLA_CHARACTERS = [

    VectorCharacterProfile(
        name="Aang",
        tagline="The last Air Nomad who refused to lose his compassion.",
        desc="Playful and deeply compassionate, Aang carries an enormous responsibility while consistently seeking peaceful solutions and protecting life.",
        image="/characters/atla/aang.png",
        geometry={"color": "#81D4FA"},
        behaviors=[Behavior.EMPATHETIC, Behavior.JUSTICE_DRIVEN, Behavior.CREATIVE],
        trait_vector=[
            0.76, 0.42, 1.00, 0.98,
            0.30, 0.86, 0.92, 0.70,
            0.88, 0.72, 0.58, 0.54
        ]
    ),

    VectorCharacterProfile(
        name="Katara",
        tagline="A healer, waterbender, and heart that would not break.",
        desc="Determined, emotionally perceptive, fiercely protective, and willing to fight for people she loves even when compassion becomes difficult.",
        image="/characters/atla/katara.png",
        geometry={"color": "#29B6F6"},
        behaviors=[Behavior.EMPATHETIC, Behavior.ACTION, Behavior.JUSTICE_DRIVEN],
        trait_vector=[
            0.90, 0.62, 0.96, 0.94,
            0.52, 0.62, 0.98, 0.72,
            0.48, 0.62, 0.70, 0.56
        ]
    ),

    VectorCharacterProfile(
        name="Sokka",
        tagline="The strategist who proved you do not need bending to matter.",
        desc="A practical strategist with sharp humor, inventive thinking, strong loyalty, and a habit of turning limited resources into workable plans.",
        image="/characters/atla/sokka.png",
        geometry={"color": "#1565C0"},
        behaviors=[Behavior.ANALYTICAL, Behavior.CREATIVE, Behavior.HUMOROUS],
        trait_vector=[
            0.68, 0.94, 0.58, 0.68,
            0.46, 0.88, 0.92, 0.66,
            0.94, 0.76, 0.94, 0.42
        ]
    ),

    VectorCharacterProfile(
        name="Toph",
        tagline="The blind bandit who could feel the world beneath her feet.",
        desc="Blunt, fiercely independent, extraordinarily perceptive, and inventive, Toph trusts her instincts and rejects anyone trying to control her.",
        image="/characters/atla/toph.png",
        geometry={"color": "#8D6E63"},
        behaviors=[Behavior.ACTION, Behavior.REBELLIOUS, Behavior.CREATIVE],
        trait_vector=[
            0.96, 0.76, 0.48, 0.64,
            0.42, 0.86, 0.62, 0.74,
            0.68, 0.92, 0.80, 0.98
        ]
    ),

    VectorCharacterProfile(
        name="Zuko",
        tagline="A prince who had to lose himself before finding honor.",
        desc="Intense and disciplined, Zuko begins consumed by shame and approval-seeking before gradually choosing responsibility, compassion, and genuine honor.",
        image="/characters/atla/zuko.png",
        geometry={"color": "#D84315"},
        behaviors=[Behavior.DISCIPLINED, Behavior.ACTION, Behavior.JUSTICE_DRIVEN],
        trait_vector=[
            0.92, 0.64, 0.74, 0.86,
            0.72, 0.34, 0.96, 0.92,
            0.22, 0.42, 0.72, 0.74
        ]
    ),

    VectorCharacterProfile(
        name="Iroh",
        tagline="A dragon who learned that wisdom is gentler than victory.",
        desc="Patient, compassionate, perceptive, humorous, and profoundly wise, Iroh values growth over domination and guides others without forcing their path.",
        image="/characters/atla/iroh.png",
        geometry={"color": "#FFB300"},
        behaviors=[Behavior.EMPATHETIC, Behavior.ANALYTICAL, Behavior.JUSTICE_DRIVEN],
        trait_vector=[
            0.58, 0.96, 0.98, 0.94,
            0.38, 0.68, 0.98, 0.88,
            0.82, 0.82, 0.92, 0.22
        ]
    ),

    VectorCharacterProfile(
        name="Azula",
        tagline="Perfection sharpened into a weapon.",
        desc="A prodigious firebender whose intelligence, ambition, control, and tactical precision are undermined by fear, isolation, and a need for control.",
        image="/characters/atla/azula.png",
        geometry={"color": "#1565C0"},
        behaviors=[Behavior.ANALYTICAL, Behavior.AMBITIOUS, Behavior.DISCIPLINED],
        trait_vector=[
            0.96, 0.98, 0.16, 0.20,
            1.00, 0.62, 0.30, 1.00,
            0.20, 0.68, 0.94, 0.72
        ]
    ),

    VectorCharacterProfile(
        name="Mai",
        tagline="Deadpan loyalty hidden beneath indifference.",
        desc="Reserved, observant, emotionally guarded, and remarkably loyal once she chooses someone, Mai acts decisively when her principles and attachments are tested.",
        image="/characters/atla/mai.png",
        geometry={"color": "#455A64"},
        behaviors=[Behavior.PRAGMATIC, Behavior.LOYAL, Behavior.DISCIPLINED],
        trait_vector=[
            0.70, 0.72, 0.66, 0.70,
            0.24, 0.30, 0.94, 0.82,
            0.62, 0.40, 0.92, 0.58
        ]
    ),

    VectorCharacterProfile(
        name="Ty Lee",
        tagline="A bright smile hiding a remarkably skilled fighter.",
        desc="Cheerful, socially perceptive, agile, and eager to connect, Ty Lee often avoids conflict but is capable of decisive action when people she cares about are threatened.",
        image="/characters/atla/ty_lee.png",
        geometry={"color": "#EC407A"},
        behaviors=[Behavior.EMPATHETIC, Behavior.HUMOROUS, Behavior.ACTION],
        trait_vector=[
            0.78, 0.52, 0.84, 0.66,
            0.22, 0.54, 0.82, 0.56,
            0.96, 0.70, 0.48, 0.40
        ]
    ),

    VectorCharacterProfile(
        name="Suki",
        tagline="A warrior who leads with discipline, courage, and loyalty.",
        desc="A highly trained Kyoshi Warrior who combines discipline and combat skill with strong moral conviction, empathy, and unwavering loyalty to her friends.",
        image="/characters/atla/suki.png",
        geometry={"color": "#43A047"},
        behaviors=[Behavior.DISCIPLINED, Behavior.JUSTICE_DRIVEN, Behavior.LOYAL],
        trait_vector=[
            0.92, 0.64, 0.86, 0.88,
            0.34, 0.42, 1.00, 0.96,
            0.40, 0.52, 0.78, 0.36
        ]
    ),

    VectorCharacterProfile(
        name="Appa",
        tagline="A gentle giant who always finds his way home.",
        desc="Gentle, loyal, affectionate, and brave, Appa is a dependable companion whose protective instincts emerge when his family is in danger.",
        image="/characters/atla/appa.png",
        geometry={"color": "#BCAAA4"},
        behaviors=[Behavior.LOYAL, Behavior.EMPATHETIC, Behavior.ACTION],
        trait_vector=[
            0.82, 0.20, 0.90, 0.62,
            0.08, 0.12, 1.00, 0.64,
            0.20, 0.18, 0.34, 0.12
        ]
    ),

    VectorCharacterProfile(
        name="Ozai",
        tagline="Power without compassion becomes tyranny.",
        desc="A ruthless ruler driven by domination, status, control, and fear, Ozai treats loyalty as obedience and power as proof of worth.",
        image="/characters/atla/ozai.png",
        geometry={"color": "#212121"},
        behaviors=[Behavior.AMBITIOUS, Behavior.DISCIPLINED, Behavior.ACTION],
        trait_vector=[
            0.96, 0.70, 0.04, 0.10,
            1.00, 0.12, 0.20, 0.94,
            0.06, 0.20, 0.86, 0.76
        ]
    ),
]


# ==========================================================
# DC CHARACTER PROFILES
# ==========================================================

DC_CHARACTERS = [

    VectorCharacterProfile(
        name="Superman",
        tagline="Powerful enough to rule, compassionate enough not to.",
        desc="A symbol of hope whose immense power is restrained by compassion, responsibility, humility, and an enduring commitment to doing what is right.",
        image="/characters/dc/superman.png",
        geometry={"color": "#1565C0"},
        behaviors=[Behavior.JUSTICE_DRIVEN, Behavior.EMPATHETIC, Behavior.DISCIPLINED],
        trait_vector=[
            0.98, 0.76, 1.00, 1.00,
            0.24, 0.54, 0.98, 0.92,
            0.54, 0.52, 0.76, 0.10
        ]
    ),

    VectorCharacterProfile(
        name="Batman",
        tagline="Preparation turned into a crusade.",
        desc="A disciplined detective who turns trauma into relentless preparation, strategic thinking, and a personal war against crime.",
        image="/characters/dc/batman.png",
        geometry={"color": "#263238"},
        behaviors=[Behavior.ANALYTICAL, Behavior.DISCIPLINED, Behavior.JUSTICE_DRIVEN],
        trait_vector=[
            0.92, 1.00, 0.54, 0.94,
            0.46, 0.72, 0.96, 1.00,
            0.26, 0.84, 0.98, 0.48
        ]
    ),

    VectorCharacterProfile(
        name="Wonder Woman",
        tagline="A warrior who believes peace is worth fighting for.",
        desc="A principled warrior who balances immense combat ability with compassion, truth, diplomacy, and a deep commitment to justice.",
        image="/characters/dc/wonder_woman.png",
        geometry={"color": "#B71C1C"},
        behaviors=[Behavior.JUSTICE_DRIVEN, Behavior.EMPATHETIC, Behavior.DISCIPLINED],
        trait_vector=[
            0.98, 0.74, 0.94, 1.00,
            0.44, 0.62, 0.96, 0.94,
            0.46, 0.58, 0.76, 0.18
        ]
    ),

    VectorCharacterProfile(
        name="The Flash",
        tagline="The fastest man alive who never stops caring.",
        desc="Optimistic, compassionate, curious, and often humorous, Barry Allen pairs immense capability with a scientist's instinct to understand problems.",
        image="/characters/dc/flash.png",
        geometry={"color": "#C62828"},
        behaviors=[Behavior.ACTION, Behavior.EMPATHETIC, Behavior.CURIOUS],
        trait_vector=[
            0.98, 0.84, 0.94, 0.90,
            0.22, 0.70, 0.90, 0.62,
            0.92, 0.98, 0.66, 0.22
        ]
    ),

    VectorCharacterProfile(
        name="Green Lantern",
        tagline="Willpower given a ring and a universe to protect.",
        desc="A courageous spacefaring hero whose defining quality is willpower, supported by imagination, responsibility, loyalty, and adaptability.",
        image="/characters/dc/green_lantern.png",
        geometry={"color": "#2E7D32"},
        behaviors=[Behavior.ACTION, Behavior.DISCIPLINED, Behavior.CREATIVE],
        trait_vector=[
            0.94, 0.68, 0.70, 0.88,
            0.30, 0.96, 0.90, 0.94,
            0.48, 0.70, 0.68, 0.32
        ]
    ),

    VectorCharacterProfile(
        name="Aquaman",
        tagline="A king torn between two worlds.",
        desc="A proud but responsible ruler who combines warrior instincts with loyalty, leadership, and an increasingly mature sense of duty.",
        image="/characters/dc/aquaman.png",
        geometry={"color": "#0277BD"},
        behaviors=[Behavior.ACTION, Behavior.LOYAL, Behavior.JUSTICE_DRIVEN],
        trait_vector=[
            0.98, 0.48, 0.68, 0.84,
            0.64, 0.28, 0.94, 0.72,
            0.44, 0.42, 0.70, 0.30
        ]
    ),

    VectorCharacterProfile(
        name="Cyborg",
        tagline="Humanity held together by technology.",
        desc="A brilliant technologist who struggles with identity while remaining deeply loyal, analytical, and committed to protecting others.",
        image="/characters/dc/cyborg.png",
        geometry={"color": "#607D8B"},
        behaviors=[Behavior.ANALYTICAL, Behavior.CREATIVE, Behavior.LOYAL],
        trait_vector=[
            0.86, 0.96, 0.78, 0.86,
            0.28, 0.94, 0.96, 0.72,
            0.42, 0.92, 0.90, 0.30
        ]
    ),

    VectorCharacterProfile(
        name="Nightwing",
        tagline="The hero who learned to lead without becoming Batman.",
        desc="A charismatic leader who combines acrobatics, empathy, humor, tactical intelligence, and strong loyalty to the people around him.",
        image="/characters/dc/nightwing.png",
        geometry={"color": "#1976D2"},
        behaviors=[Behavior.ACTION, Behavior.LOYAL, Behavior.EMPATHETIC],
        trait_vector=[
            0.94, 0.78, 0.92, 0.90,
            0.30, 0.68, 1.00, 0.86,
            0.86, 0.70, 0.76, 0.28
        ]
    ),

    VectorCharacterProfile(
        name="Harley Quinn",
        tagline="Chaos with a heart that learned to choose itself.",
        desc="A volatile and highly adaptable antihero whose intelligence, emotional intensity, humor, and independence coexist with a complicated moral history.",
        image="/characters/dc/harley_quinn.png",
        geometry={"color": "#EC407A"},
        behaviors=[Behavior.HUMOROUS, Behavior.REBELLIOUS, Behavior.CREATIVE],
        trait_vector=[
            0.82, 0.78, 0.70, 0.58,
            0.26, 0.94, 0.66, 0.28,
            1.00, 0.72, 0.42, 0.96
        ]
    ),

    VectorCharacterProfile(
        name="Joker",
        tagline="Chaos with no moral floor.",
        desc="An unpredictable agent of cruelty who treats suffering as entertainment and deliberately rejects moral order.",
        image="/characters/dc/joker.png",
        geometry={"color": "#6A1B9A"},
        behaviors=[Behavior.REBELLIOUS, Behavior.CREATIVE, Behavior.HUMOROUS],
        trait_vector=[
            0.78, 0.82, 0.02, 0.02,
            0.76, 1.00, 0.04, 0.06,
            0.98, 0.84, 0.30, 1.00
        ]
    ),

    VectorCharacterProfile(
        name="Lex Luthor",
        tagline="Genius, ambition, and resentment wearing a suit.",
        desc="A brilliant strategist driven by ambition, control, intellect, and resentment toward anyone he believes stands above humanity.",
        image="/characters/dc/lex_luthor.png",
        geometry={"color": "#37474F"},
        behaviors=[Behavior.ANALYTICAL, Behavior.AMBITIOUS, Behavior.PRAGMATIC],
        trait_vector=[
            0.56, 1.00, 0.06, 0.18,
            1.00, 0.72, 0.20, 0.78,
            0.20, 0.76, 0.96, 0.64
        ]
    ),

    VectorCharacterProfile(
        name="Raven",
        tagline="Feeling everything and refusing to be ruled by it.",
        desc="Reserved, introspective, emotionally powerful, and highly disciplined, Raven constantly works to control forces that could overwhelm her.",
        image="/characters/dc/raven.png",
        geometry={"color": "#5E35B1"},
        behaviors=[Behavior.DISCIPLINED, Behavior.ANALYTICAL, Behavior.EMPATHETIC],
        trait_vector=[
            0.82, 0.92, 0.90, 0.84,
            0.30, 0.72, 0.88, 1.00,
            0.24, 0.76, 0.74, 0.42
        ]
    ),

    VectorCharacterProfile(
        name="Starfire",
        tagline="A warrior princess who meets the world with love.",
        desc="Warm, trusting, fiercely loyal, and surprisingly powerful, Starfire combines emotional openness with a strong warrior's courage.",
        image="/characters/dc/starfire.png",
        geometry={"color": "#FF9800"},
        behaviors=[Behavior.EMPATHETIC, Behavior.ACTION, Behavior.LOYAL],
        trait_vector=[
            0.96, 0.34, 1.00, 0.90,
            0.28, 0.46, 1.00, 0.72,
            0.72, 0.62, 0.42, 0.20
        ]
    ),
]


# ==========================================================
# KUNG FU PANDA CHARACTER PROFILES
# ==========================================================

KUNG_FU_PANDA_CHARACTERS = [

    VectorCharacterProfile(
        name="Po",
        tagline="The Dragon Warrior who learned that being himself was enough.",
        desc="Joyful, empathetic, resilient, creative, and increasingly disciplined, Po turns insecurity into genuine courage and leadership.",
        image="/characters/kung_fu_panda/po.png",
        geometry={"color": "#212121"},
        behaviors=[Behavior.EMPATHETIC, Behavior.HUMOROUS, Behavior.ACTION],
        trait_vector=[
            0.94, 0.54, 0.94, 0.90,
            0.34, 0.88, 0.96, 0.72,
            1.00, 0.76, 0.60, 0.34
        ]
    ),

    VectorCharacterProfile(
        name="Master Shifu",
        tagline="A teacher who had to learn that control is not wisdom.",
        desc="A demanding master whose discipline, analytical skill, and responsibility are balanced by humility learned through painful mistakes.",
        image="/characters/kung_fu_panda/shifu.png",
        geometry={"color": "#8D6E63"},
        behaviors=[Behavior.DISCIPLINED, Behavior.ANALYTICAL, Behavior.JUSTICE_DRIVEN],
        trait_vector=[
            0.78, 0.96, 0.76, 0.90,
            0.28, 0.52, 0.92, 1.00,
            0.30, 0.82, 0.88, 0.28
        ]
    ),

    VectorCharacterProfile(
        name="Tigress",
        tagline="Discipline forged into compassion.",
        desc="Focused, formidable, reserved, and intensely disciplined, Tigress expresses loyalty and care through action more readily than words.",
        image="/characters/kung_fu_panda/tigress.png",
        geometry={"color": "#F9A825"},
        behaviors=[Behavior.DISCIPLINED, Behavior.ACTION, Behavior.LOYAL],
        trait_vector=[
            0.98, 0.72, 0.72, 0.88,
            0.30, 0.36, 0.98, 1.00,
            0.18, 0.46, 0.82, 0.40
        ]
    ),

    VectorCharacterProfile(
        name="Monkey",
        tagline="Skill, swagger, and a surprisingly soft heart.",
        desc="Playful and agile, Monkey combines humor, creativity, loyalty, and technical martial skill with a relaxed confidence.",
        image="/characters/kung_fu_panda/monkey.png",
        geometry={"color": "#795548"},
        behaviors=[Behavior.HUMOROUS, Behavior.ACTION, Behavior.CREATIVE],
        trait_vector=[
            0.90, 0.58, 0.72, 0.72,
            0.24, 0.82, 0.90, 0.70,
            0.94, 0.60, 0.54, 0.36
        ]
    ),

    VectorCharacterProfile(
        name="Mantis",
        tagline="Tiny body, sharp mind, enormous confidence.",
        desc="Quick-witted, confident, mischievous, and observant, Mantis uses intelligence and humor to compensate for his size.",
        image="/characters/kung_fu_panda/mantis.png",
        geometry={"color": "#7CB342"},
        behaviors=[Behavior.HUMOROUS, Behavior.ANALYTICAL, Behavior.ACTION],
        trait_vector=[
            0.84, 0.88, 0.60, 0.68,
            0.22, 0.74, 0.84, 0.72,
            0.96, 0.76, 0.66, 0.42
        ]
    ),

    VectorCharacterProfile(
        name="Viper",
        tagline="Gentleness wrapped around precise strength.",
        desc="Warm, graceful, patient, and highly skilled, Viper is one of the team's most emotionally balanced and dependable members.",
        image="/characters/kung_fu_panda/viper.png",
        geometry={"color": "#43A047"},
        behaviors=[Behavior.EMPATHETIC, Behavior.LOYAL, Behavior.DISCIPLINED],
        trait_vector=[
            0.84, 0.58, 0.94, 0.82,
            0.20, 0.48, 0.98, 0.86,
            0.58, 0.54, 0.62, 0.18
        ]
    ),

    VectorCharacterProfile(
        name="Crane",
        tagline="Calm, practical, and quietly reliable.",
        desc="Reserved and sensible, Crane provides stability to the Furious Five through patience, competence, caution, and loyalty.",
        image="/characters/kung_fu_panda/crane.png",
        geometry={"color": "#90A4AE"},
        behaviors=[Behavior.PRAGMATIC, Behavior.LOYAL, Behavior.DISCIPLINED],
        trait_vector=[
            0.82, 0.76, 0.78, 0.78,
            0.16, 0.38, 0.96, 0.90,
            0.42, 0.48, 0.94, 0.14
        ]
    ),

    VectorCharacterProfile(
        name="Tai Lung",
        tagline="Great talent poisoned by entitlement.",
        desc="A devastatingly skilled warrior whose intelligence and discipline are consumed by resentment, entitlement, ambition, and rage.",
        image="/characters/kung_fu_panda/tai_lung.png",
        geometry={"color": "#455A64"},
        behaviors=[Behavior.ACTION, Behavior.AMBITIOUS, Behavior.REBELLIOUS],
        trait_vector=[
            1.00, 0.76, 0.08, 0.14,
            0.96, 0.42, 0.26, 0.96,
            0.10, 0.48, 0.84, 0.94
        ]
    ),

    VectorCharacterProfile(
        name="Lord Shen",
        tagline="A brilliant strategist terrified by the future.",
        desc="Elegant, intelligent, ambitious, and inventive, Shen uses technology and strategy to control the future while being consumed by fear and prophecy.",
        image="/characters/kung_fu_panda/lord_shen.png",
        geometry={"color": "#ECEFF1"},
        behaviors=[Behavior.ANALYTICAL, Behavior.AMBITIOUS, Behavior.CREATIVE],
        trait_vector=[
            0.76, 1.00, 0.06, 0.10,
            1.00, 0.94, 0.16, 0.74,
            0.32, 0.82, 0.98, 0.76
        ]
    ),

    VectorCharacterProfile(
        name="Kai",
        tagline="A warrior who turned mastery into obsession.",
        desc="Powerful, relentless, and calculating, Kai is driven by conquest and accumulation of power rather than loyalty, empathy, or balance.",
        image="/characters/kung_fu_panda/kai.png",
        geometry={"color": "#2E7D32"},
        behaviors=[Behavior.ACTION, Behavior.AMBITIOUS, Behavior.REBELLIOUS],
        trait_vector=[
            1.00, 0.72, 0.04, 0.06,
            0.98, 0.20, 0.12, 0.88,
            0.10, 0.36, 0.92, 0.86
        ]
    ),

    VectorCharacterProfile(
        name="Mr. Ping",
        tagline="A noodle-shop father with more wisdom than he admits.",
        desc="Affectionate, optimistic, anxious, humorous, and deeply devoted, Mr. Ping's greatest strength is the unconditional love he gives Po.",
        image="/characters/kung_fu_panda/mr_ping.png",
        geometry={"color": "#F57C00"},
        behaviors=[Behavior.EMPATHETIC, Behavior.HUMOROUS, Behavior.LOYAL],
        trait_vector=[
            0.34, 0.46, 1.00, 0.76,
            0.18, 0.58, 1.00, 0.42,
            0.94, 0.72, 0.70, 0.12
        ]
    ),
]


# ==========================================================
# UNIFIED CHARACTER REGISTRY
# ==========================================================

CHARACTER_REGISTRY = {
    "marvel": MARVEL_CHARACTERS,
    "atla": ATLA_CHARACTERS,
    "dc": DC_CHARACTERS,
    "kung_fu_panda": KUNG_FU_PANDA_CHARACTERS,
}
