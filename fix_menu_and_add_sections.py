import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract header and footer
parts = content.split('<!-- Royal Menu Section -->')
if len(parts) == 2:
    header_part = parts[0]
    footer_part = parts[1].split('<!-- Footer -->')[1]
else:
    print("Could not split properly")
    exit(1)

new_menu_section = """
    <!-- Royal Menu Section -->
    <section id="menu" class="py-24 bg-darkPanel/30 relative border-t border-b border-gold/10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row justify-between items-end mb-16 gap-6">
                <div>
                    <h2 class="text-4xl md:text-6xl font-serif text-textCream mb-4">The Royal Feast</h2>
                    <div class="w-24 h-px bg-gold"></div>
                </div>
                <div class="flex flex-wrap gap-6 font-sans text-xs uppercase tracking-widest">
                    <button class="text-gold border-b border-gold pb-1">All Curations</button>
                    <button class="text-textMuted hover:text-gold transition-colors pb-1">Vegetarian</button>
                    <button class="text-textMuted hover:text-gold transition-colors pb-1">Non-Vegetarian</button>
                    <button class="text-textMuted hover:text-gold transition-colors pb-1">Desserts</button>
                    <button class="text-textMuted hover:text-gold transition-colors pb-1">Drinks</button>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
                <!-- VEG -->
                <div class="luxury-card border border-gold/10 p-5 flex flex-col group">
                    <div class="overflow-hidden aspect-[4/3] mb-4 relative border border-gold/20">
                        <img src="https://images.unsplash.com/photo-1543826173-70651703c5a4?auto=format&fit=crop&w=800&q=80" alt="Navratan Korma" class="w-full h-full object-cover cinematic-img group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute top-2 left-2 bg-green-900/80 text-green-400 text-[9px] uppercase tracking-widest px-2 py-1 border border-green-500/50">Veg</div>
                    </div>
                    <div class="flex justify-between items-start mb-2"><h3 class="font-serif text-xl text-textCream group-hover:text-gold">Navratan Korma</h3><span class="font-sans text-sm text-gold">₹499</span></div>
                    <p class="font-body text-textMuted italic text-sm mb-4 flex-grow">Nine exquisite vegetables and nuts cooked in cashew gravy.</p>
                    <button class="w-full border border-gold/30 py-2 font-sans text-[10px] uppercase tracking-widest text-gold hover:bg-gold hover:text-darkBase transition-colors">Add</button>
                </div>

                <div class="luxury-card border border-gold/10 p-5 flex flex-col group">
                    <div class="overflow-hidden aspect-[4/3] mb-4 relative border border-gold/20">
                        <img src="https://images.unsplash.com/photo-1585937421612-70a008356fbe?auto=format&fit=crop&w=800&q=80" alt="Dal Bukhara" class="w-full h-full object-cover cinematic-img group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute top-2 left-2 bg-green-900/80 text-green-400 text-[9px] uppercase tracking-widest px-2 py-1 border border-green-500/50">Veg</div>
                    </div>
                    <div class="flex justify-between items-start mb-2"><h3 class="font-serif text-xl text-textCream group-hover:text-gold">Dal Bukhara</h3><span class="font-sans text-sm text-gold">₹399</span></div>
                    <p class="font-body text-textMuted italic text-sm mb-4 flex-grow">Black lentils simmered over coal fires overnight.</p>
                    <button class="w-full border border-gold/30 py-2 font-sans text-[10px] uppercase tracking-widest text-gold hover:bg-gold hover:text-darkBase transition-colors">Add</button>
                </div>

                <div class="luxury-card border border-gold/10 p-5 flex flex-col group">
                    <div class="overflow-hidden aspect-[4/3] mb-4 relative border border-gold/20">
                        <img src="https://images.unsplash.com/photo-1596797038530-2c107229654b?auto=format&fit=crop&w=800&q=80" alt="Paneer Tikka" class="w-full h-full object-cover cinematic-img group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute top-2 left-2 bg-green-900/80 text-green-400 text-[9px] uppercase tracking-widest px-2 py-1 border border-green-500/50">Veg</div>
                    </div>
                    <div class="flex justify-between items-start mb-2"><h3 class="font-serif text-xl text-textCream group-hover:text-gold">Paneer Tikka</h3><span class="font-sans text-sm text-gold">₹449</span></div>
                    <p class="font-body text-textMuted italic text-sm mb-4 flex-grow">Cottage cheese marinated in royal spices and roasted.</p>
                    <button class="w-full border border-gold/30 py-2 font-sans text-[10px] uppercase tracking-widest text-gold hover:bg-gold hover:text-darkBase transition-colors">Add</button>
                </div>

                <div class="luxury-card border border-gold/10 p-5 flex flex-col group">
                    <div class="overflow-hidden aspect-[4/3] mb-4 relative border border-gold/20">
                        <img src="https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&w=800&q=80" alt="Malai Kofta" class="w-full h-full object-cover cinematic-img group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute top-2 left-2 bg-green-900/80 text-green-400 text-[9px] uppercase tracking-widest px-2 py-1 border border-green-500/50">Veg</div>
                    </div>
                    <div class="flex justify-between items-start mb-2"><h3 class="font-serif text-xl text-textCream group-hover:text-gold">Malai Kofta</h3><span class="font-sans text-sm text-gold">₹479</span></div>
                    <p class="font-body text-textMuted italic text-sm mb-4 flex-grow">Soft paneer dumplings in a rich, creamy white gravy.</p>
                    <button class="w-full border border-gold/30 py-2 font-sans text-[10px] uppercase tracking-widest text-gold hover:bg-gold hover:text-darkBase transition-colors">Add</button>
                </div>

                <!-- NON-VEG -->
                <div class="luxury-card border border-gold/10 p-5 flex flex-col group">
                    <div class="overflow-hidden aspect-[4/3] mb-4 relative border border-gold/20">
                        <img src="https://images.unsplash.com/photo-1626509647209-409df2ab69fa?auto=format&fit=crop&w=800&q=80" alt="Murgh Musallam" class="w-full h-full object-cover cinematic-img group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute top-2 left-2 bg-red-900/80 text-red-400 text-[9px] uppercase tracking-widest px-2 py-1 border border-red-500/50">Non-Veg</div>
                        <div class="absolute top-2 right-2 bg-gold text-darkBase text-[8px] uppercase tracking-widest px-2 py-1 font-bold">Signature</div>
                    </div>
                    <div class="flex justify-between items-start mb-2"><h3 class="font-serif text-xl text-textCream group-hover:text-gold">Murgh Musallam</h3><span class="font-sans text-sm text-gold">₹899</span></div>
                    <p class="font-body text-textMuted italic text-sm mb-4 flex-grow">A slow-roasted whole chicken in rare herbs.</p>
                    <button class="w-full border border-gold/30 py-2 font-sans text-[10px] uppercase tracking-widest text-gold hover:bg-gold hover:text-darkBase transition-colors">Add</button>
                </div>

                <div class="luxury-card border border-gold/10 p-5 flex flex-col group">
                    <div class="overflow-hidden aspect-[4/3] mb-4 relative border border-gold/20">
                        <img src="https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=800&q=80" alt="Biryani" class="w-full h-full object-cover cinematic-img group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute top-2 left-2 bg-red-900/80 text-red-400 text-[9px] uppercase tracking-widest px-2 py-1 border border-red-500/50">Non-Veg</div>
                    </div>
                    <div class="flex justify-between items-start mb-2"><h3 class="font-serif text-xl text-textCream group-hover:text-gold">Awadhi Biryani</h3><span class="font-sans text-sm text-gold">₹549</span></div>
                    <p class="font-body text-textMuted italic text-sm mb-4 flex-grow">Fragrant basmati rice layered with succulent meat.</p>
                    <button class="w-full border border-gold/30 py-2 font-sans text-[10px] uppercase tracking-widest text-gold hover:bg-gold hover:text-darkBase transition-colors">Add</button>
                </div>

                <div class="luxury-card border border-gold/10 p-5 flex flex-col group">
                    <div class="overflow-hidden aspect-[4/3] mb-4 relative border border-gold/20">
                        <img src="https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?auto=format&fit=crop&w=800&q=80" alt="Butter Chicken" class="w-full h-full object-cover cinematic-img group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute top-2 left-2 bg-red-900/80 text-red-400 text-[9px] uppercase tracking-widest px-2 py-1 border border-red-500/50">Non-Veg</div>
                    </div>
                    <div class="flex justify-between items-start mb-2"><h3 class="font-serif text-xl text-textCream group-hover:text-gold">Butter Chicken</h3><span class="font-sans text-sm text-gold">₹599</span></div>
                    <p class="font-body text-textMuted italic text-sm mb-4 flex-grow">Tender chicken in a velvety, buttery tomato sauce.</p>
                    <button class="w-full border border-gold/30 py-2 font-sans text-[10px] uppercase tracking-widest text-gold hover:bg-gold hover:text-darkBase transition-colors">Add</button>
                </div>
                
                <div class="luxury-card border border-gold/10 p-5 flex flex-col group">
                    <div class="overflow-hidden aspect-[4/3] mb-4 relative border border-gold/20">
                        <img src="https://images.unsplash.com/photo-1599487405270-87ce6d8db562?auto=format&fit=crop&w=800&q=80" alt="Chicken Tikka" class="w-full h-full object-cover cinematic-img group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute top-2 left-2 bg-red-900/80 text-red-400 text-[9px] uppercase tracking-widest px-2 py-1 border border-red-500/50">Non-Veg</div>
                    </div>
                    <div class="flex justify-between items-start mb-2"><h3 class="font-serif text-xl text-textCream group-hover:text-gold">Chicken Tikka</h3><span class="font-sans text-sm text-gold">₹499</span></div>
                    <p class="font-body text-textMuted italic text-sm mb-4 flex-grow">Smoky, spiced boneless chicken roasted to perfection.</p>
                    <button class="w-full border border-gold/30 py-2 font-sans text-[10px] uppercase tracking-widest text-gold hover:bg-gold hover:text-darkBase transition-colors">Add</button>
                </div>

                <!-- DESSERTS & DRINKS -->
                <div class="luxury-card border border-gold/10 p-5 flex flex-col group">
                    <div class="overflow-hidden aspect-[4/3] mb-4 relative border border-gold/20">
                        <img src="https://images.unsplash.com/photo-1630175860333-5131bda75071?auto=format&fit=crop&w=800&q=80" alt="Shahi Tukda" class="w-full h-full object-cover cinematic-img group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute top-2 left-2 bg-pink-900/80 text-pink-400 text-[9px] uppercase tracking-widest px-2 py-1 border border-pink-500/50">Dessert</div>
                    </div>
                    <div class="flex justify-between items-start mb-2"><h3 class="font-serif text-xl text-textCream group-hover:text-gold">Shahi Tukda</h3><span class="font-sans text-sm text-gold">₹349</span></div>
                    <p class="font-body text-textMuted italic text-sm mb-4 flex-grow">Bread soaked in saffron syrup, topped with rabri.</p>
                    <button class="w-full border border-gold/30 py-2 font-sans text-[10px] uppercase tracking-widest text-gold hover:bg-gold hover:text-darkBase transition-colors">Add</button>
                </div>

                <div class="luxury-card border border-gold/10 p-5 flex flex-col group">
                    <div class="overflow-hidden aspect-[4/3] mb-4 relative border border-gold/20">
                        <img src="https://images.unsplash.com/photo-1598514982205-f36b96d1e8d4?auto=format&fit=crop&w=800&q=80" alt="Gulab Jamun" class="w-full h-full object-cover cinematic-img group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute top-2 left-2 bg-pink-900/80 text-pink-400 text-[9px] uppercase tracking-widest px-2 py-1 border border-pink-500/50">Dessert</div>
                    </div>
                    <div class="flex justify-between items-start mb-2"><h3 class="font-serif text-xl text-textCream group-hover:text-gold">Gulab Jamun</h3><span class="font-sans text-sm text-gold">₹249</span></div>
                    <p class="font-body text-textMuted italic text-sm mb-4 flex-grow">Warm milk dumplings in fragrant cardamom syrup.</p>
                    <button class="w-full border border-gold/30 py-2 font-sans text-[10px] uppercase tracking-widest text-gold hover:bg-gold hover:text-darkBase transition-colors">Add</button>
                </div>

                <div class="luxury-card border border-gold/10 p-5 flex flex-col group">
                    <div class="overflow-hidden aspect-[4/3] mb-4 relative border border-gold/20">
                        <img src="https://images.unsplash.com/photo-1546171753-97d7676e4602?auto=format&fit=crop&w=800&q=80" alt="Mango Lassi" class="w-full h-full object-cover cinematic-img group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute top-2 left-2 bg-blue-900/80 text-blue-400 text-[9px] uppercase tracking-widest px-2 py-1 border border-blue-500/50">Drink</div>
                    </div>
                    <div class="flex justify-between items-start mb-2"><h3 class="font-serif text-xl text-textCream group-hover:text-gold">Mango Lassi</h3><span class="font-sans text-sm text-gold">₹299</span></div>
                    <p class="font-body text-textMuted italic text-sm mb-4 flex-grow">Sweet yogurt blended with fresh Alphonso mangoes.</p>
                    <button class="w-full border border-gold/30 py-2 font-sans text-[10px] uppercase tracking-widest text-gold hover:bg-gold hover:text-darkBase transition-colors">Add</button>
                </div>
                
                <div class="luxury-card border border-gold/10 p-5 flex flex-col group">
                    <div class="overflow-hidden aspect-[4/3] mb-4 relative border border-gold/20">
                        <img src="https://images.unsplash.com/photo-1551538827-9c037cb4f32a?auto=format&fit=crop&w=800&q=80" alt="Mint Mojito" class="w-full h-full object-cover cinematic-img group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute top-2 left-2 bg-blue-900/80 text-blue-400 text-[9px] uppercase tracking-widest px-2 py-1 border border-blue-500/50">Drink</div>
                    </div>
                    <div class="flex justify-between items-start mb-2"><h3 class="font-serif text-xl text-textCream group-hover:text-gold">Mint Cooler</h3><span class="font-sans text-sm text-gold">₹249</span></div>
                    <p class="font-body text-textMuted italic text-sm mb-4 flex-grow">Refreshing blend of fresh mint, lime, and ice.</p>
                    <button class="w-full border border-gold/30 py-2 font-sans text-[10px] uppercase tracking-widest text-gold hover:bg-gold hover:text-darkBase transition-colors">Add</button>
                </div>

            </div>
        </div>
    </section>

    <!-- Animated Reservation Section -->
    <section id="reservation" class="py-24 relative overflow-hidden bg-darkBase">
        <div class="absolute top-0 right-0 w-64 h-64 bg-gold/10 rounded-full blur-[80px] pointer-events-none"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="bg-darkPanel/80 border border-gold/20 p-8 md:p-16 relative overflow-hidden group">
                <!-- Animated glowing border effect -->
                <div class="absolute inset-0 border-2 border-gold/5 opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
                <div class="absolute top-0 left-[-100%] w-1/2 h-full bg-gradient-to-r from-transparent via-gold/10 to-transparent group-hover:left-[200%] transition-all duration-[2s] ease-in-out"></div>
                
                <div class="flex flex-col lg:flex-row gap-12 items-center">
                    <div class="w-full lg:w-1/2">
                        <h2 class="text-4xl md:text-5xl font-serif text-textCream mb-4">Reserve Your Royal Table</h2>
                        <div class="w-16 h-px bg-gold mb-6"></div>
                        <p class="font-body text-textMuted text-lg mb-8">Secure your place at our royal feast. Experience the majesty of dining in a setting inspired by the ancient palaces of India.</p>
                        
                        <form class="space-y-6">
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                                <input type="text" placeholder="Your Name" class="bg-darkBase/50 border border-gold/20 p-4 text-textCream font-sans text-sm focus:outline-none focus:border-gold transition-colors w-full">
                                <input type="tel" placeholder="Phone Number" class="bg-darkBase/50 border border-gold/20 p-4 text-textCream font-sans text-sm focus:outline-none focus:border-gold transition-colors w-full">
                            </div>
                            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                                <input type="date" class="bg-darkBase/50 border border-gold/20 p-4 text-textMuted font-sans text-sm focus:outline-none focus:border-gold transition-colors w-full">
                                <input type="time" class="bg-darkBase/50 border border-gold/20 p-4 text-textMuted font-sans text-sm focus:outline-none focus:border-gold transition-colors w-full">
                                <select class="bg-darkBase/50 border border-gold/20 p-4 text-textMuted font-sans text-sm focus:outline-none focus:border-gold transition-colors w-full">
                                    <option>2 Guests</option>
                                    <option>3 Guests</option>
                                    <option>4 Guests</option>
                                    <option>5+ Guests (Royal Hall)</option>
                                </select>
                            </div>
                            <button type="button" class="w-full bg-gold-gradient text-darkBase font-bold font-sans uppercase tracking-widest py-4 hover:scale-[1.02] transition-transform shadow-[0_0_20px_rgba(197,160,89,0.2)]">
                                Confirm Reservation
                            </button>
                        </form>
                    </div>
                    <div class="w-full lg:w-1/2 flex justify-center">
                        <div class="w-64 h-64 md:w-80 md:h-80 border-4 border-gold/30 rounded-full flex items-center justify-center relative animate-[spin_30s_linear_infinite]">
                            <div class="absolute inset-2 border border-dashed border-gold/40 rounded-full animate-[spin_20s_linear_infinite_reverse]"></div>
                            <i class="fa-solid fa-bell-concierge text-6xl text-gold/80 animate-pulse"></i>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Location & Contact Section -->
    <section id="location" class="py-20 border-t border-gold/10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h2 class="text-3xl font-serif text-gold mb-6">Find The Palace</h2>
            <div class="flex flex-col md:flex-row justify-center items-center gap-12 font-body text-textCream text-xl">
                <div class="flex items-center gap-3">
                    <i class="fa-solid fa-map-location-dot text-gold text-2xl"></i>
                    <span>Ore, Chakand, India</span>
                </div>
                <div class="hidden md:block w-px h-8 bg-gold/30"></div>
                <div class="flex items-center gap-3">
                    <i class="fa-solid fa-clock text-gold text-2xl"></i>
                    <span>Open Daily: 12 PM - 11 PM</span>
                </div>
                <div class="hidden md:block w-px h-8 bg-gold/30"></div>
                <div class="flex items-center gap-3">
                    <i class="fa-solid fa-phone text-gold text-2xl"></i>
                    <span>+91 98765 43210</span>
                </div>
            </div>
        </div>
    </section>
"""

new_content = header_part + new_menu_section + "\n    <!-- Footer -->" + footer_part

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
