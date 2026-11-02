#!/usr/bin/env python3
"""Article #323 - 2026-10-29 PM slot.

Topic: ribbon trim for athletic, activewear and performance apparel programmes -
stretch, recovery, sweat and chlorine exposure, wash durability, colour and
branding on stretch goods.

Why this topic: the ribbonbow123 corpus covers elastic stretch and recovery as a
material property, and covers performance testing generally, but there is no
article on the actual buying problem of trims in performance apparel - where
the trim has to survive a washing machine, a sports drink, a sun and a season of
sweat, and where a satin ribbon that looks beautiful on the hanger fails in the
first hundred wears.
"""
import sys
sys.path.insert(0, "/workspace/ribbonbow123")

from tmpl_ribbon_article import build_html

SITE = "ribbonbow123.com"
SLUG = "ribbon-oem-athletic-activewear-performance-apparel-trim-stretch-recovery-sweat-chlorine-wash-durability-branding-private-label-buyers-guide-2026-10-29-pm"
URL = f"https://{SITE}/blog-{SLUG}.html"
DATE_ISO = "2026-10-29T13:00:00+08:00"
DATE_DISPLAY = "October 29, 2026"

TITLE = ("Ribbon for Athletic &amp; Activewear Trim &mdash; Stretch, Sweat, Chlorine, Wash Durability and How to Specify It (2026)")
DESC = (
    "A buyer's guide to ribbon trim for athletic, activewear and performance apparel programmes. Covers why garment "
    "trim sits in a different durability regime from gift packaging trim - repeated washing, perspiration, sunscreen, "
    "chlorine and heat - how to specify stretch and recovery for a woven or elastic trim, sweat and chlorine "
    "fastness, how to brand ribbon that has to survive a season of wear, why a satin ribbon that looks perfect on "
    "the hanger fails at first wash, how to handle trim on performance fabric where the stretch of the garment and "
    "the stretch of the trim must be matched, and how to build wash-durability and testing requirements into a "
    "private-label specification. Written for brand owners, technical designers and sportswear procurement teams."
)
KEYWORDS = (
    "athletic apparel ribbon OEM, activewear trim supplier, performance apparel ribbon, "
    "elastic ribbon stretch recovery garment trim, sweat fastness ribbon, chlorine fastness ribbon trim, "
    "sport ribbon branding woven label, wash durability ribbon specification, "
    "private label activewear ribbon sourcing, B2B ribbon guide sportswear trim"
)

