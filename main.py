import praw
import yaml
import random

with open('config.yaml', 'r') as config_file:
    config = yaml.load(config_file, Loader=yaml.BaseLoader)

with open("replied_to.txt", "r") as replied_to_file:
    replied_to = replied_to_file.read()
    replied_to = replied_to.split("\n")

reddit = praw.Reddit(username=config['username'], password=config['password'], client_id=config['client_id'], client_secret=config['client_secret'], user_agent=config['user_agent'])

while True:
    for comment in reddit.subreddit('lotrmemes').comments(limit=25):
        if "to mind the children, to find food and bedding when the men return. what renown is there in that?" in comment.body.lower():
            reply = "My lady, a time may come for valor without renown. Who then will your people look to in the last defense?"
        elif "forged from the shards of narsil" in comment.body.lower():
            reply = "Sauron will not have forgotten the sword of Elendil. The blade that was broken shall return to Minas Tirith."
        elif "now come the days of the king" in comment.body.lower():
            reply = "This day does not belong to one man but to all. Let us together rebuild this world, that we may share in the days of peace."
        elif "the world of men will fall" in comment.body.lower() or "all will come to darkness" in comment.body.lower() or "my city to ruin" in comment.body.lower():
            reply = "I do not know what strength is in my blood, but I swear to you I will not let the White City fall, nor our people fail."
        elif "fellowship has failed" in comment.body.lower() or "it has been in vain" in comment.body.lower():
            reply = "Not if we hold true to each other. We will not abandon Merry and Pippin to torment and death. Not while we have strength left. Leave all that can be spared behind. We travel light. Let’s hunt some Orc."
        elif "second" in comment.body.lower() and "breakfast" in comment.body.lower():
            reply = comment.author.name + ", you've already had it."

        elif "aragorn" in comment.body.lower() or "strider" in comment.body.lower() or "son of arathorn" in comment.body.lower():
            if "gondor" in comment.body.lower() or "realm" in comment.body.lower() or "white" in comment.body.lower():
                choices = ['Stand your ground, sons of Gondor, of Rohan, my brothers. I see in your eyes the same fear that would take the heart of me! A day may come when the courage of men fails, when we forsake our friends and break all bonds of fellowship; but it is not this day! An hour of wolves and shattered shields when the age of men comes crashing down, but it is not this day; this day we fight!!! And for all that is dear to you in this world, I bid you stand, men of the west, and fight!',
                           'Be at peace, son of Gondor.',
                           'THE BEACONS OF MINAS TIRITH! THE BEACONS ARE LIT! GONDOR CALLS FOR AID!',
                           'You shall not enter the realm of Gondor.',
                           'I will not let the White city fall nor our people fail.',
                           'There is no strength in Gondor that can avail us.']
                reply = random.choice(choices)
            elif "dwell in the mountain" in comment.body.lower():
                reply = "Murderers… traitors! You would call upon them to fight? They believe in nothing! They answer to no one!"
            elif "beacons" in comment.body.lower():
                reply = "THE BEACONS OF MINAS TIRITH! THE BEACONS ARE LIT! GONDOR CALLS FOR AID!"
            elif "caradhras" in comment.body.lower() or "mountain" in comment.body.lower() or "saruman" in comment.body.lower():
                reply = "HE'S TRYING TO BRING DOWN THE MOUNTAIN! GANDALF, WE MUST TURN BACK!"
            elif "black" in comment.body.lower() or "gate" in comment.body.lower():
                reply = "Stand your ground, sons of Gondor, of Rohan, my brothers. I see in your eyes the same fear that would take the heart of me! A day may come when the courage of men fails, when we forsake our friends and break all bonds of fellowship; but it is not this day! An hour of wolves and shattered shields when the age of men comes crashing down, but it is not this day; this day we fight!!! And for all that is dear to you in this world, I bid you stand, men of the west, and fight!"
            elif "hope" in comment.body.lower():
                reply = "No. There is still hope for Frodo. He needs time… and safe passage across the plains of Gorgoroth. We can give him that."
            elif "sword" in comment.body.lower():
                reply = comment.author.name + ", you have my sword."
            else:
                choices = ['I would have gone with you to the end into the very fires of Mordor.',
                           'Not if we hold true to each other.',
                           'I thought I had wandered into a dream.',
                           'I will not let the White city fall nor our people fail',
                           'FOR FRODO!!!',
                           'Let us together rebuild this world that we may share in the days of peace.',
                           'The best revenge is letting go and living well.',
                           'Tis the lay of Luthien. The elf-maiden who gave her love to eren a mortal!',
                           'HE\'S TRYING TO BRING DOWN THE MOUNTAIN! GANDALF, WE MUST TURN BACK!',
                           'I swore to protect you.',
                           'If by my life or death I can protect you, I will. You have my sword.',
                           'THE BEACONS OF MINAS TIRITH! THE BEACONS ARE LIT! GONDOR CALLS FOR AID!',
                           'It is but a shadow and a thought that you love. I cannot give you what you seek.',
                           'Sauron will not have forgotten the sword of Elendil. The blade that was broken shall return to minas Tirith.',
                           'Murderers. Traitors. You would call upon them to fight? They believe in nothing. They answer to no one.',
                           'If Sauron had the ring, we would know it!',
                           'No. There is still hope for Frodo. He needs time… and safe passage across the plains of Gorgoroth. We can give him that.',
                           'Draw out Sauron\'s armies. Empty his lands. Then we gather our full strength and march on the Black Gate!',
                           'Let the lord of the Black Lands come forth, that justice be done upon him!',
                           'We have time. Every day, Frodo moves closer to Mordor.',
                           'Then I shall die as one of them!',
                           'My lady, there may come a time for valor without renown. Who then will your people look to in the last defense?',
                           'You have some skill with a blade.',
                           'You are a daughter of kings, a shieldmaiden of Rohan. I do not think that will be your fate!',
                           'They do not come to destroy Rohan\'s crops or villages. They come to destroy its people. Down to the last child.',
                           'It\'s the beards.',
                           'Open war is upon you whether you would risk it or not.',
                           'Farmers, ferriers, stable boys. These are no soldiers.',
                           'It is an army bred for a single purpose, to destroy the world of men. They will be here by nightfall.',
                           'They were once men. Great kings of men. Then Sauron the Deceiver gave to them nine rings of power. Blinded by their greed, they took them without question, one by one falling into darkness. Now they are slaves to his will. They are the Nazgul, ringwraiths, neither living nor dead. At all times they feel the presence of the Ring, drawn to the power of the one. They will never stop hunting you.',
                           'You said you\'d bind yourself to me, forsaking the immortal life of your people.',
                           'Are you frightened?',
                           'I have seen the White City, long ago.',
                           'Frodo\'s fate is no longer in our hands.',
                           'A little more caution from you; that is no trinket you carry.',
                           'Indeed. I can avoid being seen if I wish, but to disappear entirely, that is a rare gift.',
                           'You cannot wield it. None of us can. The One Ring answers to Sauron alone. It has no other master.',
                           'The same blood flows in my veins. The same weakness.',
                           'I let Frodo go.',
                           'By nightfall these hills will be swarming with orcs! We must reach the woods of Lothlórien.',
                           'Boromir! Give the Ring to Frodo.',
                           'They will look for his coming from the White Tower. But he will not return.',
                           'Sam, do you know the Athelas plant?',
                           'I will not lead the Ring within a hundred leagues of your city.',
                           'He is passing into the Shadow World. He\'ll soon become a wraith like them.',
                           'Frodo, I have lived most of my life surrounded by my enemies. I will be grateful to die among my friends.',
                           'Why have you come?',
                           'Not for ourselves. But we can give Frodo his chance if we keep Sauron\'s Eye fixed upon us. Keep him blind to all else that moves.',
                           'You shall not enter the realm of Gondor.',
                           'I do not believe it! I will not!',
                           'I summon you to fulfill your oath.',
                           'It has been remade… fight for us, and regain your honor.',
                           'What does your heart tell you?',
                           'They have a better chance defending themselves here than at Edoras…',
                           'Then what do you fear, My Lady?',
                           'He\'s not alone. Sam went with him.',
                           'Not a word.',
                           'All Isengard is emptied.',
                           'Ten thousand strong at least.',
                           'It is an army bred for a single purpose, to destroy the world of men. They will be here by nightfall.',
                           'I will not lead the Ring within a hundred leagues of your city!',
                           'That is our road. I suggest you take some rest and recover your strength, Master Dwarf.',
                           'No. Orcs patrol the eastern shore. We must wait for cover of darkness.',
                           'We cross the lake at nightfall. Hide the boats and continue on foot. We approach Mordor from the north.',
                           'Gentlemen, we do not stop til nightfall.',
                           'Come on, come on! Take cover!',
                           'The mines are no place for a pony, even one so brave as Bill.',
                           'Get back! Stay close to Gandalf!',
                           'Haldir o Lórien. Henion aníron, boe ammen i dulu lîn. Boe ammen veriad lîn.',
                           'Frodo\'s fate is no longer in our hands.',
                           'Not idly do the leaves of Lorien fall',
                           'Rohan, home of the horse-lords.',
                           'There\'s something strange at work here. Some evil gives speed to these creatures, sets its will against us',
                           'Legolas! What do your elf-eyes see?',
                           'Riders of Rohan! What news from the Mark?',
                           'We are no spies. We track a band of Uruk-hai westward across the plains. They have taken two of our friends captive.',
                           'They will be small, only children to your eyes.',
                           'Tracks lead away from the battle, into… Fangorn Forest.',
                           'Do not let him speak. He will put a spell on us!',
                           'You fell!',
                           'No my lord! No my lord. Let him go. Enough blood has been spilt on his account.',
                           'You have 2000 good men riding north as we speak. Éomer is loyal to you. His men will return and fight for their king.',
                           'He’s only doing what he thinks is best for his people. Helm’s Deep has saved them in the past.',
                           'What do you fear, my lady?',
                           'King Théoden has a good memory. He was only a small child at the time.',
                           'She stays because she still has hope.',
                           'She is sailing to the Undying Lands with all that is left of her kin.',
                           'Send out riders, my lord. You must call for aid.', 'Gondor will answer.',
                           'Hurry! Inside. Get them inside!',
                           'You said this fortress would never fall while your men defend it. They still defend it. They have died defending it.',
                           'Is there no other way for the women and children to get out of the caves? Is there no other way?',
                           'For Rohan. For your people.',
                           'One thing I have learned about Hobbits: They’re a most hardy folk.',
                           'Will you ride with us?',
                           'Six thousand will not be enough to break the lines of Mordor.',
                           'Every hour lost hastens Gondor\'s defeat. We have till dawn, then we must ride.',
                           'It will not be our end, but his.',
                           'Not this time. This time you must stay, Gimli.',
                           'I do not fear death!',
                           'One who will have your allegiance.',
                           'You will suffer me.',
                           'I summon you to fulfill your oath.',
                           'I am Isildur\'s heir. Fight for me, and I will hold your oaths fulfilled!',
                           'What say you‽ You have my word! Fight, and I will release you from this living death! ...What say you‽',
                           'Legolas, fire a warning shot past the bosun\'s ear.',
                           'I hold your oath fulfilled. Go. Be at peace.',
                           'Not for ourselves. But we can give Frodo his chance if we keep Sauron\'s Eye fixed upon us. Keep him blind to all else that moves.',
                           'Long have you hunted me. Long have I eluded you. No more… Behold the Sword of Elendil!',
                           'I do not believe it. I will not.']
                reply = random.choice(choices)

        if reply and comment.author != reddit.user.me and comment.id not in replied_to:
            print("Got one!")

            try:
                comment.reply(reply)
            except:
                print("The show must go on…")

            replied_to.append(comment.id)
            with open("replied_to.txt", "a") as db:
                db.write(comment.id + "\n")
