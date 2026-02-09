import random
from art import STAGES_HANGMAN, HANGMAN

word_list = ['ash','','abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon','banjo','bayou','beekeeper','bikini','blitz','blizzard','boggle','bookworm','boxcar','boxful','buckaroo','buffalo','buffoon','buxom','buzzard','buzzing','buzzwords','caliph','cobweb','cockiness','croquet','crypt','curacao','cycle','daiquiri','dirndl','disavow','dizzying','duplex','dwarves','embezzle','equip','espionage','euouae','exodus','faking','fishhook','fixable','fjord','flapjack','flopping','fluffiness','flyby','foxglove','frazzled','frizzled','fuchsia','funny','gabby','galaxy','galvanize','gazebo','giaour','gizmo','glowworm','glyph','gnarly','gnostic','gossip','grogginess','haiku','haphazard','hyphen','iatrogenic','icebox','injury','ivory','ivy','jackpot','jaundice','jawbreaker','jaywalk','jazziest','jazzy','jelly','jigsaw','jinx','jiujitsu','jockey','jogging','joking','jovial','joyful','juicy','jukebox','jumbo','kayak','kazoo','keyhole','khaki','kilobyte','kiosk','kitsch','kiwifruit','klutz','knapsack','larynx','length','lucky','luxury','lymph','marquis','matrix','megahertz','microwave','mnemonic','mystify','naphtha','nightclub','nowadays','numbskull','nymph','onyx','ovary','oxidize','oxygen','pajama','peekaboo','phlegm','pixel','pizazz','pneumonia','polka','pshaw','psyche','puppy','puzzling','quartz','queue','quips','quixotic','quiz','quizzes','quorum','razzmatazz','rhubarb','rhythm','rickshaw','schnapps','scratch','shiv','snazzy', 'sphinx','spritz','squawk','staff','strength','strengths','stretch','stronghold','stymied','subway','swivel','syndrome','thriftless','thumbscrew','topaz','transcript','transgress','transplant','triphthong','twelfth','twelfths','unknown','unworthy','unzip','uptown','vaporize','vixen','vodka','voodoo','vortex','voyeurism','walkway','waltz','wave','wavy','waxy','wellspring','wheezy','whiskey','whizzing','whomever','wimpy','witchcraft','wizard','woozy','wristwatch','wyvern','xylophone','yachtsman','yippee','yoked','youthful','yummy','zephyr','zigzag','zigzagging','zilch','zipper','zodiac','zombie']

#printing logo
print(HANGMAN)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
    print("_",end=" ")
print("\n")

  
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f"You have already guessed the letter {guess}.")
    else:
      
        for position in range(word_length):
            letter = chosen_word[position]
          
            if letter == guess:
                display[position] = letter

    #Check if user is wrong.
        if guess not in chosen_word:
            print(f"The chosen letter {guess} is not in the word.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
        else:
            print(f"The choosen letter {guess} is in the name")
    #Joining all the elements in the list and turning it into a String.
        print(f"{' '.join(display)}")
        

    #Checking if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")
          

        print(STAGES_HANGMAN[lives])