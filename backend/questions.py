# questions.py
from typing import List
from models import CompactQuestion, CompactOption

COMPACT_QUESTION_POOL: List[CompactQuestion] = [
    # ==========================================
    # GLOBAL PSYCH QUESTIONS (Everyday Situations)
    # ==========================================
    CompactQuestion(
        id="g_1", scope="GLOBAL", franchise="all",
        question="Your friend is crying over a bad breakup. What is your immediate move?",
        options={
            "A": CompactOption(text="Give them a hug.", weights={11: 0.9, 6: 0.4}),
            "B": CompactOption(text="Plan an epic distraction.", weights={0: 0.8, 5: 0.5}),
            "C": CompactOption(text="Offer practical solutions.", weights={1: 0.9, 9: 0.3}),
            "D": CompactOption(text="Sit quietly in support.", weights={2: 0.9, 7: 0.4})
        }
    ),
    CompactQuestion(
        id="g_2", scope="GLOBAL", franchise="all",
        question="You are working on a group project and someone isn't pulling their weight. You:",
        options={
            "A": CompactOption(text="Do it all yourself.", weights={9: 0.9, 1: 0.4}),
            "B": CompactOption(text="Confront them directly.", weights={11: 0.8, 8: 0.5}),
            "C": CompactOption(text="Make a joke out of it.", weights={0: 0.9, 5: 0.4}),
            "D": CompactOption(text="Complain to the boss.", weights={3: 0.9, 10: 0.4})
        }
    ),
    CompactQuestion(
        id="g_3", scope="GLOBAL", franchise="all",
        question="It's Friday night. What is your ideal vibe?",
        options={
            "A": CompactOption(text="Huge, chaotic party.", weights={0: 0.9, 5: 0.6}),
            "B": CompactOption(text="Chilling at home solo.", weights={2: 0.9, 7: 0.5}),
            "C": CompactOption(text="Learning something new.", weights={1: 0.9, 8: 0.4}),
            "D": CompactOption(text="Dinner with close friends.", weights={6: 0.9, 11: 0.4})
        }
    ),
    CompactQuestion(
        id="g_4", scope="GLOBAL", franchise="all",
        question="Someone cuts you off aggressively in traffic. Your instinct?",
        options={
            "A": CompactOption(text="Yell and slam steering wheel.", weights={11: 0.9, 10: 0.5}),
            "B": CompactOption(text="Ignore them and pass.", weights={2: 0.9, 1: 0.4}),
            "C": CompactOption(text="Laugh at their stupidity.", weights={0: 0.8, 5: 0.5}),
            "D": CompactOption(text="Plot a minor revenge.", weights={3: 0.9, 4: 0.6})
        }
    ),
    CompactQuestion(
        id="g_5", scope="GLOBAL", franchise="all",
        question="When you have a massive goal or problem, how do you handle it?",
        options={
            "A": CompactOption(text="Smash through it instantly.", weights={11: 0.9, 8: 0.3}),
            "B": CompactOption(text="Overthink every detail first.", weights={1: 0.9, 3: 0.5}),
            "C": CompactOption(text="Wing it and improvise.", weights={0: 0.9, 5: 0.5}),
            "D": CompactOption(text="Find a clever shortcut.", weights={4: 0.9, 7: 0.6})
        }
    ),

    # ==========================================
    # KUNG FU PANDA LORE QUESTIONS
    # ==========================================
    CompactQuestion(
        id="kfp_1", scope="FRANCHISE", franchise="kung_fu_panda",
        question="You open the legendary Dragon Scroll and see that it is completely blank. You think:",
        options={
            "A": CompactOption(text="I am the secret.", weights={0: 0.9, 2: 0.5}),
            "B": CompactOption(text="This is a scam.", weights={3: 0.8, 11: 0.4}),
            "C": CompactOption(text="It represents infinite peace.", weights={2: 0.9, 6: 0.4}),
            "D": CompactOption(text="I need to study harder.", weights={1: 0.9, 9: 0.5})
        }
    ),
    CompactQuestion(
        id="kfp_2", scope="FRANCHISE", franchise="kung_fu_panda",
        question="Mr. Ping offers you a fresh bowl of secret ingredient noodle soup. What do you do?",
        options={
            "A": CompactOption(text="Eat five bowls immediately.", weights={0: 1.0, 5: 0.4}),
            "B": CompactOption(text="Ask for the recipe.", weights={1: 0.8, 3: 0.4}),
            "C": CompactOption(text="Politely refuse to diet.", weights={9: 0.9, 7: 0.3}),
            "D": CompactOption(text="Pay extra to support him.", weights={6: 0.9, 11: 0.3})
        }
    ),
    CompactQuestion(
        id="kfp_3", scope="FRANCHISE", franchise="kung_fu_panda",
        question="An unstoppable villain escapes Chorh-Gom Prison. Your initial reaction is:",
        options={
            "A": CompactOption(text="Panic and run away.", weights={0: 0.7, 5: 0.5}),
            "B": CompactOption(text="Train until bones break.", weights={9: 0.9, 11: 0.4}),
            "C": CompactOption(text="Formulate a battlefield strategy.", weights={1: 0.9, 7: 0.4}),
            "D": CompactOption(text="Accept whatever fate brings.", weights={2: 0.9, 6: 0.3})
        }
    ),
    CompactQuestion(
        id="kfp_4", scope="FRANCHISE", franchise="kung_fu_panda",
        question="The Chameleon copies your form and fighting style perfectly. How do you beat her?",
        options={
            "A": CompactOption(text="Overwhelm her with friendship.", weights={0: 0.9, 6: 0.5}),
            "B": CompactOption(text="Outsmart her using tricks.", weights={4: 0.9, 5: 0.4}),
            "C": CompactOption(text="Pure, aggressive martial arts.", weights={9: 0.9, 11: 0.4}),
            "D": CompactOption(text="Steal her power source.", weights={3: 0.9, 4: 0.8})
        }
    ),
    CompactQuestion(
        id="kfp_5", scope="FRANCHISE", franchise="kung_fu_panda",
        question="What is the ultimate goal of your Kung Fu training?",
        options={
            "A": CompactOption(text="Achieve inner spiritual peace.", weights={2: 1.0, 6: 0.5}),
            "B": CompactOption(text="Earn respect and glory.", weights={11: 0.9, 1: 0.4}),
            "C": CompactOption(text="Protect the vulnerable villagers.", weights={0: 0.8, 9: 0.6}),
            "D": CompactOption(text="Rule over the valley.", weights={8: 1.0, 3: 0.7})
        }
    ),

    # ==========================================
    # MARVEL CINEMATIC UNIVERSE LORE QUESTIONS
    # ==========================================
    CompactQuestion(
        id="mcu_1", scope="FRANCHISE", franchise="marvel",
        question="Thanos has collected all six Infinity Stones. What is your counter-strategy?",
        options={
            "A": CompactOption(text="Build an opposing weapon.", weights={1: 0.9, 3: 0.4}),
            "B": CompactOption(text="Charge headfirst into battle.", weights={11: 0.9, 9: 0.4}),
            "C": CompactOption(text="Steal the stones back.", weights={4: 0.9, 0: 0.5}),
            "D": CompactOption(text="Sacrifice myself to win.", weights={6: 0.9, 2: 0.4})
        }
    ),
    CompactQuestion(
        id="mcu_2", scope="FRANCHISE", franchise="marvel",
        question="The Sokovia Accords require all enhanced individuals to register with the government. You:",
        options={
            "A": CompactOption(text="Sign it to maintain order.", weights={1: 0.9, 6: 0.4}),
            "B": CompactOption(text="Refuse to protect freedom.", weights={9: 0.9, 11: 0.4}),
            "C": CompactOption(text="Go entirely off grid.", weights={7: 0.9, 2: 0.5}),
            "D": CompactOption(text="Play both sides secretly.", weights={3: 0.9, 4: 0.5})
        }
    ),
    CompactQuestion(
        id="mcu_3", scope="FRANCHISE", franchise="marvel",
        question="You suddenly inherit billions of dollars and a high-tech lab. What do you build first?",
        options={
            "A": CompactOption(text="Armored weapon suits.", weights={1: 1.0, 3: 0.4}),
            "B": CompactOption(text="Global humanitarian tech.", weights={6: 0.9, 2: 0.4}),
            "C": CompactOption(text="Nothing, party all night.", weights={0: 0.9, 5: 0.5}),
            "D": CompactOption(text="Security networks for defense.", weights={9: 0.8, 7: 0.4})
        }
    ),
    CompactQuestion(
        id="mcu_4", scope="FRANCHISE", franchise="marvel",
        question="A massive alien portal opens over New York City. Where are you standing?",
        options={
            "A": CompactOption(text="Directly on the frontline.", weights={11: 0.9, 9: 0.5}),
            "B": CompactOption(text="Sniper position on rooftop.", weights={7: 0.9, 1: 0.3}),
            "C": CompactOption(text="Flanking from the shadows.", weights={4: 0.9, 3: 0.4}),
            "D": CompactOption(text="Guarding civilians down below.", weights={6: 0.9, 0: 0.4})
        }
    ),
    CompactQuestion(
        id="mcu_5", scope="FRANCHISE", franchise="marvel",
        question="An ancient magical artifact falls right into your hands. Your reaction?",
        options={
            "A": CompactOption(text="Study its historical patterns.", weights={1: 0.9, 2: 0.4}),
            "B": CompactOption(text="Lock it away safely.", weights={6: 0.9, 9: 0.4}),
            "C": CompactOption(text="Use it immediately.", weights={0: 0.8, 11: 0.5}),
            "D": CompactOption(text="Sell it for profit.", weights={3: 0.9, 4: 0.4})
        }
    ),

    # ==========================================
    # AVATAR: THE LAST AIRBENDER
    # ==========================================

    CompactQuestion(
        id="atla_1", scope="FRANCHISE", franchise="avatar",
        question="A lion turtle offers you immense power—but only if you abandon one core belief. You:",
        options={
            "A": CompactOption(text="Refuse. Some values aren't negotiable.", weights={3: 0.9, 6: 0.5}),
            "B": CompactOption(text="Accept if it saves everyone.", weights={9: 0.8, 1: 0.4}),
            "C": CompactOption(text="Look for a third option.", weights={2: 0.9, 1: 0.5}),
            "D": CompactOption(text="Take the power. Strength comes first.", weights={4: 0.9, 8: 0.6})
        }
    ),

    CompactQuestion(
        id="atla_2", scope="FRANCHISE", franchise="avatar",
        question="You're invited to train under the greatest bending master alive. What's your approach?",
        options={
            "A": CompactOption(text="Master every lesson exactly as taught.", weights={3: 0.9, 1: 0.5}),
            "B": CompactOption(text="Experiment and invent your own style.", weights={2: 0.9, 8: 0.5}),
            "C": CompactOption(text="Focus on understanding the philosophy first.", weights={6: 0.9, 1: 0.4}),
            "D": CompactOption(text="Train harder than everyone else.", weights={0: 0.8, 4: 0.6})
        }
    ),

    CompactQuestion(
        id="atla_3", scope="FRANCHISE", franchise="avatar",
        question="The Fire Nation is approaching your village. Your first priority is:",
        options={
            "A": CompactOption(text="Protect every civilian.", weights={6: 0.9, 9: 0.5}),
            "B": CompactOption(text="Challenge their strongest fighter.", weights={0: 0.9, 10: 0.5}),
            "C": CompactOption(text="Organize a tactical defense.", weights={1: 0.9, 9: 0.4}),
            "D": CompactOption(text="Evacuate everyone before they arrive.", weights={7: 0.8, 2: 0.5})
        }
    ),

    CompactQuestion(
        id="atla_4", scope="FRANCHISE", franchise="avatar",
        question="You discover a completely new bending technique. What excites you most?",
        options={
            "A": CompactOption(text="The possibilities it unlocks.", weights={2: 0.9, 5: 0.4}),
            "B": CompactOption(text="Perfecting it through discipline.", weights={3: 0.9, 1: 0.4}),
            "C": CompactOption(text="Using it to defend others.", weights={6: 0.9, 9: 0.4}),
            "D": CompactOption(text="Keeping it as your secret advantage.", weights={7: 0.9, 4: 0.5})
        }
    ),

    CompactQuestion(
        id="atla_5", scope="FRANCHISE", franchise="avatar",
        question="If you could master only one element, you'd choose the one that:",
        options={
            "A": CompactOption(text="Adapts to every situation.", weights={2: 0.9, 6: 0.3}),
            "B": CompactOption(text="Hits the hardest.", weights={0: 0.9, 10: 0.5}),
            "C": CompactOption(text="Requires the most precision.", weights={1: 0.9, 3: 0.4}),
            "D": CompactOption(text="Feels uniquely yours.", weights={8: 0.9, 5: 0.4})
        }
    ),

        # ==========================================
# DC UNIVERSE
# ==========================================

CompactQuestion(
    id="dc_1", scope="FRANCHISE", franchise="dc",
    question="You have one night to stop a city-wide catastrophe. Your first move is:",
    options={
        "A": CompactOption(text="Gather every fact before acting.", weights={1: 1.0, 7: 0.4}),
        "B": CompactOption(text="Head straight into danger.", weights={0: 0.9, 10: 0.5}),
        "C": CompactOption(text="Coordinate a team.", weights={9: 0.9, 6: 0.4}),
        "D": CompactOption(text="Create a backup plan for every outcome.", weights={3: 0.9, 1: 0.5})
    }
),

CompactQuestion(
    id="dc_2", scope="FRANCHISE", franchise="dc",
    question="An enemy knows your greatest weakness. You:",
    options={
        "A": CompactOption(text="Turn it into a strength.", weights={8: 0.9, 2: 0.5}),
        "B": CompactOption(text="Hide it completely.", weights={7: 0.9, 1: 0.4}),
        "C": CompactOption(text="Face them anyway.", weights={0: 0.9, 10: 0.5}),
        "D": CompactOption(text="Trust your allies to compensate.", weights={6: 0.9, 9: 0.4})
    }
),

CompactQuestion(
    id="dc_3", scope="FRANCHISE", franchise="dc",
    question="A powerful artifact chooses you. What's the hardest part?",
    options={
        "A": CompactOption(text="Resisting the temptation to misuse it.", weights={3: 0.9, 6: 0.5}),
        "B": CompactOption(text="Learning how it works.", weights={1: 0.9, 2: 0.4}),
        "C": CompactOption(text="Deciding who deserves it more.", weights={9: 0.8, 6: 0.4}),
        "D": CompactOption(text="Knowing when to let it go.", weights={11: 0.9, 6: 0.3})
    }
),

CompactQuestion(
    id="dc_4", scope="FRANCHISE", franchise="dc",
    question="Gotham needs a symbol. You become one by:",
    options={
        "A": CompactOption(text="Inspiring hope.", weights={6: 0.9, 9: 0.5}),
        "B": CompactOption(text="Making criminals fear you.", weights={7: 0.9, 10: 0.5}),
        "C": CompactOption(text="Outsmarting everyone.", weights={1: 0.9, 4: 0.4}),
        "D": CompactOption(text="Refusing to compromise your ideals.", weights={3: 0.9, 8: 0.4})
    }
),

CompactQuestion(
    id="dc_5", scope="FRANCHISE", franchise="dc",
    question="Justice means:",
    options={
        "A": CompactOption(text="Protecting everyone equally.", weights={6: 1.0, 9: 0.5}),
        "B": CompactOption(text="Doing whatever gets results.", weights={4: 0.9, 7: 0.4}),
        "C": CompactOption(text="Holding yourself to the highest standard.", weights={3: 0.9, 11: 0.4}),
        "D": CompactOption(text="Giving people a chance to change.", weights={2: 0.8, 6: 0.5})
    }
),
]