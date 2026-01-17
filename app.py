import streamlit as st
from gtts import gTTS
import base64
import io

# --- 1. Data Setup ---
# (Truncated for brevity, but includes the full logic from your HTML)
all_words = [
    "abiotic", "abreast", "abscise", "abstraction", "acclimate", "acknowledgment", "adrenaline", "advancement", "aerophyte", "affordable", "aggressive", "alate", "algorithms", "allegation", "alliteration", "alteration", "alternate", "amputation", "anarchist", "anticipation", "antiquity", "apparent", "applicable", "arcane", "armaments", "arpeggio", "assortment", "authentic", "ballium", "balustrade", "barometer", "battlements", "bellicose", "bequeath", "bifurcate", "biofuel", "biopsy", "blandishments", "brassica", "bravura", "brio", "brougham", "calends", "cannelloni", "cantaloupe", "carat", "Caribbean", "carrel", "cataplexy", "catapult", "cathartic", "cavernous", "celeriac", "cerise", "chalice", "chaperone", "chiton", "chronograph", "churlish", "cinnabar", "circumpolar", "claimant", "clevis", "clinician", "cognac", "collided", "colloquial", "commensurate", "commonality", "community", "commutative", "compatible", "compelling", "comprehend", "compromise", "concision", "concussion", "confederation", "consequently", "constituency", "contaminants", "contraction", "copyright", "corona", "corridor", "cosmetologist", "croquet", "cupreous", "curtailment", "dactyl", "dauntingly", "decadent", "decating", "declamatory", "defamation", "definitely", "delirium", "deluge", "demographics", "demonstrable", "denotation", "denudation", "deportment", "derivatives", "desirable", "destructive", "desultory", "deviate", "devour", "differential", "diffraction", "dignitaries", "diligence", "discontinue", "disgruntled", "disparity", "dispassionate", "dispensary", "distasteful", "distillation", "distributor", "diversity", "dolour", "dugong", "echinoid", "ecocidal", "Edmonton", "electrostatic", "emergency", "encounter", "endowment", "engulfed", "enigmatic", "environment", "epicanthus", "equitation", "equivocate", "eristic", "ermine", "espousal", "etching", "exiguous", "expectancy", "expunge", "exuviate", "factual", "falcate", "fatalistic", "ferity", "figurine", "finale", "finials", "fondant", "foreclosure", "forgetfulness", "fortuitous", "frugivore", "fugitive", "fundamental", "gambol", "generalities", "generation", "generator", "gloaming", "graduation", "gregale", "grimace", "groundsel", "gymnasium", "hallux", "hellebore", "hemispheric", "herbage", "hoist", "holystone", "homograph", "horoscope", "hospitable", "hovel", "hydrophone", "idiom", "illogical", "immigration", "imperative", "imperial", "imperturbable", "implement", "impudence", "inaccurate", "incentive", "inclusivity", "individual", "inductee", "inference", "infringement", "inheritance", "installation", "insulation", "intergalactic", "interglacial", "interrogation", "intimation", "irenic", "irresolute", "jewelweed", "juncture", "juvenescent", "kepi", "kombucha", "laceration", "lanate", "legitimate", "levanter", "lexigrams", "li", "limitation", "llama", "logophile", "longevity", "lucrative", "ludicrous", "macadamia", "macerate", "magnificent", "malaise", "malingerer", "mandir", "mansard", "melange", "mentor", "miracle", "misconception", "misconduct", "misdirected", "misnomer", "moderate", "monstrosity", "montage", "moraine", "motivate", "multimedia", "mutilation", "mythological", "narrative", "necropolis", "Neolithic", "nonjudgmental", "notification", "nouveau", "nutrients", "oakum", "obstinate", "ombre", "opah", "orientation", "origami", "osmosis", "otherworldly", "panini", "pannier", "pantropical", "paramount", "paternalistic", "pemmican", "penitentiary", "penury", "perception", "peripherally", "perlite", "permanent", "perpetual", "persistent", "personification", "pessimistic", "pesticide", "physiotherapy", "piquancy", "plicate", "pochard", "policymaker", "polypore", "porridge", "potable", "precatory", "preeminent", "premonition", "presage", "prescind", "prevalence", "prioress", "procedural", "proclamation", "professional", "projection", "pronounce", "proofread", "propagation", "proposition", "protectorate", "psaltery", "puissant", "puritanical", "purported", "quadrat", "quandary", "Québécois", "quinary", "raucous", "reallocation", "recreation", "refrigerate", "reimagine", "relegated", "remembrance", "reptilian", "reputation", "requirement", "residential", "resonated", "retention", "reverie", "rhebok", "rhonchus", "roustabout", "routine", "rufous", "sabbatical", "sanitary", "sapient", "saturate", "scamper", "scurried", "semipermeable", "semiquaver", "sensational", "sequel", "serialization", "shroud", "sifaka", "significant", "sinecure", "sinuous", "smorgasbord", "solvency", "sophism", "spherical", "squalid", "stalwart", "staminate", "stoppage", "strenuous", "substance", "suffocate", "summation", "swerve", "synthetic", "tableaux", "tactile", "tamarin", "telemetry", "terminal", "theodolite", "thesaurus", "thoroughbred", "tomalley", "traipse", "transcend", "transgress", "tropism", "truism", "trustworthy", "ultramarathon", "unique", "unmitigated", "unpalatable", "unshakable", "unshakeable", "utopia", "vanguard", "vaporize", "varve", "velocity", "veracious", "verrucose", "viator", "vindicated", "vitality", "volitive", "vulcanize", "wale", "wanton", "wearisome", "whimper", "whimsical", "winnow", "witheringly", "wound", "wrest", "xeric", "yeoman", "youthfulness"
]

