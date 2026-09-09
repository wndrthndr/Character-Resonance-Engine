from data.characters import CHARACTER_REGISTRY


class CharacterService:

    @staticmethod
    def get_all():

        return CHARACTER_REGISTRY

    @staticmethod
    def get_by_franchise(franchise: str):

        characters = CHARACTER_REGISTRY.get(franchise)

        if characters is None:
            raise ValueError("Franchise not found.")

        return characters

    @staticmethod
    def get_character(
        franchise: str,
        character_name: str
    ):

        characters = CHARACTER_REGISTRY.get(franchise)

        if characters is None:
            raise ValueError("Franchise not found.")

        for character in characters:

            if character.name.lower() == character_name.lower():

                return character

        raise ValueError("Character not found.")