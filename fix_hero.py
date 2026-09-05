import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the chicken image from the hero
old_composition = '''<!-- Base Bowl (Using user's paneer image mapped to a circle) -->
                        <img src="paneer_lababdar.jpg" alt="Royal Bowl" class="base-bowl border-4 border-gold/50 cinematic-img object-cover aspect-square">
                        
                        <!-- Splash/Falling Item (Using user's chicken leg image) -->
                        <img src="chicken_leg.jpg" alt="Falling Splash" class="splash-item cinematic-img rounded-full border-2 border-gold/30">'''

new_composition = '''<!-- Base Bowl (Using user's paneer image mapped to a circle) -->
                        <img src="paneer_lababdar.jpg" alt="Royal Bowl" class="w-[80%] max-w-[400px] h-auto rounded-full border-4 border-gold/50 cinematic-img object-cover aspect-square mx-auto shadow-[0_30px_60px_rgba(0,0,0,0.8)]">'''

# I also need to remove the .base-bowl and .splash-item classes because I'm replacing them with inline tailwind classes for the single image.
content = content.replace(old_composition, new_composition)

# Let's clean up the floating badge text
content = content.replace('Shahi Paneer Lababdar<br>& Royal Splash', 'Shahi Paneer Lababdar')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