SECTIONS = [
    (
        "Garment Trim Is Not Gift Packaging Trim",
        """A brand owner who has sourced ribbon for gift packaging and then moves into activewear discovers this quickly, and usually in the most expensive way possible: after the first season, when returns arrive and the reason is that the trim failed.

<b>Garment trim lives in a hostile environment that gift trim never sees.</b> A ribbon on a gift box is handled a handful of times and stored in a climate-controlled warehouse. A ribbon on a garment is washed every week for a season or more, bleached by sweat and sunscreen, exposed to chlorine if the garment is ever used near a pool, flexed and stretched with every movement of the body, abraded against skin, and dried in a hot tumble dryer. The colourfastness standard that is entirely adequate for a gift box is completely inadequate for a garment.

<b>The failure is rarely dramatic.</b> It is a gradual one: the colour fades a little each wash, the edge frays a little more, the elastic loses a little recovery, the printed logo cracks along its fold. By the time the customer notices, they have usually decided the garment was a bad purchase, and the returns data will tell you it was a quality problem without identifying which component was responsible. That is the real cost of garment trim, and it is why garment trim needs a specification written for the garment's whole life, not for the moment it leaves the factory.

<b>Stretch is a compatibility question, not a ribbon property.</b> This is the conceptual point that most often gets missed. A ribbon does not simply need to stretch; it needs to stretch <i>at the same rate as the fabric it is sewn to</i>, and it needs to recover, because the recovery rate determines whether the trim returns to its original shape after the garment has been washed, dried and worn. A trim with too much stretch relative to the garment will pucker at the seam; a trim with too little stretch will fight the fabric, will distort the panel it is applied to, and will cause the garment to lose its shape over the season. Ribbon on performance apparel is not an accessory. It is a structural component that happens to be visible.

<b>And branding on stretch goods has its own rules.</b> A woven logo badge on a stretch garment cannot be rigid. A printed logo on a stretch ribbon will crack across the stretch axis. A heat-transfer on an elastic substrate behaves differently from a heat-transfer on a woven one. The branding method has to be chosen with the substrate's stretch behaviour in mind, not after artwork is approved.

At Smith Ribbon, in Xiamen since 2004, we produce satin, grosgrain, organza, jacquard, elastic and wired ribbon, and we supply trims into sportswear, activewear and performance apparel programmes. This guide covers how to specify trim for that environment properly, what to test, and which requirements are worth paying for and which are not."""),
    (
        "Specifying Stretch and Recovery for Garment Trim",
        """Stretch and recovery are the two numbers that determine whether a trim works on a performance garment, and they have to be read as a pair.

<b>What stretch actually means on ribbon.</b> Most ribbon has a small amount of inherent give, because it is a woven textile and any woven textile extends under load. Elastic ribbon has a great deal. The useful specification states the elongation at a defined load, and the load has to be defined: percentage elongation at a stated force, or percentage elongation at a stated extension, or a force required to reach a stated extension. These are three different measurements and they are not interchangeable. A mill that quotes "30% stretch" without a test condition has told you nothing, and a buyer comparing two quotes on those numbers is comparing noise.

<b>Recovery is the more commercially important of the two.</b> Recovery is the proportion of the original length that returns after the load is released, usually measured after a defined hold time. A trim with high stretch and poor recovery is worse than a trim with modest stretch and good recovery, because it will not return to shape. The practical consequence is a garment that looks baggy and wrong after a few wears, with no visible fault and no obvious cause. Specify a minimum recovery percentage at a stated extension and a stated hold, and specify that it is measured after wash if the garment will be washed - because recovery after a wash is lower than recovery on a new sample, and the new-sample number will flatter the product.

<b>Match the trim to the fabric, not to a generic elastic.</b> A four-way stretch fabric with a high recovery needs trim with comparable elongation and recovery. A rigid woven panel needs trim with almost no stretch, and a stretch trim applied to a rigid panel will cause the panel to bow. The order of operations matters here: the fabric is usually selected first by the performance designer, and the trim is then specified to fit it. If the trim is being sourced in parallel with the fabric, the fabric's stretch specification should be attached to the trim brief as a requirement rather than left to the trim mill to assume.

<b>Stretch in the warp direction versus the weft direction.</b> Elastic ribbon is not necessarily equal in both directions, and a woven elastic with mechanical stretch in one direction behaves very differently from a stretch film or a knitted elastic. State which direction the stretch runs relative to the seam, because a trim applied in the wrong orientation will not perform.

<b>Set, or residual deformation.</b> The number buyers ask for least often is set: the permanent length change after a load cycle. A trim with low set will return to the same length after every wash; a trim with high set will lengthen progressively. On a garment this shows as the trim becoming looser over the season and eventually as the trim sitting oddly. Specify a maximum set at a stated extension and hold.

<b>And specify what happens at the seam.</b> Trim performance in a garment is not ribbon performance. A ribbon with excellent stretch and recovery can still fail because the seam it is attached to has no give, because the stitch type is wrong for elastic, or because the trim is attached with too few stitches for the load. This is a garment-construction question that belongs in the trim specification only insofar as the trim must state its stitch recommendation. Ask the mill for it - a supplier who has sewn their own trim into garments will have a view, and it is worth having on file."""),
    (
        "Colour Fastness for Sweat, Sunscreen, Chlorine and Wash",
        """This is the part of the garment trim specification that most often turns out to have been written for the wrong end use. Here is what actually needs testing, and why.

<b>Sweat fastness.</b> Perspiration is not water. It is a solution, and it is alkaline - human perspiration typically sits around pH 5.5 to 7 but the components of it, particularly the salts and the urea, behave very differently from neutral water in the presence of a dye. A ribbon that passes a standard water-based colourfastness test can still bleed badly in perspiration. For trims that contact skin - a neckline binding, a sleeve trim, a hair tie worn against the scalp - sweat fastness should be specified and tested on the actual construction, because the presence of a backing, a coating or an elastic yarn changes the result. Also specify the staining behaviour, which is not the same as the bleeding behaviour: a trim that does not bleed can still transfer dye onto the skin or onto the adjacent garment panel, and that is a consumer-complaint generator even though it is not a test failure.

<b>Chlorine fastness.</b> Relevant for swim and water-fitness programmes, and increasingly relevant for anything that might be laundered in a chlorinated pool environment. Chlorine attacks many disperse dyes severely and it degrades elastomeric fibres, so a ribbon that looks fine after a normal wash can be visibly attacked after a few pool sessions. If there is any chance of chlorine exposure, specify a chlorine fastness requirement and specify whether the trim is intended for pool use or for fresh water only.

<b>Sunscreen and oil resistance.</b> This one is specific to outdoor and performance-wear programmes and it is increasingly a source of consumer complaints. Modern sunscreens contain oils and film-forming agents that can interact with dye and with the surface of a ribbon. A trim that discolours in the presence of sunscreen looks like a defect. Where the garment will be worn in sun, specify the resistance requirement.

<b>Wash fastness at the real wash setting.</b> This is where most garment trim specifications fail, because the test is written against a standard domestic wash cycle, while the garment will be washed at the care label setting, which may be a higher temperature, a longer cycle, or a tumble dry. The right requirement is the garment's own care label. If the care label says wash at 40 degrees and tumble dry low, then that is the condition the trim must survive - and the test should be run at that condition, on the trim, and the trim should be tested in the sewn state if at all possible, because seam thread, backing and interfacing all participate in the dimensional behaviour.

<b>Rub and abrasion.</b> Trim at a cuff, a hem or a neckline rubs against itself and against skin. For a woven logo badge on a performance garment, abrasion is a real failure mode and it should be tested with a Martindale or a similar abrasion test at a defined cycle count.

<b>And specify the number of washes the trim must survive.</b> "Wash fastness grade 4-5" is a laboratory number that says nothing about the season. "Must retain at least 90% of its colour strength after 20 wash cycles at 40 degrees with tumble dry, and 95% of its original elongation" is a product requirement the mill can design against and a quality team can verify. This is the level of specificity that makes garment trim sourcing work.

<b>Also specify the standards by name.</b> A requirement that references a specific published test method - ISO 105 for colourfastness, ISO 12947 for abrasion, or the equivalent AATCC methods - removes the ambiguity of what the mill actually tested and how comparable the result is to another supplier's result."""),
    (
        "Branding Ribbon That Has to Survive a Season",
        """Branding on athletic and activewear garments fails in ways that are specific to the substrate, and the fix is always to let the substrate behaviour drive the method.

<b>The core constraint: branding must stretch with the fabric, or it will not survive.</b> A rigid woven logo badge applied to a four-way stretch panel is a defect waiting to happen - it will pucker, it will lift at the corners, and it will eventually detach. This does not mean the badge cannot be used; it means it has to be designed as a stretch-compatible badge, with a stretch or knit construction, an appropriate percentage of elastane content, and a perimeter stitch or an appliqué method that allows the badge to move with the panel.

<b>The direction of stretch determines the design.</b> A badge with horizontal stretch applied to a vertically-stretching panel will not work. Specify the stretch axis of the badge and the stretch axis of the panel, and confirm they are compatible, or specify a badge with stretch in both directions.

<b>Heat transfer on elastic.</b> A heat-transfer or silicone transfer mark on an elasticated or stretch-woven substrate needs different temperature, dwell time and pressure than the same transfer on a stable woven. The failure mode is typically a mark that looks correct immediately after application and then cracks, peels or distorts after the first few washes as the substrate moves. If heat transfer is the method, specify that the transfer be tested on the actual substrate and laundered before approval, and that the test result be part of the approval rather than a later check.

<b>Printed ribbon vs woven ribbon for logo marks.</b> A printed mark on a ribbon is cheaper, allows more colour and more detail, and is fine where the trim carries no stretch and takes no abrasion. A woven mark is more durable, has no ink to crack or peel, survives more washes, and is the correct answer where the trim is at a cuff, a hem or a high-abrasion zone. Where a programme mixes both, the specification should say which method applies to which trim, because the approval and test requirements differ.

<b>Jacquard for a repeated brand motif on an activewear trim.</b> Where the ribbon itself carries a repeating pattern - a small geometric, a tonal signature - a jacquard weave gives a mark that cannot peel off and will survive the life of the garment. The constraint is the same as in any small-format jacquard: the pattern must be legible at the trim width, and the repeat pitch and the colourway must be set before the loom setup.

<b>Reflective and high-visibility trims.</b> A reflective trim on a performance garment is a safety product and needs to be specified as one, with a defined retroreflectivity requirement and, where relevant, certification against the applicable standard for the market and the use.

<b>And the sub-brand, the size tag, the care label.</b> These are all ribbon-adjacent items in an activewear programme and they are all subject to the same wash and stretch environment. A woven size tab that shrinks 8% after five washes will read as a defect. A care label that fades is a compliance problem. If the programme uses these, specify them in the same document and with the same durability requirements as the visible trim - they are all trims, they are just less glamorous."""),
    (
        "The Failure Modes, and What They Tell You",
        """Here are the recurring garment trim failures, in the order we see them, and what each one actually tells you about the specification.

<b>1. Fading and shade shift, non-uniform across the garment.</b> The trim on one panel has faded and the matching trim on another has not. This is a lot-to-lot variation in the trim itself, and it is the direct consequence of the trim being produced in separate lots against a colour target rather than against a physical standard. The fix is a retained standard from the first lot and a lot-approval process.

<b>2. Trim relaxed or bagged after a season.</b> The elastic has lost recovery, or the seam has failed to hold the stretch, or the trim was specified with too little stretch for the panel and has distorted it. The diagnostic is straightforward: if the fabric panel is also bagged, the problem is the fabric. If the panel holds its shape and only the trim has relaxed, it is the trim's recovery or its stretch ratio. This is why a recovery requirement after wash, not just a stretch requirement on a new sample, is worth specifying.

<b>3. Logo cracking or lifting after washing.</b> Almost always a heat-transfer or print method on a moving substrate, or a badge that was too rigid for the panel. Diagnose by inspecting the failed sample against the approved sample and checking whether the failure follows the stretch axis.

<b>4. Frayed trim edge against skin.</b> A cut edge on a narrow elastic or on a woven trim contacting skin will fray and will feel sharp. This is an edge-treatment specification issue and it is also an ergonomic and a consumer-safety issue.

<b>5. Trim shrinkage mismatch.</b> The trim shrank and the panel did not, so the trim is now pulling the seam. Specify shrinkage as a percentage after the wash condition, and specify it for the trim, not only for the garment fabric.

<b>6. Print or transfer stiffening the trim.</b> A printed or heat-transferred mark on an elastic trim makes that section of the trim rigid, and the rigid section is where it will fail. The area of the mark and the rigidity it introduces need to be considered against the total stretch of the trim.

<b>7. Discolouration from sunscreen or oil.</b> Covered above. It is now one of the more common complaints in outdoor performance wear and it is entirely preventable with the right specification.

<b>8. The trim that passed everything and still failed.</b> Occasionally a programme fails because the test specimen was not representative - a swatch tested without the backing, the interfacing or the seam construction that the real garment has. Whenever a trim requirement is important, the test should be run on the trim as it will be used, or at minimum on a sample that includes the construction. This is worth paying for, because the alternative is a specification that certifies the wrong thing."""),
    (
        "Building a Garment Trim Specification That Holds Up",
        """The structure below is what we recommend for an activewear trim specification. It is longer than a gift packaging specification, and it should be - the garment asks more questions.

<b>End use and construction.</b> Which garment, which panel, which trim position, and the fabric it is attached to - with the fabric's stretch specification attached as a requirement.

<b>Construction and material.</b> Material family, fibre content, elastane content if applicable, construction type, and whether the trim is woven, knitted or non-woven. Note that fibre content declarations on performance trims are frequently inaccurate, and a declaration that does not match the product is a compliance problem in the EU and the UK, not just a quality one.

<b>Dimensions.</b> Width and width tolerance, length or reel specification, and thickness where relevant to the seam.

<b>Mechanical requirements.</b> Elongation at a stated load or extension, recovery percentage at a stated extension and hold, set at a stated condition, and whether these are measured on new samples, after wash, or both.

<b>Colour.</b> Standard reference, the physical standard the mill matches against, colour difference tolerance, measurement geometry, and the lighting condition for assessment. For performance wear, state whether the colour is required to be stable in perspiration as well as in water.

<b>Colourfastness requirements.</b> Named tests at named conditions: wash at the garment's care-label setting with a stated cycle count, perspiration, chlorinated water where applicable, seawater where applicable, oil and sunscreen where applicable, and rubbing. Each with a minimum grade or a minimum retention percentage.

<b>Branding.</b> Method, artwork reference, substrate compatibility, stretch axis of the mark, adhesion or wash retention requirement, and abrasion requirement where the mark sits in a high-wear zone.

<b>Shrinkage and dimensional stability.</b> Maximum shrinkage after the specified wash, and the same figure for any backing or elastic component.

<b>Edge and finish.</b> Selvedge condition, end treatment, and any requirement for the edge that contacts skin.

<b>Compliance and documentation.</b> Required certifications with scope and expiry, fibre content declaration, country of origin, restricted substances, and the care and labelling requirements for the destination market.

<b>Testing and approval.</b> The test programme, who runs it, on what specimen, what evidence is provided, and the pre-production approval gate. For performance wear, this should include a garment-level trial - a real garment, washed the real number of times, inspected - before the bulk release, because trim testing on swatches does not catch seam interaction.

<b>Retention.</b> Retained standard from the first lot, retained sample per lot, and the duration.

<b>Traceability.</b> Lot coding, carton marking, and the records needed to tie a specific garment serial or batch back to a specific trim lot. This matters more than buyers expect, because it is what makes a recall or a quality investigation bounded instead of open-ended.

<b>The programme plan.</b> Lead times at each stage, the approval calendar, and the reorder mechanism with the price band agreed in advance."""),
]