# Paste your wordDefinitions dictionary here (keeping original mapping)
word_definitions = {
  "abiotic": "relating to or derived from non-living things.",
    "abreast": "side-by-side and facing the same way; kept up to date with the latest information.",
    "abscise": "to cut off or away; detach by shedding (used primarily in biology).",
    "abstraction": "the quality of dealing with ideas rather than events; a concept or idea not associated with any specific instance.",
    "acclimate": "to adjust or adapt to a new climate, place, or situation.",
    "acknowledgment": "the act of accepting or admitting the existence or truth of something.",
    "adrenaline": "a hormone secreted by the adrenal glands, especially in moments of stress, increasing heart rate and energy.",
    "advancement": "the development or improvement of something; a promotion in rank or status.",
    "aerophyte": "a plant that grows above ground without soil, absorbing moisture and nutrients from the air (an air plant).",
    "affordable": "inexpensive; reasonably priced.",
    "aggressive": "ready or likely to attack or confront; pursuing aims forcefully.",
    "alate": "having wings or wing-like appendages.",
    "algorithms": "a set of rules or instructions, typically involving computation, for solving a problem or achieving a result.",
    "allegation": "a claim or assertion that someone has done something illegal or wrong, typically without proof.",
    "alliteration": "the occurrence of the same letter or sound at the beginning of adjacent or closely connected words.",
    "alteration": "the process of adjusting or changing something.",
    "alternate": "occurring or succeeding by turns; (verb) to regularly change back and forth between two states or actions.",
    "amputation": "the action of surgically cutting off a limb or other part of the body.",
    "anarchist": "a person who believes in or tries to bring about anarchy (absence of government and order).",
    "anticipation": "the action of anticipating something; expectation or prediction.",
    "antiquity": "the ancient past, especially the period before the Middle Ages.",
    "apparent": "clearly visible or understood; obvious.",
    "applicable": "relevant or appropriate.",
    "arcane": "understood by few; mysterious or secret.",
    "armaments": "military weapons and equipment.",
    "arpeggio": "the notes of a musical chord played quickly, one after the other.",
    "assortment": "a mixed collection of various things.",
    "authentic": "of undisputed origin; genuine.",
    "ballium": "the space enclosed by the inner curtain wall of a castle.",
    "balustrade": "a railing supported by a row of vertical posts or spindles (balusters).",
    "barometer": "an instrument measuring atmospheric pressure, used to forecast weather.",
    "battlements": "a parapet at the top of a wall, often with cut-out sections for defense.",
    "bellicose": "demonstrating aggression and willingness to fight.",
    "bequeath": "to leave a personal estate or property to a person or institution by a will.",
    "bifurcate": "to divide into two branches or forks.",
    "biofuel": "a fuel derived directly from living matter (biomass).",
    "biopsy": "an examination of tissue removed from a living body to discover the presence, cause, or extent of a disease.",
    "blandishments": "flattering or pleasing statements or actions used to persuade someone gently.",
    "brassica": "a plant of the cabbage family, including cabbage, broccoli, and mustard.",
    "bravura": "great technical skill and brilliance shown in a performance or activity.",
    "brio": "vigor or vivacity of style or performance.",
    "brougham": "a light, four-wheeled carriage, typically with a closed body and an open driver's seat.",
    "calends": "the first day of the month in the ancient Roman calendar.",
    "cannelloni": "pasta tubes usually stuffed with a filling and baked in a sauce.",
    "cantaloupe": "a variety of melon with a sweet, orange, fleshy interior.",
    "carat": "a measure of the purity of gold (out of 24) or a unit of weight for precious stones.",
    "Caribbean": "relating to the area of the Caribbean Sea, its islands, and the surrounding coasts.",
    "carrel": "a small, separate enclosure or study area in a library.",
    "cataplexy": "a medical condition involving sudden, brief loss of muscle control, often triggered by strong emotion.",
    "catapult": "a device used to launch projectiles with force; (verb) to hurl or launch something.",
    "cathartic": "providing psychological relief through the open expression of strong emotions.",
    "cavernous": "like a cavern in size, shape, or atmosphere; huge and hollow.",
    "celeriac": "a variety of celery cultivated for its edible root.",
    "cerise": "a deep, vivid reddish-pink color.",
    "chalice": "a large cup or goblet, typically used for drinking wine.",
    "chaperone": "a person who accompanies and looks after another person or group of people.",
    "chiton": "a long woolen tunic worn by men and women in ancient Greece.",
    "chronograph": "an instrument for recording time with great accuracy, such as a stopwatch.",
    "churlish": "rude in a mean-spirited and surly way.",
    "cinnabar": "a bright red mineral, the most common source of mercury.",
    "circumpolar": "located or operating in one of the polar areas.",
    "claimant": "a person making a claim, especially in a lawsuit or benefit application.",
    "clevis": "a U-shaped metal piece with holes in the ends, secured by a pin or bolt.",
    "clinician": "a doctor or health care professional who is directly involved in the treatment and observation of patients.",
    "cognac": "a high-quality brandy, properly from the French town of Cognac.",
    "collided": "struck or bumped into something with force.",
    "colloquial": "used in ordinary or familiar conversation; informal.",
    "commensurate": "corresponding in size or degree; in proportion.",
    "commonality": "the sharing of features or attributes.",
    "community": "a group of people living in the same place or having a particular characteristic in common.",
    "commutative": "relating to an operation that produces the same result regardless of the order of the operands (e.g., in math, a+b = b+a).",
    "compatible": "able to exist or occur together without conflict.",
    "compelling": "evoking interest, attention, or admiration in a powerfully irresistible way.",
    "comprehend": "to grasp mentally; to understand.",
    "compromise": "an agreement or a settlement of a dispute that is reached by each side making concessions.",
    "concision": "the quality of being brief and to the point; succinctness.",
    "concussion": "temporary unconsciousness or confusion caused by a blow to the head.",
    "confederation": "an organization that consists of a number of parties or groups united in an alliance or league.",
    "consequently": "as a result; therefore.",
    "constituency": "a body of voters in a specified area who elect a representative to a legislative body.",
    "contaminants": "a polluting or poisonous substance that makes something impure.",
    "contraction": "the process of becoming smaller.",
    "copyright": "the exclusive legal right to print, publish, perform, film, or record literary, artistic, or musical material.",
    "corona": "the outermost layer of the sun's atmosphere, visible during a total solar eclipse.",
    "corridor": "a long passage in a building from which doors lead into rooms.",
    "cosmetologist": "a person who gives beauty treatments, such as manicures, pedicures, and hairstyling.",
    "croquet": "a game played on a lawn in which players hit wooden balls through hoops.",
    "cupreous": "of or containing copper; copper-colored.",
    "curtailment": "the action or fact of reducing or restricting something.",
    "dactyl": "a metrical foot consisting of one stressed syllable followed by two unstressed syllables.",
    "dauntingly": "in a way that seems difficult to deal with in anticipation; intimidatingly.",
    "decadent": "characterized by moral or cultural decline; luxuriously self-indulgent.",
    "decating": "a finishing process for woolen fabrics that improves their look and feel and minimizes shrinkage.",
    "declamatory": "expressing feelings or opinions in a loud, passionate, or forceful way.",
    "defamation": "the action of damaging the good reputation of someone; slander or libel.",
    "definitely": "without doubt; certainly.",
    "delirium": "an acutely disturbed state of mind resulting from illness or intoxication and characterized by restlessness and incoherence.",
    "deluge": "a severe flood; a large number of things arriving at the same time.",
    "demographics": "statistical data relating to the population and particular groups within it.",
    "demonstrable": "clearly apparent or capable of being logically proved.",
    "denotation": "the literal or primary meaning of a word, in contrast to the feelings or ideas that the word suggests (connotation).",
    "denudation": "the process of wearing away or uncovering the earth's surface (erosion).",
    "deportment": "a person's behavior or manners.",
    "derivatives": "something that is based on another source; (finance) a contract whose value is dependent on an underlying asset.",
    "desirable": "wished for as being an attractive, useful, or necessary quality.",
    "destructive": "causing great and irreparable damage.",
    "desultory": "lacking a plan, purpose, or enthusiasm; jumping from one thing to another.",
    "deviate": "to depart from an established course, standard, or accepted norm.",
    "devour": "to eat food quickly and eagerly; to consume or destroy completely.",
    "differential": "relating to or showing a difference.",
    "diffraction": "the process by which a beam of light or other system of waves is spread out as a result of passing through a narrow aperture or across an edge.",
    "dignitaries": "a person considered to be important because of high rank or office.",
    "diligence": "careful and persistent work or effort.",
    "discontinue": "to cease doing or providing something.",
    "disgruntled": "angry or dissatisfied.",
    "disparity": "a great difference.",
    "dispassionate": "not influenced by strong emotion; impartial.",
    "dispensary": "a place where medicines are prepared and provided.",
    "distasteful": "causing dislike or disgust; offensive.",
    "distillation": "the action of purifying a liquid by a process of heating and cooling; the extraction of the essential meaning of something.",
    "distributor": "an agent who supplies goods to retailers or consumers.",
    "diversity": "the state of being diverse; variety.",
    "dolour": "a state of sadness or distress.",
    "dugong": "a large, plant-eating marine mammal, related to the manatee.",
    "echinoid": "a marine invertebrate of the class Echinoidea, which includes sea urchins and sand dollars.",
    "ecocidal": "relating to or causing the destruction of the natural environment.",
    "Edmonton": "the capital city of the Canadian province of Alberta.",
    "electrostatic": "relating to stationary electric charges or fields.",
    "emergency": "a serious, unexpected, and often dangerous situation requiring immediate action.",
    "encounter": "an unexpected or casual meeting with someone or something.",
    "endowment": "an income or form of property given to a person or institution.",
    "engulfed": "swept over (something) and covered it completely.",
    "enigmatic": "difficult to interpret or understand; mysterious.",
    "environment": "the surroundings or conditions in which a person, animal, or plant lives or operates.",
    "epicanthus": "a vertical fold of skin at the inner corner of the eye, characteristic of certain populations.",
    "equitation": "the art or practice of horse riding.",
    "equivocate": "to use ambiguous language so as to conceal the truth or avoid committing oneself.",
    "eristic": "relating to or characterized by debate intended to score points rather than to reach truth.",
    "ermine": "a stoat, especially in its white winter coat; a luxurious white fur.",
    "espousal": "the act of adopting or supporting a cause, belief, or way of life.",
    "etching": "a print made from an engraved metal plate, or the process of creating it.",
    "exiguous": "extremely small in amount; scanty.",
    "expectancy": "the state of anticipating or awaiting something.",
    "expunge": "to erase or remove completely (something unwelcome or unpleasant).",
    "exuviate": "to shed an outer covering or skin; to molt.",
    "factual": "concerned with facts; actual.",
    "falcate": "curved like a sickle; hooked.",
    "fatalistic": "believing that all events are predetermined and therefore inevitable.",
    "ferity": "the state of being fierce or savage; wildness.",
    "figurine": "a small ornamental statue, typically of a human or animal.",
    "finale": "the last part of a performance, piece of music, or series of events.",
    "finials": "a distinctive ornament at the apex of a roof, canopy, or gable.",
    "fondant": "a thick paste made of sugar and water, used as a basis for candies or icing.",
    "foreclosure": "the process of taking possession of a mortgaged property when the mortgagor fails to keep up their mortgage payments.",
    "forgetfulness": "the quality or state of being prone to forgetting.",
    "fortuitous": "happening by a lucky chance; accidental but positive.",
    "frugivore": "an animal that feeds on fruit.",
    "fugitive": "a person who has escaped from a place or is in hiding, especially to avoid arrest.",
    "fundamental": "forming a necessary base or core; of central importance.",
    "gambol": "to run or jump about playfully.",
    "generalities": "a statement that is vague and lacks detail.",
    "generation": "all of the people born and living at about the same time.",
    "generator": "a machine that converts mechanical energy into electrical energy.",
    "gloaming": "twilight; dusk.",
    "graduation": "the ceremony of being awarded an academic degree or diploma.",
    "gregale": "a strong, cold, northeasterly wind of the central Mediterranean region.",
    "grimace": "an ugly, twisted expression on a person's face, expressing pain or disapproval.",
    "groundsel": "a plant of the daisy family, often considered a weed.",
    "gymnasium": "a room or building equipped for physical exercise.",
    "hallux": "the big toe or first digit of the hind foot.",
    "hellebore": "a plant of the buttercup family, typically with white, pink, or purple flowers.",
    "hemispheric": "relating to or situated in a hemisphere (half of a sphere, especially Earth).",
    "herbage": "the edible parts of plants, especially the leaves and stems.",
    "hoist": "to raise (something) by means of ropes and pulleys.",
    "holystone": "a soft sandstone used for scouring the decks of ships.",
    "homograph": "each of two or more words spelled the same but having different meanings (e.g., tear/tear).",
    "horoscope": "a forecast of a person's future based on the relative positions of the stars and planets at the time of their birth.",
    "hospitable": "friendly and welcoming to guests or strangers.",
    "hovel": "a small, squalid, unpleasant, or simply constructed dwelling.",
    "hydrophone": "a microphone used underwater to detect sound.",
    "idiom": "a group of words established by usage as having a meaning not deducible from those of the individual words (e.g., 'kick the bucket').",
    "illogical": "lacking sense or sound reasoning.",
    "immigration": "the action of coming to live permanently in a foreign country.",
    "imperative": "absolutely necessary or required.",
    "imperial": "relating to an empire or an emperor.",
    "imperturbable": "unable to be upset or excited; calm.",
    "implement": "(noun) a tool or instrument; (verb) to put (a decision, plan, or agreement) into effect.",
    "impudence": "the quality of being impertinent, rude, or disrespectful.",
    "inaccurate": "not accurate; incorrect or untrue.",
    "incentive": "a thing that motivates or encourages someone to do something.",
    "inclusivity": "the practice or policy of providing equal access to opportunities and resources for people who might otherwise be excluded.",
    "individual": "single; separate.",
    "inductee": "a person who has been inducted into an organization, military service, or an office.",
    "inference": "a conclusion reached on the basis of evidence and reasoning.",
    "infringement": "the action of breaking the terms of a law, agreement, or right.",
    "inheritance": "a property or money passed from an ancestor or previous owner.",
    "installation": "the action of setting something up in position for use.",
    "insulation": "material used to prevent the transfer of heat, electricity, or sound.",
    "intergalactic": "located or situated between galaxies.",
    "interglacial": "relating to a period of warmer climate between two glacial periods.",
    "interrogation": "the action of questioning someone thoroughly or aggressively.",
    "intimation": "an indication or hint.",
    "irenic": "aiming at peace or conciliation.",
    "irresolute": "showing or feeling hesitancy; uncertain.",
    "jewelweed": "a plant with bright yellow or orange flowers, often found in damp ground.",
    "juncture": "a particular point in time or a place where things join.",
    "juvenescent": "becoming youthful.",
    "kepi": "a French military cap with a flat circular top and a visor.",
    "kombucha": "a beverage consisting of sweetened black or green tea fermented with a culture of yeast and bacteria.",
    "laceration": "a deep cut or tear in skin or flesh.",
    "lanate": "covered with long, soft, woolly hairs (used mainly in botany).",
    "legitimate": "conforming to the law or to rules; justifiable.",
    "levanter": "a strong easterly wind that blows through the Strait of Gibraltar into the Mediterranean Sea.",
    "lexigrams": "a symbol that represents a word but is not necessarily suggestive of the object it represents.",
    "li": "a traditional Chinese unit of distance, commonly standardized to 500 meters (about 0.3 miles).",
    "limitation": "a restrictive weakness; a condition of being limited.",
    "llama": "a domesticated South American camelid, used as a pack animal and for its wool.",
    "logophile": "a lover of words.",
    "longevity": "long existence or service.",
    "lucrative": "producing a great deal of profit; financially advantageous.",
    "ludicrous": "so foolish, unreasonable, or out of place as to be amusing; ridiculous.",
    "macadamia": "a type of nut produced by an evergreen tree native to Australia.",
    "macerate": "to soften or separate into pieces by soaking in a liquid.",
    "magnificent": "impressively beautiful, elaborate, or extravagant; superb.",
    "malaise": "a general feeling of discomfort, illness, or unease whose exact cause is difficult to identify.",
    "malingerer": "a person who exaggerates or feigns illness to escape duty or work.",
    "mandir": "a Hindu temple.",
    "mansard": "a roof that has four sloping sides, each of which becomes steeper halfway down.",
    "melange": "a varied mixture.",
    "mentor": "an experienced and trusted advisor.",
    "miracle": "an extraordinary and welcome event that is not explicable by natural or scientific laws and is therefore attributed to a divine agency.",
    "misconception": "a view or opinion that is incorrect because it is based on faulty thinking or understanding.",
    "misconduct": "unacceptable or improper behavior.",
    "misdirected": "wrongly aimed or guided.",
    "misnomer": "a wrong or inaccurate name or designation.",
    "moderate": "average in amount, intensity, or quality; neither hot nor cold.",
    "monstrosity": "something, especially a building, that is unsightly, huge, or grotesque.",
    "montage": "the process or technique of selecting, editing, and piecing together separate sections of film or sound to form a continuous whole.",
    "moraine": "a mass of rocks and sediment carried down and deposited by a glacier.",
    "motivate": "to provide someone with a motive for doing something.",
    "multimedia": "the use of a variety of artistic or communicative media.",
    "mutilation": "the action of destroying or severely damaging something.",
    "mythological": "based on or appearing in myths or traditional stories.",
    "narrative": "a spoken or written account of connected events; a story.",
    "necropolis": "a large, elaborate cemetery belonging to an ancient city.",
    "Neolithic": "relating to the later part of the Stone Age, when ground or polished stone weapons and tools predominated.",
    "nonjudgmental": "avoiding the expression of moral or critical opinions.",
    "notification": "the action of notifying someone or something; a formal statement or announcement.",
    "nouveau": "newly arrived or developed; modern.",
    "nutrients": "a substance that provides nourishment essential for the maintenance of life and growth.",
    "oakum": "loose fiber obtained by untwisting and picking apart old ropes, used for caulking seams in wooden ships.",
    "obstinate": "stubbornly refusing to change one's opinion or chosen course of action.",
    "ombre": "the gradual blending of one color hue to another, usually from light to dark.",
    "opah": "a large, colorful, deep-sea fish, also known as a moonfish.",
    "orientation": "the relative position or direction of something; a person's attitudes, beliefs, or interests.",
    "origami": "the Japanese art of folding paper into decorative shapes and figures.",
    "osmosis": "a process by which molecules of a solvent pass through a semipermeable membrane; gradual and often unconscious assimilation of ideas.",
    "otherworldly": "relating to an imaginary or spiritual world; ethereal.",
    "panini": "a small Italian bread roll, often grilled or toasted with a filling.",
    "pannier": "a basket, bag, or similar container, especially one of a pair carried on either side of a bicycle or pack animal.",
    "pantropical": "occurring in or distributed throughout the tropics worldwide.",
    "paramount": "more important than anything else; supreme.",
    "paternalistic": "the policy or practice on the part of people in positions of authority of restricting the freedom and responsibilities of those subordinate to them.",
    "pemmican": "a concentrated paste of meat and fat, traditionally used by North American indigenous peoples.",
    "penitentiary": "a prison for people convicted of serious crimes.",
    "penury": "the state of being extremely poor; destitution.",
    "perception": "the way in which something is regarded, understood, or interpreted.",
    "peripherally": "relating to or situated on the edge or periphery of something.",
    "perlite": "a form of obsidian (volcanic glass) used in horticulture and insulation.",
    "permanent": "lasting or intended to last or remain unchanged indefinitely.",
    "perpetual": "never ending or changing.",
    "persistent": "continuing firmly or obstinately in a course of action in spite of difficulty or opposition.",
    "personification": "the attribution of a personal nature or human characteristics to something nonhuman.",
    "pessimistic": "tending to see the worst aspect of things or believe that the worst will happen.",
    "pesticide": "a substance used for destroying insects or other organisms harmful to cultivated plants or animals.",
    "physiotherapy": "the treatment of disease or injury by physical methods such as massage, heat treatment, and exercise, rather than by drugs or surgery.",
    "piquancy": "a pleasingly sharp and appetizing flavor; the quality of being stimulating or intriguing.",
    "plicate": "folded like a fan (used mainly in botany and zoology).",
    "pochard": "a diving duck with a short bill and a rounded head.",
    "policymaker": "a person responsible for making policies, especially in government.",
    "polypore": "a bracket fungus with pores or tubes on the underside.",
    "porridge": "a dish consisting of oatmeal or another cereal boiled in water or milk.",
    "potable": "safe to drink; drinkable.",
    "precatory": "expressing a wish or request (used mainly in law).",
    "preeminent": "surpassing all others; very distinguished.",
    "premonition": "a strong feeling that something is about to happen, especially something unpleasant.",
    "presage": "a sign or warning that something is going to happen; (verb) to be a sign or warning of.",
    "prescind": "to detach or separate (an idea) from other ideas, or from reality.",
    "prevalence": "the state of being common or widespread.",
    "prioress": "a nun who is second in authority to an abbess in a convent.",
    "procedural": "relating to or denoting an established way of doing something.",
    "proclamation": "a public or official announcement, especially one dealing with a matter of great importance.",
    "professional": "relating to or belonging to a profession; competent and paid for one's work.",
    "projection": "an estimate or forecast of a future situation based on current trends.",
    "pronounce": "to make the sound of a word or part of a word; to officially declare.",
    "proofread": "to read a text and mark any errors.",
    "propagation": "the action of widely spreading and promoting an idea, theory, etc.; the breeding of plants or animals.",
    "proposition": "a statement or assertion that expresses a judgment or opinion; a suggested plan.",
    "protectorate": "a state that is controlled and protected by another.",
    "psaltery": "an ancient stringed musical instrument, played by plucking the strings.",
    "puissant": "having great power or influence.",
    "puritanical": "practicing or affecting strict religious or moral behavior.",
    "purported": "appearing or stated to be true, though not necessarily so; alleged.",
    "quadrat": "a small square frame used by ecologists to isolate a standard area for study.",
    "quandary": "a state of perplexity or uncertainty over what to do in a difficult situation.",
    "Québécois": "a native or inhabitant of the province of Quebec in Canada.",
    "quinary": "relating to or based on the number five.",
    "raucous": "making or constituting a disturbingly harsh and loud noise.",
    "reallocation": "the action or process of distributing something differently.",
    "recreation": "activity done for enjoyment when one is not working.",
    "refrigerate": "to subject (food or drink) to cold in order to chill or preserve it.",
    "reimagine": "to imagine again or anew; to rethink (something) in a new or different way.",
    "relegated": "consigned or dismissed to an inferior rank or position.",
    "remembrance": "the action of remembering something; a memory.",
    "reptilian": "relating to or characteristic of reptiles.",
    "reputation": "the beliefs or opinions that are generally held about someone or something.",
    "requirement": "a thing that is compulsory; a necessary condition.",
    "residential": "designed for people to live in.",
    "resonated": "produced or be filled with a deep, full, reverberating sound; evoked a strong, corresponding emotion or idea.",
    "retention": "the continued possession, use, or control of something; the capacity to keep something in mind.",
    "reverie": "a state of being pleasantly lost in one's thoughts; a daydream.",
    "rhebok": "a small African antelope with slender horns.",
    "rhonchus": "a dry, rattling sound in a lung or bronchial tube due to partial obstruction.",
    "roustabout": "an unskilled laborer, especially one working on oil rigs or at circuses.",
    "routine": "a sequence of actions regularly followed; a fixed program.",
    "rufous": "reddish-brown.",
    "sabbatical": "a period of paid leave granted to a university teacher for study or travel; a break from customary work.",
    "sanitary": "relating to the conditions that affect health, especially with respect to cleanliness and disease prevention.",
    "sapient": "wise, or attempting to appear wise.",
    "saturate": "to soak thoroughly with liquid so that no more can be absorbed; to completely fill something.",
    "scamper": "to run with quick light steps, especially through fear or excitement.",
    "scurried": "moved hurriedly with short, quick steps.",
    "semipermeable": "allowing certain small molecules or ions to pass through it by diffusion or osmosis.",
    "semiquaver": "a sixteenth note, a musical note lasting one sixteenth of the time value of a whole note.",
    "sensational": "presenting information in a way that is intended to provoke public interest and excitement, often at the expense of accuracy.",
    "sequel": "a published, broadcast, or recorded work that continues the story or develops the theme of an earlier one.",
    "serialization": "the process of arranging data or objects into a format that can be stored or transmitted.",
    "shroud": "a length of cloth or an enveloping garment in which a dead person is wrapped for burial.",
    "sifaka": "a type of lemur native to Madagascar, known for its distinctive movement.",
    "significant": "sufficiently great or important to be worthy of attention; noteworthy.",
    "sinecure": "a position requiring little or no work but giving the holder status or financial benefit.",
    "sinuous": "having many curves and turns.",
    "smorgasbord": "a buffet-style meal with various hot and cold dishes; a wide range of things.",
    "solvency": "the possession of assets in excess of liabilities; ability to pay one's debts.",
    "sophism": "a clever but false argument, especially one used to deceive.",
    "spherical": "shaped like a sphere or ball.",
    "squalid": "extremely dirty and unpleasant, especially as a result of poverty or neglect.",
    "stalwart": "loyal, reliable, and hardworking.",
    "staminate": "having or producing stamens (the male organs of a flower).",
    "stoppage": "an instance of hindering or stopping a process or movement.",
    "strenuous": "requiring or using great exertion; laborious.",
    "substance": "the real physical matter of which a person or thing consists and which has a tangible existence.",
    "suffocate": "to die or cause to die from lack of air or inability to breathe.",
    "summation": "the process of adding things up; the presentation of a summary.",
    "swerve": "to change or cause to change direction suddenly.",
    "synthetic": "made by chemical synthesis to imitate a natural product; artificial.",
    "tableaux": "a group of models or silent, motionless figures representing a scene (often historical).",
    "tactile": "of or connected with the sense of touch.",
    "tamarin": "a small, forest-dwelling monkey of Central and South America.",
    "telemetry": "the process of recording and transmitting the readings of an instrument.",
    "terminal": "of, relating to, or situated at the end of a sequence; a point of connection for an electric current.",
    "theodolite": "a portable surveying instrument for measuring horizontal and vertical angles.",
    "thesaurus": "a book that lists words grouped together according to similarity of meaning (including synonyms and sometimes antonyms).",
    "thoroughbred": "a horse of a pure breed, especially a breed used for racing.",
    "tomalley": "the liver and digestive gland of a lobster or crab, used in cooking.",
    "traipse": "to walk or move wearily or reluctantly.",
    "transcend": "to be or go beyond the range or limits of (something); surpass.",
    "transgress": "to go beyond the bounds of (a moral principle or other established standard of behavior).",
    "tropism": "the turning or growth movement of a plant or animal in response to a stimulus (e.g., light).",
    "truism": "a statement that is obviously true and says nothing new or interesting.",
    "trustworthy": "able to be relied on as honest or truthful.",
    "ultramarathon": "a running race longer than the traditional marathon length of 26.2 miles.",
    "unique": "being the only one of its kind; unusually special.",
    "unmitigated": "absolute; unqualified.",
    "unpalatable": "not pleasant to taste; difficult to accept or tolerate.",
    "unshakable": "not able to be disputed, questioned, or lessened; firm.",
    "unshakeable": "an alternative spelling of 'unshakable'.",
    "utopia": "an imagined place or state of things in which everything is perfect.",
    "vanguard": "a group of people leading the way in new ideas or developments.",
    "vaporize": "to convert or change into vapor or gas.",
    "varve": "an annual layer of sediment or rock formed in a body of water, especially a lake.",
    "velocity": "the speed of something in a given direction.",
    "veracious": "speaking or representing the truth; truthful.",
    "verrucose": "covered with wart-like bumps or excrescences.",
    "viator": "a traveler.",
    "vindicated": "cleared someone of blame or suspicion; shown to be right or justified.",
    "vitality": "the state of being strong and active; energy.",
    "volitive": "expressing wish or will (used mainly in grammar).",
    "vulcanize": "to treat rubber with sulfur or other chemicals to improve its elasticity and strength.",
    "wale": "a streak or ridge, typically raised on the skin by a whip or stick; (nautical) a plank running along the side of a boat.",
    "wanton": "deliberate and unprovoked; sexually unrestrained.",
    "wearisome": "causing one to feel tired or bored.",
    "whimper": "to make a series of low, weak sounds expressive of fear, pain, or discontent.",
    "whimsical": "playfully quaint or fanciful, especially in an appealing and amusing way.",
    "winnow": "to blow a current of air through (grain) to remove the chaff; to separate desirable from undesirable parts.",
    "witheringly": "in a way that is intended to make someone feel small or ashamed; scathingly.",
    "wound": "an injury to living tissue caused by a cut, blow, or other impact.",
    "wrest": "to pull (something) away with a forceful twisting movement.",
    "xeric": "requiring only a small amount of moisture (used mainly in ecology).",
    "yeoman": "a man holding and cultivating a small landed estate; a naval petty officer in charge of clerical work.",
    "youthfulness": "the state or quality of being young or youthful."
}

