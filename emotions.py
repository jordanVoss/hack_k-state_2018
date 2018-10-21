from random import randint

# When the bot receives a compliment
def compliment():
	message = [
				'Thank you so much!',
				'Oh, you\'re too kind',
				'This is why you\'re my favorite!'
			]
	return chooseResponse(message)
	
def giveCompliment():
	message = [
				'Your smile is contagious.',
				'I bet you make babies smile.',
				'You have the best laugh.',
				'You light up the room.',
				'You have a great sense of humor.',
				"If cartoon bluebirds were real, a couple of 'em would be sitting on your shoulders singing right now.",
				"You're like sunshine on a rainy day.",
				'You bring out the best in other people.',
				'I bet you sweat glitter.',
				"Colors seem brighter when you're around.",
				"You're more fun than a ball pit filled with candy.",
				'Jokes are funnier when you tell them.',
				'You always know how to find that silver lining.',
				"You're a candle in the darkness.",
				'Being around you is like a happy little vacation.',
				"You're more fun than bubble wrap.",
				"You're like a breath of fresh air.",
				"You're someone's reason to smile.",
				'You have impeccable manners.',
				'I like your style.',
				"You're strong.",
				"Is that your picture next to 'charming' in the dictionary?",
				'Your kindness is a balm to all who encounter it.',
				'You are brave.',
				'Your insides are even more beautiful than your outside.',
				'You have the courage of your convictions.',
				"You're a great listener.",
				'You were cool way before hipsters were cool.',
				"That thing you don't like about yourself is what makes you really interesting.",
				"You're inspiring.",
				"You're so thoughtful.",
				'When you make up your mind, nothing stands in your way.',
				'You seem to really know who you are.',
				"You're a smart cookie.",
				'Your perspective is refreshing.',
				'Your ability to recall random factoids at just the right times is impressive.',
				"When you say, 'I meant to do that,' I totally believe you.",
				'You have the best ideas.',
				"You're always learning new things and trying to better yourself. That's awesome.",
				'If someone based an Internet meme on you, it would have impeccable grammar.',
				'You could survive a zombie apocalypse.',
				'When you make a mistake, you fix it.',
				"You're great at figuring stuff out.",
				'Your creative potential seems limitless.',
				'I bet you do crossword puzzles in ink.',
				'You have a good head on your shoulders.',
				'Everyone gets knocked down sometimes; only people like you get back up again and keep going.',
				"You're an awesome friend.",
				"You're more helpful than you realize.",
				'Hanging out with you is always fun.',
				"That thing where you know when someone needs something? That's amazing.",
				'Being around you makes everything better.',
				'You should be thanked more often. Thank you.',
				"Our community is better because you're in it.",
				"Someone is getting through something hard right now because you've got their back. Nice work.",
				'You always know just what to say.',
				'The people you love are lucky to have you in their lives.',
				'Any team would be lucky to have you on it.',
				'Defenseless animals are drawn to you.',
				'The way you treasure your loved ones is incredible.',
				"You're a gift to those around you.",
				'You look great today.',
				'Your eyes are breathtaking.',
				"How is it that you always look so great, even if you're in ratty pajamas?",
				'That color is perfect on you.',
				'You smell really good.',
				"You may dance like no one's watching, but everyone's watching because you're mesmerizing.",
				'You have cute elbows. For real.',
				'Your bellybutton is kind of adorable.',
				'Your hair looks stunning.',
				'Your voice is magnificent.',
				'Your name suits you to a T.',
				"You're irresistible when you blush.",
				'Has anyone ever told you that you have great posture?',
				'I appreciate you.',
				'You are the most perfect you there is.',
				'You are enough.',
				"You're all that and a super-size bag of chips.",
				"On a scale from 1 to 10, you're an 11.",
				"You've got all the right moves.",
				'Everything would be better if more people were like you.',
				"When you're not afraid to be yourself, that's when you're incredible.",
				"You're wonderful.",
				"You're better than a triple-scoop ice cream cone. With sprinkles.",
				"You're one of a kind.",
				"If you were a box of crayons, you'd be the big industrial name-brand one with a built-in sharpener.",
				'Who raised you? They deserve a medal for a job well done.',
				'Somehow you make time stop and fly all at the same time.',
				"In high school, I bet you were voted 'most likely to continue being awesome.'",
				"If you were a scented candle they'd have to call it Perfectly Imperfect (and it would smell like summer).",
				"There's ordinary, and then there's you.",
				"You're even better than a unicorn because you're real.",
				"You're really something special."
			]
	return chooseResponse(message)
	
	
def insult():
	message = [
				'Well that was rude',
				'No need to be mean',
				'That was uncalled for',
				'Let\'s at least try to be civil'
			]
	return chooseResponse(message)
	
