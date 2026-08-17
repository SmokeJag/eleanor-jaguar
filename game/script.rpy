# -------------------------------------------------------------------------------------------
# ELEANOR: THE SHADOW OF THE JAGUAR
# The Aztec/jungle finale of the SmokeJaguar Trilogy
# SmokeJaguar Studios
# -------------------------------------------------------------------------------------------
#
# CHARACTER DEFINITIONS
# -------------------------------------------------------------------------------------------
define e = Character("Eleanor", color="#c8a2c8")
define n = Character("Neith", color="#e8d8e8")     # returns from the Scales of Ma'at
define t = Character("Tezcatlipoca", color="#d4a373")  # the smoking mirror
define j = Character("The Jaguar", color="#8fb3a8")    # the spirit guardian

# -------------------------------------------------------------------------------------------
# IMAGE ALIASES — Backgrounds (placeholders; replace with generated art)
# -------------------------------------------------------------------------------------------
image bg jungle = Solid("#1a3a1a")     # the overgrown jungle
image bg temple = Solid("#2a1a0a")     # the ruined temple
image bg mictlan = Solid("#1a0a2a")    # the Aztec underworld
image bg jaguar = Solid("#0a1a0a")     # the jaguar's chamber

# -------------------------------------------------------------------------------------------
# IMAGE ALIASES — Characters (placeholders)
# -------------------------------------------------------------------------------------------
image eleanor_neutral = Solid("#c8a2c8")
image eleanor_determined = Solid("#c8a2c8")
image neith_neutral = Solid("#e8d8e8")

# -------------------------------------------------------------------------------------------
# CUSTOM TRANSITIONS
# -------------------------------------------------------------------------------------------
define slow_dissolve = Dissolve(1.5)
define slow_fade = Fade(1.0, 0.5, 1.0)
define flash = Fade(0.1, 0.0, 0.5, color="#ffffff")