FAQ = [
    (
        "How much stretch should ribbon have for an activewear garment?",
        "There is no universal figure - the correct answer is the one that matches the fabric it is sewn to. The trim should elongate at approximately the same rate as the panel it is attached to, so that neither the trim nor the panel is fighting the other. In practice a performance panel with high four-way stretch needs trim with comparable elongation and, critically, comparable recovery, whereas a rigid woven panel needs trim with almost no stretch. Attach the fabric's stretch specification to the trim brief rather than asking the trim mill to assume, and specify the measurement condition for the stretch number so that quotes are comparable.",
    ),
    (
        "What is the difference between stretch and recovery, and which matters more commercially?",
        "Stretch is how far the trim extends under load; recovery is how much of that extension is returned once the load is removed. Stretch is the visible, easy-to-measure number. Recovery is the one that determines whether the garment still looks right after a season. A trim with high stretch and poor recovery will not return to shape and will cause the garment to look baggy with no visible fault - which makes it far more expensive than it looks on the specification sheet. Specify recovery explicitly, at a stated extension and hold time, and specify that it is measured after wash as well as on a new sample.",
    ),
    (
        "Do I need to specify sweat and chlorine fastness separately from wash fastness?",
        "Yes, and this is where many garment trim specifications are underspecified. Perspiration is alkaline and behaves quite differently from neutral water, so a ribbon can pass a water-based colourfastness test and still bleed in sweat - particularly on trims that contact skin. Chlorine attacks disperse dyes and degrades elastomeric fibres, so it matters for swim and water-fitness programmes and for anything with any possibility of pool exposure. Sunscreen and oil resistance matters for outdoor performance wear, where it is now one of the more common sources of consumer complaints. Each should be specified by name and by method.",
    ),
    (
        "Why does my printed logo on an elastic trim crack after a few washes?",
        "Because the print or heat transfer was approved on a swatch and not on the moving substrate. A rigid print on a stretch substrate will crack along the stretch axis as the substrate moves, and a heat transfer applied at the wrong temperature, dwell or pressure for an elastic substrate will look correct immediately and then peel. The fix is to specify the substrate compatibility of the transfer, to test the transfer on the actual trim construction laundered to the care-label condition, and to make that test part of the approval rather than a later verification. Where the trim sits at a cuff or hem, a woven mark is usually the more durable answer.",
    ),
    (
        "Can I use a rigid woven logo badge on a stretch garment panel?",
        "Not without designing it as a stretch-compatible badge. A rigid badge on a four-way stretch panel will pucker at the seams, lift at the corners and eventually detach. The badge itself needs to be a stretch or knit construction with an appropriate elastane content, its stretch axis has to match the panel's stretch axis, and the attachment method has to allow the badge to move with the panel - typically a perimeter stitch or an appliqué technique. If the badge is small and applied to a highly stretchy zone, the right answer may be to move the branding off the stretch panel altogether.",
    ),
    (
        "How many wash cycles should garment ribbon be required to survive?",
        "Enough to cover the life of the garment, which is a commercial decision rather than a laboratory one. A typical performance apparel programme should specify retention after a stated number of cycles - commonly 20 or more - at the garment's own care-label wash setting including tumble dry where applicable, and should require a minimum retained colour strength and a minimum retained elongation or recovery at that point. The important point is to write the requirement in product terms rather than laboratory terms: a colourfastness grade on a new swatch tells you very little about what the customer experiences after a season.",
    ),
    (
        "How do I prevent the trim on different panels of one garment from fading at different rates?",
        "The usual cause is that the trim was produced in separate lots against a colour target rather than against a physical standard, so each lot is individually acceptable and the set is not. The remedy is a retained standard from the first production lot, a lot-to-lot approval step against that standard, and a retained sample from every lot for the life of the programme. It is worth noting that a garment often contains trim from more than one lot - a neckline binding from one run and a sleeve trim from another - so the standard needs to be shared across every trim position in the programme rather than held per component.",
    ),
]

