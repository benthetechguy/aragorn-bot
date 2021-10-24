# Original code from u/Aragorn-bot, will rewrite soon
# Shoutout to the u/Gandalf-bot for help on sentience!
# 3/18/20 Edit 1: Added more quotes
import praw
import yaml
import random
import time
import re
import os

with open('config.yaml', 'r') as config_file:
    config = yaml.load(config_file, Loader=yaml.BaseLoader)

def bot_login():
    r = praw.Reddit(username=config['username'],
                    password=config['password'],
                    client_id=config['client_id'],
                    client_secret=config['client_secret'],
                    user_agent=config['user_agent'])
    return r

# these are contain possiblkeywords. For simplicity sake I made the name of each string/variable thingy related, but all that matters is that the first step will look for a comment containing something inside my first variable/string thingy, which naturally is Aragorn, then afterwords it proceeds to look for any other words that should get a special phrase every time.
aragorn = ['Aragorn', 'aragorn']  # for example first look for Aragorn, aragorn
gondor_aragorn = ['Gondor', 'gondor', 'realm', 'white']
beacons = ['beacons', 'Beacons', ]
breakfast = ['breakfast', 'Breakfast', 'second',
             'Second']  # Nothing in LOTR was worse than the war of Aragorn vs Second Breakfast
Caradhras = ['Caradhras', 'caradhras', 'mountain', 'Mountain', 'Saruman']
Gate = ['Black', 'black', 'Gate', 'gate']
axe = ['Sword', 'sword']
hope = ['Hope', 'hope']
Strider = ['Strider', 'strider']
humor = ['Penis', 'penis', 'dick', 'Dick']
fellowship = ['fellowship has failed','it has been in vain', 'It has been in vain', 'Fellowship has failed']
men = ['The world of Men will fall', 'the world of Men will fall', 'The world of men will fall', 'the world of men will fall', 'all will come to darkness', 'my city to ruin', 'My city to ruin']
king = ['Now come the days of the king','now come the days of the king', 'now comes the days of the king', 'Now comes the days of the king']
anduril = ['Andúril, Flame of the West, forged from the shards of Narsil', 'forged from the shards of Narsil', 'Forged from the shards of Narsil', 'forged from the shards of Narsil']
mountain = ['There are those who dwell in the mountain', 'there are those who dwell in the mountain', 'dwell in the mountain']
renown = ['To mind the children, to find food and bedding when the men return. What renown is there in that?', 'To mind the children to find food and bedding when the men return. What renown is there in that?', 'What renown is there in that']
def run_bot(r, comment_replied_to):
    for comment in r.subreddit('lotrmemes').comments(limit=25):
        for keyword in aragorn:  # look first for Aragorn if found then look for the any of the following otherwise proceed to last phase, just Aragorn
            if keyword in comment.body and comment.id not in comment_replied_to and not comment.author == r.user.me:
                #When aragorn asked Lady Eowyn to go the caves with the ladies and the women
                for keyword in renown:
                    if re.search(r"\b(" + "|".join(renown) + r")\b",comment.body,re.IGNORECASE) and comment.id not in comment_replied_to and not comment.author == r.user.me:
                        print("renown")
                        comment.reply("My lady, a time may come for valor without renown. Who then will your people look to in the last defense?")
                        comment_replied_to.append(comment.id)
                        with open("comment_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")

                # this is for any thing related to gondor
                for keyword in gondor_aragorn:
                    if keyword in comment.body and comment.id not in comment_replied_to and not comment.author == r.user.me:
                        print("GONDOR")  # you can ignore this line it is for me
                        gondor = ['Stand your ground, sons of Gondor of Rohan my brothers. I see in your eyes the same fear that would take the heart of me! A day may come when the courage of men fails when we forsake our friends and break all bonds of fellowship but it is not this day! An hour of wolves and shattered shields when the age of men comes crashing down but it is not this day, this day we fight!!! And for all that is dear to you in this world I bid you stand men of the west and fight! ',
                            'Be at peace son of Gondor.',
                            'THE BEACONS OF MINAS TIRITH! THE BEACONS ARE LIT! GONDOR CALLS FOR AID!',
                            'You shall not enter the realm of Gondor.',
                            'I will not let the White city fall nor our people fail',
                            'There is no strength in Gondor that can avail us']  # these are the quotes that it will say when Gondor is found
                        random_item = random.choice(gondor)  # choose a random quote from the phrases
                        comment.reply(random_item)  # reply to the comment
                        comment_replied_to.append(comment.id)  # I'm going to be honest I have no idea what the following lines code do. All I know is without it the bot starts to spam
                        with open("comment_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")
                #for the ghost people
                for keyword in mountain:
                    if keyword in comment.body and comment.id not in comment_replied_to and not comment.author == r.user.me:
                        print("Oath breakers")
                        comment.reply("Murderers… traitors! You would call upon them to fight? They believe in nothing! They answer to no one!")
                        comment_replied_to.append(comment.id)
                        with open("comment_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")

                # regarding anduril
                for keyword in anduril:
                    if keyword in comment.body and comment.id not in comment_replied_to and not comment.author == r.user.me:
                        print("Elendil")
                        comment.reply("Sauron will not have forgotten the sword of Elendil. The blade that was broken shall return to minas Tirith.")
                        comment_replied_to.append(comment.id)
                        with open("comment_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")
                # for the days of the king
                for keyword in king:
                    if keyword in comment.body and comment.id not in comment_replied_to and not comment.author == r.user.me:
                        print("May they be blessed")
                        comment.reply("This day does not belong to one man but to all. Let us together rebuild this world, that we may share in the days of peace.")
                        comment_replied_to.append(comment.id)
                        with open("comment_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")

                # for the failing of the white city
                for keyword in men:
                    if keyword in comment.body and comment.id not in comment_replied_to and not comment.author == r.user.me:
                        print("White city")
                        comment.reply("I do not know what strength is in my blood, but I swear to you I will not let the White City fall, nor our people fail.")
                        comment_replied_to.append(comment.id)
                        with open("comment_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")

                # for anything related to the beacons of minas tirith
                for keyword in beacons:
                    if keyword in comment.body and comment.id not in comment_replied_to and not comment.author == r.user.me:
                        print("Gondor calls ")
                        comment.reply("THE BEACONS OF MINAS TIRITH! THE BEACONS ARE LIT! GONDOR CALLS FOR AID!")
                        comment_replied_to.append(comment.id)
                        with open("comment_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")
                #if the fellowship was in vain
                for keyword in fellowship:
                    if keyword in comment.body and comment.id not in comment_replied_to and not comment.author == r.user.me:
                        print("Nay Gimli")
                        comment.reply("Not if we hold true to each other. We will not abandon Merry and Pippin to torment and death. Not while we have strength left. Leave all that can be spared behind. We travel light. Let’s hunt some Orc.")
                        comment_replied_to.append(comment.id)
                        with open("comment_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")

                # for something related to the Fellowship's journey through the Caradharas
                for keyword in Caradhras:
                    if keyword in comment.body and comment.id not in comment_replied_to and not comment.author == r.user.me:
                        print("Saruman is bringing the mountain")
                        comment.reply("HES TRYING TO BRING DOWN THE MOUNTAIN! GANDALF WE MUST TURN BACK!")
                        comment_replied_to.append(comment.id)
                        with open("comment_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")
                # if someone mentions the second greatest speech (if you think that anything was better Theoden's you are no longer welcome
                for keyword in Gate:
                    if keyword in comment.body and comment.id not in comment_replied_to and not comment.author == r.user.me:
                        print("I came")
                        comment.reply(
                            "Hold your ground, hold your ground. Sons of Gondor, of Rohan my brothers. I see in your eyes the same fear that would take the heart of me. A day may come when the courage of men fails when we forsake our friends and break all bonds of fellowship but it is not this day. An hour of woes and shattered shields when the age of men comes crashing down but it is not this day. This day we fight! By all that you hold dear on this good earth I bid you stand, men of the west!")
                        comment_replied_to.append(comment.id)

                        with open("comment_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")
                # if a smartass mentions the greatest tragedy: the tragedy of second breakfast
                for keyword in breakfast:
                    if keyword in comment.body and comment.id not in comment_replied_to and not comment.author == r.user.me:
                        print("I dont think he knows about that")
                        comment.reply(comment.author.name + " " + "you've already had it")
                        comment_replied_to.append(comment.id)

                        with open("comment_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")
                # for hope of the fellowship winning
                for keyword in hope:
                    if keyword in comment.body and comment.id not in comment_replied_to and not comment.author == r.user.me:
                        print("Ring")
                        comment.reply(
                            "No. There is still hope for Frodo. He needs time... And safe passage across the plains of Gorgoroth. We can give him that.'")
                        comment_replied_to.append(comment.id)

                        with open("comment_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")
                # Gimli's axe is superior
                for keyword in axe:
                    if keyword in comment.body and comment.id not in comment_replied_to and not comment.author == r.user.me:
                        print("Gimli is a chad")
                        comment.reply(comment.author.name + " " + "you have my sword")
                        comment_replied_to.append(comment.id)

                        with open("comment_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")
                # If someone says Aragorn plus Strider

                # if some comedian says penis or dick
                for keyword in humor:
                    if keyword in comment.body and comment.id not in comment_replied_to and not comment.author == r.user.me:
                        print("Shlong")
                        comment.reply("You should be dead. That spear would have skewered a wild boar.")
                        comment_replied_to.append(comment.id)

                        with open("comment_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")
            # this is if no key phrases besides aragorn were found
            for keyword in aragorn:
                if keyword in comment.body and comment.id not in comment_replied_to and not comment.author == r.user.me:
                    print("Breakfast has been found")
                    list = ['I would have gone with you to the end into the very fires of Mordor.',
                            'Not if we hold true to each other.', 'I thought I had wandered into a dream.',
                            'I will not let the White city fall nor our people fail', 'FOR FRODO!!',
                            'I will not let the White city fall nor our people fail.',
                            '[Let us together rebuild this world that we may share in the days of peace.](https://www.youtube.com/watch?v=W6t9OF8_3n8)',
                            'The best revenge is letting go and living well.',
                            'Tis the lay of Luthien. The elf-maiden who gave her love to eren a mortal!',
                            'HES TRYING TO BRING DOWN THE MOUNTAIN! GANDALF WE MUST TURN BACK!',
                            'I swore to protect you.',
                            'If by my life or death I can protect you, I will. You have my sword.', 'You have my sword'
                                                                                                    'THE BEACONS OF MINAS TIRITH! THE BEACONS ARE LIT! GONDOR CALLS FOR AID!',
                            'It is but a shadow and a thought that you love. I cannot give you what you seek',
                            ' Sauron will not have forgotten the sword of Elendil. The blade that was broken shall return to minas Tirith.',
                            'Murderers. Traitors. You would call upon them to fight? They believe in nothing. They answer to no one.',
                            'If Sauron had the ring we would know it!',
                            'No. There is still hope for Frodo. He needs time... And safe passage across the plains of Gorgoroth. We can give him that.',
                            'Draw out Sauron\'s armies. Empty his lands. Then we gather our full strength and march on the Black Gate!',
                            'Hold your ground, hold your ground. Sons of Gondor, of Rohan my brothers. I see in your eyes the same fear that would take the heart of me. A day may come when the courage of men fails when we forsake our friends and break all bonds of fellowship but it is not this day. An hour of woes and shattered shields when the age of men comes crashing down but it is not this day. This day we fight! By all that you hold dear on this good earth I bid you stand, men of the west!',
                            'Let the lord of the Black Lands come forth, that justice be done upon him!',
                            ' We have time. Every day Frodo moves closer to Mordor.',
                            ' Then I shall die as one of them!',
                            'My lady, there may come a time for valor without renown. Who then will your people look to in the last defense?',
                            'You have some skill with a blade.',
                            'You are a daughter of kings a shieldmaiden of Rohan. I do not think that will be your fate!',
                            'They do not come to destroy Rohan\'s crops or villages. They come to destroy its people. Down to the last child.',
                            'Its the beards.',
                            'Open war is upon you whether you would risk it or not.',
                            'Farmers, ferriers, stable boys. These are no soldiers.',
                            ' It is an army bred for a single purpose, to destroy the world of men. They will be here by nightfall.',
                            'They were once men. Great kings of men. Then Sauron the Deceiver gave to them nine rings of power. Blinded by their greed, they took them without question, one by one falling into darkness. Now they are slaves to his will. They are the Nazgul, ringwraiths, neither living nor dead. At all times they feel the presence of the Ring, drawn to the power of the one. They will never stop hunting you.',
                            'You said you\'d bind yourself to me, forsaking the immortal life of your people.',
                            ' Are you frightened?', 'I have seen the White City, long ago',
                            'Frodos fate is no longer in our hands.',
                            'A little more caution from you; that is no trinket you carry',
                            'Indeed. I can avoid being seen if I wish, but to disappear entirely, that is a rare gift.',
                            'You cannot wield it. None of us can. The One Ring answers to Sauron alone. It has no other master.',
                            'The same blood flows in my veins. The same weakness.', 'I let Frodo go.',
                            ' By nightfall these hills will be swarming with orcs!... We must reach the woods of Lothlórien.',
                            'Boromir! Give the Ring to Frodo.',
                            'They will look for his coming from the White Tower. But he will not return.',
                            'Sam, do you know the Athelas plant?',
                            ' I will not lead the Ring within a hundred leagues of your city.',
                            '  You should be dead. That spear would have skewered a wild boar.',
                            'He is passing into the Shadow World. He\'ll soon become a wraith like them.',
                            'Frodo, I have lived most of my life surrounded by my enemies. I will be grateful to die among my friends.',
                            'Why have you come?',
                            'Not for ourselves. But we can give Frodo his chance if we keep Sauron\'s Eye fixed upon us. Keep him blind to all else that moves.',
                            'You shall not enter the realm of Gondor.', 'I do not believe it! I will not!',
                            'I summon you to fulfill your oath.',
                            ' It has been remade... Fight for us... and regain your honor.',
                            'What does your heart tell you?',
                            'They have a better chance defending themselves here than at Edoras...',
                            'Then what do you fear, My Lady?', 'He\'s not alone. Sam went with him.', 'Not a word.',
                            'All Isengard is emptied.', 'Ten thousand strong at least.',
                            'It is an army bred for a single purpose, to destroy the world of men. They will be here by nightfall.',
                            'They will look for his coming from the White Tower. But he will not return.',
                            ' Indeed. I can avoid being seen if I wish, but to disappear entirely, that is a rare gift.',
                            'There is no strength in Gondor that can avail us',
                            'I will not lead the Ring within a hundred leagues of your city!',
                            comment.author.name + "," + "  "'the Argonath! Long have I desired to look upon the kings of old... My kin',
                            ' That is our road. I suggest you take some rest and recover your strength, Master Dwarf',
                            'No. Orcs patrol the eastern shore. We must wait for cover of darkness.',
                            'We cross the lake at nightfall. Hide the boats and continue on foot. We approach Mordor from the north.',
                            'Gentlemen, we do not stop til nightfal',
                            'You said you\'d bind yourself to me. Forsaking the immortal life of your people.',
                            'Come on, come on! Take cover!', 'Boromir! Give the Ring to Frodo.',
                            ' The mines are no place for a pony, even one so brave as Bill.',
                            'Get back! Stay close to Gandalf!',
                            'Haldir o Lórien. Henion aníron, boe ammen i dulu lîn. Boe ammen veriad lîn.',
                            ' Frodo’s fate is no longer in our hands.', 'Not idly do the leaves of Lorien fall',
                            'Rohan, home of the horse-lords',
                            'There\'s something strange at work here. Some evil gives speed to these creatures, sets it\'s will against us',
                            'Legolas! What do your elf-eyes see?', 'Riders of Rohan! What news from the Mark?',
                            'We are no spies. We track a band of Uruk-hai westward across the plains. They have taken two of our friends captive.',
                            'They will be small, only children to your eyes',
                            'Tracks lead away from the battle, into...Fangorn Forest.',
                            'Do not let him speak. He will put a spell on us!', 'You fell!',
                            'No my lord! No my lord. Let him go. Enough blood has been spilt on his account.',
                            'You have 2000 good men riding north as we speak. Éomer is loyal to you. His men will return and fight for their king.',
                            'He’s only doing what he thinks is best for his people. Helm’s Deep has saved them in the past.',
                            'What do you fear my lady?',
                            'King Théoden has a good memory. He was only a small child at the time.',
                            'She stays because she still has hope.',
                            'She is sailing to the Undying Lands with all that is left of her kin.',
                            'Send out riders, my lord. You must call for aid.', 'Gondor will answer.',
                            'Hurry! Inside. Get them inside!',
                            ' You said this fortress would never fall while your men defend it. They still defend it. They have died defending it.',
                            'Is there no other way for the women and children to get out of the caves? Is there no other way?',
                            'For Rohan. For your people.',
                            'One thing I have learned about Hobbits: They’re a most hardy folk.',
                            'Will you ride with us?', 'Six thousand will not be enough to break the lines of Mordor.',
                            'Every hour lost hastens Gondor’s defeat. We have till dawn, then we must ride.',
                            'It will not be our end, but his.', 'Not this time. This time you must stay, Gimli.',
                            'I do not fear death!', 'One who will have your allegiance.', 'You will suffer me.',
                            'I summon you to fulfill your oath.',
                            'I am Isildur’s heir. Fight for me, and I will hold your oaths fulfilled!',
                            'What say you?! You have my word! Fight, and I will release you from this living death! ...What say you?!',
                            'Legolas, fire a warning shot past the bosun’s ear.',
                            ' I hold your oath fulfilled. Go. Be at peace.',
                            'Not for ourselves. But we can give Frodo his chance if we keep Sauron’s Eye fixed upon us. Keep him blind to all else that moves.',
                            ' Long have you hunted me. Long have I eluded you. No more...Behold the Sword of Elendil!',
                            ' I do not believe it. I will not.']  # I honestly don't know how many quotes there are here if you anyone wants to count feel free to do it and please let me know ]
                    random_item = random.choice(list)
                    comment.reply(random_item)
                    comment_replied_to.append(comment.id)

                    with open("comment_replied_to.txt", "a") as f:
                        f.write(comment.id + "\n")
        for keyword in Strider:
            if keyword in comment.body and comment.id not in comment_replied_to and comment.author not in comment_replied_to and comment.author != r.user.me():
                print("Fat man")
                comment.reply("'Strider' I am to one fat man who lives within a day's march of foes that would freeze his heart, or lay his little town in ruin, if he were not guarded ceaselessly.")
                comment_replied_to.append(comment.id)

                with open("comment_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")

    print("Sleep")


def get_saved_comments():
    if not os.path.isfile("comment_replied_to.txt"):
        comment_replied_to = []
    else:
        with open("comment_replied_to.txt", "r") as f:
            comment_replied_to = f.read()
            comment_replied_to = comment_replied_to.split("\n")
    return comment_replied_to


r = bot_login()
comment_replied_to = get_saved_comments()
while True:
    run_bot(r, comment_replied_to)
