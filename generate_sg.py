import re

def main():
    with open('beauty.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract head and nav
    head_nav_match = re.search(r'(.*?<body>.*?<main>)', content, re.DOTALL)
    if not head_nav_match:
        print("Could not find head/nav")
        return
    head_nav = head_nav_match.group(1)
    
    # Update title
    head_nav = head_nav.replace('<title>Beauty | Amor Maison</title>', '<title>She Glows | Amor Maison</title>')

    # Add custom styles for She Glows
    custom_styles = """
        /* She Glows Specific Styles */
        .she-glows-hero-bg {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: url('assets/images/she-glows-hero.jpg');
            background-size: cover;
            background-position: center;
            filter: grayscale(100%) contrast(1.1);
            z-index: -2;
            animation: kenBurns 20s linear infinite alternate;
        }
        .two-col-layout {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 60px;
            align-items: center;
            margin-top: 80px;
        }
        .content-image {
            width: 100%;
            height: auto;
            filter: grayscale(100%);
        }
        .content-text p {
            margin-bottom: 20px;
        }
        @media (max-width: 768px) {
            .two-col-layout {
                grid-template-columns: 1fr;
            }
        }
    """
    head_nav = head_nav.replace('</style>', custom_styles + '\n    </style>')

    # Extract footer and scripts
    footer_scripts_match = re.search(r'(<!-- Marquee Carousel -->.*)', content, re.DOTALL)
    if not footer_scripts_match:
        print("Could not find footer/scripts")
        return
    footer_scripts = footer_scripts_match.group(1)

    # Custom main content for She Glows
    main_content = """
        <!-- Hero Section -->
        <section class="page-hero">
            <div class="she-glows-hero-bg"></div>
            <div class="page-hero-overlay"></div>
            <div class="page-hero-content">
                <span class="uppercase-label fade-up">Empowering Women in Dubai</span>
                <h1 class="page-hero-title fade-up delay-1">She Glows</h1>
            </div>
        </section>

        <!-- Focus Text -->
        <section class="manifesto section-padding container">
            <div class="fade-up">
                <div class="focus-text">
                    Starting a business in Dubai presents unique opportunities and challenges. 'She Glows' is an initiative dedicated to guiding and empowering women entrepreneurs through the intricacies of business setup, strategic positioning, and launch in the UAE, ensuring you build a brand that not only succeeds but leaves a lasting legacy.
                </div>
            </div>
        </section>

        <!-- Information Section -->
        <section class="container fade-up delay-1" style="padding-bottom: var(--spacing-section);">
            <div class="two-col-layout">
                <div class="content-text">
                    <h2 class="italic-serif mb-40">Navigate with Confidence.</h2>
                    <br>
                    <p>From understanding legal structures to establishing a distinguished brand presence, the journey to entrepreneurship requires both resilience and expert guidance.</p>
                    <p>We provide comprehensive support, connecting you with vital resources, elite mentorship, and the definitive strategic roadmap needed to seamlessly start and scale your enterprise in Dubai.</p>
                </div>
                <div class="content-image-wrapper">
                    <img src="assets/images/grid1.jpg" alt="Woman entrepreneur" class="content-image">
                </div>
            </div>
        </section>

        <!-- The divide -->
        <div class="divider fade-up"></div>

        <!-- Contact Section -->
        <section id="contact" class="contact section-padding container dark-section">
            <div class="fade-up">
                <h2 class="contact-heading">Begin Your Journey</h2>

                <div class="contact-info">
                    <span>Dubai &mdash; Paris &mdash; London</span>
                    <span>sheglows@amormaison.com</span>
                    <span>+971 50 000 0000</span>
                </div>
                <a href="inside-maison.html" class="btn btn-inverted interactive-el">Connect With Us</a>
            </div>
        </section>
    </main>
    """

    final_html = head_nav + main_content + footer_scripts

    with open('she-glows.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

    print("Successfully created she-glows.html")

if __name__ == '__main__':
    main()
