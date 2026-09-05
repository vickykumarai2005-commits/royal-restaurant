import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Tailwind Config
new_tailwind = """
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: '#3b0909',
                        primaryLight: '#5c0f0f',
                        gold: '#C5A059',
                        goldLight: '#E8D099',
                        cream: '#FDFBF7',
                        darkbrown: '#1A120B',
                        accentGreen: '#2E7D32',
                    },
                    fontFamily: {
                        serif: ['"Playfair Display"', 'serif'],
                        sans: ['"Inter"', 'sans-serif'],
                        hindi: ['"Yatra One"', 'system-ui'],
                    }
                }
            }
        }
"""
content = re.sub(r'tailwind\.config\s*=\s*\{.*?\}\s*\}', new_tailwind.strip(), content, flags=re.DOTALL)

# 2. Add Royal Pattern CSS and modify body
royal_css = """
        .royal-pattern {
            background-color: #FDFBF7;
            background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23c5a059' fill-opacity='0.08'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
        }
"""
content = content.replace('.pb-safe {', royal_css + '\n        .pb-safe {')
content = content.replace('bg-cream text-darkbrown', 'royal-pattern text-darkbrown')

# 3. Update Hero Section
old_hero_text = '''<h1 class="text-5xl sm:text-6xl lg:text-7xl font-serif font-extrabold text-primary mb-3 leading-tight">
                        Royal Taste, <br>
                        <span class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-primaryLight">Desi Heart.</span>
                    </h1>'''
new_hero_text = '''<h1 class="text-5xl sm:text-6xl lg:text-7xl font-serif font-extrabold text-primary mb-3 leading-tight drop-shadow-sm">
                        A Feast for the <br>
                        <span class="text-transparent bg-clip-text bg-gradient-to-r from-gold to-yellow-600">Maharajas.</span>
                    </h1>'''
content = content.replace(old_hero_text, new_hero_text)

old_hero_p = 'Experience the magical 3D taste of authentic Indian, Mughlai & Chinese specialties — freshly prepared for you.'
new_hero_p = 'Step into the era of kings. Experience authentic Shahi Mughlai and Royal Indian delicacies served with unparalleled luxury and modern elegance.'
content = content.replace(old_hero_p, new_hero_p)

# 4. Update Hero Image
old_hero_images = '''<img src="https://images.unsplash.com/photo-1596797038530-2c107229654b?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Bowl" class="w-full h-full object-cover bowl-base border-[12px] border-white">
                        <img src="https://images.unsplash.com/photo-1585937421612-70a008356fbe?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Paneer Pop" class="food-pop rounded-full object-cover shadow-[0_30px_40px_rgba(0,0,0,0.4)] border-4 border-gold group-hover:scale-125 transition-transform duration-700">'''

new_hero_images = '''<img src="paneer_lababdar.jpg" alt="Sahi Katore Paneer" class="w-full h-full object-cover bowl-base border-[8px] border-gold shadow-[0_0_40px_rgba(197,160,89,0.5)]">
                        <img src="chicken_leg.jpg" alt="Falling Chicken Splash" class="food-pop rounded-full object-cover shadow-[0_30px_40px_rgba(0,0,0,0.5)] border-[6px] border-gold group-hover:scale-110 transition-transform duration-700" style="width:70%; height:70%; left:15%; top:-10%;">'''
content = content.replace(old_hero_images, new_hero_images)

content = content.replace('Special Paneer Lababdar', 'Shahi Paneer Lababdar & Murgh Splash')
content = content.replace("Chef's Signature", "The King's Choice")

