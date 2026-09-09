from models import CompactQuestion, CompactOption, Behavior


QUESTION_POOL = [

    # =====================================================
    # GLOBAL QUESTIONS — PERSONALITY DISCOVERY
    # =====================================================

    CompactQuestion(
        id="global_1",
        scope="GLOBAL",
        franchise="all",
        question="You suddenly get a completely free day. What sounds most satisfying?",
        options={
            "A": CompactOption(text="Explore somewhere I've never been", behaviors=[Behavior.CURIOUS, Behavior.REBELLIOUS]),
            "B": CompactOption(text="Practice something until I'm noticeably better", behaviors=[Behavior.DISCIPLINED, Behavior.AMBITIOUS]),
            "C": CompactOption(text="Spend it with people I genuinely care about", behaviors=[Behavior.EMPATHETIC, Behavior.LOYAL]),
            "D": CompactOption(text="Make or invent something for the fun of it", behaviors=[Behavior.CREATIVE, Behavior.HUMOROUS]),
        },
    ),

    CompactQuestion(
        id="global_2",
        scope="GLOBAL",
        franchise="all",
        question="You run into a problem nobody around you knows how to solve. What interests you most?",
        options={
            "A": CompactOption(text="Figuring out exactly how the problem works", behaviors=[Behavior.ANALYTICAL, Behavior.CURIOUS]),
            "B": CompactOption(text="Trying something and learning from the result", behaviors=[Behavior.ACTION, Behavior.PRAGMATIC]),
            "C": CompactOption(text="Finding a solution nobody would normally consider", behaviors=[Behavior.CREATIVE, Behavior.REBELLIOUS]),
            "D": CompactOption(text="Finding the solution that causes the least harm", behaviors=[Behavior.EMPATHETIC, Behavior.JUSTICE_DRIVEN]),
        },
    ),

    CompactQuestion(
        id="global_3",
        scope="GLOBAL",
        franchise="all",
        question="Which kind of achievement would make you proudest?",
        options={
            "A": CompactOption(text="Mastering something extremely difficult", behaviors=[Behavior.DISCIPLINED, Behavior.CURIOUS]),
            "B": CompactOption(text="Building something that becomes uniquely mine", behaviors=[Behavior.CREATIVE, Behavior.AMBITIOUS]),
            "C": CompactOption(text="Changing something I believe is wrong", behaviors=[Behavior.JUSTICE_DRIVEN, Behavior.REBELLIOUS]),
            "D": CompactOption(text="Becoming someone others can always count on", behaviors=[Behavior.LOYAL, Behavior.EMPATHETIC]),
        },
    ),

    CompactQuestion(
        id="global_4",
        scope="GLOBAL",
        franchise="all",
        question="Which kind of environment would you enjoy spending time in?",
        options={
            "A": CompactOption(text="A place full of puzzles, books, and unanswered questions", behaviors=[Behavior.ANALYTICAL, Behavior.CURIOUS]),
            "B": CompactOption(text="A place where people constantly train and compete", behaviors=[Behavior.ACTION, Behavior.AMBITIOUS]),
            "C": CompactOption(text="A place where rules are loose and experimentation is encouraged", behaviors=[Behavior.CREATIVE, Behavior.REBELLIOUS]),
            "D": CompactOption(text="A close-knit community where everyone knows everyone", behaviors=[Behavior.LOYAL, Behavior.EMPATHETIC]),
        },
    ),

    CompactQuestion(
        id="global_5",
        scope="GLOBAL",
        franchise="all",
        question="When plans fall apart, which response feels most like you?",
        options={
            "A": CompactOption(text="Work out what went wrong before changing anything", behaviors=[Behavior.ANALYTICAL, Behavior.DISCIPLINED]),
            "B": CompactOption(text="Forget the plan and start moving", behaviors=[Behavior.ACTION, Behavior.PRAGMATIC]),
            "C": CompactOption(text="Turn the failure into a completely different idea", behaviors=[Behavior.CREATIVE, Behavior.CURIOUS]),
            "D": CompactOption(text="Question whether the original plan was worth following at all", behaviors=[Behavior.REBELLIOUS, Behavior.JUSTICE_DRIVEN]),
        },
    ),

    CompactQuestion(
        id="global_6",
        scope="GLOBAL",
        franchise="all",
        question="What makes a person impressive to you?",
        options={
            "A": CompactOption(text="They stay composed and prepared", behaviors=[Behavior.DISCIPLINED, Behavior.PRAGMATIC]),
            "B": CompactOption(text="They can see possibilities nobody else notices", behaviors=[Behavior.CREATIVE, Behavior.CURIOUS]),
            "C": CompactOption(text="They stand up for people who need it", behaviors=[Behavior.JUSTICE_DRIVEN, Behavior.EMPATHETIC]),
            "D": CompactOption(text="They never abandon the people beside them", behaviors=[Behavior.LOYAL, Behavior.ACTION]),
        },
    ),

    CompactQuestion(
        id="global_7",
        scope="GLOBAL",
        franchise="all",
        question="If you could instantly become exceptional at one thing, what would you choose?",
        options={
            "A": CompactOption(text="A complex technical or intellectual skill", behaviors=[Behavior.ANALYTICAL, Behavior.DISCIPLINED]),
            "B": CompactOption(text="A physical skill that lets me act decisively", behaviors=[Behavior.ACTION, Behavior.PRAGMATIC]),
            "C": CompactOption(text="A creative skill I could make completely my own", behaviors=[Behavior.CREATIVE, Behavior.REBELLIOUS]),
            "D": CompactOption(text="A skill that helps me understand people deeply", behaviors=[Behavior.EMPATHETIC, Behavior.CURIOUS]),
        },
    ),

    CompactQuestion(
        id="global_8",
        scope="GLOBAL",
        franchise="all",
        question="Which kind of story would you most want to discover?",
        options={
            "A": CompactOption(text="A hidden history that changes what everyone believes", behaviors=[Behavior.CURIOUS, Behavior.ANALYTICAL]),
            "B": CompactOption(text="A legendary journey filled with impossible challenges", behaviors=[Behavior.ACTION, Behavior.AMBITIOUS]),
            "C": CompactOption(text="A strange story that breaks every convention", behaviors=[Behavior.CREATIVE, Behavior.REBELLIOUS]),
            "D": CompactOption(text="A story about people protecting each other through hardship", behaviors=[Behavior.LOYAL, Behavior.EMPATHETIC]),
        },
    ),

    CompactQuestion(
        id="global_9",
        scope="GLOBAL",
        franchise="all",
        question="Which reward would tempt you most after accomplishing something difficult?",
        options={
            "A": CompactOption(text="A chance to attempt something even harder", behaviors=[Behavior.AMBITIOUS, Behavior.ACTION]),
            "B": CompactOption(text="Time to study or understand what I just accomplished", behaviors=[Behavior.CURIOUS, Behavior.ANALYTICAL]),
            "C": CompactOption(text="Freedom to do whatever I want next", behaviors=[Behavior.REBELLIOUS, Behavior.PRAGMATIC]),
            "D": CompactOption(text="Sharing the moment with the people who helped me", behaviors=[Behavior.LOYAL, Behavior.HUMOROUS]),
        },
    ),

    CompactQuestion(
        id="global_10",
        scope="GLOBAL",
        franchise="all",
        question="What kind of rule bothers you most?",
        options={
            "A": CompactOption(text="One that makes no logical sense", behaviors=[Behavior.ANALYTICAL, Behavior.REBELLIOUS]),
            "B": CompactOption(text="One that gets in the way of getting something done", behaviors=[Behavior.PRAGMATIC, Behavior.ACTION]),
            "C": CompactOption(text="One that treats people unfairly", behaviors=[Behavior.JUSTICE_DRIVEN, Behavior.EMPATHETIC]),
            "D": CompactOption(text="One that exists only because people are afraid of doing things differently", behaviors=[Behavior.CREATIVE, Behavior.CURIOUS]),
        },
    ),

    CompactQuestion(
        id="global_11",
        scope="GLOBAL",
        franchise="all",
        question="When you join a new group, what do you naturally look for?",
        options={
            "A": CompactOption(text="The person who actually knows what they're doing", behaviors=[Behavior.ANALYTICAL, Behavior.DISCIPLINED]),
            "B": CompactOption(text="Something useful I can immediately contribute", behaviors=[Behavior.ACTION, Behavior.PRAGMATIC]),
            "C": CompactOption(text="The people I'd genuinely want beside me", behaviors=[Behavior.LOYAL, Behavior.EMPATHETIC]),
            "D": CompactOption(text="The interesting personalities and possibilities", behaviors=[Behavior.CURIOUS, Behavior.HUMOROUS]),
        },
    ),

    CompactQuestion(
        id="global_12",
        scope="GLOBAL",
        franchise="all",
        question="Which kind of challenge sounds the most fun?",
        options={
            "A": CompactOption(text="Something that tests my endurance and determination", behaviors=[Behavior.DISCIPLINED, Behavior.AMBITIOUS]),
            "B": CompactOption(text="Something that requires a clever unconventional solution", behaviors=[Behavior.CREATIVE, Behavior.ANALYTICAL]),
            "C": CompactOption(text="Something unpredictable where I have to improvise", behaviors=[Behavior.ACTION, Behavior.REBELLIOUS]),
            "D": CompactOption(text="Something where understanding others is the key", behaviors=[Behavior.EMPATHETIC, Behavior.CURIOUS]),
        },
    ),

    CompactQuestion(
        id="global_13",
        scope="GLOBAL",
        franchise="all",
        question="You get access to a place you've never seen before. What draws you in?",
        options={
            "A": CompactOption(text="The parts nobody has documented yet", behaviors=[Behavior.CURIOUS, Behavior.REBELLIOUS]),
            "B": CompactOption(text="The hardest area to reach", behaviors=[Behavior.ACTION, Behavior.AMBITIOUS]),
            "C": CompactOption(text="The place with the strangest objects or ideas", behaviors=[Behavior.CREATIVE, Behavior.HUMOROUS]),
            "D": CompactOption(text="The part that tells you how the place really works", behaviors=[Behavior.ANALYTICAL, Behavior.PRAGMATIC]),
        },
    ),

    CompactQuestion(
        id="global_14",
        scope="GLOBAL",
        franchise="all",
        question="What kind of legacy would you rather leave?",
        options={
            "A": CompactOption(text="Proof that I mastered my craft", behaviors=[Behavior.DISCIPLINED, Behavior.AMBITIOUS]),
            "B": CompactOption(text="Something original that could not have come from anyone else", behaviors=[Behavior.CREATIVE, Behavior.REBELLIOUS]),
            "C": CompactOption(text="People remembering that I always stood by them", behaviors=[Behavior.LOYAL, Behavior.EMPATHETIC]),
            "D": CompactOption(text="A change that made things fairer", behaviors=[Behavior.JUSTICE_DRIVEN, Behavior.PRAGMATIC]),
        },
    ),

    CompactQuestion(
        id="global_15",
        scope="GLOBAL",
        franchise="all",
        question="Which kind of information would you be unable to resist learning?",
        options={
            "A": CompactOption(text="How something works beneath the surface", behaviors=[Behavior.ANALYTICAL, Behavior.CURIOUS]),
            "B": CompactOption(text="A secret that powerful people do not want known", behaviors=[Behavior.REBELLIOUS, Behavior.JUSTICE_DRIVEN]),
            "C": CompactOption(text="How to turn knowledge into something useful", behaviors=[Behavior.PRAGMATIC, Behavior.CREATIVE]),
            "D": CompactOption(text="The story behind the people involved", behaviors=[Behavior.EMPATHETIC, Behavior.LOYAL]),
        },
    ),

    CompactQuestion(
        id="global_16",
        scope="GLOBAL",
        franchise="all",
        question="Someone gives you complete freedom to solve a problem. What do you value most?",
        options={
            "A": CompactOption(text="Having a clear method that I can trust", behaviors=[Behavior.DISCIPLINED, Behavior.ANALYTICAL]),
            "B": CompactOption(text="Being able to act without waiting around", behaviors=[Behavior.ACTION, Behavior.PRAGMATIC]),
            "C": CompactOption(text="Not being forced into the obvious solution", behaviors=[Behavior.CREATIVE, Behavior.REBELLIOUS]),
            "D": CompactOption(text="Making sure the result works for the people involved", behaviors=[Behavior.JUSTICE_DRIVEN, Behavior.EMPATHETIC]),
        },
    ),

    CompactQuestion(
        id="global_17",
        scope="GLOBAL",
        franchise="all",
        question="Which person would you most want as a long-term partner?",
        options={
            "A": CompactOption(text="Someone reliable who always follows through", behaviors=[Behavior.LOYAL, Behavior.DISCIPLINED]),
            "B": CompactOption(text="Someone who constantly pushes both of us to improve", behaviors=[Behavior.AMBITIOUS, Behavior.ACTION]),
            "C": CompactOption(text="Someone who always has an unexpected idea", behaviors=[Behavior.CREATIVE, Behavior.HUMOROUS]),
            "D": CompactOption(text="Someone who makes me question what I thought I knew", behaviors=[Behavior.CURIOUS, Behavior.ANALYTICAL]),
        },
    ),

    CompactQuestion(
        id="global_18",
        scope="GLOBAL",
        franchise="all",
        question="Which kind of victory feels most meaningful?",
        options={
            "A": CompactOption(text="Winning because I prepared better than everyone else", behaviors=[Behavior.DISCIPLINED, Behavior.PRAGMATIC]),
            "B": CompactOption(text="Winning after taking a risk nobody else would take", behaviors=[Behavior.ACTION, Behavior.REBELLIOUS]),
            "C": CompactOption(text="Winning while making sure nobody was treated unfairly", behaviors=[Behavior.JUSTICE_DRIVEN, Behavior.EMPATHETIC]),
            "D": CompactOption(text="Winning with a solution nobody saw coming", behaviors=[Behavior.CREATIVE, Behavior.ANALYTICAL]),
        },
    ),

    CompactQuestion(
        id="global_19",
        scope="GLOBAL",
        franchise="all",
        question="If you could spend a year learning from one kind of mentor, which appeals most?",
        options={
            "A": CompactOption(text="A master who demands absolute discipline", behaviors=[Behavior.DISCIPLINED, Behavior.AMBITIOUS]),
            "B": CompactOption(text="A wandering expert who ignores conventional methods", behaviors=[Behavior.REBELLIOUS, Behavior.CURIOUS]),
            "C": CompactOption(text="A leader known for protecting their people", behaviors=[Behavior.LOYAL, Behavior.JUSTICE_DRIVEN]),
            "D": CompactOption(text="An inventor who sees possibilities everywhere", behaviors=[Behavior.CREATIVE, Behavior.PRAGMATIC]),
        },
    ),

    CompactQuestion(
        id="global_20",
        scope="GLOBAL",
        franchise="all",
        question="What would make you explore a completely unfamiliar world?",
        options={
            "A": CompactOption(text="The chance to uncover something nobody understands", behaviors=[Behavior.CURIOUS, Behavior.ANALYTICAL]),
            "B": CompactOption(text="The chance to test myself against it", behaviors=[Behavior.ACTION, Behavior.AMBITIOUS]),
            "C": CompactOption(text="The freedom to reinvent myself there", behaviors=[Behavior.REBELLIOUS, Behavior.CREATIVE]),
            "D": CompactOption(text="The chance to build a life with people I care about", behaviors=[Behavior.EMPATHETIC, Behavior.LOYAL]),
        },
    ),


    # =====================================================
    # MARVEL — LORE / WORLD DISCOVERY
    # =====================================================

    CompactQuestion(
        id="marvel_1",
        scope="FRANCHISE",
        franchise="marvel",
        question="Which Marvel location would you most want to explore?",
        options={
            "A": CompactOption(text="Wakanda", behaviors=[Behavior.CURIOUS, Behavior.AMBITIOUS]),
            "B": CompactOption(text="The Sanctum Sanctorum", behaviors=[Behavior.ANALYTICAL, Behavior.CREATIVE]),
            "C": CompactOption(text="Avengers Tower", behaviors=[Behavior.ACTION, Behavior.LOYAL]),
            "D": CompactOption(text="Knowhere", behaviors=[Behavior.REBELLIOUS, Behavior.HUMOROUS]),
        },
    ),

    CompactQuestion(
        id="marvel_2",
        scope="FRANCHISE",
        franchise="marvel",
        question="Which piece of Marvel technology would you most want to examine?",
        options={
            "A": CompactOption(text="Tony Stark's arc-reactor technology", behaviors=[Behavior.ANALYTICAL, Behavior.CREATIVE]),
            "B": CompactOption(text="Pym Particles", behaviors=[Behavior.CURIOUS, Behavior.REBELLIOUS]),
            "C": CompactOption(text="Wakandan vibranium technology", behaviors=[Behavior.PRAGMATIC, Behavior.AMBITIOUS]),
            "D": CompactOption(text="The Guardians' ship technology", behaviors=[Behavior.ACTION, Behavior.HUMOROUS]),
        },
    ),

    CompactQuestion(
        id="marvel_3",
        scope="FRANCHISE",
        franchise="marvel",
        question="Which Marvel artifact would you most want to see up close?",
        options={
            "A": CompactOption(text="The Eye of Agamotto", behaviors=[Behavior.CURIOUS, Behavior.DISCIPLINED]),
            "B": CompactOption(text="The Tesseract", behaviors=[Behavior.ANALYTICAL, Behavior.AMBITIOUS]),
            "C": CompactOption(text="The Ten Rings", behaviors=[Behavior.ACTION, Behavior.REBELLIOUS]),
            "D": CompactOption(text="Mjolnir", behaviors=[Behavior.JUSTICE_DRIVEN, Behavior.LOYAL]),
        },
    ),

    CompactQuestion(
        id="marvel_4",
        scope="FRANCHISE",
        franchise="marvel",
        question="Which Marvel organization would you most want to spend a day inside?",
        options={
            "A": CompactOption(text="S.H.I.E.L.D.", behaviors=[Behavior.DISCIPLINED, Behavior.PRAGMATIC]),
            "B": CompactOption(text="The Avengers", behaviors=[Behavior.ACTION, Behavior.LOYAL]),
            "C": CompactOption(text="The Guardians of the Galaxy", behaviors=[Behavior.HUMOROUS, Behavior.REBELLIOUS]),
            "D": CompactOption(text="The Wakandan royal and scientific institutions", behaviors=[Behavior.ANALYTICAL, Behavior.AMBITIOUS]),
        },
    ),

    CompactQuestion(
        id="marvel_5",
        scope="FRANCHISE",
        franchise="marvel",
        question="Which Marvel event would you most want to witness firsthand?",
        options={
            "A": CompactOption(text="The Battle of New York", behaviors=[Behavior.ACTION, Behavior.JUSTICE_DRIVEN]),
            "B": CompactOption(text="The opening of the Bifrost", behaviors=[Behavior.CURIOUS, Behavior.CREATIVE]),
            "C": CompactOption(text="The Battle of Wakanda", behaviors=[Behavior.LOYAL, Behavior.DISCIPLINED]),
            "D": CompactOption(text="The Guardians' first encounter with the wider cosmic world", behaviors=[Behavior.REBELLIOUS, Behavior.HUMOROUS]),
        },
    ),

    CompactQuestion(
        id="marvel_6",
        scope="FRANCHISE",
        franchise="marvel",
        question="Which part of Wakanda would you most want to experience?",
        options={
            "A": CompactOption(text="The vibranium research and technology labs", behaviors=[Behavior.ANALYTICAL, Behavior.CURIOUS]),
            "B": CompactOption(text="The Border Tribe's mountain region", behaviors=[Behavior.DISCIPLINED, Behavior.ACTION]),
            "C": CompactOption(text="The Golden City", behaviors=[Behavior.AMBITIOUS, Behavior.PRAGMATIC]),
            "D": CompactOption(text="The traditions and community life outside the royal center", behaviors=[Behavior.EMPATHETIC, Behavior.LOYAL]),
        },
    ),

    CompactQuestion(
        id="marvel_7",
        scope="FRANCHISE",
        franchise="marvel",
        question="Which kind of Stark invention would interest you most?",
        options={
            "A": CompactOption(text="A suit built around precision and advanced analysis", behaviors=[Behavior.ANALYTICAL, Behavior.DISCIPLINED]),
            "B": CompactOption(text="A machine designed to solve an impossible problem", behaviors=[Behavior.CREATIVE, Behavior.AMBITIOUS]),
            "C": CompactOption(text="A compact gadget that gives you an unexpected advantage", behaviors=[Behavior.PRAGMATIC, Behavior.REBELLIOUS]),
            "D": CompactOption(text="Technology designed primarily to protect people", behaviors=[Behavior.JUSTICE_DRIVEN, Behavior.EMPATHETIC]),
        },
    ),

    CompactQuestion(
        id="marvel_8",
        scope="FRANCHISE",
        franchise="marvel",
        question="Which cosmic destination would you most want to visit?",
        options={
            "A": CompactOption(text="Xandar", behaviors=[Behavior.CURIOUS, Behavior.DISCIPLINED]),
            "B": CompactOption(text="Knowhere", behaviors=[Behavior.REBELLIOUS, Behavior.HUMOROUS]),
            "C": CompactOption(text="Asgard", behaviors=[Behavior.AMBITIOUS, Behavior.LOYAL]),
            "D": CompactOption(text="A completely unknown world beyond the established routes", behaviors=[Behavior.CREATIVE, Behavior.ACTION]),
        },
    ),

    CompactQuestion(
        id="marvel_9",
        scope="FRANCHISE",
        franchise="marvel",
        question="Which type of Marvel power would you most want to understand?",
        options={
            "A": CompactOption(text="Mystic magic and the rules behind it", behaviors=[Behavior.ANALYTICAL, Behavior.CURIOUS]),
            "B": CompactOption(text="Cosmic energy and how it can be controlled", behaviors=[Behavior.AMBITIOUS, Behavior.CREATIVE]),
            "C": CompactOption(text="Superhuman physical abilities", behaviors=[Behavior.ACTION, Behavior.DISCIPLINED]),
            "D": CompactOption(text="Powers that could be used to protect ordinary people", behaviors=[Behavior.EMPATHETIC, Behavior.JUSTICE_DRIVEN]),
        },
    ),

    CompactQuestion(
        id="marvel_10",
        scope="FRANCHISE",
        franchise="marvel",
        question="Which place connected to Doctor Strange would you most want to explore?",
        options={
            "A": CompactOption(text="The library of the Masters of the Mystic Arts", behaviors=[Behavior.CURIOUS, Behavior.ANALYTICAL]),
            "B": CompactOption(text="The Sanctum's hidden rooms", behaviors=[Behavior.REBELLIOUS, Behavior.CREATIVE]),
            "C": CompactOption(text="The Mirror Dimension", behaviors=[Behavior.CREATIVE, Behavior.PRAGMATIC]),
            "D": CompactOption(text="The training spaces where sorcerers practice", behaviors=[Behavior.DISCIPLINED, Behavior.AMBITIOUS]),
        },
    ),

    CompactQuestion(
        id="marvel_11",
        scope="FRANCHISE",
        franchise="marvel",
        question="Which piece of Captain America's history would you most want to witness?",
        options={
            "A": CompactOption(text="The transformation from Steve Rogers into a super-soldier", behaviors=[Behavior.AMBITIOUS, Behavior.DISCIPLINED]),
            "B": CompactOption(text="The Howling Commandos' wartime operations", behaviors=[Behavior.ACTION, Behavior.LOYAL]),
            "C": CompactOption(text="Steve choosing what to do when orders conflict with his principles", behaviors=[Behavior.JUSTICE_DRIVEN, Behavior.REBELLIOUS]),
            "D": CompactOption(text="Steve adapting to a world completely different from his own", behaviors=[Behavior.CURIOUS, Behavior.EMPATHETIC]),
        },
    ),

    CompactQuestion(
        id="marvel_12",
        scope="FRANCHISE",
        franchise="marvel",
        question="Which Spider-Man setting would you most want to spend a day in?",
        options={
            "A": CompactOption(text="A New York rooftop route", behaviors=[Behavior.ACTION, Behavior.CURIOUS]),
            "B": CompactOption(text="Peter Parker's science workspace", behaviors=[Behavior.ANALYTICAL, Behavior.CREATIVE]),
            "C": CompactOption(text="A neighborhood where Spider-Man protects ordinary people", behaviors=[Behavior.EMPATHETIC, Behavior.JUSTICE_DRIVEN]),
            "D": CompactOption(text="A place where Spider-Man can operate completely outside normal expectations", behaviors=[Behavior.REBELLIOUS, Behavior.HUMOROUS]),
        },
    ),

    CompactQuestion(
        id="marvel_13",
        scope="FRANCHISE",
        franchise="marvel",
        question="Which part of the Avengers' headquarters would you most want access to?",
        options={
            "A": CompactOption(text="The training facilities", behaviors=[Behavior.DISCIPLINED, Behavior.ACTION]),
            "B": CompactOption(text="The research and development areas", behaviors=[Behavior.ANALYTICAL, Behavior.CREATIVE]),
            "C": CompactOption(text="The strategy and operations rooms", behaviors=[Behavior.PRAGMATIC, Behavior.AMBITIOUS]),
            "D": CompactOption(text="The common areas where the team actually lives together", behaviors=[Behavior.LOYAL, Behavior.HUMOROUS]),
        },
    ),

    CompactQuestion(
        id="marvel_14",
        scope="FRANCHISE",
        franchise="marvel",
        question="Which Asgardian tradition or place would you most want to experience?",
        options={
            "A": CompactOption(text="The halls of Asgard", behaviors=[Behavior.AMBITIOUS, Behavior.CURIOUS]),
            "B": CompactOption(text="The Bifrost Observatory", behaviors=[Behavior.ANALYTICAL, Behavior.CREATIVE]),
            "C": CompactOption(text="Asgardian combat training", behaviors=[Behavior.DISCIPLINED, Behavior.ACTION]),
            "D": CompactOption(text="The feasts and celebrations of Asgard", behaviors=[Behavior.HUMOROUS, Behavior.LOYAL]),
        },
    ),

    CompactQuestion(
        id="marvel_15",
        scope="FRANCHISE",
        franchise="marvel",
        question="Which Wakandan technology would you most want to use?",
        options={
            "A": CompactOption(text="Kimoyo Beads", behaviors=[Behavior.CURIOUS, Behavior.PRAGMATIC]),
            "B": CompactOption(text="A vibranium-powered suit", behaviors=[Behavior.ACTION, Behavior.AMBITIOUS]),
            "C": CompactOption(text="A remote-controlled vibranium vehicle", behaviors=[Behavior.CREATIVE, Behavior.REBELLIOUS]),
            "D": CompactOption(text="Medical technology used to heal people", behaviors=[Behavior.EMPATHETIC, Behavior.JUSTICE_DRIVEN]),
        },
    ),

    CompactQuestion(
        id="marvel_16",
        scope="FRANCHISE",
        franchise="marvel",
        question="Which Marvel relic would you rather investigate?",
        options={
            "A": CompactOption(text="An Infinity Stone", behaviors=[Behavior.CURIOUS, Behavior.AMBITIOUS]),
            "B": CompactOption(text="A relic from the Ancient One's collection", behaviors=[Behavior.ANALYTICAL, Behavior.DISCIPLINED]),
            "C": CompactOption(text="A piece of advanced alien technology", behaviors=[Behavior.CREATIVE, Behavior.PRAGMATIC]),
            "D": CompactOption(text="An object with a history tied to a heroic sacrifice", behaviors=[Behavior.LOYAL, Behavior.EMPATHETIC]),
        },
    ),

    CompactQuestion(
        id="marvel_17",
        scope="FRANCHISE",
        franchise="marvel",
        question="Which Marvel team dynamic would you most want to be part of?",
        options={
            "A": CompactOption(text="The Avengers' disciplined response to a global threat", behaviors=[Behavior.DISCIPLINED, Behavior.JUSTICE_DRIVEN]),
            "B": CompactOption(text="The Guardians solving problems while barely following a plan", behaviors=[Behavior.HUMOROUS, Behavior.REBELLIOUS]),
            "C": CompactOption(text="A Wakandan team built around technology and strategy", behaviors=[Behavior.ANALYTICAL, Behavior.PRAGMATIC]),
            "D": CompactOption(text="A group exploring places nobody has mapped", behaviors=[Behavior.CURIOUS, Behavior.ACTION]),
        },
    ),

    CompactQuestion(
        id="marvel_18",
        scope="FRANCHISE",
        franchise="marvel",
        question="Which Marvel training experience would you choose?",
        options={
            "A": CompactOption(text="Avengers combat training", behaviors=[Behavior.ACTION, Behavior.DISCIPLINED]),
            "B": CompactOption(text="Mystic Arts training", behaviors=[Behavior.CURIOUS, Behavior.ANALYTICAL]),
            "C": CompactOption(text="Wakandan technology training", behaviors=[Behavior.CREATIVE, Behavior.PRAGMATIC]),
            "D": CompactOption(text="Learning to operate as part of a chaotic space crew", behaviors=[Behavior.REBELLIOUS, Behavior.HUMOROUS]),
        },
    ),

    CompactQuestion(
        id="marvel_19",
        scope="FRANCHISE",
        franchise="marvel",
        question="Which Marvel story would you most want to uncover the missing details of?",
        options={
            "A": CompactOption(text="The history behind the Infinity Stones", behaviors=[Behavior.CURIOUS, Behavior.ANALYTICAL]),
            "B": CompactOption(text="The origins of Wakanda's vibranium civilization", behaviors=[Behavior.AMBITIOUS, Behavior.PRAGMATIC]),
            "C": CompactOption(text="The hidden history of the Ten Rings", behaviors=[Behavior.REBELLIOUS, Behavior.ACTION]),
            "D": CompactOption(text="The lives of heroes whose sacrifices were forgotten", behaviors=[Behavior.JUSTICE_DRIVEN, Behavior.EMPATHETIC]),
        },
    ),

    CompactQuestion(
        id="marvel_20",
        scope="FRANCHISE",
        franchise="marvel",
        question="If you could spend one day inside the Marvel universe with no mission attached, where would you go?",
        options={
            "A": CompactOption(text="A Wakandan research center", behaviors=[Behavior.ANALYTICAL, Behavior.CREATIVE]),
            "B": CompactOption(text="The Avengers training facility", behaviors=[Behavior.ACTION, Behavior.AMBITIOUS]),
            "C": CompactOption(text="A strange corner of the cosmic universe", behaviors=[Behavior.CURIOUS, Behavior.REBELLIOUS]),
            "D": CompactOption(text="A place where heroes and ordinary people actually live side by side", behaviors=[Behavior.LOYAL, Behavior.EMPATHETIC]),
        },
    ),


    # =====================================================
    # AVATAR: THE LAST AIRBENDER — LORE / WORLD DISCOVERY
    # =====================================================

    CompactQuestion(
        id="atla_1",
        scope="FRANCHISE",
        franchise="atla",
        question="Which place in the Four Nations would you most want to explore?",
        options={
            "A": CompactOption(text="Ba Sing Se", behaviors=[Behavior.CURIOUS, Behavior.ANALYTICAL]),
            "B": CompactOption(text="Omashu", behaviors=[Behavior.CREATIVE, Behavior.HUMOROUS]),
            "C": CompactOption(text="The Northern Water Tribe", behaviors=[Behavior.LOYAL, Behavior.DISCIPLINED]),
            "D": CompactOption(text="The Fire Nation capital", behaviors=[Behavior.AMBITIOUS, Behavior.PRAGMATIC]),
        },
    ),

    CompactQuestion(
        id="atla_2",
        scope="FRANCHISE",
        franchise="atla",
        question="Which bending discipline would you most want to study?",
        options={
            "A": CompactOption(text="Airbending", behaviors=[Behavior.CREATIVE, Behavior.REBELLIOUS]),
            "B": CompactOption(text="Waterbending", behaviors=[Behavior.EMPATHETIC, Behavior.CURIOUS]),
            "C": CompactOption(text="Earthbending", behaviors=[Behavior.DISCIPLINED, Behavior.ACTION]),
            "D": CompactOption(text="Firebending", behaviors=[Behavior.AMBITIOUS, Behavior.PRAGMATIC]),
        },
    ),

    CompactQuestion(
        id="atla_3",
        scope="FRANCHISE",
        franchise="atla",
        question="Which advanced bending technique would you most want to witness?",
        options={
            "A": CompactOption(text="Lightning generation", behaviors=[Behavior.DISCIPLINED, Behavior.ANALYTICAL]),
            "B": CompactOption(text="Metalbending", behaviors=[Behavior.CURIOUS, Behavior.CREATIVE]),
            "C": CompactOption(text="Bloodbending", behaviors=[Behavior.AMBITIOUS, Behavior.REBELLIOUS]),
            "D": CompactOption(text="Healing with waterbending", behaviors=[Behavior.EMPATHETIC, Behavior.JUSTICE_DRIVEN]),
        },
    ),

    CompactQuestion(
        id="atla_4",
        scope="FRANCHISE",
        franchise="atla",
        question="Which historic moment would you most want to witness?",
        options={
            "A": CompactOption(text="The invasion during the Day of Black Sun", behaviors=[Behavior.ACTION, Behavior.JUSTICE_DRIVEN]),
            "B": CompactOption(text="The discovery of metalbending", behaviors=[Behavior.CURIOUS, Behavior.REBELLIOUS]),
            "C": CompactOption(text="A great Agni Kai from Fire Nation history", behaviors=[Behavior.DISCIPLINED, Behavior.AMBITIOUS]),
            "D": CompactOption(text="The creation of a major alliance between the nations", behaviors=[Behavior.LOYAL, Behavior.EMPATHETIC]),
        },
    ),

    CompactQuestion(
        id="atla_5",
        scope="FRANCHISE",
        franchise="atla",
        question="Which part of an Air Nomad temple would you most want to see?",
        options={
            "A": CompactOption(text="The old meditation chambers", behaviors=[Behavior.DISCIPLINED, Behavior.CURIOUS]),
            "B": CompactOption(text="The flying bison stables", behaviors=[Behavior.EMPATHETIC, Behavior.LOYAL]),
            "C": CompactOption(text="The training grounds", behaviors=[Behavior.ACTION, Behavior.AMBITIOUS]),
            "D": CompactOption(text="The hidden rooms and forgotten passages", behaviors=[Behavior.REBELLIOUS, Behavior.CREATIVE]),
        },
    ),

    CompactQuestion(
        id="atla_6",
        scope="FRANCHISE",
        franchise="atla",
        question="Which part of the Spirit World would you most want to understand?",
        options={
            "A": CompactOption(text="How spirits interact with humans", behaviors=[Behavior.CURIOUS, Behavior.EMPATHETIC]),
            "B": CompactOption(text="The rules governing the Spirit World", behaviors=[Behavior.ANALYTICAL, Behavior.DISCIPLINED]),
            "C": CompactOption(text="The strangest creatures and landscapes", behaviors=[Behavior.CREATIVE, Behavior.REBELLIOUS]),
            "D": CompactOption(text="How spirits can affect the balance of the world", behaviors=[Behavior.JUSTICE_DRIVEN, Behavior.PRAGMATIC]),
        },
    ),

    CompactQuestion(
        id="atla_7",
        scope="FRANCHISE",
        franchise="atla",
        question="Which destination from Team Avatar's travels would you most want to visit?",
        options={
            "A": CompactOption(text="The Si Wong Desert", behaviors=[Behavior.ACTION, Behavior.CURIOUS]),
            "B": CompactOption(text="Kyoshi Island", behaviors=[Behavior.LOYAL, Behavior.DISCIPLINED]),
            "C": CompactOption(text="The Foggy Swamp", behaviors=[Behavior.CREATIVE, Behavior.REBELLIOUS]),
            "D": CompactOption(text="The Earth Kingdom countryside", behaviors=[Behavior.EMPATHETIC, Behavior.PRAGMATIC]),
        },
    ),

    CompactQuestion(
        id="atla_8",
        scope="FRANCHISE",
        franchise="atla",
        question="Which White Lotus connection would you most want to experience?",
        options={
            "A": CompactOption(text="Learning its history and philosophy", behaviors=[Behavior.ANALYTICAL, Behavior.CURIOUS]),
            "B": CompactOption(text="Training alongside its masters", behaviors=[Behavior.DISCIPLINED, Behavior.AMBITIOUS]),
            "C": CompactOption(text="Seeing how its members operate across nations", behaviors=[Behavior.REBELLIOUS, Behavior.PRAGMATIC]),
            "D": CompactOption(text="Taking part in a mission that protects people", behaviors=[Behavior.JUSTICE_DRIVEN, Behavior.LOYAL]),
        },
    ),

    CompactQuestion(
        id="atla_9",
        scope="FRANCHISE",
        franchise="atla",
        question="Which creature from the Avatar world would you most want to encounter?",
        options={
            "A": CompactOption(text="A sky bison", behaviors=[Behavior.LOYAL, Behavior.EMPATHETIC]),
            "B": CompactOption(text="A shirshu", behaviors=[Behavior.CURIOUS, Behavior.PRAGMATIC]),
            "C": CompactOption(text="A badgermole", behaviors=[Behavior.DISCIPLINED, Behavior.ANALYTICAL]),
            "D": CompactOption(text="A dragon", behaviors=[Behavior.AMBITIOUS, Behavior.ACTION]),
        },
    ),

    CompactQuestion(
        id="atla_10",
        scope="FRANCHISE",
        franchise="atla",
        question="Which part of Ba Sing Se would you most want to explore?",
        options={
            "A": CompactOption(text="The Upper Ring", behaviors=[Behavior.AMBITIOUS, Behavior.DISCIPLINED]),
            "B": CompactOption(text="The Lower Ring", behaviors=[Behavior.EMPATHETIC, Behavior.JUSTICE_DRIVEN]),
            "C": CompactOption(text="The underground tunnels and hidden routes", behaviors=[Behavior.REBELLIOUS, Behavior.CURIOUS]),
            "D": CompactOption(text="The city's vast systems and architecture", behaviors=[Behavior.ANALYTICAL, Behavior.PRAGMATIC]),
        },
    ),

    CompactQuestion(
        id="atla_11",
        scope="FRANCHISE",
        franchise="atla",
        question="Which Fire Nation tradition would you most want to witness?",
        options={
            "A": CompactOption(text="An Agni Kai", behaviors=[Behavior.ACTION, Behavior.DISCIPLINED]),
            "B": CompactOption(text="A royal ceremony", behaviors=[Behavior.AMBITIOUS, Behavior.CURIOUS]),
            "C": CompactOption(text="Fire Nation theater and performance", behaviors=[Behavior.CREATIVE, Behavior.HUMOROUS]),
            "D": CompactOption(text="A traditional family gathering", behaviors=[Behavior.LOYAL, Behavior.EMPATHETIC]),
        },
    ),

    CompactQuestion(
        id="atla_12",
        scope="FRANCHISE",
        franchise="atla",
        question="Which item from the Avatar world would you most want to examine?",
        options={
            "A": CompactOption(text="A piece of ancient Avatar relics", behaviors=[Behavior.CURIOUS, Behavior.ANALYTICAL]),
            "B": CompactOption(text="A Kyoshi Warrior fan", behaviors=[Behavior.DISCIPLINED, Behavior.ACTION]),
            "C": CompactOption(text="Sokka's meteorite sword", behaviors=[Behavior.CREATIVE, Behavior.PRAGMATIC]),
            "D": CompactOption(text="A White Lotus tile", behaviors=[Behavior.LOYAL, Behavior.REBELLIOUS]),
        },
    ),

    CompactQuestion(
        id="atla_13",
        scope="FRANCHISE",
        franchise="atla",
        question="Which Avatar-era invention would you most want to see developed?",
        options={
            "A": CompactOption(text="A new form of transportation between nations", behaviors=[Behavior.CREATIVE, Behavior.PRAGMATIC]),
            "B": CompactOption(text="A new technique for studying bending", behaviors=[Behavior.CURIOUS, Behavior.ANALYTICAL]),
            "C": CompactOption(text="A weapon that could change the balance of a war", behaviors=[Behavior.AMBITIOUS, Behavior.ACTION]),
            "D": CompactOption(text="Technology that makes life safer for ordinary people", behaviors=[Behavior.EMPATHETIC, Behavior.JUSTICE_DRIVEN]),
        },
    ),

    CompactQuestion(
        id="atla_14",
        scope="FRANCHISE",
        franchise="atla",
        question="Which moment in Avatar history would you most want to ask a witness about?",
        options={
            "A": CompactOption(text="Avatar Kyoshi's decisions as a leader", behaviors=[Behavior.JUSTICE_DRIVEN, Behavior.AMBITIOUS]),
            "B": CompactOption(text="The life of Avatar Roku", behaviors=[Behavior.DISCIPLINED, Behavior.CURIOUS]),
            "C": CompactOption(text="The earliest known Avatar traditions", behaviors=[Behavior.ANALYTICAL, Behavior.CREATIVE]),
            "D": CompactOption(text="How ordinary people survived during the Hundred Year War", behaviors=[Behavior.EMPATHETIC, Behavior.PRAGMATIC]),
        },
    ),

    CompactQuestion(
        id="atla_15",
        scope="FRANCHISE",
        franchise="atla",
        question="Which place associated with the Water Tribes would you most want to visit?",
        options={
            "A": CompactOption(text="The Northern Water Tribe", behaviors=[Behavior.DISCIPLINED, Behavior.LOYAL]),
            "B": CompactOption(text="The Southern Water Tribe", behaviors=[Behavior.EMPATHETIC, Behavior.CURIOUS]),
            "C": CompactOption(text="A Water Tribe hunting route", behaviors=[Behavior.ACTION, Behavior.PRAGMATIC]),
            "D": CompactOption(text="An isolated coastal settlement far from the main cities", behaviors=[Behavior.REBELLIOUS, Behavior.CREATIVE]),
        },
    ),

    CompactQuestion(
        id="atla_16",
        scope="FRANCHISE",
        franchise="atla",
        question="Which bending philosophy would you most want to understand?",
        options={
            "A": CompactOption(text="Airbending's idea of freedom and movement", behaviors=[Behavior.REBELLIOUS, Behavior.CURIOUS]),
            "B": CompactOption(text="Earthbending's patience and rooted strength", behaviors=[Behavior.DISCIPLINED, Behavior.PRAGMATIC]),
            "C": CompactOption(text="Waterbending's adaptability", behaviors=[Behavior.CREATIVE, Behavior.EMPATHETIC]),
            "D": CompactOption(text="Firebending's connection to drive and purpose", behaviors=[Behavior.AMBITIOUS, Behavior.ACTION]),
        },
    ),

    CompactQuestion(
        id="atla_17",
        scope="FRANCHISE",
        franchise="atla",
        question="Which kind of Avatar training would you choose?",
        options={
            "A": CompactOption(text="Mastering precise bending forms", behaviors=[Behavior.DISCIPLINED, Behavior.ANALYTICAL]),
            "B": CompactOption(text="Learning how to negotiate between opposing sides", behaviors=[Behavior.EMPATHETIC, Behavior.JUSTICE_DRIVEN]),
            "C": CompactOption(text="Exploring ancient techniques nobody teaches anymore", behaviors=[Behavior.CURIOUS, Behavior.REBELLIOUS]),
            "D": CompactOption(text="Learning to improvise when a fight changes unexpectedly", behaviors=[Behavior.ACTION, Behavior.CREATIVE]),
        },
    ),

    CompactQuestion(
        id="atla_18",
        scope="FRANCHISE",
        franchise="atla",
        question="Which location would you most want to see during a festival?",
        options={
            "A": CompactOption(text="Omashu during a city celebration", behaviors=[Behavior.CREATIVE, Behavior.HUMOROUS]),
            "B": CompactOption(text="A Fire Nation royal celebration", behaviors=[Behavior.AMBITIOUS, Behavior.CURIOUS]),
            "C": CompactOption(text="A Water Tribe community festival", behaviors=[Behavior.LOYAL, Behavior.EMPATHETIC]),
            "D": CompactOption(text="A small Earth Kingdom village celebration", behaviors=[Behavior.PRAGMATIC, Behavior.JUSTICE_DRIVEN]),
        },
    ),

    CompactQuestion(
        id="atla_19",
        scope="FRANCHISE",
        franchise="atla",
        question="Which secret from the Avatar world would you most want to uncover?",
        options={
            "A": CompactOption(text="A forgotten technique from an ancient master", behaviors=[Behavior.CURIOUS, Behavior.DISCIPLINED]),
            "B": CompactOption(text="A hidden political history of one of the nations", behaviors=[Behavior.ANALYTICAL, Behavior.REBELLIOUS]),
            "C": CompactOption(text="A lost location connected to the Avatar cycle", behaviors=[Behavior.CREATIVE, Behavior.AMBITIOUS]),
            "D": CompactOption(text="A story about people whose actions changed the war without becoming famous", behaviors=[Behavior.LOYAL, Behavior.JUSTICE_DRIVEN]),
        },
    ),

    CompactQuestion(
        id="atla_20",
        scope="FRANCHISE",
        franchise="atla",
        question="If you could spend one peaceful year anywhere in the Avatar world, where would you go?",
        options={
            "A": CompactOption(text="A quiet Air Nomad temple", behaviors=[Behavior.DISCIPLINED, Behavior.CURIOUS]),
            "B": CompactOption(text="A lively city like Omashu", behaviors=[Behavior.HUMOROUS, Behavior.CREATIVE]),
            "C": CompactOption(text="A close Water Tribe community", behaviors=[Behavior.LOYAL, Behavior.EMPATHETIC]),
            "D": CompactOption(text="A remote mountain or desert settlement", behaviors=[Behavior.REBELLIOUS, Behavior.PRAGMATIC]),
        },
    ),


    # =====================================================
    # KUNG FU PANDA — LORE / WORLD DISCOVERY
    # =====================================================

    CompactQuestion(
        id="kfp_1",
        scope="FRANCHISE",
        franchise="kung_fu_panda",
        question="Which place in the Kung Fu Panda world would you most want to explore?",
        options={
            "A": CompactOption(text="The Jade Palace", behaviors=[Behavior.DISCIPLINED, Behavior.AMBITIOUS]),
            "B": CompactOption(text="The Panda Village", behaviors=[Behavior.LOYAL, Behavior.EMPATHETIC]),
            "C": CompactOption(text="Gongmen City", behaviors=[Behavior.CURIOUS, Behavior.PRAGMATIC]),
            "D": CompactOption(text="The Spirit Realm", behaviors=[Behavior.CREATIVE, Behavior.REBELLIOUS]),
        },
    ),

    CompactQuestion(
        id="kfp_2",
        scope="FRANCHISE",
        franchise="kung_fu_panda",
        question="Which part of the Jade Palace would you most want to see?",
        options={
            "A": CompactOption(text="The training hall", behaviors=[Behavior.DISCIPLINED, Behavior.ACTION]),
            "B": CompactOption(text="The masters' living quarters", behaviors=[Behavior.CURIOUS, Behavior.LOYAL]),
            "C": CompactOption(text="The courtyard and surrounding grounds", behaviors=[Behavior.EMPATHETIC, Behavior.PRAGMATIC]),
            "D": CompactOption(text="The hidden corners nobody talks about", behaviors=[Behavior.REBELLIOUS, Behavior.CREATIVE]),
        },
    ),

    CompactQuestion(
        id="kfp_3",
        scope="FRANCHISE",
        franchise="kung_fu_panda",
        question="Which legendary object from the series would you most want to examine?",
        options={
            "A": CompactOption(text="The Dragon Scroll", behaviors=[Behavior.CURIOUS, Behavior.ANALYTICAL]),
            "B": CompactOption(text="Oogway's staff", behaviors=[Behavior.DISCIPLINED, Behavior.EMPATHETIC]),
            "C": CompactOption(text="Kai's jade weapons", behaviors=[Behavior.ACTION, Behavior.AMBITIOUS]),
            "D": CompactOption(text="A piece of Shen's weapon technology", behaviors=[Behavior.CREATIVE, Behavior.PRAGMATIC]),
        },
    ),

    CompactQuestion(
        id="kfp_4",
        scope="FRANCHISE",
        franchise="kung_fu_panda",
        question="Which legendary moment from the story would you most want to witness?",
        options={
            "A": CompactOption(text="Oogway choosing Po as the Dragon Warrior", behaviors=[Behavior.CURIOUS, Behavior.REBELLIOUS]),
            "B": CompactOption(text="The Furious Five becoming legends", behaviors=[Behavior.DISCIPLINED, Behavior.AMBITIOUS]),
            "C": CompactOption(text="Po discovering the truth about his past", behaviors=[Behavior.EMPATHETIC, Behavior.LOYAL]),
            "D": CompactOption(text="The final confrontation with Kai in the Spirit Realm", behaviors=[Behavior.ACTION, Behavior.JUSTICE_DRIVEN]),
        },
    ),

    CompactQuestion(
        id="kfp_5",
        scope="FRANCHISE",
        franchise="kung_fu_panda",
        question="Which kind of training at the Jade Palace would you most want to experience?",
        options={
            "A": CompactOption(text="Traditional kung fu fundamentals", behaviors=[Behavior.DISCIPLINED, Behavior.PRAGMATIC]),
            "B": CompactOption(text="Advanced combat against the Furious Five", behaviors=[Behavior.ACTION, Behavior.AMBITIOUS]),
            "C": CompactOption(text="Learning how to turn an unusual body or style into an advantage", behaviors=[Behavior.CREATIVE, Behavior.REBELLIOUS]),
            "D": CompactOption(text="Studying the philosophy behind kung fu", behaviors=[Behavior.CURIOUS, Behavior.ANALYTICAL]),
        },
    ),

    CompactQuestion(
        id="kfp_6",
        scope="FRANCHISE",
        franchise="kung_fu_panda",
        question="Which part of Po's journey would you most want to understand firsthand?",
        options={
            "A": CompactOption(text="How he became the Dragon Warrior", behaviors=[Behavior.AMBITIOUS, Behavior.CURIOUS]),
            "B": CompactOption(text="How he learned to use his own style of fighting", behaviors=[Behavior.CREATIVE, Behavior.REBELLIOUS]),
            "C": CompactOption(text="How he developed inner peace", behaviors=[Behavior.DISCIPLINED, Behavior.EMPATHETIC]),
            "D": CompactOption(text="How he learned to lead others", behaviors=[Behavior.LOYAL, Behavior.JUSTICE_DRIVEN]),
        },
    ),

    CompactQuestion(
        id="kfp_7",
        scope="FRANCHISE",
        franchise="kung_fu_panda",
        question="Which place would you choose as your home base?",
        options={
            "A": CompactOption(text="The Jade Palace", behaviors=[Behavior.DISCIPLINED, Behavior.AMBITIOUS]),
            "B": CompactOption(text="Mr. Ping's noodle shop", behaviors=[Behavior.HUMOROUS, Behavior.LOYAL]),
            "C": CompactOption(text="The Panda Village", behaviors=[Behavior.EMPATHETIC, Behavior.PRAGMATIC]),
            "D": CompactOption(text="A remote mountain temple", behaviors=[Behavior.CURIOUS, Behavior.REBELLIOUS]),
        },
    ),

    CompactQuestion(
        id="kfp_8",
        scope="FRANCHISE",
        franchise="kung_fu_panda",
        question="Which aspect of kung fu philosophy in the series would you most want to study?",
        options={
            "A": CompactOption(text="The discipline required for mastery", behaviors=[Behavior.DISCIPLINED, Behavior.AMBITIOUS]),
            "B": CompactOption(text="Finding peace within yourself", behaviors=[Behavior.EMPATHETIC, Behavior.CURIOUS]),
            "C": CompactOption(text="Turning your own differences into strengths", behaviors=[Behavior.CREATIVE, Behavior.REBELLIOUS]),
            "D": CompactOption(text="Understanding the deeper principles behind a technique", behaviors=[Behavior.ANALYTICAL, Behavior.PRAGMATIC]),
        },
    ),

    CompactQuestion(
        id="kfp_9",
        scope="FRANCHISE",
        franchise="kung_fu_panda",
        question="Which member of the Furious Five's fighting specialties would you most want to study?",
        options={
            "A": CompactOption(text="Tigress's powerful Tiger Style", behaviors=[Behavior.DISCIPLINED, Behavior.ACTION]),
            "B": CompactOption(text="Monkey's agility and unpredictable movement", behaviors=[Behavior.HUMOROUS, Behavior.CREATIVE]),
            "C": CompactOption(text="Crane's aerial movement and positioning", behaviors=[Behavior.CURIOUS, Behavior.PRAGMATIC]),
            "D": CompactOption(text="Viper's fluid and controlled movement", behaviors=[Behavior.EMPATHETIC, Behavior.DISCIPLINED]),
        },
    ),

    CompactQuestion(
        id="kfp_10",
        scope="FRANCHISE",
        franchise="kung_fu_panda",
        question="Which part of Gongmen City's history would you most want to uncover?",
        options={
            "A": CompactOption(text="The city's relationship with kung fu", behaviors=[Behavior.CURIOUS, Behavior.ANALYTICAL]),
            "B": CompactOption(text="The rise of its weapons technology", behaviors=[Behavior.CREATIVE, Behavior.PRAGMATIC]),
            "C": CompactOption(text="The story of its resistance against Shen", behaviors=[Behavior.JUSTICE_DRIVEN, Behavior.REBELLIOUS]),
            "D": CompactOption(text="The traditions of its people before the conflict", behaviors=[Behavior.LOYAL, Behavior.EMPATHETIC]),
        },
    ),

    CompactQuestion(
        id="kfp_11",
        scope="FRANCHISE",
        franchise="kung_fu_panda",
        question="Which kind of weapon or fighting tool from the series would you most want to learn?",
        options={
            "A": CompactOption(text="A traditional staff", behaviors=[Behavior.DISCIPLINED, Behavior.PRAGMATIC]),
            "B": CompactOption(text="The Furious Five's specialized combat techniques", behaviors=[Behavior.ACTION, Behavior.AMBITIOUS]),
            "C": CompactOption(text="An unconventional tool used in a surprising way", behaviors=[Behavior.CREATIVE, Behavior.HUMOROUS]),
            "D": CompactOption(text="A weapon whose mechanics you could study and master", behaviors=[Behavior.ANALYTICAL, Behavior.CURIOUS]),
        },
    ),

    CompactQuestion(
        id="kfp_12",
        scope="FRANCHISE",
        franchise="kung_fu_panda",
        question="Which moment from Master Shifu's life would you most want to witness?",
        options={
            "A": CompactOption(text="His years of training under Oogway", behaviors=[Behavior.DISCIPLINED, Behavior.CURIOUS]),
            "B": CompactOption(text="His early years teaching Tai Lung", behaviors=[Behavior.EMPATHETIC, Behavior.AMBITIOUS]),
            "C": CompactOption(text="His transformation as a teacher of Po", behaviors=[Behavior.CREATIVE, Behavior.PRAGMATIC]),
            "D": CompactOption(text="His battles as a kung fu master", behaviors=[Behavior.ACTION, Behavior.JUSTICE_DRIVEN]),
        },
    ),

    CompactQuestion(
        id="kfp_13",
        scope="FRANCHISE",
        franchise="kung_fu_panda",
        question="Which part of the Valley of Peace would you most want to spend time in?",
        options={
            "A": CompactOption(text="The busy village streets", behaviors=[Behavior.HUMOROUS, Behavior.CURIOUS]),
            "B": CompactOption(text="The training grounds near the Jade Palace", behaviors=[Behavior.DISCIPLINED, Behavior.ACTION]),
            "C": CompactOption(text="The surrounding mountains and quiet paths", behaviors=[Behavior.CREATIVE, Behavior.REBELLIOUS]),
            "D": CompactOption(text="The places where villagers gather and work together", behaviors=[Behavior.LOYAL, Behavior.EMPATHETIC]),
        },
    ),

    CompactQuestion(
        id="kfp_14",
        scope="FRANCHISE",
        franchise="kung_fu_panda",
        question="Which part of Po's connection to his family would you most want to explore?",
        options={
            "A": CompactOption(text="The story of his biological parents", behaviors=[Behavior.CURIOUS, Behavior.EMPATHETIC]),
            "B": CompactOption(text="His relationship with Mr. Ping", behaviors=[Behavior.LOYAL, Behavior.HUMOROUS]),
            "C": CompactOption(text="How his past shaped the way he fights", behaviors=[Behavior.ANALYTICAL, Behavior.PRAGMATIC]),
            "D": CompactOption(text="How he built an identity different from what others expected", behaviors=[Behavior.REBELLIOUS, Behavior.AMBITIOUS]),
        },
    ),

    CompactQuestion(
        id="kfp_15",
        scope="FRANCHISE",
        franchise="kung_fu_panda",
        question="Which legendary master would you most want to learn from?",
        options={
            "A": CompactOption(text="Master Oogway", behaviors=[Behavior.CURIOUS, Behavior.EMPATHETIC]),
            "B": CompactOption(text="Master Shifu", behaviors=[Behavior.DISCIPLINED, Behavior.ANALYTICAL]),
            "C": CompactOption(text="A master known for extraordinary combat ability", behaviors=[Behavior.ACTION, Behavior.AMBITIOUS]),
            "D": CompactOption(text="A master whose methods completely break tradition", behaviors=[Behavior.CREATIVE, Behavior.REBELLIOUS]),
        },
    ),

    CompactQuestion(
        id="kfp_16",
        scope="FRANCHISE",
        franchise="kung_fu_panda",
        question="Which part of the Spirit Realm would you most want to discover?",
        options={
            "A": CompactOption(text="How warriors exist there after death", behaviors=[Behavior.CURIOUS, Behavior.ANALYTICAL]),
            "B": CompactOption(text="The realm's connection to chi", behaviors=[Behavior.DISCIPLINED, Behavior.EMPATHETIC]),
            "C": CompactOption(text="The strangest landscapes and creatures", behaviors=[Behavior.CREATIVE, Behavior.REBELLIOUS]),
            "D": CompactOption(text="The places where legendary masters continue to train", behaviors=[Behavior.ACTION, Behavior.AMBITIOUS]),
        },
    ),

    CompactQuestion(
        id="kfp_17",
        scope="FRANCHISE",
        franchise="kung_fu_panda",
        question="Which part of the panda village would you most want to experience?",
        options={
            "A": CompactOption(text="The community's everyday life", behaviors=[Behavior.LOYAL, Behavior.EMPATHETIC]),
            "B": CompactOption(text="The traditions surrounding food and celebration", behaviors=[Behavior.HUMOROUS, Behavior.CREATIVE]),
            "C": CompactOption(text="The history of the pandas and their connection to chi", behaviors=[Behavior.CURIOUS, Behavior.ANALYTICAL]),
            "D": CompactOption(text="The training and preparation that helped them defend themselves", behaviors=[Behavior.DISCIPLINED, Behavior.ACTION]),
        },
    ),

    CompactQuestion(
        id="kfp_18",
        scope="FRANCHISE",
        franchise="kung_fu_panda",
        question="Which villain's rise would you most want to study?",
        options={
            "A": CompactOption(text="Tai Lung's rise from gifted student to enemy", behaviors=[Behavior.AMBITIOUS, Behavior.CURIOUS]),
            "B": CompactOption(text="Lord Shen's obsession with controlling his future", behaviors=[Behavior.ANALYTICAL, Behavior.PRAGMATIC]),
            "C": CompactOption(text="Kai's quest to take the chi of kung fu masters", behaviors=[Behavior.ACTION, Behavior.REBELLIOUS]),
            "D": CompactOption(text="How each villain's choices shaped the people around them", behaviors=[Behavior.JUSTICE_DRIVEN, Behavior.EMPATHETIC]),
        },
    ),

    CompactQuestion(
        id="kfp_19",
        scope="FRANCHISE",
        franchise="kung_fu_panda",
        question="Which legendary kung fu event would you most want to witness?",
        options={
            "A": CompactOption(text="Oogway and Kai's ancient conflict", behaviors=[Behavior.ACTION, Behavior.JUSTICE_DRIVEN]),
            "B": CompactOption(text="The Five defending the Valley of Peace", behaviors=[Behavior.LOYAL, Behavior.DISCIPLINED]),
            "C": CompactOption(text="Po's first major victory as the Dragon Warrior", behaviors=[Behavior.AMBITIOUS, Behavior.HUMOROUS]),
            "D": CompactOption(text="The moment an unexpected student proves they belong", behaviors=[Behavior.REBELLIOUS, Behavior.CREATIVE]),
        },
    ),

    CompactQuestion(
        id="kfp_20",
        scope="FRANCHISE",
        franchise="kung_fu_panda",
        question="If you could spend one peaceful year in the Kung Fu Panda world, where would you choose?",
        options={
            "A": CompactOption(text="Training at the Jade Palace", behaviors=[Behavior.DISCIPLINED, Behavior.AMBITIOUS]),
            "B": CompactOption(text="Living in the Panda Village", behaviors=[Behavior.LOYAL, Behavior.EMPATHETIC]),
            "C": CompactOption(text="Traveling between the Valley of Peace and distant regions", behaviors=[Behavior.CURIOUS, Behavior.ACTION]),
            "D": CompactOption(text="Studying old kung fu teachings and forgotten places", behaviors=[Behavior.ANALYTICAL, Behavior.REBELLIOUS]),
        },
    ),
]