METRICS = [
    ("Typical garment trim width band", "6mm to 25mm, with 10-19mm the most common"),
    ("Stretch figure worth quoting without a condition", "None - always require the test condition"),
    ("Recovery worth specifying after wash", "Minimum percentage at a stated extension and hold"),
    ("Wash fastness test condition", "The garment's own care-label setting, with cycle count stated"),
    ("Programme recommendation for trim wear life", "20+ wash cycles at the care-label setting"),
    ("Sun and sweat exposure", "Specify oil and sunscreen resistance for outdoor programmes"),
    ("Factory continuity", "Weaving, dyeing, printing, finishing and converting in Xiamen since 2004"),
]

AUTHOR_BULLETS = [
    "In-house weaving, dyeing, printing, finishing and converting in Xiamen since 2004",
    "Elastic, satin, grosgrain, organza, jacquard and wired ribbon for performance and activewear programmes",
    "OEKO-TEX, FSC, BSCI, SEDEX, ISO 9001 and SMETA documentation for private-label sportswear brands",
    "Trim specified against the garment fabric, tested in the sewn state, and approved before bulk release",
]

CLOSING_PARAGRAPH = (
    "Garment trim is a durability specification wearing a costume as a design element. The ribbon is small, "
    "the programme is large, and the customer will hold the whole garment responsible for a failure that was "
    "actually decided by a number on a spec sheet three months earlier - an elongation without a condition, "
    "a colourfastness grade that was never tested against sweat, a logo mark approved on a swatch that does not move. "
    "The buyers who get this right treat the trim specification as part of the garment engineering, which is what it is."
)