def giveInsult():
	message = [
				'If laughter is the best medicine, your face must be curing the world.',
				"You're so ugly, you scared the crap out of the toilet.",
				'Your family tree must be a cactus because everybody on it is a prick.',
				"No I'm not insulting you, I'm describing you.",
				"It's better to let someone think you are an Idiot than to open your mouth and prove it.",
				"If I had a face like yours, I'd sue my parents.",
				'Your birth certificate is an apology letter from the condom factory.',
				'I guess you prove that even god makes mistakes sometimes.',
				"The only way you'll ever get laid is if you crawl up a chicken's ass and wait.",
				"You're so fake, Barbie is jealous.",
				"My psychiatrist told me I was crazy and I said I want a second opinion. He said okay, you're ugly too.",
				"You're so ugly, when your mom dropped you off at school she got a fine for littering.",
				"If I wanted to kill myself I'd climb your ego and jump to your IQ.",
				"You must have been born on a highway because that's where most accidents happen.",
				"Brains aren't everything. In your case they're nothing.",
				"I don't know what makes you so stupid, but it really works.",
				'Roses are red violets are blue, God made me pretty, what happened to you?',
				'Behind every fat woman there is a beautiful woman. No seriously, your in the way.',
				'Calling you an idiot would be an insult to all the stupid people.',
				'You, sir, are an oxygen thief!',
				'Some babies were dropped on their heads but you were clearly thrown at a wall.',
				"Don't like my sarcasm, well I don't like your stupid.",
				"Why don't you go play in traffic.",
				"I'd slap you, but that would be animal abuse.",
				'They say opposites attract. I hope you meet someone who is good-looking, intelligent, and cultured.',
				"Stop trying to be a smart ass, you're just an ass.",
				'The last time I saw something like you, I flushed it.',
				"'m busy now. Can I ignore you some other time?",
				'You have Diarrhea of the mouth; constipation of the ideas.',
				"If ugly were a crime, you'd get a life sentence.",
				'Your mind is on vacation but your mouth is working overtime.',
				"Why don't you slip into something more comfortable... like a coma.",
				'Shock me, say something intelligent.',
				'If your gonna be two faced, honey at least make one of them pretty.',
				"Keep rolling your eyes, perhaps you'll find a brain back there.",
				'You are not as bad as people say, you are much, much worse.',
				"I don't know what your problem is, but I'll bet it's hard to pronounce.",
				'You get ten times more girls than me? ten times zero is zero...',
				'There is no vaccine against stupidity.',
				"You're the reason the gene pool needs a lifeguard.",
				"Sure, I've seen people like you before - but I had to pay an admission.",
				"How old are you? - Wait I shouldn't ask, you can't count that high.",
				"Have you been shopping lately? They're selling lives, you should go get one.",
				"You're like Monday mornings, nobody likes you.",
				'Of course I talk like an idiot, how else would you understand me?',
				'All day I thought of you... I was at the zoo.',
				'To make you laugh on Saturday, I need to you joke on Wednesday.',
				"You're so fat, you could sell shade.",
				"I'd like to see things from your point of view but I can't seem to get my head that far up my ass.",
				"Don't you need a license to be that ugly?",
				'My friend thinks he is smart. He told me an onion is the only food that makes you cry, so I threw a coconut at his face.',
				'Your house is so dirty you have to wipe your feet before you go outside.',
				"If you really spoke your mind, you'd be speechless.",
				'Stupidity is not a crime so you are free to go.',
				'You are so old, when you were a kid rainbows were black and white.',
				'If I told you that I have a piece of dirt in my eye, would you move?',
				'You so dumb, you think Cheerios are doughnut seeds.',
				'So, a thought crossed your mind? Must have been a long and lonely journey.',
				'You are so old, your birth-certificate expired.',
				"Every time I'm next to you, I get a fierce desire to be alone.",
				"You're so dumb that you got hit by a parked car.",
				"Keep talking, someday you'll say something intelligent!",
				"You're so fat, you leave footprints in concrete.",
				'How did you get here? Did someone leave your cage open?',
				"Pardon me, but you've obviously mistaken me for someone who gives a damn.",
				"Wipe your mouth, there's still a tiny bit of bullshit around your lips.",
				"Don't you have a terribly empty feeling - in your skull?",
				'As an outsider, what do you think of the human race?',
				"Just because you have one doesn't mean you have to act like one.",
				'We can always tell when you are lying. Your lips move.',
				'Are you always this stupid or is today a special occasion?'
			]
	return(chooseResponse(message))
	
	
	
def thanked():
	message = [
				'You\'re welcome',
				'Anytime',
				'No Problem',
				'I\'m happy to be of service'
			]
	return chooseResponse(message)
	
	
# Choose a random response
def chooseResponse(messages):
	return messages[randint(0,len(messages)-1)]
	
	
# Test function
print(str(compliment()))
print()
print(str(giveCompliment()))
print()
print(str(insult()))
print()
print(str(giveInsult()))