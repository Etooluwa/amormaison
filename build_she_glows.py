import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract styles
style_match = re.search(r'<style>.*?</style>', index_content, flags=re.DOTALL)
styles = style_match.group(0) if style_match else '<style></style>'

# Extract script
script_match = re.search(r'<script>.*?</script>', index_content, flags=re.DOTALL)
script_code = script_match.group(0) if script_match else '<script></script>'

# Construct new HTML
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>She Glows | Amor Maison</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Manrope:wght@300;400;500&display=swap" rel="stylesheet">
    {styles.replace('</style>', '''
        /* She Glows Specific Styles */
        .hero-bg-glows {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: url('assets/images/she-glows-hero.jpg');
            background-size: cover;
            background-position: center;
            filter: grayscale(100%) contrast(1.1);
            z-index: -2;
            animation: kenBurns 20s linear infinite alternate;
        }

        .focus-text {
            max-width: 900px;
            margin: 0 auto;
            text-align: center;
            font-size: clamp(20px, 2.5vw, 32px);
            line-height: 1.5;
            font-family: var(--font-serif);
        }

        .glow-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 6vw;
            align-items: center;
            margin-top: 100px;
        }

        .glow-text p {
            margin-bottom: 24px;
        }

        .glow-image-wrapper {
            position: relative;
            overflow: hidden;
            aspect-ratio: 4/5;
        }

        .glow-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
            filter: grayscale(100%);
            transition: transform 1.2s cubic-bezier(0.16, 1, 0.3, 1);
        }
        
        .glow-image-wrapper:hover .glow-image {
            transform: scale(1.05);
        }

        @media (max-width: 768px) {
            .glow-grid {
                grid-template-columns: 1fr;
                gap: 40px;
            }
        }
    </style>''')}