proper_nouns = ["Caribbean", "Edmonton", "Neolithic", "Québécois"]

# --- 2. Logic Functions ---
def get_masked_word(word):
    vowels = "aeiouAEIOU"
    masked = "".join(['_' if c in vowels else c for c in word])
    return masked if word in proper_nouns else masked.lower()

def text_to_speech(text):
    tts = gTTS(text=text, lang='en', tld='ca')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    return fp

# --- 3. Streamlit State Management ---
if 'word_index' not in st.session_state:
    st.session_state.word_index = 0
if 'current_group' not in st.session_state:
    st.session_state.current_group = None
if 'score' not in st.session_state:
    st.session_state.score = 0

# --- 4. UI Layout ---
st.set_page_config(page_title="Vivian's Spelling Bee", page_icon="🧠")

st.markdown("""
    <style>
    .main { background-color: #F8F4FF; }
    .stButton>button { background-color: #673AB7; color: white; border-radius: 8px; }
    .mission-box { background-color: #F0E5FF; padding: 15px; border-radius: 10px; border-left: 5px solid #B39DDB; margin-bottom: 20px;}
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 Vivian's Spelling Challenge")


all_words.sort(key=str.lower)

# This will group them after sorting
GROUP_SIZE = 33
groups = [all_words[i:i + GROUP_SIZE] for i in range(0, len(all_words), GROUP_SIZE)]


group_options = [f"Group {i+1} ({g[0][0].upper()} - {g[-1][0].upper()})" for i, g in enumerate(groups)]

selected_group_name = st.selectbox("Select your word group:", ["-- select --"] + group_options)

if selected_group_name != "-- select --":
    group_idx = group_options.index(selected_group_name)
    current_words = groups[group_idx]
    
    # Reset if group changes
    if st.session_state.current_group != group_idx:
        st.session_state.current_group = group_idx
        st.session_state.word_index = 0
    
    # Progress Display
    st.markdown(f"""
        <div class="mission-box">
        💡 Daily Mission: Spell this group of {len(current_words)} words! 
        ({st.session_state.word_index} / {len(current_words)} completed)
        </div>
        """, unsafe_allow_html=True)

    if st.session_state.word_index < len(current_words):
        target_word = current_words[st.session_state.word_index]
        
        st.subheader("Current Word:")
        st.markdown(f"<h1 style='text-align: center; letter-spacing: 10px;'>{get_masked_word(target_word)}</h1>", unsafe_allow_html=True)
        
        # Audio Hint
        if st.button("🔊 Hear Word Hint"):
            audio_fp = text_to_speech(target_word)
            st.audio(audio_fp, format="audio/mp3", autoplay=True)

        # Input Area
        user_input = st.text_input("Type the full word here:", key=f"input_{st.session_state.word_index}").strip()
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("✅ Check Word"):
                is_correct = False
                if target_word in proper_nouns:
                    is_correct = (user_input == target_word)
                else:
                    is_correct = (user_input.lower() == target_word.lower())
                
                if is_correct:
                    st.success(f"Correct! Great job!")
                    st.info(f"**Meaning:** {word_definitions.get(target_word, 'No definition found.')}")
                    st.session_state.word_index += 1
                    st.rerun()
                else:
                    st.error(f"Incorrect. The correct word was: {target_word}")
                    st.info(f"**Meaning:** {word_definitions.get(target_word, 'No definition found.')}")

        with col2:
            if st.button("➡️ Skip Word"):
                st.session_state.word_index += 1
                st.rerun()
    else:
        st.balloons()
        st.success("Hooray! Today's mission completed. Select a new group to continue.")
else:
    st.write("Please select a group above to start your daily mission.")
