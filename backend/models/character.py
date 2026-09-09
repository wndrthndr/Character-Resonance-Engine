from typing import Dict, List, Optional

from pydantic import BaseModel

from models.behavior import Behavior


class VectorCharacterProfile(BaseModel):
    """
    Represents one fictional character.
    """

    name: str

    tagline: str

    desc: str

    image: Optional[str] = None

    geometry: Dict[str, str] = {}

    # Personality embedding used by RankingEngine
    trait_vector: List[float]

    # Human-readable behavior tags
    behaviors: List[Behavior] = []

    # Optional UI stats
    stats: Dict[str, int] = {}