</head>
<body>
    <!-- Custom Cursor -->
    <div class="cursor" id="custom-cursor"></div>

    <!-- Navigation Bar -->
    <nav class="nav-wrapper" id="navbar">
        <div class="nav-content">
            <a href="index.html" class="brand-name interactive-el">Amor Maison</a>
            <div class="menu-toggle interactive-el" id="mobile-menu-btn">
                <span></span>
                <span></span>
            </div>
            <div class="nav-links">
                <a href="about.html" class="nav-link interactive-el">About</a>
                <div class="dropdown interactive-el">
                    <span class="nav-link" style="cursor:none;">Maison</span>
                    <div class="dropdown-menu">
                        <a href="fashion.html" class="dropdown-item interactive-el">Fashion</a>
                        <a href="beauty.html" class="dropdown-item interactive-el">Beauty</a>
                        <a href="wellness.html" class="dropdown-item interactive-el">Wellness</a>
                    </div>
                </div>
                <a href="she-glows.html" class="nav-link interactive-el" style="border-bottom: 1px solid currentColor;">She Glows</a>
                <a href="inside-maison.html" class="nav-link interactive-el">Inside The Maison</a>
            </div>
        </div>
    </nav>

    <main>
        <!-- Hero Section -->
        <section class="hero">
            <div class="hero-bg-glows"></div>
            <div class="hero-overlay"></div>
            <div class="hero-content">
                <span class="uppercase-label hero-tagline fade-up">Maison Initiative</span>
                <h1 class="hero-title fade-up delay-1">She Glows</h1>
                <p class="hero-desc fade-up delay-2">An exclusive sanctuary of strategic elevation and uncompromising operational support for female founders in Dubai.</p>
                <div class="fade-up delay-3">
                    <a href="#manifesto" class="btn btn-inverted interactive-el">Explore The Initiative</a>
                </div>
            </div>
        </section>

        <!-- Manifesto / Focus Text -->
        <section id="manifesto" class="section-padding container">
            <div class="fade-up">
                <div class="focus-text">
                    "The ambition to build is universal, but navigating the architectural intricacies of establishing a business in Dubai can be profoundly taxing. We believe that entrepreneurial logistics should never compromise creative energy."
                </div>
            </div>

            <div class="glow-grid fade-up delay-1">
                <div class="glow-image-wrapper">
                    <!-- Business woman abstract -->
                    <img src="assets/images/mq2.jpg" class="glow-image" alt="She Glows Initiative">
                </div>
                <div class="glow-text">
                    <h2 class="italic-serif" style="margin-bottom: 24px;">Frictionless Ascension.</h2>
                    <p>
                        "She Glows" was conceived as an exclusive sanctuary of strategic elevation for female founders.
                        The reality of licensing, jurisdiction, and legal frameworks in the UAE often acts as a massive
                        barrier to profound feminine talent.
                    </p>
                    <p>
                        Our mission is radically simple: we absorb the operational chaos, providing women with a
                        seamless, uncompromisingly luxurious framework to establish their enterprise. From entity
                        incorporation and premium banking liaisons to bespoke real estate advisory for your commercial
                        spaces, we construct the foundation so you can remain inherently focused on the vision.
                    </p>
                </div>
            </div>
        </section>

        <div class="divider fade-up"></div>

        <!-- Services Section Specific to She Glows -->
        <section class="services section-padding container">
            <div class="section-title-wrapper fade-up">
                <h2 class="section-title">Initiative Architecture</h2>
            </div>
            <div class="services-row">
                <div class="service-item fade-up">
                    <span class="uppercase-label">01</span>
                    <h3 class="service-title">Entity Incorporation</h3>
                    <p>Guiding you through the labyrinth of strict jurisdictions and licensing to orchestrate a pristine corporate architecture for your new maison.</p>
                </div>
                <div class="service-item fade-up delay-1">
                    <span class="uppercase-label">02</span>
                    <h3 class="service-title">Premium Banking</h3>
                    <p>Facilitating immaculate introductions and seamless liaison with tier-one financial institutions, securing the fiscal backbone of your venture.</p>
                </div>
                <div class="service-item fade-up delay-2">
                    <span class="uppercase-label">03</span>
                    <h3 class="service-title">Bespoke Real Estate</h3>
                    <p>Exclusive advisory and acquisition of elite commercial spaces, transforming raw square footage into legendary environments of brand expression.</p>
                </div>
            </div>
        </section>

        <div class="divider fade-up"></div>

        <!-- Contact Section -->
        <section id="contact" class="contact section-padding container dark-section">
            <div class="fade-up">
                <h2 class="contact-heading">Establish Your Legacy</h2>
                <div class="contact-info">
                    <span>Paris &mdash; Dubai &mdash; London</span>
                    <span>sheglows@amormaison.com</span>
                    <span>+971 4 000 0000</span>
                </div>
                <a href="inside-maison.html" class="btn btn-inverted interactive-el">Initiate Setup</a>
            </div>
        </section>
    </main>

    <!-- Marquee Carousel -->
    <section class="marquee-wrapper">
        <div class="marquee-track">
            <!-- First Set -->
            <div class="marquee-item"><img src="assets/images/mq1.jpg" alt="Fashion 1"></div>
            <div class="marquee-item"><img src="assets/images/mq2.jpg" alt="Fashion 2"></div>
            <div class="marquee-item"><img src="assets/images/mq3.jpg" alt="Fashion 3"></div>
            <div class="marquee-item"><img src="assets/images/mq4.jpg" alt="Fashion 4"></div>
            <div class="marquee-item"><img src="assets/images/mq5.jpg" alt="Fashion 5"></div>
            <div class="marquee-item"><img src="assets/images/mq6.jpg" alt="Fashion 8"></div>
            <!-- Duplicated Set for Infinite Loop -->
            <div class="marquee-item"><img src="assets/images/mq1.jpg" alt="Fashion 1"></div>
            <div class="marquee-item"><img src="assets/images/mq2.jpg" alt="Fashion 2"></div>
            <div class="marquee-item"><img src="assets/images/mq3.jpg" alt="Fashion 3"></div>
            <div class="marquee-item"><img src="assets/images/mq4.jpg" alt="Fashion 4"></div>
            <div class="marquee-item"><img src="assets/images/mq5.jpg" alt="Fashion 5"></div>
            <div class="marquee-item"><img src="assets/images/mq6.jpg" alt="Fashion 8"></div>
        </div>
    </section>

    <footer class="footer">
        <div>&copy; 2026 Amor Maison. All rights reserved.</div>
        <div class="footer-links">
            <a href="#" class="interactive-el">Instagram</a>
            <a href="#" class="interactive-el">LinkedIn</a>
            <a href="#" class="interactive-el">X</a>
        </div>
    </footer>

    {script_code}
</body>
</html>
"""

with open('/Users/etosegun/Documents/experiments/experiment 3/she-glows.html', 'w', encoding='utf-8') as f:
    f.write(html_template)
print("she-glows.html generated successfully.")
