import pandas as pd

#this script performs the content analysis

#lists of words
swear_words = ['shit', 'fuck', 'nigga', 'niggas', 'niggaz', 'nigger', 'bitches', 'bitch', 'hoes', 'fuckin', 'fucking', 'fucker', 'fucked', 'dick', 'pussy', 'fucked', 'motherfucker', 'motherfuckers', 'bum','motherfucking', 'motherfuck', 'slut', 'shite', 'whore',
               'piss', 'cunt', 'hell' ,'gay' , 'fag', 'faggot', 'dyke',
               'dickhead', 'jackass', 'asshole', 'retard', 'retarded', 'damn', 'goddamn', 'thot', ]
violent_words = ['dead', 'die', 'war', 'suicide', 'gun', 'murder', 'murdered', 'murderer', 'homicide', 'kill', 'killer','killing', 'killed', 'fight', 'fighting', 'fighter', 'fights', 'violence', 'violent', 'deadly', 'dying', 'bloodshed','stab', 'knife','terrorism',
                 'terrorist', 'warfare', 'combat', 'militant', 'military', 'army', 'navy','warrior','death', 'battlefield', 'punch', 'punches', 'K.O', 'sword', '9mm', 'blaster', 'draco', 'shooter', 'chopper', 'bullet', 'bullets', 'glock','trigger','uzi', 'guns',  ]
alcohol_words = ['alcohol','alcoholic','hangover', 'hungover','liquor', 'cocktail','booze','boozy','bottle', 'beer','cider', 'ale','tequila','vodka','wine','gin','whiskey','scotch','rum','bourbon','champagne','mojito','martini','daiquiri', 'drunk', 'drank', 'patron', 'hennessey', 'henny', 'bacardi', 'smirnoff', 'corona',
                 'coors', 'perignon','drinker','pint', 'firewater', 'hootch', 'moonshine', 'spirits', 'swig', 'tipple', 'heineken', 'coors', 'moet', 'jager',
                    'jagermeister','budweiser', 'jager', 'cup', 'sippin']
drug_words = ['drug', 'drugs', 'druggie', 'dope', 'coke', 'relapse', 'rehab', 'pills', 'spliff', 'purp', 'blunt', 'weed', 'xanax', 'xannie', 'joint', 'addiction', 'addicted', 'addict', 'junkie', 'meds', 'geekin', 'ecstasy', 'xan','cocaine', 'benzo', 'benzos', 'codeine', 'actavis', 'marijuana', ]
love_words = ['love', 'lover', 'loving', 'lovers','loving', 'loves', 'lovin', 'adore', 'romance', 'beloved', 'intimate', 'intimacy','darling', 'baby', 'boyfriend', 'girlfriend', 'babe' , 'romantic', 'honey', 'loved' 'kiss', 'kissin', 'kisser', 'kissing', 'bae', 'boo', 'sweetheart', 'honey',  ]
smoke_words = ['cigarette', 'cigarettes', 'cigar', 'ashtray', 'cigars', 'smokes', 'smoking', 'smoker', 'cigs', 'ciggie', 'cig', 'smokers', 'backwoods', 'marlboro',]
sex_words = ['sex', 'sexy', 'tits', 'ass', 'boobs', 'booty', 'butt', 'boobies', 'anal', 'intercourse','boner', 'erection', 'dick', 'pussy', 'pussycat', 'cock', 'cum', 'twerk', 'twerking', 'twerkin', ]

#converter is important to ensure proper counting
df = pd.read_csv('Tokenized3.csv', converters={'tokenW': eval})

#creates rows in the dataset for info to be stored
df["swear"] = df.tokenW.apply(lambda x: sum([x.count(word) for word in swear_words]))
df['violence'] = df.tokenW.apply(lambda x: sum([x.count(word) for word in violent_words]))
df["alcohol"] = df.tokenW.apply(lambda x: sum([x.count(word) for word in alcohol_words]))
df['drug'] = df.tokenW.apply(lambda x: sum([x.count(word) for word in drug_words]))
df['love'] = df.tokenW.apply(lambda x: sum([x.count(word) for word in love_words]))
df["smoke"] = df.tokenW.apply(lambda x: sum([x.count(word) for word in smoke_words]))
df['sex'] = df.tokenW.apply(lambda x: sum([x.count(word) for word in sex_words]))

df.to_csv('Tokenized3.csv')
