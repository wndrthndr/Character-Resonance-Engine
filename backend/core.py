# core.py
import random
import math
from typing import List, Dict, Literal
from config import NUM_TAGS, FRANCHISE_VECTOR_REGISTRY, VectorCharacterProfile
from models import CompactQuestion, UserResponse

class ProductionQuizEngine:
    @classmethod
    def assemble_quiz(
        cls, 
        franchise: Literal['marvel', 'kung_fu_panda'], 
        pool: List[CompactQuestion], 
        num_global: int = 5, 
        num_lore: int = 5
    ) -> List[CompactQuestion]:
        """
        Assembles a customized quiz containing random global questions 
        and random franchise-specific lore questions.
        """
        global_questions = [q for q in pool if q.scope == "GLOBAL"]
        lore_questions = [q for q in pool if q.scope == "FRANCHISE" and q.franchise == franchise]
        
        selected = random.sample(global_questions, min(num_global, len(global_questions)))
        selected += random.sample(lore_questions, min(num_lore, len(lore_questions)))
        
        random.shuffle(selected)
        return selected

    @classmethod
    def calculate_closest_character(
        cls, 
        franchise: str, 
        responses: List[UserResponse], 
        pool: List[CompactQuestion]
    ) -> Dict:
        """
        Runs a proper Cosine Similarity vector matching algorithm against the user's 
        aggregated archetype weights and returns the matching profile.
        """
        # Step 1: Initialize a zeroed 12-dimensional user profile vector
        user_vector = [0.0] * NUM_TAGS
        question_map = {q.id: q for q in pool}
        
        # Step 2: Accumulate weights across indices 0-11
        for resp in responses:
            question = question_map.get(resp.question_id)
            if not question:
                continue
            chosen_option = question.options.get(resp.selected_option)
            if not chosen_option:
                continue
                
            for idx, weight in chosen_option.weights.items():
                if 0 <= idx < NUM_TAGS:
                    user_vector[idx] += weight

        # Calculate User Vector Magnitude (Euclidean Norm)
        user_magnitude = math.sqrt(sum(val ** 2 for val in user_vector))

        # Step 3: Compute similarity metrics against character rosters
        candidates: List[VectorCharacterProfile] = FRANCHISE_VECTOR_REGISTRY.get(franchise, [])
        best_match = None
        highest_score = -1.0
        scores_sheet = {}

        for char in candidates:
            dot_product = 0.0
            char_sq_sum = 0.0
            
            for i in range(NUM_TAGS):
                dot_product += user_vector[i] * char.trait_vector[i]
                char_sq_sum += char.trait_vector[i] ** 2
                
            char_magnitude = math.sqrt(char_sq_sum)
            
            # True Cosine Similarity calculation
            if user_magnitude > 0 and char_magnitude > 0:
                cosine_sim = dot_product / (user_magnitude * char_magnitude)
                # Convert from range [0, 1] to [0%, 100%]
                score_pct = round(cosine_sim * 100, 1)
            else:
                score_pct = 0.0
            
            scores_sheet[char.name] = score_pct
            
            if score_pct > highest_score:
                highest_score = score_pct
                best_match = char.name

        return {
            "matched_character": best_match,
            "match_confidence": highest_score,
            "full_breakdown": dict(sorted(scores_sheet.items(), key=lambda x: x[1], reverse=True))
        }