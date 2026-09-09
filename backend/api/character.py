from fastapi import APIRouter, HTTPException

from data.characters import CHARACTER_REGISTRY
from utils.serializer import get_top_traits 
from utils.serializer import get_stats
from utils.serializer import serialize_character
router = APIRouter(
    prefix="/api/characters",
    tags=["Characters"]
)


@router.get("/")
def get_all_characters():
    """
    Returns every character across every franchise.
    """

    all_characters = []

    for franchise, characters in CHARACTER_REGISTRY.items():
        for character in characters:

            character_data = character.model_dump()

            # 🔥 ADD BOTH
            character_data["traits"] = get_top_traits(character.trait_vector)
            character_data["stats"] = get_stats(character.trait_vector)

            character_data["franchise"] = franchise

            all_characters.append(character_data)

    return all_characters


@router.get("/{franchise}")
def get_characters_by_franchise(franchise: str):
    """
    Returns all characters for a franchise.
    """

    characters = CHARACTER_REGISTRY.get(franchise)

    if characters is None:
        raise HTTPException(
            status_code=404,
            detail="Franchise not found."
        )

    return [
            serialize_character(char, franchise)
            for char in characters
            ]

@router.get("/{franchise}/{character_name}")
def get_character(
    franchise: str,
    character_name: str
):
    """
    Returns one character.
    """

    characters = CHARACTER_REGISTRY.get(franchise)

    if characters is None:
        raise HTTPException(
            status_code=404,
            detail="Franchise not found."
        )

    for character in characters:

        if character.name.lower() == character_name.lower():

           return serialize_character(character, franchise)

    raise HTTPException(
        status_code=404,
        detail="Character not found."
    )