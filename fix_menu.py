import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract everything before the menu section
parts = content.split('<!-- Royal Menu Section -->')
if len(parts) == 2:
    header_part = parts[0]
    footer_part = parts[1].split('<!-- Footer -->')[1]
else:
    print("Could not split properly")
    exit(1)

new_menu_section = """
    <!-- Royal Menu Section -->
    <section id="menu" class="py-24 bg-darkPanel relative border-t border-b border-gold/10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center mb-20">
                <h2 class="text-5xl md:text-7xl font-serif text-textCream mb-6">The Royal Menu</h2>
                <div class="w-32 h-px bg-gold mx-auto mb-2"></div>
                <div class="w-16 h-px bg-gold/50 mx-auto"></div>
            </div>

            <!-- VEGETARIAN SECTION -->
            <div class="mb-24">
                <div class="flex items-center justify-center gap-6 mb-12">
                    <div class="h-px bg-gradient-to-r from-transparent to-green-500/50 flex-grow max-w-[200px]"></div>
                    <h3 class="text-4xl md:text-5xl font-serif text-green-400 font-bold tracking-wide drop-shadow-[0_0_15px_rgba(74,222,128,0.3)]">Vegetarian</h3>
                    <div class="h-px bg-gradient-to-l from-transparent to-green-500/50 flex-grow max-w-[200px]"></div>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-12">
                    <!-- Veg Item 1 -->
                    <div class="text-center group">
                        <div class="relative w-56 h-56 mx-auto mb-6">
                            <div class="absolute inset-0 rounded-full border-2 border-dashed border-green-500/30 group-hover:rotate-180 transition-transform duration-1000"></div>
                            <img src="https://images.unsplash.com/photo-1543826173-70651703c5a4?auto=format&fit=crop&w=400&q=80" alt="Navratan Korma" class="w-full h-full object-cover rounded-full cinematic-img border-4 border-darkPanel shadow-[0_15px_35px_rgba(0,0,0,0.6)] group-hover:scale-105 transition-transform duration-500">
                        </div>
                        <h4 class="font-serif text-2xl text-gold mb-2 group-hover:text-goldLight transition-colors">Navratan Korma</h4>
                        <div class="font-sans text-lg text-textCream font-bold mb-3">₹499</div>
                        <p class="font-body text-textMuted italic text-sm px-4">Nine exquisite vegetables and nuts cooked in a rich, velvety cashew and saffron gravy.</p>
                    </div>

                    <!-- Veg Item 2 -->
                    <div class="text-center group">
                        <div class="relative w-56 h-56 mx-auto mb-6">
                            <div class="absolute inset-0 rounded-full border-2 border-dashed border-green-500/30 group-hover:rotate-180 transition-transform duration-1000"></div>
                            <img src="https://images.unsplash.com/photo-1585937421612-70a008356fbe?auto=format&fit=crop&w=400&q=80" alt="Dal Bukhara" class="w-full h-full object-cover rounded-full cinematic-img border-4 border-darkPanel shadow-[0_15px_35px_rgba(0,0,0,0.6)] group-hover:scale-105 transition-transform duration-500">
                        </div>
                        <h4 class="font-serif text-2xl text-gold mb-2 group-hover:text-goldLight transition-colors">Dal Bukhara</h4>
                        <div class="font-sans text-lg text-textCream font-bold mb-3">₹399</div>
                        <p class="font-body text-textMuted italic text-sm px-4">Black lentils simmered over coal fires overnight, finished with churned butter and fresh cream.</p>
                    </div>

                    <!-- Veg Item 3 -->
                    <div class="text-center group">
                        <div class="relative w-56 h-56 mx-auto mb-6">
                            <div class="absolute inset-0 rounded-full border-2 border-dashed border-green-500/30 group-hover:rotate-180 transition-transform duration-1000"></div>
                            <img src="https://images.unsplash.com/photo-1596797038530-2c107229654b?auto=format&fit=crop&w=400&q=80" alt="Paneer Tikka" class="w-full h-full object-cover rounded-full cinematic-img border-4 border-darkPanel shadow-[0_15px_35px_rgba(0,0,0,0.6)] group-hover:scale-105 transition-transform duration-500">
                        </div>
                        <h4 class="font-serif text-2xl text-gold mb-2 group-hover:text-goldLight transition-colors">Paneer Tikka</h4>
                        <div class="font-sans text-lg text-textCream font-bold mb-3">₹449</div>
                        <p class="font-body text-textMuted italic text-sm px-4">Cottage cheese marinated in royal spices and roasted perfectly in a traditional tandoor.</p>
                    </div>
                </div>
            </div>

            <!-- NON-VEGETARIAN SECTION -->
            <div class="mb-24">
                <div class="flex items-center justify-center gap-6 mb-12">
                    <div class="h-px bg-gradient-to-r from-transparent to-red-500/50 flex-grow max-w-[200px]"></div>
                    <h3 class="text-4xl md:text-5xl font-serif text-red-500 font-bold tracking-wide drop-shadow-[0_0_15px_rgba(239,68,68,0.3)]">Non-Vegetarian</h3>
                    <div class="h-px bg-gradient-to-l from-transparent to-red-500/50 flex-grow max-w-[200px]"></div>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-12 max-w-4xl mx-auto">
                    <!-- Non-Veg Item 1 -->
                    <div class="text-center group">
                        <div class="relative w-56 h-56 mx-auto mb-6">
                            <div class="absolute inset-0 rounded-full border-2 border-dashed border-red-500/40 group-hover:rotate-180 transition-transform duration-1000"></div>
                            <img src="https://images.unsplash.com/photo-1626509647209-409df2ab69fa?auto=format&fit=crop&w=400&q=80" alt="Murgh Musallam" class="w-full h-full object-cover rounded-full cinematic-img border-4 border-darkPanel shadow-[0_15px_35px_rgba(0,0,0,0.6)] group-hover:scale-105 transition-transform duration-500">
                        </div>
                        <h4 class="font-serif text-2xl text-gold mb-2 group-hover:text-goldLight transition-colors">Murgh Musallam</h4>
                        <div class="font-sans text-lg text-textCream font-bold mb-3">₹899</div>
                        <p class="font-body text-textMuted italic text-sm px-4">A slow-roasted whole chicken, marinated for 48 hours in rare herbs and authentic Awadhi spices.</p>
                    </div>

                    <!-- Non-Veg Item 2 -->
                    <div class="text-center group">
                        <div class="relative w-56 h-56 mx-auto mb-6">
                            <div class="absolute inset-0 rounded-full border-2 border-dashed border-red-500/40 group-hover:rotate-180 transition-transform duration-1000"></div>
                            <img src="https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=400&q=80" alt="Awadhi Biryani" class="w-full h-full object-cover rounded-full cinematic-img border-4 border-darkPanel shadow-[0_15px_35px_rgba(0,0,0,0.6)] group-hover:scale-105 transition-transform duration-500">
                        </div>
                        <h4 class="font-serif text-2xl text-gold mb-2 group-hover:text-goldLight transition-colors">Awadhi Biryani</h4>
                        <div class="font-sans text-lg text-textCream font-bold mb-3">₹549</div>
                        <p class="font-body text-textMuted italic text-sm px-4">Fragrant basmati rice layered with succulent meat, sealed with dough and cooked in dum style.</p>
                    </div>
                </div>
            </div>

            <!-- DESSERTS SECTION -->
            <div class="mb-24">
                <div class="flex items-center justify-center gap-6 mb-12">
                    <div class="h-px bg-gradient-to-r from-transparent to-pink-400/50 flex-grow max-w-[200px]"></div>
                    <h3 class="text-4xl md:text-5xl font-serif text-pink-300 font-bold tracking-wide drop-shadow-[0_0_15px_rgba(244,114,182,0.3)]">Desserts</h3>
                    <div class="h-px bg-gradient-to-l from-transparent to-pink-400/50 flex-grow max-w-[200px]"></div>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-12 max-w-4xl mx-auto">
                    <!-- Dessert Item 1 -->
                    <div class="text-center group">
                        <div class="relative w-56 h-56 mx-auto mb-6">
                            <div class="absolute inset-0 rounded-full border-2 border-dashed border-pink-400/40 group-hover:rotate-180 transition-transform duration-1000"></div>
                            <img src="https://images.unsplash.com/photo-1630175860333-5131bda75071?auto=format&fit=crop&w=400&q=80" alt="Shahi Tukda" class="w-full h-full object-cover rounded-full cinematic-img border-4 border-darkPanel shadow-[0_15px_35px_rgba(0,0,0,0.6)] group-hover:scale-105 transition-transform duration-500">
                        </div>
                        <h4 class="font-serif text-2xl text-gold mb-2 group-hover:text-goldLight transition-colors">Shahi Tukda</h4>
                        <div class="font-sans text-lg text-textCream font-bold mb-3">₹349</div>
                        <p class="font-body text-textMuted italic text-sm px-4">Fried artisanal bread soaked in saffron-infused syrup, topped with silver leaf and thick rabri.</p>
                    </div>
                    
                    <!-- Dessert Item 2 -->
                    <div class="text-center group">
                        <div class="relative w-56 h-56 mx-auto mb-6">
                            <div class="absolute inset-0 rounded-full border-2 border-dashed border-pink-400/40 group-hover:rotate-180 transition-transform duration-1000"></div>
                            <img src="https://images.unsplash.com/photo-1598514982205-f36b96d1e8d4?auto=format&fit=crop&w=400&q=80" alt="Gulab Jamun" class="w-full h-full object-cover rounded-full cinematic-img border-4 border-darkPanel shadow-[0_15px_35px_rgba(0,0,0,0.6)] group-hover:scale-105 transition-transform duration-500">
                        </div>
                        <h4 class="font-serif text-2xl text-gold mb-2 group-hover:text-goldLight transition-colors">Royal Gulab Jamun</h4>
                        <div class="font-sans text-lg text-textCream font-bold mb-3">₹249</div>
                        <p class="font-body text-textMuted italic text-sm px-4">Warm, melt-in-mouth milk dumplings served in a fragrant rose and cardamom syrup.</p>
                    </div>
                </div>
            </div>

            <!-- DRINKS SECTION -->
            <div class="mb-10">
                <div class="flex items-center justify-center gap-6 mb-12">
                    <div class="h-px bg-gradient-to-r from-transparent to-blue-400/50 flex-grow max-w-[200px]"></div>
                    <h3 class="text-4xl md:text-5xl font-serif text-blue-300 font-bold tracking-wide drop-shadow-[0_0_15px_rgba(147,197,253,0.3)]">Drinks</h3>
                    <div class="h-px bg-gradient-to-l from-transparent to-blue-400/50 flex-grow max-w-[200px]"></div>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-12 max-w-4xl mx-auto">
                    <!-- Drink 1 -->
                    <div class="text-center group">
                        <div class="relative w-56 h-56 mx-auto mb-6">
                            <div class="absolute inset-0 rounded-full border-2 border-dashed border-blue-400/40 group-hover:rotate-180 transition-transform duration-1000"></div>
                            <img src="https://images.unsplash.com/photo-1546171753-97d7676e4602?auto=format&fit=crop&w=400&q=80" alt="Mango Lassi" class="w-full h-full object-cover rounded-full cinematic-img border-4 border-darkPanel shadow-[0_15px_35px_rgba(0,0,0,0.6)] group-hover:scale-105 transition-transform duration-500">
                        </div>
                        <h4 class="font-serif text-2xl text-gold mb-2 group-hover:text-goldLight transition-colors">Saffron Mango Lassi</h4>
                        <div class="font-sans text-lg text-textCream font-bold mb-3">₹299</div>
                        <p class="font-body text-textMuted italic text-sm px-4">Thick, sweet yogurt blended with Alphonso mangoes and topped with crushed pistachios.</p>
                    </div>
                    
                    <!-- Drink 2 -->
                    <div class="text-center group">
                        <div class="relative w-56 h-56 mx-auto mb-6">
                            <div class="absolute inset-0 rounded-full border-2 border-dashed border-blue-400/40 group-hover:rotate-180 transition-transform duration-1000"></div>
                            <img src="https://images.unsplash.com/photo-1551538827-9c037cb4f32a?auto=format&fit=crop&w=400&q=80" alt="Mint Mojito" class="w-full h-full object-cover rounded-full cinematic-img border-4 border-darkPanel shadow-[0_15px_35px_rgba(0,0,0,0.6)] group-hover:scale-105 transition-transform duration-500">
                        </div>
                        <h4 class="font-serif text-2xl text-gold mb-2 group-hover:text-goldLight transition-colors">Shahi Mint Cooler</h4>
                        <div class="font-sans text-lg text-textCream font-bold mb-3">₹249</div>
                        <p class="font-body text-textMuted italic text-sm px-4">A refreshing blend of fresh mint, lime, and crushed ice, finished with a hint of roasted cumin.</p>
                    </div>
                </div>
            </div>

        </div>
    </section>
"""

new_content = header_part + new_menu_section + "\n    <!-- Footer -->" + footer_part

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
