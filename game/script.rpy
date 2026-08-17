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

    "To be continued..."

    return