CLOSING_CTA = (
    "If you are sourcing trim for an athletic, activewear or performance apparel programme, send us the garment "
    "fabric, its stretch specification, the trim dimensions and the care-label wash setting, and we will tell you "
    "what construction will hold, what the stretch and recovery figures will be for the actual substrate, and what "
    "test programme we would put behind the approval. We will also tell you honestly if a branding method you have "
    "in mind will not survive a season on a moving substrate."
)

cfg = {
    "url": URL,
    "title": TITLE,
    "desc": DESC,
    "keywords": KEYWORDS,
    "date_iso": DATE_ISO,
    "date_display": DATE_DISPLAY,
    "num": 323,
    "sections": SECTIONS,
    "faq": FAQ,
    "metrics": METRICS,
    "author_bullets": AUTHOR_BULLETS,
    "author_name": "Xiamen Smith Ribbon&amp;Bow Co., Ltd.",
    "author_url": "https://ribbonbow123.com/about.html",
    "logo_url": "https://ribbonbow123.com/img/banner.png",
    "site": f"https://{SITE}",
    "closing_paragraph": CLOSING_PARAGRAPH,
    "closing_cta": CLOSING_CTA,
    "h2_title": "Specifying Athletic &amp; Activewear Trim With Smith Ribbon",
}

html = build_html(cfg)
with open(f"/workspace/ribbonbow123/blog-{SLUG}.html", "w", encoding="utf-8") as f:
    f.write(html)

wc = sum(len(p.split()) for _, p in SECTIONS) + sum(len(a.split()) for _, a in FAQ)
print(f"Wrote blog-{SLUG}.html ({len(html):,} bytes), ~{wc} words, {len(SECTIONS)} sections, {len(FAQ)} FAQ")
