from models import Behavior


# ============================================================
# Trait Order
#
# 0  ACTION
# 1  ANALYTICAL
# 2  EMPATHETIC
# 3  JUSTICE_DRIVEN
# 4  AMBITIOUS
# 5  CREATIVE
# 6  LOYAL
# 7  DISCIPLINED
# 8  HUMOROUS
# 9  CURIOUS
# 10 PRAGMATIC
# 11 REBELLIOUS
#
# Values represent how strongly a behavior contributes to
# each personality trait.
#
# Design:
#   0.00 - no meaningful relationship
#   0.05 - very weak
#   0.10-0.25 - weak secondary relationship
#   0.30-0.50 - moderate relationship
#   0.55-0.75 - strong relationship
#   0.80-1.00 - defining relationship
#
# Keep profiles sparse and distinctive.
# ============================================================


BEHAVIOR_PROFILES = {

    # ========================================================
    # ACTION
    # ========================================================
    Behavior.ACTION: [
        1.00,  # ACTION
        0.10,  # ANALYTICAL
        0.05,  # EMPATHETIC
        0.20,  # JUSTICE_DRIVEN
        0.35,  # AMBITIOUS
        0.10,  # CREATIVE
        0.20,  # LOYAL
        0.15,  # DISCIPLINED
        0.10,  # HUMOROUS
        0.05,  # CURIOUS
        0.55,  # PRAGMATIC
        0.45,  # REBELLIOUS
    ],

    # ========================================================
    # ANALYTICAL
    # ========================================================
    Behavior.ANALYTICAL: [
        0.10,  # ACTION
        1.00,  # ANALYTICAL
        0.05,  # EMPATHETIC
        0.25,  # JUSTICE_DRIVEN
        0.20,  # AMBITIOUS
        0.20,  # CREATIVE
        0.05,  # LOYAL
        0.45,  # DISCIPLINED
        0.05,  # HUMOROUS
        0.70,  # CURIOUS
        0.65,  # PRAGMATIC
        0.05,  # REBELLIOUS
    ],

    # ========================================================
    # EMPATHETIC
    # ========================================================
    Behavior.EMPATHETIC: [
        0.05,  # ACTION
        0.05,  # ANALYTICAL
        1.00,  # EMPATHETIC
        0.55,  # JUSTICE_DRIVEN
        0.05,  # AMBITIOUS
        0.15,  # CREATIVE
        0.75,  # LOYAL
        0.10,  # DISCIPLINED
        0.15,  # HUMOROUS
        0.20,  # CURIOUS
        0.10,  # PRAGMATIC
        0.05,  # REBELLIOUS
    ],

    # ========================================================
    # JUSTICE DRIVEN
    # ========================================================
    Behavior.JUSTICE_DRIVEN: [
        0.25,  # ACTION
        0.15,  # ANALYTICAL
        0.55,  # EMPATHETIC
        1.00,  # JUSTICE_DRIVEN
        0.15,  # AMBITIOUS
        0.05,  # CREATIVE
        0.65,  # LOYAL
        0.45,  # DISCIPLINED
        0.05,  # HUMOROUS
        0.10,  # CURIOUS
        0.20,  # PRAGMATIC
        0.15,  # REBELLIOUS
    ],

    # ========================================================
    # AMBITIOUS
    # ========================================================
    Behavior.AMBITIOUS: [
        0.40,  # ACTION
        0.20,  # ANALYTICAL
        0.05,  # EMPATHETIC
        0.10,  # JUSTICE_DRIVEN
        1.00,  # AMBITIOUS
        0.30,  # CREATIVE
        0.10,  # LOYAL
        0.40,  # DISCIPLINED
        0.05,  # HUMOROUS
        0.10,  # CURIOUS
        0.45,  # PRAGMATIC
        0.55,  # REBELLIOUS
    ],

    # ========================================================
    # CREATIVE
    # ========================================================
    Behavior.CREATIVE: [
        0.15,  # ACTION
        0.25,  # ANALYTICAL
        0.15,  # EMPATHETIC
        0.05,  # JUSTICE_DRIVEN
        0.25,  # AMBITIOUS
        1.00,  # CREATIVE
        0.10,  # LOYAL
        0.05,  # DISCIPLINED
        0.60,  # HUMOROUS
        0.70,  # CURIOUS
        0.15,  # PRAGMATIC
        0.55,  # REBELLIOUS
    ],

    # ========================================================
    # LOYAL
    # ========================================================
    Behavior.LOYAL: [
        0.15,  # ACTION
        0.05,  # ANALYTICAL
        0.70,  # EMPATHETIC
        0.60,  # JUSTICE_DRIVEN
        0.05,  # AMBITIOUS
        0.05,  # CREATIVE
        1.00,  # LOYAL
        0.55,  # DISCIPLINED
        0.05,  # HUMOROUS
        0.05,  # CURIOUS
        0.20,  # PRAGMATIC
        0.05,  # REBELLIOUS
    ],

    # ========================================================
    # DISCIPLINED
    # ========================================================
    Behavior.DISCIPLINED: [
        0.25,  # ACTION
        0.50,  # ANALYTICAL
        0.10,  # EMPATHETIC
        0.50,  # JUSTICE_DRIVEN
        0.35,  # AMBITIOUS
        0.05,  # CREATIVE
        0.50,  # LOYAL
        1.00,  # DISCIPLINED
        0.05,  # HUMOROUS
        0.10,  # CURIOUS
        0.70,  # PRAGMATIC
        0.05,  # REBELLIOUS
    ],

    # ========================================================
    # HUMOROUS
    # ========================================================
    Behavior.HUMOROUS: [
        0.15,  # ACTION
        0.05,  # ANALYTICAL
        0.30,  # EMPATHETIC
        0.05,  # JUSTICE_DRIVEN
        0.05,  # AMBITIOUS
        0.60,  # CREATIVE
        0.15,  # LOYAL
        0.05,  # DISCIPLINED
        1.00,  # HUMOROUS
        0.25,  # CURIOUS
        0.15,  # PRAGMATIC
        0.60,  # REBELLIOUS
    ],

    # ========================================================
    # CURIOUS
    # ========================================================
    Behavior.CURIOUS: [
        0.10,  # ACTION
        0.70,  # ANALYTICAL
        0.20,  # EMPATHETIC
        0.05,  # JUSTICE_DRIVEN
        0.10,  # AMBITIOUS
        0.70,  # CREATIVE
        0.05,  # LOYAL
        0.10,  # DISCIPLINED
        0.25,  # HUMOROUS
        1.00,  # CURIOUS
        0.20,  # PRAGMATIC
        0.30,  # REBELLIOUS
    ],

    # ========================================================
    # PRAGMATIC
    # ========================================================
    Behavior.PRAGMATIC: [
        0.45,  # ACTION
        0.55,  # ANALYTICAL
        0.05,  # EMPATHETIC
        0.15,  # JUSTICE_DRIVEN
        0.30,  # AMBITIOUS
        0.05,  # CREATIVE
        0.10,  # LOYAL
        0.55,  # DISCIPLINED
        0.05,  # HUMOROUS
        0.10,  # CURIOUS
        1.00,  # PRAGMATIC
        0.25,  # REBELLIOUS
    ],

    # ========================================================
    # REBELLIOUS
    # ========================================================
    Behavior.REBELLIOUS: [
        0.65,  # ACTION
        0.05,  # ANALYTICAL
        0.05,  # EMPATHETIC
        0.10,  # JUSTICE_DRIVEN
        0.45,  # AMBITIOUS
        0.50,  # CREATIVE
        0.05,  # LOYAL
        0.05,  # DISCIPLINED
        0.50,  # HUMOROUS
        0.20,  # CURIOUS
        0.15,  # PRAGMATIC
        1.00,  # REBELLIOUS
    ],
}