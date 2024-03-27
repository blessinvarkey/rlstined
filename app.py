import streamlit as st
# Initialize 'current_node' in session_state if it doesn't exist

if 'current_node' not in st.session_state:
    st.session_state['current_node'] = '0'

def display_story_node(node_id):
    # Story content for the "Shadow Over Bhangarh" game.
    story_content = {
        '0': {
            'text': 'Welcome to the town of Bhangarh, where legends whisper and shadows linger. Will you brave the secrets of the past, or will the mysteries of Bhangarh consume you?',
            'choices': [('Let\'s begin!', '1')],
            'image': 'intro.jpeg'
        },
        '1': {
            'text': 'You are a tween who recently moved to the mysterious town of Bhangarh. You have joined the new school and lived in the town for a week now. The neighbours and school children started sharing rumors of your attic being haunted, you decide to:',
            'choices': [('Explore the attic.', '1A'), ('Forget about it and go to school the next day.', '1B')],
            'image': 'image0.jpeg'
        },
        '1A': {
            'text': 'In the attic, you find an old diary and a strange shadowy corner. Do you:',
            'choices': [('Spot a strange shadow in the corner.', '2AA'),
                        ('Spot an ancient chest.', '2AB')],
            'image': 'image1A.jpeg'
        },
        '1B': {
            'text': 'At school, whispers about the "Bhangarh Shadows" that live in your attic reach your ears. Do you:',
            'choices': [('Ignore the whispers and go about your day.', '2BA'),
                        ('Ask your new friend Jay about the "Bhangarh Shadows."', '2BB')],
            'image': 'image1B.jpeg'
        },
        '2AA': {
            'text': 'The shadow moves! It seems to want to communicate. Do you:',
            'choices': [('Flee from the attic.', '3AAA'), ('Stay and communicate with the shadow.', '3AAB')],
            'image': 'image2AA.jpeg'
        },

      #### New section added here:
        '3AAA': {
            'text': 'While fleeing you see the shadow begin forming the words in the air, "Help... Curse..." It leads you to a hidden part of the attic. Do you:',
            'choices': [('Follow the shadow\'s guidance.', '4AAA'),
                        ('Ignore the shadow and explore another part of the attic.', '4AAB')],
            'image': 'image3AAA.jpeg'
        },
        '4AAA': {
            'text': 'The shadow leads you to a wall that doesn’t seem to belong. You discover a loose brick and behind it, a small, ornate key with a skull design. Do you:',
            'choices': [('Take the key and find the lock and the door it fits.', '3AB6'),
                        ('Leave the key and turn around.', '5AAC')],
            'image': 'image4AAA.jpeg'},

       '5AAC': {
            'text': 'A shadow, emerges. It accuses you of trespassing into the attic. Do you:' ,
             'choices': [('Plead for forgiveness.', '6AAE'),
                     ('Challenge the shadow.', '6AAF')],
            'image': 'image5AAC.jpeg'
         },
      '6AAE': {
        'text': 'The shadow shows you a mirror. Asks you to break it.',
        'choices': [('Break the mirror instantly.', 'End_Bad_2'), ('Look inside the mirror and you see your reflection.', '3AB5')],
        'image': 'image6AAE.jpeg'
      },
      '6AAF': {
          'text': 'Your challenge incites the guardian\'s fury.It attacks, but in the struggle, a hidden compartment opens, revealing a crystal that shines with pure light.Grabbing it, you banish the guardian and the shadows, but the house collapses around you.Trapped in the rubble, your last sight is the crystal\'s fading glow. The end.',
      'choices': [],
      'image': 'image6AAF.jpeg'
      },
      '6AAG': {
          'text': 'Descending into the darkness, you find yourself in a room filled with ancient artifacts. Among them, a mirror shows not your reflection, but a scene of Bhangarh in ruins. Suddenly, the mirror cracks, and the curse of ruin spreads to the town. You\'ve unleashed an ancient evil.The end.',
           'choices': [],
          'image': 'image6AAG.jpeg'
      },
      '6AAH': {
          'text': 'Choosing not to descend, you search for more clues. In a hidden drawer, you find a letter admitting remorse for summoning the curse. It provides instructions for a ritual to end it. As you begin the ritual, the shadows converge on you, desperate to stop you. The ritual completes, but at a great cost - your life is forfeit, yet Bhangarh is saved. The end.',
          'choices': [],
          'image': 'image6AAH.jpeg'
      },
  
      ### end of the new section
          '2AB': {
              'text': 'Inside the chest, you find a mysterious mirror. Do you:',
              'choices': [('Take the mirror.', '3AB1'),
                          ('Leave everything untouched and investigate the diary further.', '3ABB')],
              'image': 'image2AB.jpeg'
          },
          '2BA': {
              'text': 'After school, you ponder your next move. Do you:',
              'choices': [('Research the history of your house.', '3BAA'),
                          ('Visit Jay to learn more about the legend.', '3BAB')],
              'image': 'image2BA.jpeg'
          },
          '2BB': {
              'text': 'Jay feels that its probably just a play of curtains. Do you:',
              'choices': [('Plan a visit to the attic by yourself based on Jay\'s feelings.', '1A'),
                          ('Decide to take Jay along.', '3ABB2')],
              'image': 'image2BB.jpeg'
          },
          '3AB1': {
              'text': 'With the mysterious mirror in hand, you feel its power pulsating. What do you do next?',
              'choices': [('Study the mirror\'s origins.', '3AB2'),
                          ('Communicate with the mirror.', '3AB3'),
                          ('Investigate why your reflection is acting on its own.', '3AB5'),
                          ('Search the house based on the spirit\'s clue.', '3AB44')],
              'image': 'image3AB1.jpeg'
          },
          '3AB44': {
              'text': 'The spirit\'s clue leads you to a forgotten part of the house, where the air feels charged with a mysterious energy. You stand before a door barely hanging on its hinges, beyond which lies the unknown. Do you dare to enter?',
              'choices': [('Enter the mysterious room.', '3AB6'),
                          ('Look for another way around.', '3AB7')],
              'image': 'image3AB4.jpeg'
          },
          '3AB6': {
              'text': 'Inside, the room is shrouded in darkness. As your eyes adjust, you notice strange symbols etched into the walls, glowing faintly. In the center, a book rests on a pedestal, seemingly inviting you to read it.',
              'choices': [('Read the book.', '3AB8'),
                          ('Examine the symbols on the walls.', '3AB9')],
              'image': 'image3AB6.jpeg'
          },
          '3AB7': {
              'text': 'Circling the house, you find a window looking into the mysterious room. Through it, you see the room is filled with artifacts and relics, each potentially holding answers or more questions.',
              'choices': [('Enter through the window.', '3AB6'),
                          ('Return to the door and enter.', '3AB6')],
              'image': 'image3AB7.jpeg'
          },
          '3AB8': {
              'text': 'The book, bound in unfamiliar material, whispers secrets of the past as you flip through its pages. It tells the story of the original occupant of the house, a sorcerer who battled the Bhangarh Shadow.',
              'choices': [('The book asks you to read out a spell ', '3AB14'),
                          ('Go on the last page to find the name of the sorcerer', '3AB11')],
              'image': 'image3AB8.jpeg'
          },
  
          '3AB9': {
              'text': 'The symbols are ancient runes used in warding magic. They speak of a ritual to protect against darkness. A piece of parchment lies on the floor, offering instructions for a protective circle.',
              'choices': [('Attempt the ritual.', '3AB12'),
                          ('Ignore the ritual and keep exploring.', '3AB13')],
              'image': 'image3AB9.jpeg'
          },
  
  # END?
          '3AB10': {
              'text': 'Armed with knowledge from the book, you prepare to cast the spell. The air thickens, and shadows in the room begin to swirl menacingly. It\'s now or never.',
              'choices': [('Cast the spell.', '3AB14'),
                          ('Hesitate and reconsider.', '3AB15')],
              'image': 'image3AB10.jpeg'
          },
  
  
          '3ABB': {
              'text': 'You decide to meet your friend Jay.',
              'choices': [('Call him.', '3ABB1'),
                          ('Meet him.', '3ABB1')],
              'image': 'image3AB11.jpeg'
          },
          '3ABB1': {
              'text': 'As he was unavailable, you decide to meet him at school the next day',
              'choices': [('Ask Jay about legend behind your house.', '3ABB2'),
                          ('Ask Jay to check out his attic someday.', '3ABB2')],
              'image': 'image3AB12.jpeg'
          },
  
          '3ABB2': {
              'text': 'Jay decides to join you on your quest. He goes to the attic and finds a mirror.',
              'choices': [('Jay sees his reflection.', '3AB55'),
                          ('Jay breaks the mirror.', 'End_Bad_2')],
              'image': 'image3AB12.jpeg'
          },
  
          '3AB13': {
              'text': 'Choosing to ignore the ritual, you continue to explore the room, discovering a series of personal belongings that once belonged to the sorcerer, each holding a story of loss and hope.',
              'choices': [('Reflect on the sorcerer\'s journey.', '3AB20'),
                          ('Keep searching for something to use against the Shadow.', '3AB21')],
              'image': 'image3AB13.jpeg'
          },
  
          '3AB14': {
              'text': 'As you cast the spell, the shadows scream in agony, swirling into a vortex before disappearing. The house instantly feels lighter, free of the oppressive darkness that had lurked in every corner.',
              'choices': [('You shut the book.', 'GoodEnding'), ('You leave the book open', 'BADENDING')],
              'image': 'image3AB14.jpeg'
          },
          '3AB15': {
              'text': 'Your hesitation costs you dearly. The shadows sense your fear, converging into a solid form that envelops you. As everything goes dark, you realize you\'ve become part of the house\'s haunted legacy.',
              'choices': [],  # No choices, this is an ending.
              'image': 'image3AB15.jpeg'
          },
          '3AB16': {
              'text': 'The artifact, a crystal pulsating with light, sits hidden in a wall cavity. As you touch it, the house shakes violently, and the Shadow appears, furious at being challenged.',
              'choices': [('Use the crystal against the Shadow.', '3AB14'),
                          ('Try to bargain with the Shadow.', '3AB22')],
              'image': 'image3AB16.jpeg'
          },
          '3AB17': {
              'text': 'Using the diary\'s knowledge, you understand the Shadow was once a protector of the house, corrupted by dark magic. Sympathy and understanding form your plan of action.',
              'choices': [('Attempt to purify the Shadow.', '3AB23'),
                          ('Strengthen the house\'s wards to contain it.', '3AB24')],
              'image': 'image3AB17.jpeg'
          },
          '3AB18': {
              'text': 'With the room now safe, you find a collection of magical tools and books, a legacy of a long-forgotten battle against darkness. Among them, a letter addressed to the future protector of the house - you.',
              'choices': [('Accept your role as the protector.', 'GoodEnding')],
              'image': 'image3AB18.jpeg'
          },
          '3AB19': {
              'text': 'Breaking the circle, the shadows return, more menacing than before. They form into hands that drag you into the darkness. Your last thought is a wish to have never broken the protective circle.',
              'choices': [],  # No choices, this is an ending.
              'image': 'image3AB19.jpeg'
          },
          '3AB20': {
              'text': 'Reflection brings understanding. The sorcerer fought not for power, but love - to save Bhangarh from the Shadow. Inspired, you vow to finish their work, feeling the weight of history on your shoulders.',
              'choices': [('Seek a way to banish the Shadow forever.', '3AB23')],
              'image': 'image0.jpeg'
          },
          '3AB21': {
              'text': 'Your search uncovers nothing more than trinkets and baubles, powerless against the dark forces at play. The real weapon, it seems, was within you all along - courage and the will to fight.',
              'choices': [('Confront the Shadow with newfound resolve.', '3AB14')],
              'image': 'image0.jpeg'
          },
          '3AB22': {
              'text': 'The Shadow cannot be bargained with. It seeks only to consume and destroy. Your attempt to negotiate shows weakness, and it strikes swiftly, engulfing you in darkness.',
              'choices': [],  # No choices, this is an ending.
              'image': 'image0.jpeg'
          },
          '3AB23': {
              'text': 'Through an ancient ritual, you attempt to purify the Shadow. As it screams in torment, a figure emerges - the sorcerer, freed at last. He thanks you before vanishing into the light, leaving the house truly protected.',
              'choices': [('Live in the house, now a beacon of light.', 'GoodEnding')],
              'image': 'image3AB23.jpeg'
          },
          '3AB24': {
              'text': 'Strengthening the wards only angers the Shadow further. It breaks through your defenses, consuming everything in its path. Bhangarh is lost to darkness, and you with it.',
              'choices': [],  # No choices, this is an ending.
              'image': 'image0.jpeg'
          },
          'GoodEnding': {
              'text': 'The house, once a place of darkness, now shines as a beacon of hope in Bhangarh. You, its protector, have not only saved the town but also reclaimed its legacy. The Shadow Over Bhangarh is no more',
              'choices': [],  # No choices, this is an ending.
              'image': 'bestcase.jpeg'
          },
  
              #---
          '3AB2': {
              'text': 'Your research uncovers the mirror\'s cursed nature, trapping souls. You:',
              'choices': [('Seek a way to break the curse.', 'End_Good'),
                          ('Break the mirror.', 'End_Bad_2')],
              'image': 'image3AB2.jpeg'
          },
  
          '3AB3': {
              'text': 'The mirror begins to communicate, warning of the shadow\'s intentions. You:',
              'choices': [('Shows you the spot of a loose brick.', '4AAA'),
                          ('You see your reflection in the mirror.', '3AB5')],
              'image': 'image3AB3.jpeg'
          },
          '3AB4': {
              'text': 'Your reflection no longer mimics you perfectly. It seems to have its own will. You:',
              'choices': [('Investigate the anomaly further.', 'End_Good'),
                          ('Cover the mirror, hoping to stop it.', 'End_Bad_4')],
              'image': 'image3AB4.jpeg'
          },
          '3AB5': {
              'text': 'The doppelgänger created by the mirror steps out and replaces you. Trapped in the mirror, you watch helplessly as it takes over your life.',
              'choices': [],  # End of path, no further choices
              'image': 'image3AB5.jpeg'
          },
  
          '3AB55': {
              'text': 'The doppelgänger created by the mirror steps out and replaces Jay. The new Jay pushes you down the stairs and the real Jay watchs helplessly from the mirror.',
              'choices': [],  # End of path, no further choices
              'image': 'image3AB5.jpeg'
          },
  
          'End_Good': {
              'text': 'Using the knowledge and artifacts you\'ve gathered, you manage to break the curse. The spirits are freed, and peace returns to your home.',
              'choices': [],  # End of path, no further choices
              'image': 'image_end_good.jpeg'
          },
          'End_Bad_2': {
              'text': 'In your attempt to break the mirror, shadows come out of the mirror and get aggressive, eventually consuming the entire house in darkness, trapping you in a world devoid of light. The End.',
              'choices': [],  # End of path, no further choices
              'image': 'image_end_bad_2.jpeg'
          },
          'End_Bad_3': {
              'text': 'Ignoring the mirror\'s warning, you find yourself facing the wrath of the shadow directly. It envelops you, and you become another lost soul trapped within the mirror, your face forever etched in its glass, warning future owners.',
              'choices': [],  # End of path, no further choices
              'image': 'image_end_bad_3.jpeg'
          },
          'End_Bad_4': {
              'text': 'Covering the mirror does little to contain its malevolence. One night, the cover falls away, and the shadow steps out into your world, replacing you. Your existence is erased as if you were never there, and the doppelgänger takes your place, leaving you trapped in the shadow realm.',
              'choices': [],  # End of path, no further choices
              'image': 'image_end_bad_4.jpeg'
          },
    }

    node = story_content.get(node_id)
    if node:
        st.image(node['image'], caption=None, width=500)  # Display the image
        st.write(node['text'])

        for choice_text, next_node in node['choices']:
            if st.button(choice_text):
                st.session_state['current_node'] = next_node  # Update the current node in session state
                break  # Break to only allow one choice to be made
    else:
        st.write("The story node is missing or the story has ended. Choose a new path or restart the game.")

# Initial call to start or continue the story based on the current node in the session state
display_story_node(st.session_state['current_node'])