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

    centered "{size=+6}{color=#d4a373}To be continued...{/color}{/size}"

    pause 1.5

    return
