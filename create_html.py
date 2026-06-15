import csv

def generate_html():
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Reels Presentation</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<style>
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
    body {
        background-color: #0f0f0f;
        color: #fff;
        font-family: 'Inter', sans-serif;
        padding: 2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 4rem;
    }
    h1 {
        text-align: center;
        margin-bottom: 2rem;
        font-size: 2.5rem;
        color: #D4AF37;
    }
    .video-group {
        width: 100%;
        max-width: 1200px;
        margin-bottom: 4rem;
    }
    .video-title {
        font-size: 1.5rem;
        color: #888;
        margin-bottom: 1rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-align: center;
    }
    .slides-container {
        display: flex;
        gap: 2rem;
        justify-content: center;
        flex-wrap: wrap;
    }
    .slide {
        width: 320px;
        height: 568px; /* 9:16 aspect ratio approximation */
        background: linear-gradient(135deg, #2a2a2a 0%, #111 100%);
        position: relative;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 2rem;
        text-align: center;
    }

    /* Slide 1 Styles */
    .s1-badge {
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 4px;
        color: #fff;
        position: absolute;
        top: 20%;
    }
    .s1-symptom {
        font-family: 'Inter', sans-serif;
        font-size: 40px; /* Scaled down slightly to fit 320px */
        font-weight: 900;
        line-height: 1.1;
        margin-top: -20%;
        color: #fff;
    }
    .highlight-cyan {
        color: #00F0FF;
    }
    .highlight-gold {
        color: #D4AF37;
    }

    /* Slide 2 Styles */
    .s2-badge {
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 4px;
        color: #fff;
        position: absolute;
        top: 15%;
    }
    .s2-box {
        border: 1px solid rgba(255, 255, 255, 0.25);
        padding: 2rem 1.5rem;
        width: 90%;
        position: relative;
        margin-top: 10%;
    }
    .s2-cause {
        font-family: 'Inter', sans-serif;
        font-size: 18px;
        font-weight: 400;
        margin-bottom: 2rem;
        color: #fff;
        line-height: 1.4;
    }
    .s2-solution {
        font-family: 'Playfair Display', serif;
        font-size: 24px;
        font-weight: 700;
        font-style: italic;
        color: #fff;
        line-height: 1.3;
    }

    /* Slide 3 Styles */
    .s3-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-end;
        height: 100%;
        padding-bottom: 20%;
    }
    .bottle-placeholder {
        width: 120px;
        height: 180px;
        background: rgba(255,255,255,0.1);
        border: 2px dashed rgba(255,255,255,0.3);
        border-radius: 10px;
        margin-bottom: 2rem;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 12px;
        color: rgba(255,255,255,0.5);
        box-shadow: 0 20px 40px rgba(0,0,0,0.8);
    }
    .cta-button {
        background-color: #fff;
        color: #111;
        font-family: 'Inter', sans-serif;
        font-weight: 900;
        font-size: 16px;
        text-transform: uppercase;
        padding: 1rem 2rem;
        border-radius: 30px;
        animation: pulse 2s infinite;
        white-space: nowrap;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.03); }
        100% { transform: scale(1); }
    }
</style>
</head>
<body>
    <h1>High-Ticket Health Affiliate Reels</h1>
"""

    import re

    def process_s1(text):
        parts = text.split('\\n')
        badge = parts[0] if len(parts) > 0 else ""
        symptom = parts[1] if len(parts) > 1 else ""

        words = symptom.split()
        if not words: return badge, symptom

        trigger_words = [
            'screaming', 'suffocated', 'clogged', 'solid', 'dead', 'insane', 'torturing',
            'scorching', 'lava', 'burning', 'agonizing', 'electrocuting', 'paralyzed',
            'frozen', 'agonizingly', 'broken', 'glass', 'savage', 'terrifyingly', 'stubborn',
            'ravenous', 'disastrously', 'disgusting', 'emergency', 'violently', 'spinning',
            'nauseous', 'terrifying', 'severe', 'nausea', 'destroyed', 'forcefully', 'slammed',
            'desperate', 'miserably', 'paralysis', 'buried', 'incapable', 'chaos'
        ]

        # Find the single most aggressive word to highlight (prioritize by length)
        best_match_idx = -1
        best_match_len = -1

        for i, w in enumerate(words):
            clean_w = w.lower().strip(',?.!')
            if clean_w in trigger_words:
                if len(clean_w) > best_match_len:
                    best_match_len = len(clean_w)
                    best_match_idx = i

        highlighted = []
        for i, w in enumerate(words):
            if i == best_match_idx:
                highlighted.append(f'<span class="highlight-cyan">{w}</span>')
            else:
                highlighted.append(w)

        return badge, " ".join(highlighted)

    def process_s2(text):
        parts = text.split('\\n')
        badge = parts[0] if len(parts) > 0 else ""
        rest = parts[1] if len(parts) > 1 else ""

        sentences = rest.split('. ')
        cause = sentences[0] + "." if len(sentences) > 0 else ""
        solution = sentences[1] if len(sentences) > 1 else ""

        # Highlight active solution keywords in Gold
        sol_text = re.sub(
            r"(This\s+(?:\w+\s+){0,2}(?:liquid|oil|vitamin|extract|herb|formula|capsule|blend|enzyme|tea|mix|drop|drops|mineral|plant|acid))",
            r'<span class="highlight-gold">\1</span>',
            solution,
            flags=re.IGNORECASE
        )

        return badge, cause, sol_text

    with open('canva_bulk_data.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader) # skip header

        current_product = ""
        video_count = 1

        for row in reader:
            product = row[0]
            if product != current_product:
                if current_product != "":
                    html_content += "    </div>\n"
                html_content += f'    <div class="video-group">\n'
                html_content += f'        <div class="video-title">{product}</div>\n'
                current_product = product
                video_count = 1

            s1 = row[1]
            s2 = row[2]
            s3 = row[3]

            s1_badge, s1_symptom = process_s1(s1)
            s2_badge, s2_cause, s2_solution = process_s2(s2)

            html_content += f'''
        <h3 style="text-align: center; color: #555; margin: 2rem 0 1rem 0;">Video {video_count}</h3>
        <div class="slides-container">
            <!-- Slide 1 -->
            <div class="slide">
                <div class="s1-badge">{s1_badge}</div>
                <div class="s1-symptom">{s1_symptom}</div>
            </div>
            <!-- Slide 2 -->
            <div class="slide">
                <div class="s2-badge">{s2_badge}</div>
                <div class="s2-box">
                    <div class="s2-cause">{s2_cause}</div>
                    <div class="s2-solution">{s2_solution}</div>
                </div>
            </div>
            <!-- Slide 3 -->
            <div class="slide">
                <div class="s3-container">
                    <div class="bottle-placeholder">[ {product} Bottle PNG ]</div>
                    <div class="cta-button">{s3}</div>
                </div>
            </div>
        </div>
'''
            video_count += 1

        if current_product != "":
            html_content += "    </div>\n"

    html_content += """
</body>
</html>
"""

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

generate_html()
