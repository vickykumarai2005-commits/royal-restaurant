import os

html_content = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Royal Taste, Desi Heart | Ultra Premium Dining</title>
    
    <!-- Google Fonts for Luxury Feel -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;800&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,400&family=Montserrat:wght@200;300;400;500&display=swap" rel="stylesheet">
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
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
                    fontFamily: {
                        serif: ['"Cinzel"', 'serif'],
                        body: ['"Cormorant Garamond"', 'serif'],
                        sans: ['"Montserrat"', 'sans-serif'],
                    },
                    backgroundImage: {
                        'gold-gradient': 'linear-gradient(to right, #8A6D3B, #C5A059, #E8D099, #C5A059, #8A6D3B)',
                        'dark-gradient': 'linear-gradient(to bottom, rgba(10,8,6,0) 0%, rgba(10,8,6,1) 100%)',
                    }
                }
            }
        }
    </script>
    
    <!-- FontAwesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        body {
            background-color: #0a0806;
            color: #FDFBF7;
            overflow-x: hidden;
        }
        
        /* Custom Scrollbar for Luxury */
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: #0a0806; }
        ::-webkit-scrollbar-thumb { background: #C5A059; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #E8D099; }

        /* Text Gradients */
        .text-gold-gradient {
            background: linear-gradient(to right, #C5A059, #E8D099, #C5A059);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            background-size: 200% auto;
            animation: shine 5s linear infinite;
        }
        @keyframes shine { to { background-position: 200% center; } }

        /* Ornate Background Pattern (Mughal Style) */
        .mughal-pattern {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background-image: url("data:image/svg+xml,%3Csvg width='100' height='100' viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M50 0c0 27.614-22.386 50-50 50 27.614 0 50 22.386 50 50 0-27.614 22.386-50 50-50-27.614 0-50-22.386-50-50z' fill='%23C5A059' fill-opacity='0.03' fill-rule='evenodd'/%3E%3C/svg%3E");
            z-index: -1;
            pointer-events: none;
        }

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

        /* Floating Animation */
        .float-slow { animation: float 6s ease-in-out infinite; }
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-15px); }
            100% { transform: translateY(0px); }
        }

        /* Steam effect */
        .steam-container { position: absolute; width: 100%; height: 100%; top: 0; left: 0; pointer-events: none; }
        .steam {
            position: absolute; width: 50px; height: 50px;
            background: rgba(255, 255, 255, 0.15); border-radius: 50%;
            filter: blur(15px); opacity: 0; pointer-events: none;
        }
        .steam-1 { top: 30%; left: 40%; animation: steamRise 4s ease-out infinite; }
        .steam-2 { top: 40%; left: 50%; animation: steamRise 5s ease-out infinite 1.5s; }
        .steam-3 { top: 35%; left: 60%; animation: steamRise 6s ease-out infinite 0.7s; }
        
        @keyframes steamRise {
            0% { transform: translateY(0) scale(1) translateX(0); opacity: 0; }
            30% { opacity: 0.8; }
            100% { transform: translateY(-150px) scale(4) translateX(-30px); opacity: 0; }
        }

        /* Golden Borders */
        .border-gold-ornate {
            border: 1px solid rgba(197, 160, 89, 0.3);
            position: relative;
        }
        .border-gold-ornate::before, .border-gold-ornate::after {
            content: ''; position: absolute; width: 8px; height: 8px; border: 1px solid #C5A059;
        }
        .border-gold-ornate::before { top: -4px; left: -4px; border-right: none; border-bottom: none; }
        .border-gold-ornate::after { bottom: -4px; right: -4px; border-left: none; border-top: none; }

        /* Menu Card Hover */
        .luxury-card { transition: all 0.5s ease; background: linear-gradient(145deg, #14100c, #0a0806); }
        .luxury-card:hover { transform: translateY(-10px); box-shadow: 0 20px 40px rgba(197, 160, 89, 0.1); border-color: rgba(197, 160, 89, 0.6); }

        /* Dynamic Image composition */
        .dynamic-composition { position: relative; width: 100%; max-width: 500px; aspect-ratio: 1/1; margin: auto; }
        .base-bowl { position: absolute; bottom: 0; left: 10%; width: 80%; height: auto; z-index: 10; border-radius: 50%; box-shadow: 0 30px 60px rgba(0,0,0,0.8); }
        .splash-item { position: absolute; top: -10%; left: 25%; width: 50%; z-index: 20; transform: rotate(10deg); filter: drop-shadow(0 20px 20px rgba(0,0,0,0.6)); animation: splashAnim 4s infinite alternate ease-in-out; }

        @keyframes splashAnim {
            0% { transform: translateY(0px) rotate(5deg) scale(1); }
            100% { transform: translateY(-20px) rotate(10deg) scale(1.05); }
        }
    </style>
</head>
<body class="font-body antialiased">
    <div class="mughal-pattern"></div>

    <!-- Navigation -->
    <nav class="fixed w-full z-50 transition-all duration-500 bg-darkBase/80 backdrop-blur-lg border-b border-gold/10" id="navbar">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-24">
                <div class="flex-shrink-0 flex flex-col items-center justify-center cursor-pointer">
                    <img src="https://cdn-icons-png.flaticon.com/512/8207/8207264.png" class="w-8 h-8 mb-1 filter invert opacity-80" style="filter: sepia(1) hue-rotate(10deg) saturate(3) brightness(0.8);" alt="Crown">
                    <div class="font-serif font-bold text-2xl text-gold tracking-[0.2em] uppercase">Royal Taste</div>
                    <div class="text-[9px] text-textMuted tracking-[0.4em] font-sans uppercase mt-1">Ore, Chakand</div>
                </div>
                
                <div class="hidden md:flex space-x-12 items-center">
                    <a href="#home" class="font-sans text-xs uppercase tracking-widest text-gold transition-colors hover:text-textCream relative group">
                        Home
                        <span class="absolute -bottom-2 left-1/2 w-0 h-px bg-gold transition-all duration-300 group-hover:w-full group-hover:left-0"></span>
                    </a>
                    <a href="#experience" class="font-sans text-xs uppercase tracking-widest text-textMuted transition-colors hover:text-textCream relative group">
                        The Experience
                        <span class="absolute -bottom-2 left-1/2 w-0 h-px bg-gold transition-all duration-300 group-hover:w-full group-hover:left-0"></span>
                    </a>
                    <a href="#menu" class="font-sans text-xs uppercase tracking-widest text-textMuted transition-colors hover:text-textCream relative group">
                        Royal Menu
                        <span class="absolute -bottom-2 left-1/2 w-0 h-px bg-gold transition-all duration-300 group-hover:w-full group-hover:left-0"></span>
                    </a>
                    <a href="#reservation" class="font-sans text-xs uppercase tracking-widest text-textMuted transition-colors hover:text-textCream relative group">
                        Reservation
                        <span class="absolute -bottom-2 left-1/2 w-0 h-px bg-gold transition-all duration-300 group-hover:w-full group-hover:left-0"></span>
                    </a>
                </div>

                <div class="hidden md:flex items-center space-x-6">
                    <button class="text-gold hover:text-textCream transition-colors">
                        <i class="fa-solid fa-shopping-bag text-lg"></i>
                    </button>
                    <button class="bg-transparent border border-gold text-gold hover:bg-gold hover:text-darkBase px-8 py-3 font-sans text-xs uppercase tracking-widest transition-all duration-500">
                        Reserve a Table
                    </button>
                </div>
            </div>
        </div>
    </nav>

    <!-- Cinematic Hero Section -->
    <section id="home" class="relative min-h-screen flex items-center justify-center pt-24 overflow-hidden">
        <!-- Cinematic Background elements -->
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[80vw] h-[80vw] max-w-[800px] max-h-[800px] bg-gold/5 rounded-full blur-[120px] pointer-events-none z-0"></div>
        <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1542665952-14513db15293?q=80&w=2070&auto=format&fit=crop')] bg-cover bg-center opacity-10 mix-blend-overlay z-0"></div>

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full">
            <div class="flex flex-col lg:flex-row items-center justify-between gap-12 lg:gap-24">
                
                <!-- Typography / Text -->
                <div class="w-full lg:w-1/2 flex flex-col items-center lg:items-start text-center lg:text-left">
                    <div class="flex items-center gap-4 mb-6 opacity-80">
                        <span class="w-12 h-px bg-gold"></span>
                        <span class="font-sans text-xs uppercase tracking-[0.3em] text-gold">Dining Reimagined</span>
                        <span class="w-12 h-px bg-gold"></span>
                    </div>
                    
                    <h1 class="text-5xl sm:text-7xl lg:text-8xl font-serif leading-[1.1] mb-6 text-textCream">
                        The Legacy of <br>
                        <span class="text-gold-gradient">Maharajas.</span>
                    </h1>
                    
                    <p class="font-body text-xl md:text-2xl text-textMuted mb-10 max-w-xl leading-relaxed italic">
                        "Experience the culinary secrets of ancient Indian palaces. A symphony of spices, meticulously crafted in the royal kitchens."
                    </p>
                    
                    <div class="flex flex-col sm:flex-row gap-6 w-full sm:w-auto">
                        <button class="bg-gold-gradient text-darkBase px-10 py-4 font-sans text-sm uppercase tracking-widest font-bold transition-all hover:scale-105 shadow-[0_0_30px_rgba(197,160,89,0.3)] border border-transparent">
                            Explore the Feast
                        </button>
                        <button class="bg-transparent text-textCream border border-gold/40 px-10 py-4 font-sans text-sm uppercase tracking-widest transition-all hover:border-gold hover:bg-gold/5">
                            View Story
                        </button>
                    </div>
                </div>
                
                <!-- Hero Image Composition -->
                <div class="w-full lg:w-1/2 relative mt-16 lg:mt-0">
                    <div class="dynamic-composition float-slow">
                        <!-- Steam overlay -->
                        <div class="steam-container z-30">
                            <div class="steam steam-1"></div>
                            <div class="steam steam-2"></div>
                            <div class="steam steam-3"></div>
                        </div>
                        
                        <!-- Base Bowl (Using user's paneer image mapped to a circle) -->
                        <img src="paneer_lababdar.jpg" alt="Royal Bowl" class="base-bowl border-4 border-gold/50 cinematic-img object-cover aspect-square">
                        
                        <!-- Splash/Falling Item (Using user's chicken leg image) -->
                        <img src="chicken_leg.jpg" alt="Falling Splash" class="splash-item cinematic-img rounded-full border-2 border-gold/30">
                        
                        <!-- Floating Badge -->
                        <div class="absolute bottom-10 -right-10 bg-darkPanel/90 backdrop-blur-md p-5 rounded-none border border-gold/40 shadow-2xl z-40 hidden md:block border-gold-ornate">
                            <div class="text-gold font-sans text-[10px] uppercase tracking-widest mb-1">Signature Dish</div>
                            <h3 class="font-serif text-lg text-textCream mb-2">Shahi Paneer Lababdar<br>& Royal Splash</h3>
                            <div class="w-full h-px bg-gold/20 mb-2"></div>
                            <div class="font-body italic text-textMuted text-sm">Served in pure gold vessels</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Scroll Indicator -->
        <div class="absolute bottom-10 left-1/2 -translate-x-1/2 flex flex-col items-center gap-2 opacity-50 z-20">
            <span class="font-sans text-[10px] uppercase tracking-[0.2em] text-gold writing-vertical-rl">Scroll</span>
            <div class="w-px h-16 bg-gradient-to-b from-gold to-transparent"></div>
        </div>
    </section>

    <!-- Divider -->
    <div class="w-full h-px bg-gradient-to-r from-transparent via-gold/30 to-transparent my-10"></div>

    <!-- The Experience Section -->
    <section id="experience" class="py-24 relative">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <div class="inline-flex items-center gap-4 mb-4">
                <span class="w-8 h-px bg-gold"></span>
                <span class="font-sans text-xs uppercase tracking-widest text-gold">Our Philosophy</span>
                <span class="w-8 h-px bg-gold"></span>
            </div>
            <h2 class="text-4xl md:text-5xl font-serif text-textCream mb-8">Culinary Heritage<br>Redefined</h2>
            <p class="font-body text-xl text-textMuted max-w-3xl mx-auto leading-relaxed">
                Step into an era where food was an art form. Our chefs revive centuries-old recipes from the Mughal era and royal Rajputana kitchens, presenting them with avant-garde modern luxury. Every ingredient is hand-picked, every spice hand-ground.
            </p>
        </div>
    </section>

    <!-- Royal Menu Section -->
    <section id="menu" class="py-24 bg-darkPanel/30 relative border-t border-b border-gold/10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row justify-between items-end mb-16 gap-6">
                <div>
                    <h2 class="text-4xl md:text-6xl font-serif text-textCream mb-4">The Royal Menu</h2>
                    <div class="w-24 h-px bg-gold"></div>
                </div>
                <div class="flex gap-6 font-sans text-xs uppercase tracking-widest">
                    <button class="text-gold border-b border-gold pb-1">All Curations</button>
                    <button class="text-textMuted hover:text-gold transition-colors pb-1">Vegetarian</button>
                    <button class="text-textMuted hover:text-gold transition-colors pb-1">Non-Vegetarian</button>
                    <button class="text-textMuted hover:text-gold transition-colors pb-1">Desserts</button>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
                <!-- Premium Menu Item 1 -->
                <div class="luxury-card border border-gold/10 p-6 flex flex-col group">
                    <div class="overflow-hidden aspect-[4/3] mb-6 relative border border-gold/20">
                        <div class="absolute inset-0 bg-darkBase/20 group-hover:bg-transparent transition-all z-10"></div>
                        <img src="https://images.unsplash.com/photo-1543826173-70651703c5a4?auto=format&fit=crop&w=800&q=80" alt="Navratan Korma" class="w-full h-full object-cover cinematic-img group-hover:scale-110 transition-transform duration-700">
                    </div>
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="font-serif text-2xl text-textCream group-hover:text-gold transition-colors">Navratan Korma</h3>
                        <span class="font-sans text-sm text-gold">₹499</span>
                    </div>
                    <p class="font-body text-textMuted italic mb-6 flex-grow">Nine exquisite vegetables and nuts cooked in a rich, velvety cashew and saffron gravy.</p>
                    <button class="w-full border border-gold/30 py-3 font-sans text-xs uppercase tracking-widest text-gold hover:bg-gold hover:text-darkBase transition-colors">
                        Add to Order
                    </button>
                </div>

                <!-- Premium Menu Item 2 -->
                <div class="luxury-card border border-gold/10 p-6 flex flex-col group relative overflow-hidden">
                    <div class="absolute top-4 right-4 bg-gold text-darkBase text-[9px] uppercase tracking-widest font-bold px-2 py-1 z-20">Signature</div>
                    <div class="overflow-hidden aspect-[4/3] mb-6 relative border border-gold/20">
                        <div class="absolute inset-0 bg-darkBase/20 group-hover:bg-transparent transition-all z-10"></div>
                        <img src="https://images.unsplash.com/photo-1626509647209-409df2ab69fa?auto=format&fit=crop&w=800&q=80" alt="Murgh Musallam" class="w-full h-full object-cover cinematic-img group-hover:scale-110 transition-transform duration-700">
                    </div>
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="font-serif text-2xl text-textCream group-hover:text-gold transition-colors">Murgh Musallam</h3>
                        <span class="font-sans text-sm text-gold">₹899</span>
                    </div>
                    <p class="font-body text-textMuted italic mb-6 flex-grow">A slow-roasted whole chicken, marinated for 48 hours in rare herbs and authentic Awadhi spices.</p>
                    <button class="w-full border border-gold/30 py-3 font-sans text-xs uppercase tracking-widest text-gold hover:bg-gold hover:text-darkBase transition-colors">
                        Add to Order
                    </button>
                </div>

                <!-- Premium Menu Item 3 -->
                <div class="luxury-card border border-gold/10 p-6 flex flex-col group">
                    <div class="overflow-hidden aspect-[4/3] mb-6 relative border border-gold/20">
                        <div class="absolute inset-0 bg-darkBase/20 group-hover:bg-transparent transition-all z-10"></div>
                        <img src="https://images.unsplash.com/photo-1630175860333-5131bda75071?auto=format&fit=crop&w=800&q=80" alt="Shahi Tukda" class="w-full h-full object-cover cinematic-img group-hover:scale-110 transition-transform duration-700">
                    </div>
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="font-serif text-2xl text-textCream group-hover:text-gold transition-colors">Shahi Tukda</h3>
                        <span class="font-sans text-sm text-gold">₹349</span>
                    </div>
                    <p class="font-body text-textMuted italic mb-6 flex-grow">Fried artisanal bread soaked in saffron-infused syrup, topped with silver leaf and thick rabri.</p>
                    <button class="w-full border border-gold/30 py-3 font-sans text-xs uppercase tracking-widest text-gold hover:bg-gold hover:text-darkBase transition-colors">
                        Add to Order
                    </button>
                </div>
                
                <!-- Extra Item 4: Dal Bukhara -->
                <div class="luxury-card border border-gold/10 p-6 flex flex-col group">
                    <div class="overflow-hidden aspect-[4/3] mb-6 relative border border-gold/20">
                        <div class="absolute inset-0 bg-darkBase/20 group-hover:bg-transparent transition-all z-10"></div>
                        <img src="https://images.unsplash.com/photo-1585937421612-70a008356fbe?auto=format&fit=crop&w=800&q=80" alt="Dal Bukhara" class="w-full h-full object-cover cinematic-img group-hover:scale-110 transition-transform duration-700">
                    </div>
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="font-serif text-2xl text-textCream group-hover:text-gold transition-colors">Dal Bukhara</h3>
                        <span class="font-sans text-sm text-gold">₹399</span>
                    </div>
                    <p class="font-body text-textMuted italic mb-6 flex-grow">Black lentils simmered over coal fires overnight, finished with churned butter and fresh cream.</p>
                    <button class="w-full border border-gold/30 py-3 font-sans text-xs uppercase tracking-widest text-gold hover:bg-gold hover:text-darkBase transition-colors">
                        Add to Order
                    </button>
                </div>
                
                <!-- Extra Item 5: Paneer Tikka -->
                <div class="luxury-card border border-gold/10 p-6 flex flex-col group">
                    <div class="overflow-hidden aspect-[4/3] mb-6 relative border border-gold/20">
                        <div class="absolute inset-0 bg-darkBase/20 group-hover:bg-transparent transition-all z-10"></div>
                        <img src="https://images.unsplash.com/photo-1596797038530-2c107229654b?auto=format&fit=crop&w=800&q=80" alt="Paneer Tikka" class="w-full h-full object-cover cinematic-img group-hover:scale-110 transition-transform duration-700">
                    </div>
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="font-serif text-2xl text-textCream group-hover:text-gold transition-colors">Paneer Tikka</h3>
                        <span class="font-sans text-sm text-gold">₹449</span>
                    </div>
                    <p class="font-body text-textMuted italic mb-6 flex-grow">Cottage cheese marinated in royal spices and roasted perfectly in a traditional tandoor.</p>
                    <button class="w-full border border-gold/30 py-3 font-sans text-xs uppercase tracking-widest text-gold hover:bg-gold hover:text-darkBase transition-colors">
                        Add to Order
                    </button>
                </div>
                
                <!-- Extra Item 6: Biryani -->
                <div class="luxury-card border border-gold/10 p-6 flex flex-col group">
                    <div class="overflow-hidden aspect-[4/3] mb-6 relative border border-gold/20">
                        <div class="absolute inset-0 bg-darkBase/20 group-hover:bg-transparent transition-all z-10"></div>
                        <img src="https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=800&q=80" alt="Biryani" class="w-full h-full object-cover cinematic-img group-hover:scale-110 transition-transform duration-700">
                    </div>
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="font-serif text-2xl text-textCream group-hover:text-gold transition-colors">Awadhi Biryani</h3>
                        <span class="font-sans text-sm text-gold">₹549</span>
                    </div>
                    <p class="font-body text-textMuted italic mb-6 flex-grow">Fragrant basmati rice layered with succulent meat, sealed with dough and cooked in dum style.</p>
                    <button class="w-full border border-gold/30 py-3 font-sans text-xs uppercase tracking-widest text-gold hover:bg-gold hover:text-darkBase transition-colors">
                        Add to Order
                    </button>
                </div>

            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="py-16 text-center border-t border-gold/20">
        <img src="https://cdn-icons-png.flaticon.com/512/8207/8207264.png" class="w-10 h-10 mx-auto mb-6 filter invert opacity-50" style="filter: sepia(1) hue-rotate(10deg) saturate(3) brightness(0.5);" alt="Crown">
        <h3 class="font-serif text-3xl text-gold mb-2">Royal Taste, Desi Heart</h3>
        <p class="font-sans text-xs uppercase tracking-[0.3em] text-textMuted mb-8">Ore, Chakand</p>
        <p class="font-body text-sm text-textMuted/50">&copy; 2026 Royal Taste. All Rights Reserved.</p>
    </footer>

    <script>
        // Smooth Navigation Scroll and Background Blur
        const navbar = document.getElementById('navbar');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('shadow-[0_4px_30px_rgba(0,0,0,0.5)]');
                navbar.style.backgroundColor = 'rgba(10, 8, 6, 0.95)';
            } else {
                navbar.classList.remove('shadow-[0_4px_30px_rgba(0,0,0,0.5)]');
                navbar.style.backgroundColor = 'rgba(10, 8, 6, 0.8)';
            }
        });
    </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