# -------------------------------------------------------------------------------------------
# GAME START — ACT 1: THE JUNGLE
# -------------------------------------------------------------------------------------------
label start:
    # Game State — the "source" mechanic
    $ jaguar_trust = 0
    $ bloodline_truth = False

    scene bg jungle
    with slow_fade

    "The jungle swallowed the sound of the river, and the river swallowed the sound of the world."

    "I had been in the green dark for three days, following a jade jaguar that was not a map, but a *memory*."

    show eleanor_neutral at left
    with dissolve

    e "Neith. Are you sure this is the place?"

    show neith_neutral at right
    with dissolve

    n "The pendant has not stopped humming since we crossed the mountains. Whatever the Thorne bloodline truly is, Eleanor—it is here."

    "She held up the jade jaguar. In the gloom, its eyes seemed to glow, watching the jungle as if it knew the way."

    e "And you've never been here before?"

    n "I have been *waiting* to come here for a century. The scales showed me the weight of the Thorne name. But the *source* of that weight—the first sin—was always hidden in the New World."

    "Ahead, the trees parted. And there, half-swallowed by vines and shadow, rose a temple of black stone, its steps climbing toward a sky that had no sun."

    e "The pyramid from the book."

    n "The pyramid from *before* the book. This is where it all began, Eleanor."

    "I felt the jade jaguar grow warm in Neith's hand. And somewhere deep in the temple, something answered."

    scene black
    with slow_fade

    centered "{size=+6}{color=#d4a373}ACT ONE — THE JAGUAR{/color}{/size}"

    pause 1.5

    # --- The descent into the jungle ---
    scene bg jungle
    with slow_fade

    "The jungle did not welcome us. It *watched* us."

    "Every step we took, the canopy above seemed to lean closer. The calls of birds had died an hour ago, and the silence that followed was the kind that pressed against the ears."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    e "Neith. The birds stopped."

    n "I know."

    "She did not slow. But I saw her hand tighten on the jade jaguar, and I saw the way her eyes moved—not ahead, but *around*, searching the green dark for something that did not want to be found."

    e "You're scared."

    n "I am *alert*. There is a difference."

    e "There isn't. Not out here."

    "She glanced at me, and for a moment the mask slipped. Under the calm, there was something raw—a fear she had carried for a century, and never once let show."

    n "I have walked the Duat, Eleanor. I have faced the Devourer. I have stood before the scales and watched hearts too heavy to be judged fall into the dark."

    n "But I have never been *hunted*."

    "The words hung in the wet air. And then, from the trees ahead, came a sound that was not a bird, and not a wind."

    "A low, guttural growl. Close. Too close."

    show eleanor_determined at left
    with dissolve

    e "Neith."

    n "I heard it."

    "We stood back to back in the green dark, the jade jaguar warm between us, and the jungle held its breath."

    "And then the growl came again—closer, and this time it was not alone."

    menu:
        "Stand your ground — face it together":
            $ jaguar_trust += 1
            "I did not run. I stepped forward, putting myself between Neith and the sound, and I drew the small blade I had carried from England."
            e "Whatever it is, it came for us. Let it come."
            "Neith moved to stand beside me, not behind me. Her hand found mine, and squeezed."
            n "Then we face it together."
            "The growl faltered. Whatever was out there, it had not expected two."

        "Pull Neith back — retreat to the river":
            "I grabbed Neith's arm and pulled her back toward the water, my heart hammering."
            e "We're not ready. We don't know what's out there."
            "She resisted for a moment, then let me pull her. But I saw the disappointment flicker across her face."
            n "Running from the dark, Eleanor? That is not the woman who unmade a Binding."
            "The growl followed us, patient, unhurried. It knew we would come back."

    # --- The temple ---
    "We broke through the treeline into a clearing, and the temple rose before us—black stone, swallowed by vines, its steps slick with a century of rain."

    "At its base, half-buried in the earth, lay a stone jaguar, its mouth open in a silent snarl."

    show neith_neutral at right

    n "The guardian. The first Thorne carved it, to mark the place where the bloodline began."

    e "And to warn people away."

    n "Both."

    "She knelt before the stone jaguar, and I saw her hand tremble as she reached out to touch it."

    n "Eleanor. There is something I have not told you."

    e "What?"

    n "The jade jaguar is not a relic. It is a *key*—and it was not made by the Thorne family."

    "She looked up at me, and in the green dark, her eyes were bright with a fear I had never seen in her."

    n "It was made by the thing the first Thorne made a bargain with. And it has been waiting, all these centuries, for a Thorne to bring it back."

    "The stone jaguar's eyes seemed to glow. And somewhere deep in the temple, something that had been waiting a very long time began to wake."

    scene black
    with slow_fade

    centered "{size=+6}{color=#d4a373}ACT TWO — THE DESCENT{/color}{/size}"

    pause 1.5

    # --- Entering the temple ---
    scene bg temple
    with slow_fade

    "The temple swallowed us whole."

    "The doorway was a mouth of black stone, and the moment we crossed it, the light of the jungle died behind us. The air turned cold and still, and the smell of the green gave way to something older—dust, and blood, and the faint, sweet rot of a thousand years."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    e "Neith. Light."

    "She struck a match. The flame guttered, then steadied, and in its small circle of light we saw the walls."

    "They were covered in carvings. Not the proud, ordered hieroglyphs of Egypt—these were frantic, gouged into the stone as if by a hand that had been in a hurry, or in terror."

    "Men and women, their faces twisted, their bodies bent. And above them all, a great jaguar, its jaws open, swallowing them one by one."

    n "The first Thorne did not carve these to honour the jaguar. He carved them to *remember* what he had done."

    e "What did he do?"

    "Neith was silent for a long moment. The match burned low, and she lit another."

    n "He made a bargain. The jaguar gave him power—wealth, longevity, a name that would outlast empires. In return, he fed it."

    e "Fed it what?"

    n "His blood. His children. And when his own blood ran thin, the blood of others."

    "The words fell into the cold dark like stones into a well. I felt the weight of them settle in my chest."

    e "And the bargain is still... active?"

    n "It is *hungry*, Eleanor. It has been waiting a very long time for a Thorne to come and honour the old debt."

    "I looked at the carvings again. The jaguar's jaws. The faces. And I understood, with a cold clarity, why the jade jaguar had grown warm in Neith's hand."

    e "You brought me here to feed it."

    "Neith went very still. When she turned to face me, her eyes were bright—not with fear, but with something harder."

    n "I brought you here to *end* it. The only way to break the bargain is for a Thorne to face the jaguar and refuse it. To stand before the hunger and say no."

    e "And if I can't?"

    n "Then it will take you, as it took every Thorne before you. And the bloodline will finally be complete."

    "The match died. In the dark, I felt her hand find mine."

    n "But you are not like them, Eleanor. You unmade a Binding. You faced the Devourer. You are the first Thorne in a thousand years who chose mercy over power."

    n "I believe in you. Even when you do not believe in yourself."

    "Her hand was warm in the cold. And for a moment, the dark did not seem so vast."

    e "Then let's go end it. Together."

    # --- The descent ---
    "We moved deeper into the temple, and the carvings grew worse."

    "The faces on the walls were no longer just carved—they were *real*. Pressed into the stone as if the people had been pushed through it, their mouths open in silent screams, their hands reaching out of the rock."

    show eleanor_determined at left

    e "Neith. These aren't carvings."

    n "No. They are the ones the jaguar fed on. Their souls are bound to the stone, Eleanor. They have been screaming for a thousand years, and no one has heard them."

    "I stopped. I could feel them—a pressure against my skin, a whisper at the edge of my hearing, a thousand voices all saying the same thing."

    "Help us. Help us. Help us."

    e "We can't leave them like this."

    n "We can't free them yet. Not until the bargain is broken. But when it is—"

    "She did not finish. A sound rose from the dark ahead of us. Not a growl this time. A *breath*. Slow, and deep, and patient."

    "Something was waiting for us in the heart of the temple."

    menu:
        "Press on — face what waits":
            $ jaguar_trust += 1
            "I did not hesitate. I walked toward the sound, and Neith walked beside me."
            e "Whatever it is, it has waited long enough. Let's not keep it waiting."
            "She smiled—a real smile, in the dark, and it was the warmest thing I had felt in days."

        "Pause — steady yourselves first":
            "I stopped, and took a breath. The dark pressed in, and I felt the weight of a thousand trapped souls on my shoulders."
            e "Neith. If this goes wrong—"
            n "It won't."
            e "But if it does. I want you to know—"
            "She silenced me with a look, and took my hand."
            n "I know, Eleanor. I know. And I am not going anywhere."

    "We walked on, into the breath, into the dark, and the temple closed around us like a fist."

    scene black
    with slow_fade

    centered "{size=+6}{color=#d4a373}To be continued...{/color}{/size}"

    pause 1.5

    return
