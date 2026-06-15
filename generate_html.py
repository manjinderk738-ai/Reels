import csv
import io

data = r""""Product","Slide 1 Hook","Slide 2 Cause & Solution","Slide 3 CTA"
"ZenCortex","⚠️ HEALTH ALERT\nRinging won't stop screaming?","🧬 CLINICAL UPDATE\nSwelling chokes your hearing wires. This liquid silences the noise.","👉 [LINK IN BIO NOW]"
"ZenCortex","⚠️ HEALTH ALERT\nEars feel clogged tight?","🧬 CLINICAL UPDATE\nToxic buildup blocks your sound signals. This oil clears the pipe.","👉 [LINK IN BIO NOW]"
"ZenCortex","⚠️ HEALTH ALERT\nSounds getting quieter?","🧬 CLINICAL UPDATE\nInner nerve armor is wearing thin. This vitamin rebuilds it.","👉 [LINK IN BIO NOW]"
"ZenCortex","⚠️ HEALTH ALERT\nBuzzing driving you mad?","🧬 CLINICAL UPDATE\nBrain wires are misfiring random shocks. This extract calms the storm.","👉 [LINK IN BIO NOW]"
"ZenCortex","⚠️ HEALTH ALERT\nPhantom noises torture you?","🧬 CLINICAL UPDATE\nDeep blood flow is cut off inside. This herb opens the floodgates.","👉 [LINK IN BIO NOW]"
"Nerve Fresh","⚠️ HEALTH ALERT\nFeet burning like fire?","🧬 CLINICAL UPDATE\nHard sugar crystals shred your nerve endings. This formula fixes it.","👉 [LINK IN BIO NOW]"
"Nerve Fresh","⚠️ HEALTH ALERT\nElectric shocks in legs?","🧬 CLINICAL UPDATE\nNerve wires are left exposed and raw. This capsule wraps them.","👉 [LINK IN BIO NOW]"
"Nerve Fresh","⚠️ HEALTH ALERT\nToes numb and frozen?","🧬 CLINICAL UPDATE\nVital blood is choked from your limbs. This extract restores feeling.","👉 [LINK IN BIO NOW]"
"Nerve Fresh","⚠️ HEALTH ALERT\nWalking on broken glass?","🧬 CLINICAL UPDATE\nDeep nerve pathways are inflamed and angry. This blend kills the fire.","👉 [LINK IN BIO NOW]"
"Nerve Fresh","⚠️ HEALTH ALERT\nPain spreading upward fast?","🧬 CLINICAL UPDATE\nThe deep root cause has been ignored. This enzyme heals the root.","👉 [LINK IN BIO NOW]"
"All Day Slimming Tea","⚠️ HEALTH ALERT\nBelly fat won't move?","🧬 CLINICAL UPDATE\nYour liver is completely clogged with waste sludge. This tea flushes it.","👉 [LINK IN BIO NOW]"
"All Day Slimming Tea","⚠️ HEALTH ALERT\nCravings own your mind?","🧬 CLINICAL UPDATE\nBad toxic bugs have hijacked your brain. This blend starves them out.","👉 [LINK IN BIO NOW]"
"All Day Slimming Tea","⚠️ HEALTH ALERT\nScale stuck for years?","🧬 CLINICAL UPDATE\nYour internal metabolism switch is turned off. This herb flips it on.","👉 [LINK IN BIO NOW]"
"All Day Slimming Tea","⚠️ HEALTH ALERT\nDiet makes you fatter?","🧬 CLINICAL UPDATE\nStress hormones trap emergency fat deep inside. This tea releases it.","👉 [LINK IN BIO NOW]"
"All Day Slimming Tea","⚠️ HEALTH ALERT\nMuffin top emergency?","🧬 CLINICAL UPDATE\nYour system is swollen with hidden poisons. This mix detoxes cells.","👉 [LINK IN BIO NOW]"
"Vertigenics","⚠️ HEALTH ALERT\nRoom spins again?","🧬 CLINICAL UPDATE\nTiny balance stones slipped loose inside your ear. This drops resets them.","👉 [LINK IN BIO NOW]"
"Vertigenics","⚠️ HEALTH ALERT\nStanding makes you dizzy?","🧬 CLINICAL UPDATE\nYour brain instantly loses position signals. This vitamin repairs the wire.","👉 [LINK IN BIO NOW]"
"Vertigenics","⚠️ HEALTH ALERT\nFalling without warning?","🧬 CLINICAL UPDATE\nHeavy fluid pressure crushes the main balance nerve. This herb drains it.","👉 [LINK IN BIO NOW]"
"Vertigenics","⚠️ HEALTH ALERT\nNausea from turning head?","🧬 CLINICAL UPDATE\nScrambled inner signals confuse your brain. This mineral syncs them.","👉 [LINK IN BIO NOW]"
"Vertigenics","⚠️ HEALTH ALERT\nBalance gone overnight?","🧬 CLINICAL UPDATE\nInternal crystals shifted out of place. This plant extract locks them firm.","👉 [LINK IN BIO NOW]"
"Pineal XT","⚠️ HEALTH ALERT\nThird eye still closed?","🧬 CLINICAL UPDATE\nChemical crust has completely calcified the gland. This acid dissolves it.","👉 [LINK IN BIO NOW]"
"Pineal XT","⚠️ HEALTH ALERT\nManifestation never works?","🧬 CLINICAL UPDATE\nYour spiritual signals are blocked by toxic waste. This oil clears the way.","👉 [LINK IN BIO NOW]"
"Pineal XT","⚠️ HEALTH ALERT\nSleep paralysis worsening?","🧬 CLINICAL UPDATE\nDeep rest hormones are trapped in a tight cage. This mineral breaks the lock.","👉 [LINK IN BIO NOW]"
"Pineal XT","⚠️ HEALTH ALERT\nIntuition completely dead?","🧬 CLINICAL UPDATE\nYour inner focus stone has hardened like rock. This extract softens it.","👉 [LINK IN BIO NOW]"
"Pineal XT","⚠️ HEALTH ALERT\nCan't lucid dream?","🧬 CLINICAL UPDATE\nYour biological dream faucet was turned off hard. This plant restarts the flow.","👉 [LINK IN BIO NOW]"
"""