# 5. Add more menu items
new_menu_items = """
                <!-- Shahi Tukda -->
                <div class="menu-item menu-card bg-white rounded-3xl p-5 border border-gold/30 relative group cursor-pointer shadow-[0_4px_20px_rgba(197,160,89,0.15)]" data-category="dessert veg">
                    <div class="absolute top-5 left-5 z-10 bg-pink-50 border border-pink-200 px-2 py-1 rounded shadow-sm text-[10px] font-bold text-pink-600">ROYAL SWEET</div>
                    <div class="h-40 w-40 mx-auto mb-4 relative">
                        <div class="absolute inset-4 bg-gray-200 rounded-full shadow-inner opacity-50"></div>
                        <img src="https://images.unsplash.com/photo-1630175860333-5131bda75071?auto=format&fit=crop&w=400&q=80" alt="Shahi Tukda" class="w-full h-full object-cover rounded-full dish-img relative z-10 shadow-xl border-4 border-gold/50">
                    </div>
                    <div class="text-center">
                        <h3 class="text-xl font-bold text-primary mb-1 font-serif">Shahi Tukda</h3>
                        <p class="text-xs text-gray-500 mb-4 h-8">Rich bread pudding with rabri and dry fruits.</p>
                        <div class="flex justify-between items-center bg-cream px-4 py-2.5 rounded-2xl border border-gold/20">
                            <span class="text-lg font-bold text-darkbrown">₹149</span>
                            <button class="add-to-cart-btn bg-gold text-white w-8 h-8 rounded-lg flex items-center justify-center hover:bg-yellow-600 transition-colors shadow-md text-sm"><i class="fa-solid fa-plus"></i></button>
                        </div>
                    </div>
                </div>

                <!-- Navratan Korma -->
                <div class="menu-item menu-card bg-white rounded-3xl p-5 border border-gold/30 relative group cursor-pointer shadow-[0_4px_20px_rgba(197,160,89,0.15)]" data-category="veg mughlai">
                    <div class="absolute top-5 left-5 z-10 bg-green-50 border border-green-200 p-1.5 rounded-full shadow-sm"><div class="w-2.5 h-2.5 bg-accentGreen rounded-full"></div></div>
                    <div class="h-40 w-40 mx-auto mb-4 relative">
                        <div class="absolute inset-4 bg-gray-200 rounded-full shadow-inner opacity-50"></div>
                        <img src="https://images.unsplash.com/photo-1543826173-70651703c5a4?auto=format&fit=crop&w=400&q=80" alt="Navratan Korma" class="w-full h-full object-cover rounded-full dish-img relative z-10 shadow-xl border-4 border-gold/50">
                    </div>
                    <div class="text-center">
                        <h3 class="text-xl font-bold text-primary mb-1 font-serif">Navratan Korma</h3>
                        <p class="text-xs text-gray-500 mb-4 h-8">Nine-gem curry cooked in royal cashew gravy.</p>
                        <div class="flex justify-between items-center bg-cream px-4 py-2.5 rounded-2xl border border-gold/20">
                            <span class="text-lg font-bold text-darkbrown">₹279</span>
                            <button class="add-to-cart-btn bg-gold text-white w-8 h-8 rounded-lg flex items-center justify-center hover:bg-yellow-600 transition-colors shadow-md text-sm"><i class="fa-solid fa-plus"></i></button>
                        </div>
                    </div>
                </div>

                <!-- Murgh Musallam -->
                <div class="menu-item menu-card bg-white rounded-3xl p-5 border border-gold/30 relative group cursor-pointer shadow-[0_4px_20px_rgba(197,160,89,0.15)]" data-category="nonveg mughlai">
                    <div class="absolute top-5 left-5 z-10 bg-red-50 border border-red-200 p-1.5 rounded-full shadow-sm"><div class="w-2.5 h-2.5 bg-red-600 rounded-full"></div></div>
                    <div class="h-40 w-40 mx-auto mb-4 relative">
                        <div class="absolute inset-4 bg-gray-200 rounded-full shadow-inner opacity-50"></div>
                        <img src="https://images.unsplash.com/photo-1626509647209-409df2ab69fa?auto=format&fit=crop&w=400&q=80" alt="Murgh Musallam" class="w-full h-full object-cover rounded-full dish-img relative z-10 shadow-xl border-4 border-gold/50">
                    </div>
                    <div class="text-center">
                        <h3 class="text-xl font-bold text-primary mb-1 font-serif">Murgh Musallam</h3>
                        <p class="text-xs text-gray-500 mb-4 h-8">Whole chicken roasted with royal spices.</p>
                        <div class="flex justify-between items-center bg-cream px-4 py-2.5 rounded-2xl border border-gold/20">
                            <span class="text-lg font-bold text-darkbrown">₹599</span>
                            <button class="add-to-cart-btn bg-gold text-white w-8 h-8 rounded-lg flex items-center justify-center hover:bg-yellow-600 transition-colors shadow-md text-sm"><i class="fa-solid fa-plus"></i></button>
                        </div>
                    </div>
                </div>
"""

# Insert new menu items right after the <div class="grid grid-cols-1 ... id="menu-grid">
content = content.replace('<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8" id="menu-grid">', '<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8" id="menu-grid">\n' + new_menu_items)

# Add some golden borders to existing cards to make them premium
content = content.replace('border border-gray-100', 'border border-gold/20')
content = content.replace('bg-primary text-white w-8 h-8', 'bg-gradient-to-br from-gold to-yellow-600 text-white w-8 h-8')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

