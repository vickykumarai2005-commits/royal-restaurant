import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update background and panel colors in tailwind config to be rich deep maroon
old_colors = """
                    colors: {
                        darkBase: '#0a0806',
                        darkPanel: '#14100c',
                        primaryRed: '#5c0f0f',
                        gold: '#C5A059',
                        goldLight: '#E8D099',
                        goldDark: '#8A6D3B',
                        textCream: '#FDFBF7',
                        textMuted: '#A9A39A',
                    },
"""
new_colors = """
                    colors: {
                        darkBase: '#1c0505',
                        darkPanel: '#2b0a0a',
                        primaryRed: '#8b0000',
                        gold: '#d4af37',
                        goldLight: '#f3e5ab',
                        goldDark: '#aa7c11',
                        textCream: '#ffffff',
                        textMuted: '#e0c097',
                    },
"""
content = content.replace(old_colors, new_colors)

# 2. Fix image filters that made it look "fika" (dull)
old_filter = """
        /* Cinematic Color Grading over images */
        .cinematic-img {
            filter: contrast(1.15) saturate(1.2) brightness(0.9) sepia(0.2);
            mix-blend-mode: luminosity;
            transition: all 0.7s ease;
        }
        .cinematic-img:hover {
            filter: contrast(1.2) saturate(1.4) brightness(1.1) sepia(0.1);
            mix-blend-mode: normal;
        }
"""
new_filter = """
        /* Vibrant Royal Color Grading over images */
        .cinematic-img {
            filter: contrast(1.1) saturate(1.3) brightness(1.05);
            transition: all 0.5s ease;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }
        .cinematic-img:hover {
            filter: contrast(1.15) saturate(1.5) brightness(1.15);
            transform: scale(1.05);
        }
"""
content = content.replace(old_filter, new_filter)

# 3. Fix background CSS for the pattern to match new darkBase
old_body = "background-color: #0a0806;"
new_body = "background-color: #1c0505;"
content = content.replace(old_body, new_body)
content = content.replace("rgba(10,8,6,1)", "rgba(28,5,5,1)")
content = content.replace("rgba(10, 8, 6, 0.95)", "rgba(28, 5, 5, 0.95)")
content = content.replace("rgba(10, 8, 6, 0.8)", "rgba(28, 5, 5, 0.8)")
content = content.replace("background-image: url(\"data:image/svg+xml,%3Csvg width='100'", "background-image: url(\"data:image/svg+xml,%3Csvg width='100'")
content = content.replace("fill='%23C5A059'", "fill='%23d4af37'")

# 4. Remove mix-blend-overlay on the hero background image which makes it dull
content = content.replace("mix-blend-overlay", "mix-blend-multiply opacity-40")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