html_start = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>75 World-Class Reels Slides</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Inter:wght@400;700;900&family=Playfair+Display:ital,wght@0,700;1,700&display=swap');

        * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        body, html {
            background: #0d0d0d;
            font-family: 'Inter', -apple-system, sans-serif;
            overflow-x: hidden;
            touch-action: pan-y;
            scroll-snap-type: y mandatory;
        }

        .slide {
            width: 100vw;
            height: 100vh;
            height: 100dvh;
            scroll-snap-align: start;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 50px 30px;
            position: relative;
            background: radial-gradient(circle at 50% 50%, #1c1c1e 0%, #0d0d0d 100%);
            overflow: hidden;
        }

        /* Slow-moving cinematic dark charcoal background */
        .cinematic-bg {
            position: absolute;
            top: -50%; left: -50%;
            width: 200%; height: 200%;
            background: linear-gradient(45deg, #0d0d0d, #1c1c1e, #0d0d0d, #252529, #0d0d0d);
            background-size: 400% 400%;
            animation: slowPan 25s ease infinite;
            z-index: 0;
            opacity: 0.6;
        }

        @keyframes slowPan {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .content {
            position: relative;
            z-index: 10;
            width: 100%;
            max-width: 400px;
        }

        /* Slide 1 Styles */
        .badge-alert {
            color: #FF2D55;
            font-size: 13px;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: 4px;
            margin-bottom: 24px;
            display: inline-block;
            text-shadow: 0 0 15px rgba(255, 45, 85, 0.4);
        }

        .symptom {
            color: #FFFFFF;
            font-size: 11vw;
            line-height: 1.05;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: -1px;
            text-shadow: 0 4px 20px rgba(0,0,0,0.8);
        }

        @media (min-width: 500px) {
            .symptom { font-size: 55px; }
        }

        .highlight-cyan {
            color: #00F0FF;
            text-shadow: 0 0 20px rgba(0, 240, 255, 0.6);
        }

        .highlight-gold {
            color: #D4AF37;
            text-shadow: 0 0 20px rgba(212, 175, 55, 0.6);
        }

        /* Slide 2 Styles */
        .badge-clinical {
            color: #00E676;
            font-size: 13px;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: 4px;
            margin-bottom: 24px;
            display: inline-block;
            text-shadow: 0 0 15px rgba(0, 230, 118, 0.4);
        }

        .viewfinder-box {
            position: relative;
            padding: 35px 25px;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
        }

        .viewfinder-box::before, .viewfinder-box::after {
            content: ''; position: absolute; width: 15px; height: 15px; border-color: rgba(255,255,255,0.7); border-style: solid;
        }
        .viewfinder-box::before { top: -1px; left: -1px; border-width: 2px 0 0 2px; }
        .viewfinder-box::after { bottom: -1px; right: -1px; border-width: 0 2px 2px 0; }
        .viewfinder-box .accent-1 { position: absolute; top: -1px; right: -1px; width: 15px; height: 15px; border-top: 2px solid rgba(255,255,255,0.7); border-right: 2px solid rgba(255,255,255,0.7); }
        .viewfinder-box .accent-2 { position: absolute; bottom: -1px; left: -1px; width: 15px; height: 15px; border-bottom: 2px solid rgba(255,255,255,0.7); border-left: 2px solid rgba(255,255,255,0.7); }

        .cause {
            color: #D1D1D6;
            font-size: 18px;
            line-height: 1.5;
            font-weight: 400;
            margin-bottom: 24px;
        }

        .solution {
            color: #FFFFFF;
            font-family: 'Playfair Display', serif;
            font-size: 26px;
            line-height: 1.3;
            font-weight: 700;
            font-style: italic;
        }

        /* Slide 3 Styles */
        .bottle-container {
            margin-bottom: 40px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .bottle-placeholder {
            width: 140px;
            height: 220px;
            background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.02));
            border-radius: 20px 20px 10px 10px;
            border: 1px solid rgba(255,255,255,0.2);
            box-shadow: 0 30px 60px rgba(0,0,0,0.8), inset 0 0 20px rgba(255,255,255,0.05);
            position: relative;
            backdrop-filter: blur(5px);
            display: flex;
            align-items: center;
            justify-content: center;
            color: rgba(255,255,255,0.5);
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            writing-mode: vertical-rl;
            text-orientation: mixed;
        }

        .bottle-placeholder::after {
            content: '';
            position: absolute;
            top: -25px;
            left: 50%;
            transform: translateX(-50%);
            width: 50px;
            height: 25px;
            background: rgba(255,255,255,0.15);
            border-radius: 5px 5px 0 0;
            border: 1px solid rgba(255,255,255,0.2);
            border-bottom: none;
        }

        .ios-btn {
            background: #FFFFFF;
            color: #000000;
            padding: 18px 40px;
            border-radius: 50px;
            font-size: 18px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 10px 30px rgba(255,255,255,0.15);
            text-decoration: none;
        }

        .slide-indicator {
            position: absolute;
            top: 25px;
            right: 25px;
            color: rgba(255,255,255,0.3);
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 1px;
            z-index: 100;
        }

        .product-tag {
            position: absolute;
            top: 25px;
            left: 25px;
            color: rgba(255,255,255,0.3);
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
            z-index: 100;
        }

    </style>
</head>
<body>
"""

html_end = """
</body>
</html>
"""

def highlight_symptom(text, index):
    words = text.split()
    if not words: return text
    last_word = words[-1]
    color_class = "highlight-cyan" if index % 2 == 0 else "highlight-gold"
    return " ".join(words[:-1]) + f" <span class='{color_class}'>{last_word}</span>"

def parse_line(line):
    parts = line.split(r'\n')
    if len(parts) == 2:
        return parts[0].strip(), parts[1].strip()
    return "", line.strip()

f = io.StringIO(data)
reader = csv.reader(f)
next(reader)  # skip header

slide_counter = 1
slides_html = ""

for index, row in enumerate(reader):
    if len(row) != 4:
        continue
    product, hook, cause_solution, cta = row

    # Process Slide 1
    hook_badge, hook_symptom = parse_line(hook)
    hook_symptom = highlight_symptom(hook_symptom, index)

    slides_html += f'''
    <!-- {product} - Slide 1 -->
    <div class="slide">
        <div class="cinematic-bg"></div>
        <div class="product-tag">{product}</div>
        <div class="slide-indicator">{slide_counter}/75</div>
        <div class="content">
            <div class="badge-alert">{hook_badge}</div>
            <div class="symptom">{hook_symptom}</div>
        </div>
    </div>
    '''
    slide_counter += 1

    # Process Slide 2
    cs_badge, cs_text = parse_line(cause_solution)

    # Split cause and solution based on ". This "
    if '. This ' in cs_text:
        cause, solution = cs_text.split('. This ', 1)
        cause += '.'
        solution = 'This ' + solution
    else:
        cause = cs_text
        solution = ""

    slides_html += f'''
    <!-- {product} - Slide 2 -->
    <div class="slide">
        <div class="cinematic-bg"></div>
        <div class="product-tag">{product}</div>
        <div class="slide-indicator">{slide_counter}/75</div>
        <div class="content">
            <div class="badge-clinical">{cs_badge}</div>
            <div class="viewfinder-box">
                <div class="accent-1"></div>
                <div class="accent-2"></div>
                <div class="cause">{cause}</div>
                <div class="solution">{solution}</div>
            </div>
        </div>
    </div>
    '''
    slide_counter += 1

    # Process Slide 3
    cta_text = cta
    slides_html += f'''
    <!-- {product} - Slide 3 -->
    <div class="slide">
        <div class="cinematic-bg"></div>
        <div class="product-tag">{product}</div>
        <div class="slide-indicator">{slide_counter}/75</div>
        <div class="content">
            <div class="bottle-container">
                <div class="bottle-placeholder">{product}<br>Bottle</div>
            </div>
            <a href="#" class="ios-btn">{cta_text}</a>
        </div>
    </div>
    '''
    slide_counter += 1

with open('index.html', 'w') as out:
    out.write(html_start + slides_html + html_end)

print("Generated index.html successfully.")
