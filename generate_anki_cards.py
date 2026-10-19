# -*- coding: utf-8 -*-
"""
Generates a comprehensive Anki-importable flashcard deck for Art Appreciation (Lessons 1-4).
Format: Tab-separated values (TSV) with standard Anki metadata headers.
Columns:
1. Front (Definition / Meaning / Clues)
2. Back (Target Word / Technical Term)
3. Tags (Lesson and Category tags)
"""

cards = [
    # =========================================================================
    # LESSON 1: INTRODUCTION TO ART APPRECIATION
    # =========================================================================
    (
        "The study and understanding of the value, significance, and meaning of art, involving the analysis and interpretation of visual and performing arts.",
        "Art Appreciation",
        "ArtAppreciation::Lesson1 ArtAppreciation::Definitions"
    ),
    (
        "The goal of art appreciation that involves learning about the historical, cultural, and social backgrounds in which an artwork was created to understand its purpose.",
        "Understanding Context",
        "ArtAppreciation::Lesson1 ArtAppreciation::Goals"
    ),
    (
        "The goal of art appreciation that entails examining visual tools (line, shape, color, texture, space) and compositional techniques (balance, contrast, unity) used by artists.",
        "Analyzing Elements and Principles",
        "ArtAppreciation::Lesson1 ArtAppreciation::Goals"
    ),
    (
        "The goal of art appreciation focused on identifying distinct eras and aesthetic categories such as Renaissance, Baroque, Impressionism, Modernism, and Contemporary art.",
        "Recognizing Styles and Movements",
        "ArtAppreciation::Lesson1 ArtAppreciation::Goals"
    ),
    (
        "The goal of art appreciation that explores symbolism, themes, messages, artist intentions, and the viewer's personal subjective response.",
        "Interpreting Meaning",
        "ArtAppreciation::Lesson1 ArtAppreciation::Goals"
    ),
    (
        "The goal of art appreciation focused on developing criteria for assessing the beauty, craftsmanship, and effectiveness of an artwork using subjective and objective factors.",
        "Evaluating Aesthetics",
        "ArtAppreciation::Lesson1 ArtAppreciation::Goals"
    ),
    (
        "The key reason why art appreciation is important that provides insight into different traditions, histories, and lifestyles, fostering empathy for diversity.",
        "Cultural Awareness and Understanding",
        "ArtAppreciation::Lesson1 ArtAppreciation::Importance"
    ),
    (
        "The sub-benefit of art appreciation where visual artworks serve as physical historical records, capturing the values, beliefs, and events of past eras.",
        "Preserves History",
        "ArtAppreciation::Lesson1 ArtAppreciation::Importance"
    ),
    (
        "The reason why art appreciation matters that stimulates personal imagination, encourages innovative problem-solving, and offers a non-verbal outlet for feelings.",
        "Personal Growth and Development",
        "ArtAppreciation::Lesson1 ArtAppreciation::Importance"
    ),
    (
        "The educational advantage of art appreciation whereby it intersects with multiple fields like history, literature, philosophy, and psychology.",
        "Interdisciplinary Learning",
        "ArtAppreciation::Lesson1 ArtAppreciation::Importance"
    ),
    (
        "The psychological benefit of engaging with art that fosters present-moment awareness, calm, and attentiveness to the finer details of life.",
        "Mindfulness",
        "ArtAppreciation::Lesson1 ArtAppreciation::Importance"
    ),
    (
        "The first function of art discussed in Lesson 1, centered on aesthetic prettiness and the power to bring dull, lifeless walls and environments to life.",
        "Beauty",
        "ArtAppreciation::Lesson1 ArtAppreciation::Functions"
    ),
    (
        "The function of art demonstrated when uplifting paintings are displayed in daunting hospital environments or when relatable typography inspires optimism.",
        "Happiness and Hope",
        "ArtAppreciation::Lesson1 ArtAppreciation::Functions"
    ),
    (
        "The function of art that provides tangible external expressions to define personal struggles, gender questions, disconnectedness, and mental health.",
        "Identity and Understanding of the Self",
        "ArtAppreciation::Lesson1 ArtAppreciation::Functions"
    ),
    (
        "The generational label cited in Lesson 1 reflecting struggles with disconnectedness from social media, regionalism, and mental health challenges.",
        "The Me Generation (or Anxious Generation)",
        "ArtAppreciation::Lesson1 ArtAppreciation::Concepts"
    ),
    (
        "The psychological and clinical intervention that utilizes artistic creation to help individuals communicate, process trauma, and navigate sensitive experiences.",
        "Art Therapy",
        "ArtAppreciation::Lesson1 ArtAppreciation::Functions"
    ),
    (
        "The function of art prominently emerging after World War II that allows societies to confront human suffering, express pain, and make mourning dignified.",
        "Grief and Healing",
        "ArtAppreciation::Lesson1 ArtAppreciation::Functions"
    ),
    (
        "The British sculptor who created the experiential Judenplatz Holocaust memorial 'Ghost Library' in Vienna, exploring memory in an architectural setting.",
        "Rachel Whiteread",
        "ArtAppreciation::Lesson1 ArtAppreciation::Artists"
    ),
    (
        "The poignant architectural memorial created by Rachel Whiteread in Vienna consisting of cast concrete inverted library books to honor Holocaust victims.",
        "Ghost Library",
        "ArtAppreciation::Lesson1 ArtAppreciation::Artworks"
    ),
    (
        "The civic function of art that uses tangible monuments and landmarks to help communities commemorate national heroes and sustain nationalistic values.",
        "Remembering and Mark-Making",
        "ArtAppreciation::Lesson1 ArtAppreciation::Functions"
    ),
    (
        "The iconic national landmark in Manila cited in Lesson 1 as a prime example of tangible art functioning for remembering and civic nationalism.",
        "Rizal Monument (Luneta Park)",
        "ArtAppreciation::Lesson1 ArtAppreciation::Artworks"
    ),
    (
        "The British sculptor who designed the massive public landmark 'Angel of the North' featuring an imposing human figure with airplane-like wings.",
        "Antony Gormley",
        "ArtAppreciation::Lesson1 ArtAppreciation::Artists"
    ),
    (
        "The colossal 20-meter-tall steel sculpture in Gateshead, England, featuring 54-meter airplane-like wings that serves as an identifying regional landmark.",
        "Angel of the North",
        "ArtAppreciation::Lesson1 ArtAppreciation::Artworks"
    ),
    (
        "The British-Indian sculptor who designed the reflective, bean-shaped metallic public sculpture 'Cloud Gate' in Chicago.",
        "Anish Kapoor",
        "ArtAppreciation::Lesson1 ArtAppreciation::Artists"
    ),
    (
        "The humongous, reflective metallic bean-shaped public sculpture in Millennium Park, Chicago, that anchors place identity in a heavy pedestrian zone.",
        "Cloud Gate (The Bean)",
        "ArtAppreciation::Lesson1 ArtAppreciation::Artworks"
    ),
    (
        "The function of art that uses public visual statements—ranging from protest effigies to political satire—to expose social issues and critique authorities.",
        "Raising Awareness",
        "ArtAppreciation::Lesson1 ArtAppreciation::Functions"
    ),
    (
        "A form of politically charged visual art, such as large paper-mâché effigies burned during street protests, intended to mobilize collective action.",
        "Activist Art (Protest Art)",
        "ArtAppreciation::Lesson1 ArtAppreciation::Concepts"
    ),
    (
        "The architectural and decorative elements in medieval Gothic cathedrals that served as subtle visual methods for educating congregations and raising awareness.",
        "Stained Glass Windows (and Illuminated Manuscripts)",
        "ArtAppreciation::Lesson1 ArtAppreciation::Concepts"
    ),
    (
        "The function of art that unites geographically and culturally dispersed communities by providing localized pride and overcoming historic divisions.",
        "Culture and Togetherness",
        "ArtAppreciation::Lesson1 ArtAppreciation::Functions"
    ),
    (
        "The historic colonial military and political strategy used by Spanish colonizers in the Philippines that fractured regional unity, which localized art helps redeem.",
        "Divide and Conquer",
        "ArtAppreciation::Lesson1 ArtAppreciation::Concepts"
    ),
    (
        "The reigning titleholder who wore a 2019 national costume symbolically unifying the Philippines by integrating cultural elements from Luzon, Visayas, and Mindanao.",
        "Catriona Gray",
        "ArtAppreciation::Lesson1 ArtAppreciation::Concepts"
    ),
    (
        "The Spanish romantic master who painted 'The Third of May 1808', depicting the brutal execution of Spanish resistance fighters by Napoleon's troops.",
        "Francisco Goya",
        "ArtAppreciation::Lesson1 ArtAppreciation::Artists"
    ),
    (
        "The famous historical painting by Francisco Goya depicting the horrors of war and execution of Spanish patriots by French soldiers.",
        "The Third of May 1808",
        "ArtAppreciation::Lesson1 ArtAppreciation::Artworks"
    ),
    (
        "The Filipino master painter who created 'Spoliarium', which won a gold medal at the 1884 Madrid Exposición Nacional de Bellas Artes.",
        "Juan Luna",
        "ArtAppreciation::Lesson1 ArtAppreciation::Artists"
    ),
    (
        "The monumental painting by Juan Luna depicting dead Roman gladiators being dragged into the dark basement of the Coliseum, symbolizing colonial oppression.",
        "Spoliarium",
        "ArtAppreciation::Lesson1 ArtAppreciation::Artworks"
    ),

    # =========================================================================
    # LESSON 2: LANGUAGE OF ART: ELEMENTS OF ART
    # =========================================================================
    (
        "The foundational visual tools—described as the 'ingredients' of visual communication—used by artists to construct artworks.",
        "Elements of Art",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "The essential one-dimensional element of art that provides the impression of path and movement across a space.",
        "Line",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "The term defining the amount of space a line occupies in an artwork, differentiated based on length, width, and thickness.",
        "Dimension",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "Lines whose movement direction moves upward or downward, representing upright human posture, architectural pillars, and stability.",
        "Vertical Lines",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "Lines that run horizontally from left to right or vice-versa, evoking the horizon, a lying body, calmness, and static rest.",
        "Horizontal Lines",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "Slanted lines that convey an impression of rising or falling, frequently utilized to express instability, tension, and dynamic excitement.",
        "Diagonal Lines",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "Connected combinations of diagonal lines forming sharp angles that convey feelings of chaos, confusion, anxiety, or lightning-like energy.",
        "Zigzag Lines",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "Non-linear lines whose directions are fluid and not rigidly established, capturing natural forms like clouds, leaves, and petals.",
        "Curved Lines",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "Lines that define the edges, silhouette, and inner structural planes of a subject, effectively mapping its three-dimensional form without shading.",
        "Contour Lines",
        "ArtAppreciation::Lesson2 ArtAppreciation::Techniques"
    ),
    (
        "A rapid, highly expressive sketching technique used to capture the movement, weight, and essential life energy of a subject rather than fine details.",
        "Gesture Drawing",
        "ArtAppreciation::Lesson2 ArtAppreciation::Techniques"
    ),
    (
        "The art of beautiful handwriting, often associated with Asian characters where line strokes represent character language.",
        "Calligraphy",
        "ArtAppreciation::Lesson2 ArtAppreciation::Techniques"
    ),
    (
        "The ancestral writing traditions from which Philippine calligraphy developed, including Indian, Sulawesi, Kawi, Indo-Arabic, and Islamic scripts.",
        "Ethno-linguistic Calligraphic Roots",
        "ArtAppreciation::Lesson2 ArtAppreciation::Concepts"
    ),
    (
        "A defined two-dimensional area created and enclosed by an outline, having length and width but lacking depth.",
        "Shape",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "Shapes governed by precise mathematical measurements and formulas, including circles, squares, rectangles, triangles, and polygons.",
        "Geometric Shapes",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "Irregular, asymmetric shapes composed of flowing curves and uneven angles, typically found in natural entities like leaves, animals, and clouds.",
        "Free-form Shapes (Organic Shapes)",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "The three-dimensional counterpart of shape that possesses depth, volume, and mass in addition to length and width.",
        "Form",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "The characterizing spatial component that fundamentally distinguishes a three-dimensional form from a two-dimensional shape.",
        "Depth",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "The Italian term meaning 'bright' and 'dark', referring to strong tonal contrasts between light and shadow used to render 3D volume on a flat surface.",
        "Chiaroscuro",
        "ArtAppreciation::Lesson2 ArtAppreciation::Techniques"
    ),
    (
        "The literal Italian root word in chiaroscuro that translates to 'bright' or 'light'.",
        "Chiaro",
        "ArtAppreciation::Lesson2 ArtAppreciation::Concepts"
    ),
    (
        "The literal Italian root word in chiaroscuro that translates to 'dark' or 'obscure'.",
        "Oscuro",
        "ArtAppreciation::Lesson2 ArtAppreciation::Concepts"
    ),
    (
        "The Italian Baroque painter whose 1602 masterpiece 'Divine Love Conquering Earthly Love' exemplifies masterful chiaroscuro lighting.",
        "Giovanni Baglione",
        "ArtAppreciation::Lesson2 ArtAppreciation::Artists"
    ),
    (
        "The 1602–1603 masterwork by Giovanni Baglione cited in Lesson 2 to demonstrate dramatic light-and-dark chiaroscuro modeling.",
        "Divine Love Conquering Earthly Love",
        "ArtAppreciation::Lesson2 ArtAppreciation::Artworks"
    ),
    (
        "The hypothetical area in which the subject and other artistic elements operate, encompassing both inner boundaries and external surrounds.",
        "Space",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "The primary subject, figure, object, or occupied focal area within an artwork's composition.",
        "Positive Space",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "The unoccupied, empty area that surrounds or passes between the primary subjects of an artwork, framing the composition.",
        "Negative Space",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "The element of art derived from light and the varied spectral reflections perceived by the human eye.",
        "Color",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "The pure, base color family on the color wheel determined by dominant spectral wavelength, without the addition of white, black, or gray.",
        "Hue",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "The property of color that describes its relative lightness or darkness, altered by adding white (tint) or black (shade).",
        "Value",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "The property of color that refers to its brightness, saturation, or purity; high when unmixed, and dull when gray or a complement is added.",
        "Intensity (Saturation)",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "The state of a pure, unadulterated hue straight from the spectrum or pigment tube, characterized by maximum brightness and purity.",
        "High Intensity",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "Colors positioned directly opposite one another on the color wheel which, when mixed together, neutralize intensity and produce dull tones.",
        "Complementary Colors",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "The element of art describing how a surface physically feels to the touch (tactile) or how it is visually simulated through light and shadow.",
        "Texture",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "Surfaces that scatter uneven, jagged shadows and reflect irregular light patterns, conveying coarse physical tactile quality.",
        "Rough Texture",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "Surfaces that cast uniform, consistent shadows and reflect light evenly without physical or visual resistance.",
        "Smooth Texture",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "Surfaces such as denim, unfinished wood, paper, and human skin that absorb glare and reflect soft, dull light.",
        "Matte Texture (Matte Surface)",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "Surfaces like calm water or polished glass windows that produce sharp, bright highlights and mirror-like specular reflections.",
        "Shiny Texture (Glossy Surface)",
        "ArtAppreciation::Lesson2 ArtAppreciation::Elements"
    ),
    (
        "The artistic technique where paper is placed over a raised textured surface and rubbed with graphite, crayon, or pastel to capture its texture.",
        "Frottage Technique",
        "ArtAppreciation::Lesson2 ArtAppreciation::Techniques"
    ),

    # =========================================================================
    # LESSON 3: PRINCIPLES OF DESIGN & PSYCHOLOGY IN ART
    # =========================================================================
    (
        "Long-held compositional techniques and guidelines proven and used by fine and graphic artists to organize elements and communicate ideas effectively.",
        "Principles of Design",
        "ArtAppreciation::Lesson3 ArtAppreciation::Principles"
    ),
    (
        "The principle of design defined by the repeated arrangement of elements that suggests visual movement, tempo, or continuous flow.",
        "Rhythm",
        "ArtAppreciation::Lesson3 ArtAppreciation::Principles"
    ),
    (
        "The perception of movement stimulated when alternating positive shapes are rhythmically separated by negative spaces across a field.",
        "Visual Rhythm",
        "ArtAppreciation::Lesson3 ArtAppreciation::Principles"
    ),
    (
        "The principle of design defined by the consistent, organized, and predictable repetition of elements, serving both decorative and structural purposes.",
        "Pattern",
        "ArtAppreciation::Lesson3 ArtAppreciation::Principles"
    ),
    (
        "A type of rhythm or pattern characterized by a complete absence of regularity or uniform intervals between repeating units.",
        "Random Pattern",
        "ArtAppreciation::Lesson3 ArtAppreciation::Principles"
    ),
    (
        "A type of rhythm or pattern characterized by identical motifs, standardized beats, and unchanging intervals of space.",
        "Regular Pattern",
        "ArtAppreciation::Lesson3 ArtAppreciation::Principles"
    ),
    (
        "A type of pattern or rhythm that alternates between two distinct motifs or changes the distance between beats in a regular sequence.",
        "Alternating Pattern",
        "ArtAppreciation::Lesson3 ArtAppreciation::Principles"
    ),
    (
        "A type of rhythm or pattern in which the repeated motif undergoes a steady, gradual change in size, value, or form with every repetition.",
        "Progressive Pattern",
        "ArtAppreciation::Lesson3 ArtAppreciation::Principles"
    ),
    (
        "The principle of design concerned with distributing visual weight so that all elements are accorded equal visual force and stability.",
        "Balance",
        "ArtAppreciation::Lesson3 ArtAppreciation::Principles"
    ),
    (
        "The perceived gravitational pull or visual prominence that each element carries based on its size, color intensity, texture, and placement.",
        "Visual Weight",
        "ArtAppreciation::Lesson3 ArtAppreciation::Principles"
    ),
    (
        "The type of balance demonstrating equal visual weight on opposing sides of a central axis, often called bilateral symmetry.",
        "Formal Balance (Symmetrical Balance)",
        "ArtAppreciation::Lesson3 ArtAppreciation::Principles"
    ),
    (
        "The type of balance where compositional elements radiate outward in all directions from a centralized focal anchor.",
        "Radial Balance",
        "ArtAppreciation::Lesson3 ArtAppreciation::Principles"
    ),
    (
        "The circular geometric design representing wholeness and radial balance, utilized by Carl Jung in his psychological theory of personality.",
        "Mandala",
        "ArtAppreciation::Lesson3 ArtAppreciation::Concepts"
    ),
    (
        "The founder of Analytic Psychology who analyzed mandalas as visual manifestations of balanced inner selfhood and psychic wholeness.",
        "Carl Jung",
        "ArtAppreciation::Lesson3 ArtAppreciation::Psychology"
    ),
    (
        "The type of balance achieved through non-identical arrangements on either side of a composition, offering complex, dynamic visual interest without exact symmetry.",
        "Informal Balance (Asymmetrical Balance)",
        "ArtAppreciation::Lesson3 ArtAppreciation::Principles"
    ),
    (
        "The principle of design that relates the size, amount, or location of one part of an artwork to another internal part.",
        "Proportion",
        "ArtAppreciation::Lesson3 ArtAppreciation::Principles"
    ),
    (
        "The famous pen-and-ink drawing by Leonardo da Vinci illustrating ideal human anatomical proportions inscribed within a square and a circle.",
        "Vitruvian Man",
        "ArtAppreciation::Lesson3 ArtAppreciation::Artworks"
    ),
    (
        "The Renaissance master who created the 'Vitruvian Man' and 'Madonna of the Rocks', demonstrating mathematical and geometric composition.",
        "Leonardo da Vinci",
        "ArtAppreciation::Lesson3 ArtAppreciation::Artists"
    ),
    (
        "The mathematical ratio (approx. 1:1.618) explored by ancient Greek thinkers as the ideal aesthetic proportion in nature and design.",
        "Golden Mean (Golden Ratio)",
        "ArtAppreciation::Lesson3 ArtAppreciation::Principles"
    ),
    (
        "The ancient Greek philosopher and mathematician who believed the universe operated on constant mathematical equations, laying the groundwork for geometric ratios.",
        "Pythagoras",
        "ArtAppreciation::Lesson3 ArtAppreciation::Concepts"
    ),
    (
        "The Greek mathematician who investigated the mathematical principles of proportion and formalized the perfect geometric ratio.",
        "Euclid",
        "ArtAppreciation::Lesson3 ArtAppreciation::Concepts"
    ),
    (
        "The principle of design that relates the overall size of an object or artwork to a standardized external reference, such as the human body or a ruler.",
        "Scale",
        "ArtAppreciation::Lesson3 ArtAppreciation::Principles"
    ),
    (
        "The fundamental distinction between proportion and scale: proportion governs internal part-to-part relationships, whereas scale governs comparison to an external standard.",
        "Proportion vs. Scale",
        "ArtAppreciation::Lesson3 ArtAppreciation::Principles"
    ),
    (
        "The principle of design that breeds visual interest and prevents monotony by introducing contrasting shapes, lines, colors, and textures.",
        "Variety",
        "ArtAppreciation::Lesson3 ArtAppreciation::Principles"
    ),
    (
        "The principle of design that establishes visual dominance to draw the viewer's attention to a particular focal area or subject.",
        "Emphasis",
        "ArtAppreciation::Lesson3 ArtAppreciation::Principles"
    ),
    (
        "The type of emphasis achieved by making an individual element—such as a vibrant hue or stark line—stand out within the composition.",
        "Emphasizing Elements",
        "ArtAppreciation::Lesson3 ArtAppreciation::Techniques"
    ),
    (
        "The type of emphasis achieved by making a specific physical quadrant or zone of the artwork the primary center of viewer focus.",
        "Emphasizing Area (Focal Point)",
        "ArtAppreciation::Lesson3 ArtAppreciation::Techniques"
    ),
    (
        "The technique in emphasis that uses stark differences in value, color intensity, or line density (e.g. cross-hatching) to highlight the subject.",
        "Contrast (Emphasis Technique)",
        "ArtAppreciation::Lesson3 ArtAppreciation::Techniques"
    ),
    (
        "The technique in emphasis where the subject is physically separated or isolated from other surrounding elements in space.",
        "Isolation",
        "ArtAppreciation::Lesson3 ArtAppreciation::Techniques"
    ),
    (
        "The technique in emphasis where an object is placed in the exact center of the visual field, where eyes naturally gravitate.",
        "Location (Central Placement)",
        "ArtAppreciation::Lesson3 ArtAppreciation::Techniques"
    ),
    (
        "The emphasis technique where visual elements, lines, and gaze directions lead inward to converge directly upon the focal point.",
        "Convergence",
        "ArtAppreciation::Lesson3 ArtAppreciation::Techniques"
    ),
    (
        "The unconventional emphasis technique that introduces an unexpected, jarring element—such as a gun on a bed of roses or a single yellow chair among black chairs.",
        "Unusual (Odd-One-Out)",
        "ArtAppreciation::Lesson3 ArtAppreciation::Techniques"
    ),
    (
        "The principle of design where distinct elements work well together and blend smoothly, creating a pleasing and cohesive relationship that facilitates unity.",
        "Harmony",
        "ArtAppreciation::Lesson3 ArtAppreciation::Principles"
    ),
    (
        "The overarching principle of design representing the quality of wholeness and oneness achieved when all elements and principles work together as a complete whole.",
        "Unity",
        "ArtAppreciation::Lesson3 ArtAppreciation::Principles"
    ),
    (
        "The method of achieving unity by editing out unnecessary details and limiting visual qualities strictly to what is essential to the subject.",
        "Simplicity",
        "ArtAppreciation::Lesson3 ArtAppreciation::Techniques"
    ),
    (
        "The method of achieving unity across a large space or structure by repeatedly utilizing matching architectural or visual components.",
        "Repetition",
        "ArtAppreciation::Lesson3 ArtAppreciation::Techniques"
    ),
    (
        "The method of achieving unity by grouping or clustering objects closely together, thereby limiting empty negative space between them.",
        "Proximity",
        "ArtAppreciation::Lesson3 ArtAppreciation::Techniques"
    ),
    (
        "The study of how human observers perceive imagery, organize visual data into meaningful structures, and respond emotionally to art.",
        "Psychology in Art",
        "ArtAppreciation::Lesson3 ArtAppreciation::Psychology"
    ),
    (
        "The psychological theory asserting that human perception recognizes the unified whole before analyzing its discrete constituent parts.",
        "Gestalt Theory",
        "ArtAppreciation::Lesson3 ArtAppreciation::Psychology"
    ),
    (
        "The conservation organization logo cited in Lesson 3 where the human brain combines disjointed black patches into a complete panda silhouette.",
        "WWF Panda Logo",
        "ArtAppreciation::Lesson3 ArtAppreciation::Psychology"
    ),
    (
        "The psychological study of the emotional and symbolic associations that distinct hues evoke across cultural contexts.",
        "Color Psychology",
        "ArtAppreciation::Lesson3 ArtAppreciation::Psychology"
    ),
    (
        "The architectural and compositional shape that traditionally symbolizes femininity (womb-like shape), eternity (lack of corners), and social wholeness.",
        "Half-Circle (Dome)",
        "ArtAppreciation::Lesson3 ArtAppreciation::Psychology"
    ),
    (
        "The geometric compositional arrangement that symbolizes stability, balance, and interconnectedness, directing visual focus upward toward an apex figure.",
        "Triangle (Pyramidal Composition)",
        "ArtAppreciation::Lesson3 ArtAppreciation::Psychology"
    ),
    (
        "The Leonardo da Vinci masterpiece demonstrating a stable triangular composition with the Virgin Mary positioned at the supreme apex.",
        "Madonna of the Rocks",
        "ArtAppreciation::Lesson3 ArtAppreciation::Artworks"
    ),
    (
        "Invisible lines suggested by the direction of figures' gazes, pointing limbs, or aligned shapes that guide the viewer's eye toward the focal point.",
        "Implied Lines",
        "ArtAppreciation::Lesson3 ArtAppreciation::Elements"
    ),

    # =========================================================================
    # LESSON 4: MATERIALS AND TECHNIQUES
    # =========================================================================
    (
        "The physical substances—traditional or modern—that artists utilize to create artwork, influencing its color, texture, and durability.",
        "Materials (Artistic Media)",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "The specific methods, processes, and manipulative skills artists use to shape and control physical materials into an artwork.",
        "Techniques",
        "ArtAppreciation::Lesson4 ArtAppreciation::Techniques"
    ),
    (
        "One of the most foundational and versatile artistic practices, functioning both as a preparatory study for other media and as an independent standalone art form.",
        "Drawing",
        "ArtAppreciation::Lesson4 ArtAppreciation::Techniques"
    ),
    (
        "A highly accessible dry drawing medium made by encasing a graphite core in wood, capable of producing precise lines and tonal values.",
        "Pencil (Graphite Pencil)",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "Pencil grades that contain harder graphite, producing lighter, crisper, and more delicate lines for technical and preparatory work.",
        "H Grade Pencils",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "Pencil grades that contain softer graphite, producing darker, richer, and more velvety black marks well-suited for deep shading.",
        "B Grade Pencils",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "The German Renaissance master who created a remarkably precise 'Self-Portrait at 13' in 1484 using delicate linear drawing.",
        "Albrecht Dürer",
        "ArtAppreciation::Lesson4 ArtAppreciation::Artists"
    ),
    (
        "The 1484 drawing masterwork by Albrecht Dürer that exemplifies early virtuosity in pencil/silverpoint drawing, value, and depth.",
        "Self-Portrait at 13",
        "ArtAppreciation::Lesson4 ArtAppreciation::Artworks"
    ),
    (
        "A traditional drawing medium made from burned wood or compressed carbon, renowned for producing intense, velvety matte blacks and dramatic contrasts.",
        "Charcoal",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "An uncompressed charcoal medium that produces light, soft, erasable marks ideal for quick sketches and initial layout studies.",
        "Vine Charcoal",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "A dense charcoal medium bound with clay or gum that creates bold, dark, permanent marks resistant to erasing.",
        "Compressed Charcoal",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "The British sculptor and official war artist whose charcoal drawings captured civilians taking shelter in the London Underground during the Blitz.",
        "Henry Moore",
        "ArtAppreciation::Lesson4 ArtAppreciation::Artists"
    ),
    (
        "The series of wartime charcoal drawings by Henry Moore depicting vulnerable Londoners sheltering in subway tunnels during WWII air raids.",
        "London Blitz Shelter Drawings",
        "ArtAppreciation::Lesson4 ArtAppreciation::Artworks"
    ),
    (
        "The 1982 mixed-media drawing by Henry Moore exploring maternal protection, vulnerability, and human safety.",
        "Sleeping Mother and Child",
        "ArtAppreciation::Lesson4 ArtAppreciation::Artworks"
    ),
    (
        "A dry drawing medium composed of pigment bound with wax, offering vibrant color saturation and a firm, graphic immediacy.",
        "Crayon (Wax Crayon)",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "A dry drawing medium made of powdered pigment held together with a minimal amount of gum or resin binder, producing soft, blendable, painterly effects.",
        "Chalk Pastels (Soft Pastels)",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "The French Impressionist artist celebrated for his layered chalk pastel depictions of ballerinas and stage lighting.",
        "Edgar Degas",
        "ArtAppreciation::Lesson4 ArtAppreciation::Artists"
    ),
    (
        "The 1878 pastel masterpiece by Edgar Degas depicting a solo ballerina floating across the stage amidst luminous theatrical illumination.",
        "The Star",
        "ArtAppreciation::Lesson4 ArtAppreciation::Artworks"
    ),
    (
        "A drawing medium consisting of pigment mixed with an oil-based binder, yielding a creamy, non-powdery stroke that adheres to paper, wood, and canvas.",
        "Oil Pastels",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "The Flemish Baroque master who created 'Study Head of a Young Woman' using oil-based drawing media on paper mounted to wood.",
        "Anthony van Dyck",
        "ArtAppreciation::Lesson4 ArtAppreciation::Artists"
    ),
    (
        "The oil-based drawing study on paper laid on wood created by Anthony van Dyck demonstrating subtle transitions in facial contours.",
        "Study Head of a Young Woman",
        "ArtAppreciation::Lesson4 ArtAppreciation::Artworks"
    ),
    (
        "An ancient liquid drawing technique applied using pens, quills, or brushes, prized for its permanence, sharp lines, and gestural washes.",
        "Ink Drawing",
        "ArtAppreciation::Lesson4 ArtAppreciation::Techniques"
    ),
    (
        "The Dutch master who demonstrated the humorous, biting, and expressive capabilities of pen and ink in his 1644 drawing 'Satire on Art Criticism'.",
        "Rembrandt van Rijn",
        "ArtAppreciation::Lesson4 ArtAppreciation::Artists"
    ),
    (
        "The 1644 pen-and-ink drawing by Rembrandt featuring gestural lines and biting satirical commentary on art critics.",
        "Satire on Art Criticism",
        "ArtAppreciation::Lesson4 ArtAppreciation::Artworks"
    ),
    (
        "A historic visual art form involving the application of pigment suspended in a liquid medium onto a two-dimensional supporting surface.",
        "Painting",
        "ArtAppreciation::Lesson4 ArtAppreciation::Techniques"
    ),
    (
        "A delicate, transparent painting medium composed of finely ground pigments bound with a water-soluble gum arabic binder.",
        "Watercolor",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "The natural water-soluble gum binder derived from the acacia tree, traditionally used in watercolor and gouache paints.",
        "Gum Arabic",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "The high-grade, durable, absorbent paper made from pure cotton fibers that serves as the premier substrate for watercolor painting.",
        "100% Cotton Rag Paper",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "The speckled, textured pigment effect that naturally occurs when fluid watercolor washes pool in the hollows of rough-textured cotton paper.",
        "Granulation",
        "ArtAppreciation::Lesson4 ArtAppreciation::Techniques"
    ),
    (
        "An opaque water-based painting medium—often called 'opaque watercolor'—containing gum arabic supplemented with white chalk or inert pigment.",
        "Gouache",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "A 20th-century water-based paint formulated from synthetic acrylic polymer resin, celebrated for vibrant hues, rapid drying, and waterproof permanence.",
        "Acrylic Paint",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "The synthetic chemical emulsion binder that cures into a durable, flexible, water-resistant plastic film in acrylic paint.",
        "Synthetic Polymers (Acrylic Emulsion)",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "The mural painting technique where water-ground pigments are applied directly onto wet lime plaster, fusing chemically into the wall as it cures.",
        "Buon Fresco (True Fresco)",
        "ArtAppreciation::Lesson4 ArtAppreciation::Techniques"
    ),
    (
        "The Italian term meaning 'a day's work', referring to the specific patch of wet plaster a fresco painter must plaster and complete in a single session.",
        "Giornata",
        "ArtAppreciation::Lesson4 ArtAppreciation::Concepts"
    ),
    (
        "The Vatican papal chapel whose ceiling and altar wall were executed by Michelangelo in monumental buon fresco.",
        "Sistine Chapel",
        "ArtAppreciation::Lesson4 ArtAppreciation::Artworks"
    ),
    (
        "The mural technique where pigments are applied onto cured, dry plaster using a binder; easier to execute but far less permanent than buon fresco.",
        "Fresco Secco (Dry Fresco)",
        "ArtAppreciation::Lesson4 ArtAppreciation::Techniques"
    ),
    (
        "The revolutionary medium popularized in the 15th century using drying oils (like linseed) that allowed for slow drying, luminous blending, and intricate detail.",
        "Oil Painting",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "The oil painting technique of applying thin, transparent or semi-transparent coats of oil color over dried opaque underlayers to produce luminous depth.",
        "Glazing",
        "ArtAppreciation::Lesson4 ArtAppreciation::Techniques"
    ),
    (
        "The Northern Renaissance painter whose revolutionary glazing technique in the 'Arnolfini Portrait' demonstrated the supreme luminosity of oil paint.",
        "Jan van Eyck",
        "ArtAppreciation::Lesson4 ArtAppreciation::Artists"
    ),
    (
        "The 1434 double portrait by Jan van Eyck renowned for its exquisite oil glazing, complex symbolism, and luminous surface textures.",
        "Arnolfini Portrait",
        "ArtAppreciation::Lesson4 ArtAppreciation::Artworks"
    ),
    (
        "An ancient and medieval painting medium consisting of ground pigment mixed with an egg yolk emulsion, producing a smooth, fast-drying, matte finish.",
        "Tempera (Egg Tempera)",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "The traditional natural water-soluble fat-and-protein emulsion binder used to bind pigments in classical tempera painting.",
        "Egg Yolk",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "An ancient painting medium where pigments are blended into molten beeswax and applied to wooden panels while warm.",
        "Encaustic Painting",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "The natural preservative and binder in encaustic painting that renders the artwork remarkably resistant to moisture and atmospheric decay.",
        "Heated Beeswax",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "The remarkably lifelike funerary portraits painted in encaustic on wooden panels from Roman Egypt (1st–3rd centuries CE) attached to mummies.",
        "Fayum Mummy Portraits",
        "ArtAppreciation::Lesson4 ArtAppreciation::Artworks"
    ),
    (
        "The Fayum mummy portrait cited in Lesson 4 illustrating luminous, lifelike skin tones achieved via encaustic beeswax painting.",
        "Portrait of the Boy Eutyches",
        "ArtAppreciation::Lesson4 ArtAppreciation::Artworks"
    ),
    (
        "A three-dimensional art form created by shaping, carving, modeling, or assembling materials like stone, wood, metal, or clay in space.",
        "Sculpture",
        "ArtAppreciation::Lesson4 ArtAppreciation::Techniques"
    ),
    (
        "The sculpting technique that involves building up malleable materials like clay, wax, or plaster onto an armature to construct a form.",
        "Additive Process (Sculpture)",
        "ArtAppreciation::Lesson4 ArtAppreciation::Techniques"
    ),
    (
        "The terracotta commemorative portrait heads modeled over an armature by the Akan peoples of Ghana, exemplifying additive sculpting.",
        "Memorial Head (Nsodie)",
        "ArtAppreciation::Lesson4 ArtAppreciation::Artworks"
    ),
    (
        "The sculptural technique that entails carving, chiseling, or cutting away material from a larger block of stone or wood to reveal the form within.",
        "Subtractive Process (Sculpture)",
        "ArtAppreciation::Lesson4 ArtAppreciation::Techniques"
    ),
    (
        "The monumental marble sculpture carved by Michelangelo from 1501 to 1504 using chisels in a tour de force of subtractive carving.",
        "Michelangelo's David",
        "ArtAppreciation::Lesson4 ArtAppreciation::Artworks"
    ),
    (
        "The sculptural method where a perishable or initial material is duplicated and replaced by a more permanent substance (such as bronze) via a mold.",
        "Substitution / Casting Method",
        "ArtAppreciation::Lesson4 ArtAppreciation::Techniques"
    ),
    (
        "The 6,000-year-old metal casting method where molten bronze replaces a melted wax model encased within a heat-resistant mold.",
        "Lost-wax Technique (Cire Perdue)",
        "ArtAppreciation::Lesson4 ArtAppreciation::Techniques"
    ),
    (
        "An artistic process where repeatable designs are transferred from an inked matrix plate onto paper or fabric using mechanical pressure.",
        "Printmaking",
        "ArtAppreciation::Lesson4 ArtAppreciation::Techniques"
    ),
    (
        "The prepared working surface (woodblock, metal plate, stone, or screen) from which ink is transferred to paper in printmaking.",
        "Matrix",
        "ArtAppreciation::Lesson4 ArtAppreciation::Concepts"
    ),
    (
        "The printmaking technique where non-image areas are carved away from a block, leaving the raised image areas to receive ink from a roller.",
        "Relief Printmaking",
        "ArtAppreciation::Lesson4 ArtAppreciation::Techniques"
    ),
    (
        "The hand roller used in relief printmaking to spread ink evenly across the raised surface of a woodcut or linocut block.",
        "Brayer",
        "ArtAppreciation::Lesson4 ArtAppreciation::Materials"
    ),
    (
        "The printmaking process where lines are incised into a metal plate, ink is wiped into the grooves, and damp paper is forced in under high pressure.",
        "Intaglio Printmaking",
        "ArtAppreciation::Lesson4 ArtAppreciation::Techniques"
    ),
    (
        "The printmaking category (such as lithography) where the inked image and non-image areas exist on the exact same flat planar surface without raised or recessed cuts.",
        "Planar Printmaking (Planographic Printing)",
        "ArtAppreciation::Lesson4 ArtAppreciation::Techniques"
    )
]

# Write to tab-separated file for Anki
output_filename = "anki_art_appreciation_full_deck.txt"

with open(output_filename, "w", encoding="utf-8") as f:
    # Standard Anki Import Directives
    f.write("#separator:tab\n")
    f.write("#html:true\n")
    f.write("#tags column:3\n")
    
    for front, back, tags in cards:
        # Clean tabs and newlines
        clean_front = front.replace("\t", " ").strip()
        clean_back = back.replace("\t", " ").strip()
        clean_tags = tags.strip()
        f.write(f"{clean_front}\t{clean_back}\t{clean_tags}\n")

print(f"Successfully generated {len(cards)} Anki flashcards in '{output_filename}'!")
