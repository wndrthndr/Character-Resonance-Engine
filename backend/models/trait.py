from enum import Enum


class Trait(str, Enum):
    """
    The 12-dimensional personality space used by the engine.

    IMPORTANT:
    The order here MUST match the order used in:

    - behavior_profiles.py
    - character trait vectors
    - user vectors
    """

    ACTION = "ACTION"
    ANALYSIS = "ANALYSIS"
    EMPATHY = "EMPATHY"
    JUSTICE = "JUSTICE"
    AMBITION = "AMBITION"
    CREATIVITY = "CREATIVITY"
    LOYALTY = "LOYALTY"
    DISCIPLINE = "DISCIPLINE"
    HUMOR = "HUMOR"
    CURIOSITY = "CURIOSITY"
    PRAGMATISM = "PRAGMATISM"
    CONFIDENCE = "CONFIDENCE"


TRAIT_ORDER = [
    Trait.ACTION,
    Trait.ANALYSIS,
    Trait.EMPATHY,
    Trait.JUSTICE,
    Trait.AMBITION,
    Trait.CREATIVITY,
    Trait.LOYALTY,
    Trait.DISCIPLINE,
    Trait.HUMOR,
    Trait.CURIOSITY,
    Trait.PRAGMATISM,
    Trait.CONFIDENCE,
]

NUM_TRAITS = len(TRAIT_ORDER)


TRAIT_INDEX = {
    trait: index
    for index, trait in enumerate(TRAIT_ORDER)
}


INDEX_TO_TRAIT = {
    index: trait
    for index, trait in enumerate(TRAIT_ORDER)
}