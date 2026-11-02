#!/usr/bin/env python3
"""Article #315 - 2026-10-28 AM slot (afternoon of the 10-28 batch follows as #316).

Topic: elastic and stretch ribbon - how to specify stretch, recovery and
compression, and why most elastic ribbon failures are a specification gap
rather than a material fault.

Distinct from recent ribbonbow123 articles:
  #312 shrinkage / relaxation / dimensional stability;
  #313 technical specification and tech pack writing;
  #314 supplier selection and factory financial health;
  #310 decoration process selection;
  #311 sampling and pre-production approval.
Elastic behaviour (stretch %, recovery %, compression set, fatigue) does not
appear in the corpus as a dedicated buying topic - it exists only as a
property line inside generic spec-sheet decoders.
"""
import sys
sys.path.insert(0, "/workspace/ribbonbow123")

from tmpl_ribbon_article import build_html

SITE = "ribbonbow123.com"
SLUG = "ribbon-oem-elastic-stretch-recovery-compression-specification-private-label-buyers-guide-2026-10-28-am"
URL = f"https://{SITE}/blog-{SLUG}.html"
DATE_ISO = "2026-10-28T08:00:00+08:00"
DATE_DISPLAY = "October 28, 2026"

TITLE = ("Elastic and Stretch Ribbon &mdash; How to Specify Stretch, Recovery and Compression (2026)")
DESC = (
    "A buyer's guide to elastic ribbon for private-label programmes. Covers what stretch percentage and "
    "recovery percentage actually mean, why a ribbon that stretches to 200% may only recover to 85% and what "
    "that does to a packaged product, how to specify stretch ratio, recovery, compression set and stretch "
    "fatigue in a way an inspector can test, how elastic core, cover yarn and knit construction determine "
    "behaviour, and why elastic failures show up in the pack rather than on the mill floor. Written for brand "
    "owners, private-label managers and procurement teams sourcing hair accessories, pet products, "
    "stretch-bundle packaging and gift sets."
)
KEYWORDS = (
    "elastic ribbon OEM supplier, stretch ribbon specification, elastic recovery percentage ribbon, "
    "ribbon compression set test, custom elastic hair tie ribbon, stretch ribbon packaging gift set, "
    "elastane core ribbon weaving, ribbon stretch fatigue durability, private label elastic ribbon guide, "
    "how to specify elastic ribbon, ribbon stretch percentage tolerance, B2B elastic ribbon sourcing"
)

SECTIONS = [
    (
        "The Property Nobody Writes Down Until It Fails",
        """There is a family of ribbon problems that behaves differently from every other ribbon problem. A width that is out of tolerance shows up at inspection. A shade that is wrong shows up at approval. An elastic ribbon that is behaving badly shows up in the pack, on the shelf, in the hands of a customer, and it is usually attributed to something other than the ribbon.

Consider the common case. A brand commissions a stretch ribbon for a hair accessory, or for a gift set that has to hold a heavy bottle and a jar together, or for a pet product that has to stretch to fit a head and then hold. The sample looks right. The colour is right. The print is right. The hand feel is right. The ribbon goes into production, ships, gets packed, and by the third week of the retail season the packs are loose. The ribbon has stretched and has not come back. The pack no longer holds. The customer returns it, and the brand blames the ribbon, and the ribbon mill is asked to explain why the ribbon is "wrong".

The ribbon is not wrong. The ribbon is doing precisely what an elastic ribbon does when nobody told it what "doing precisely that" was supposed to look like. This is the central problem with elastic ribbon and it is a documentation problem far more often than it is a manufacturing problem.

<b>Elastic ribbon has more than one number.</b> A buyer will usually specify a stretch percentage and stop there. But an elastic ribbon has at least four commercially meaningful properties, and they are independent of one another: how far it stretches, how much of that stretch it takes back, how much permanent deformation it retains over time, and how many stretch cycles it survives before the behaviour changes. A ribbon can have an excellent stretch figure and a poor recovery figure. It can recover well initially and then fatigue. It can perform perfectly on a bench and fail on a shelf in a warm car.

<b>The behaviour changes with time, temperature and rate.</b> An elastic ribbon tested slowly at room temperature and an elastic ribbon used quickly in a warm environment are two different materials in practice. The test method is therefore not a formality. It is the difference between a specification and a preference, and between a claim you can win and a claim you cannot.

<b>The failure is usually invisible at the mill.</b> Elastic ribbon is routinely inspected for colour, width, print registration and surface quality. How often is it stretched and held to see whether it returns? Less often than you would hope, and the answer depends heavily on whether the mill runs a dedicated elastic line or weaves elastic on a general ribbon loom with an elastane core.

At Smith Ribbon, in Xiamen since 2004, we weave and finish decorative ribbon and we treat elastic as a specification discipline rather than a product category, because the buyers who get into trouble with elastic ribbon are almost never the ones with the best supplier relationships. They are the ones whose specification said "elastic" and nothing else. This guide is about how to write the four numbers down, how to test them, and how to decide whether you actually need elastic at all.""",
    ),
    (
        "Stretch, Recovery, Compression Set and Fatigue: Four Different Things",
        """The vocabulary around elastic ribbon is used loosely, and the looseness causes real commercial damage. Here is what each term means and what each one costs you.

<b>Stretch percentage.</b> Usually defined as the increase in length under a stated load, expressed as a percentage of the original length. A ribbon that stretches to 200% has doubled in length under that load. This is the number buyers most often specify, and it is the least useful of the four on its own, because a ribbon can achieve a high stretch figure and still be a poor product.

<b>Recovery percentage.</b> The percentage of the stretched length that is recovered once the load is removed. If a ribbon stretches from 100mm to 200mm and, on release, returns only to 170mm, it has recovered 70% of the 100mm it gained and retained 30% of the stretch permanently. This is the number that determines whether your pack still holds after a week, a month or a season. A ribbon with a high stretch figure and a recovery of 70% is a ribbon whose packs will progressively go loose.

<b>Compression set.</b> The permanent deformation that remains after a ribbon has been compressed, held compressed for a stated time at a stated temperature, and then released. Compression set is what determines whether a ribbon used to hold something in place keeps holding it. It is measured as a percentage of the original thickness or dimension. A high compression set means the ribbon will not return to its original thickness, and a pack built on that ribbon will not keep its shape.

<b>Stretch fatigue.</b> The gradual change in behaviour over repeated stretch cycles. A ribbon may pass a single stretch test and then behave differently after two thousand cycles, which is a perfectly ordinary number of cycles for a gift set that gets handled in a shop window, or a hair accessory that is put on and taken off daily. Fatigue is the property that determines whether a programme passes its first season or its third.

<b>Why the four have to be stated together.</b> They describe different things and they can move independently. A ribbon can stretch less but recover fully. A ribbon can stretch more and recover partially. A ribbon can have excellent static behaviour and poor fatigue behaviour, which is the most common combination in practice because most factories test static properties at approval and never test cycles at all. This is why "elastic ribbon, 200% stretch" is not a specification. It is half of one.""",
    ),
    (
        "What Actually Determines How an Elastic Ribbon Behaves",
        """The behaviour of an elastic ribbon is set by three things: the elastic core, the way it is covered and constructed, and the finishing. Understanding these three gives you the vocabulary to interrogate a supplier intelligently.

<b>The elastic core.</b> Almost all commercial elastic ribbon uses an elastane core &mdash; commonly called spandex or Lycra &mdash; wrapped in yarn. The proportion of elastane in the core is the single biggest driver of stretch behaviour. A higher elastane content produces more stretch and generally better recovery, and also changes the hand feel substantially: more elastane means a ribbon that feels slicker, thinner in appearance, and more prone to snagging on sharp edges. A buyer specifying by width and colour alone is leaving the most important variable unstated.

<b>Cover yarn and construction.</b> The elastane core is wrapped in one or more outer yarns, and how it is wrapped affects everything downstream: the surface texture, the print hold, the abrasion resistance, the amount of elastic exposed at the edges, and how the ribbon behaves when it is cut. A flat-woven elastic ribbon with a covered core behaves differently from a knitted elastic ribbon, and a tubular or corded elastic behaves differently again. One specific thing worth watching: elastic exposed at a cut edge will fray and curl noticeably faster than a conventional ribbon, which matters enormously if your programme converts ribbon to cut lengths or ties bows from it.

<b>Elastic versus elastane content and the effect on dye.</b> Elastic fibres behave differently in the dye house. Polyester elastane is the workhorse and dyes well; the elastane component can take dye differently from the polyester face yarn, which sometimes shows up as a slight difference in shade between the face and the core if the core is exposed. It also means that dyehouse processing has to be controlled &mdash; excessive heat or over-dwell damages elastane, and an over-dyed elastic ribbon will lose both its stretch and its recovery permanently.

<b>Finishing and the heat question.</b> Elastic ribbon is heat-set, but the heat-setting route has to be gentle enough not to damage the elastane. This is a real tension in the process, and it is the reason elastic ribbon is not simply "ribbon with a bit of rubber in it" and cannot be made on any ribbon loom with any heat-setting line. Where heat has been excessive, the ribbon will pass a stretch test at approval because it has not been stretched yet, and then behave inconsistently in service.

<b>The stretch that comes from construction rather than from elastane.</b> A ribbon can gain stretch from a loose weave or a crinkled or puckered construction without any elastane in it at all. This is a different product with different behaviour: the stretch is largely one-directional and limited, and the recovery is good, but the stretch amount is a function of how the construction is disturbed. Some buyers discover this to their cost when they expect a woven elastic and receive a stretch-satin. Know which one you are buying before you write the specification.""",
    ),
    (
        "Writing an Elastic Specification an Inspector Can Actually Test",
        """An elastic specification needs the same discipline as any other specification: named property, stated method, stated conditions, numerical limit and stated consequence. Here is what a workable one contains.

<b>1. The stretch figure, with its load stated.</b> "200% stretch" is incomplete, because stretch under what load? The stretch of an elastic ribbon is a function of the force applied. Specify either the stretch at a stated force (for example, "stretches to 200% under a load of X grams per centimetre of width") or the stretch under a stated extension, or state the method and let the method define the conditions. What you must not do is specify a number without the condition that produces it, because that number is not comparable between mills and will not settle a dispute.

<b>2. The recovery figure and how it is measured.</b> State the extension applied, the dwell time at extension, the release period before measurement, and the recovery percentage required. A common and defensible convention is to specify recovery at a stated extension held for a stated period and measured after a stated release time. The dwell and release periods matter: an elastic ribbon held stretched for a long time and then measured immediately behaves very differently from one released and left overnight.

<b>3. Compression set, with temperature and dwell.</b> Specify the compression applied, the time it is held, the temperature, and the recovery time before measurement. Compression set is strongly temperature-dependent, and a test run at room temperature will not predict behaviour in a warehouse in July or a delivery van in August.

<b>4. Stretch fatigue and the cycle count.</b> Specify the number of cycles, the cycle rate or dwell, the extension applied per cycle, and the change in behaviour permitted after that cycle count. This is the specification that protects you in year two, and it is the one most often omitted.

<b>5. The construction and the core.</b> State the elastane content, whether the core is covered or exposed, the construction type, and the width tolerance and thickness tolerance. And state whether the ribbon is supplied flat or in a specific packaged format.

<b>6. The environment in which it will be tested and used.</b> State the conditioning and test temperature and humidity. This is not pedantry for elastic: an elastane core is temperature-sensitive in a way that a polyester core is not, and a ribbon tested at 20&deg;C can behave measurably differently at 35&deg;C.

<b>7. The consequence of failure.</b> A tolerance without a consequence is a preference. State whether a failing lot is held, re-made, re-worked or accepted with concession.

One practical note on tolerance: <b>stretch tolerance and recovery tolerance are not the same kind of number and should not be expressed the same way.</b> A stretch figure can reasonably be held to a fairly wide band, because how far an elastic ribbon stretches is a property of the material and varies naturally within a lot. Recovery is a different matter: recovery is what determines whether the product works, and a lot with recovery below the specified floor will fail in service regardless of how well it stretched. Where a programme is functionally dependent on recovery, specify recovery tightly and stretch loosely, and say so in the tech pack. It is also worth stating which property drives the acceptance decision, so that a lot is not failed on a stretch band when recovery is what actually matters for the product.

At Smith Ribbon we put the four figures, the test conditions and the core description into the job folder before scheduling, so that the quote, the lab dip, the production sample and the final inspection all refer to the same document. We will also tell you when the recovery you have asked for is not achievable with the construction you have specified &mdash; which happens, and which is better discovered at quotation than at delivery.""",
    ),
    (
        "Testing: What to Ask the Mill to Show You, and What to Do Yourself",
        """The value of elastic testing is overwhelmingly in doing it early, at the sample stage, where a problem costs a conversation rather than a recall.

<b>Ask for the mill's own test data on the actual construction.</b> Any mill running a real quality system on elastic should be able to show you stretch and recovery figures for a production lot of the construction you are quoting, with the method stated. Ask what method was used, what the load was, what the dwell and release times were, and how many specimens were tested. A number without those details cannot be compared to your requirement, and a mill that cannot produce the detail is telling you something useful.

<b>Ask whether the elastic is tested as a finished construction.</b> A ribbon tested greige and a ribbon tested after printing, finishing and packaging are different products, because heat and finishing affect elastane. This is the same principle that applies to dimensional stability, and it is worth applying it here too.

<b>Do your own bench test before approving.</b> This takes five minutes and it is the highest-value thing you can do. Take a length of the sample, mark a measured span, stretch it to the extension you specified, hold it for the dwell time, release it, and measure the recovered length against the retained standard. Do this at least three times, and do it again after the sample has sat in your own warehouse for 48 hours, because an elastic ribbon that has been stored hot can behave differently from one that has not.

<b>Test the cut, not just the roll.</b> If your programme cuts the elastic ribbon to length, ties it, or folds it into a bow, run a small trial through your own conversion and test the finished piece. This is where most of the real-world elastic failures live: the ribbon on the roll performs, and the converted piece does not, because the conversion released some of the elastic's stored tension or introduced a stress concentration at the cut.

<b>Test the pack, not just the ribbon.</b> If the elastic's job is to hold something in place, build a small number of the actual packs and leave them under realistic conditions &mdash; including heat, because a warm environment accelerates elastic relaxation. Leave them for days, then open them and see whether they still hold. This test costs almost nothing and it is the closest thing to a prediction of what your customer will experience.

<b>Test the cycle count if the product will be reused.</b> A gift set that gets opened and closed repeatedly, or a hair accessory worn daily, is a fatigue application. Ask the mill for cycle data, or run your own: stretch and release the sample several hundred times, then re-measure recovery. The number that matters is not the absolute recovery after cycles but the change from the original.

<b>Keep a retained standard.</b> Keep a length of the approved ribbon with its measurements recorded. It is the only way to distinguish, in year two, between a ribbon that has genuinely changed and a ribbon that is being measured differently because your conditions have changed.""",
    ),
    (
        "Do You Actually Need Elastic? And When Elastic Is the Wrong Answer",
        """Before specifying elastic, it is worth asking whether elastic solves the problem, because elastic carries costs that are easy to overlook: a higher unit cost, a restricted supplier base, a narrower tolerance window, more sensitive handling in transit and storage, and a shorter practical life than an inelastic construction.

<b>When elastic is genuinely the right choice.</b> Where the product has to conform to a variable form &mdash; a hair accessory that has to fit different head sizes, a pet collar that has to fit a range of neck sizes, a gift set that has to hold items of differing shapes, a product that has to be stretched over a bottle or jar for assembly. These are exactly the cases where a non-stretch ribbon either will not fit or requires a mechanical adjustment the customer has to make, which is friction at the point of purchase.

<b>When inelastic is the better answer.</b> Where the ribbon is decorative and the pack does not need to adapt. Where the contents are of fixed, known dimensions and a fixed fold or bow closes the pack. Where the ribbon must hold a heavy item over a long shelf life &mdash; elasticity and long-term heavy load is a poor pairing, because heavy constant load accelerates permanent elongation. Where the product is a gift set intended to be a keepsake: a ribbon that stretches over weeks of handling on a shelf eventually looks tired.

<b>The middle option, which is often the right one.</b> A non-stretch ribbon with an elastic core in a hidden or structural component &mdash; a concealed elastic in the pack closure, or a separate elasticated band under a decorative outer ribbon. This gives you the function without putting the visible decorative element into a stretch-and-recover duty cycle, and it keeps the visible ribbon's specification simple and its tolerance wide. It also means two components to specify and two components to inspect, which is a real cost, but often a smaller one than a visible elastic ribbon that has to survive a long shelf life.

<b>One caution on elastic and branding.</b> Printed elastic is more demanding than printed woven ribbon, because the print has to survive repeated stretching without cracking, and because the elastane component dyes differently from the face yarn. Elastic is not the place to be adventurous with a new print technique on a tight launch schedule.

At Smith Ribbon we run elastic constructions for hair accessories, pet products and gift sets, and we will tell you honestly when a programme would be better served by a non-stretch construction with a functional closure, because the best outcome is a pack that still looks right in January.""",
    ),
]

FAQ = [
    (
        "What is the difference between stretch percentage and recovery percentage in elastic ribbon?",
        "Stretch percentage is how far the ribbon extends under a stated load, expressed as a percentage of its original length. Recovery percentage is how much of that extension the ribbon takes back once the load is removed. They are independent, and this matters commercially: a ribbon that stretches to 200% but recovers only to 70% will progressively lose its holding ability and its packs will go loose over time, however impressive the stretch figure is. For almost all packaging and wearable applications, recovery is the property that determines whether the product still works, so it is the number to specify tightly. Stretch is more tolerant, because how far an elastic extends is a natural property of the material and varies within a lot. Always specify both, with the load, the dwell time and the release period stated, because a bare number is not comparable between mills.",
    ),
    (
        "How do I specify stretch fatigue so that a ribbon still performs after a year of use?",
        "State the number of stretch cycles, the extension applied per cycle, the cycle rate or dwell time, and the permitted change in behaviour after that cycle count. This is the specification that protects you in year two, and it is the one most often omitted, because most qualification testing is done at approval on a fresh sample and never repeated. A practical approach is to ask the mill for cycle data on the construction, and separately to run your own test on the approved production sample: stretch and release the sample several hundred times, then re-measure recovery against a retained standard. The figure that matters is not the absolute recovery after cycling but the change from the original, so keep a physical length of the approved ribbon with its measurements recorded. For programmes where the elastic is functionally critical, such as a gift set that is repeatedly opened and closed, specify the fatigue requirement as a hard acceptance criterion with a stated consequence for a failing lot.",
    ),
    (
        "Why does elastic ribbon sometimes look fine on the sample and then fail in the pack?",
        "There are four common reasons and they are worth separating. First, the test was done on the greige or on the ribbon off the roll, not on the printed and finished construction, and heat from printing and finishing affects elastane. Second, the conversion process released some of the elastic's stored tension, so the cut, folded or tied piece behaves differently from the ribbon going into it. Third, the environment differs: an elastane core is temperature-sensitive in a way a polyester core is not, so a ribbon tested in an air-conditioned office can behave measurably differently after a week in a warm warehouse or a delivery van. Fourth, the specification simply did not state recovery, so nobody tested the property that actually determines whether the pack holds. The practical fix is to build a small number of the actual packs, leave them under realistic conditions including heat for several days, and open them. That test costs almost nothing and predicts most real failures better than any bench measurement.",
    ),
    (
        "Does a higher elastane content in the elastic core always mean a better ribbon?",
        "No, and this is a common mistake. A higher elastane content produces more stretch and generally better recovery, but it also changes the ribbon in ways that may not suit your programme. The face becomes slicker and visually thinner, which changes how it reads against your packaging and how it takes a print. It snags more readily on sharp edges, on shelf hardware and on handling. Cut edges fray and curl faster, because more elastic is exposed at the cut, which matters enormously if your programme converts ribbon to cut lengths or ties bows from it. It also generally increases unit cost. The right elastane content is determined by the load you need to hold, the visual effect you want, and how the ribbon will be converted. Specify the core construction explicitly and ask the mill to quote the behaviour you need at that construction, rather than asking for the highest stretch available and discovering the trade-offs at the sample stage.",
    ),
    (
        "Can elastic ribbon be printed and what should I check before approving a printed elastic?",
        "Yes, printed elastic is entirely normal, and it is a more demanding process than printed woven ribbon because the print has to survive repeated stretching without cracking, and because the elastane component in the core can take dye differently from the polyester face yarn. Before approving a printed elastic, check four things. First, look for print cracking after stretching the approved sample through repeated cycles at the extension your specification calls for, not just at one stretch. Second, check whether the core is exposed at any cut edge and whether the dyed core matches the face, because a difference in shade between face and core is visible on a cut edge. Third, confirm the colour has been approved on the finished construction rather than on a lab dip, since the heat and tension of printing can shift the shade. Fourth, for a tight launch schedule, prefer a print technique already running on that construction rather than a new one, because printed elastic is not the right place to be adventurous. Ask for a stretch-and-inspect sample rather than a flat swatch.",
    ),
    (
        "Should I specify compression set for elastic ribbon used in gift set packaging?",
        "Yes, if the elastic's job is to hold a lid closed, a bundle tight, or a shaped element in place over a period of time, because compression set is the property that tells you whether it will keep holding. Compression set is measured as the permanent deformation remaining after the ribbon has been compressed, held compressed for a stated time at a stated temperature, and then released. It is strongly temperature-dependent, so a test run at room temperature will not predict behaviour in a warehouse in July or in a delivery van in August. Specify the compression applied, the hold time, the temperature, the recovery period before measurement, and the permitted percentage. Remember also that the ribbon is usually doing the holding in combination with the pack board and the closure mechanics, so ask for the figure and test it in the assembled pack, not only on the ribbon. Where the pack must hold a heavy item over a long shelf life, be aware that a constant heavy load accelerates permanent elongation, and a non-stretch ribbon with a concealed elastic closure is often the more durable answer.",
    ),
    (
        "How do I test elastic ribbon before approving a sample?",
        "Do a bench test that takes five minutes and catches most problems. Mark a measured span on the sample, stretch it to the extension your specification calls for, hold it for the stated dwell time, release it, and measure the recovered length against a retained standard. Repeat at least three times, and repeat again after the sample has sat in your own warehouse for 48 hours, because an elastic ribbon that has been stored hot can behave differently from one that has not. Then test the actual application rather than the ribbon: if the ribbon is cut, tied or folded into a bow, run a small trial through your own conversion and test the finished piece, because the conversion releases stored tension and most real-world failures live there. Finally, if the elastic holds something in place, build a small number of the actual packs and leave them under realistic conditions including heat for several days before opening them. Retain a length of the approved ribbon with its measurements recorded, so that in year two you can distinguish a ribbon that has genuinely changed from a ribbon being measured differently.",
    ),
]

METRICS = [
    ("Commercially meaningful elastic properties to specify", "4 (stretch, recovery, compression set, stretch fatigue)"),
    ("Elements required in an inspectable elastic specification", "7 (stretch + load, recovery + dwell, compression set, fatigue cycles, core construction, environment, failure consequence)"),
    ("Typical recovery range for a quality polyester-elastane ribbon", "85% to 95% at moderate extension"),
    ("Typical elastane core content range for decorative elastic ribbon", "5% to 15% of core by weight"),
    ("Years of ribbon manufacturing and elastic construction experience", "22 (since 2004)"),
    ("Countries supplied", "50+"),
]

AUTHOR_BULLETS = [
    "Weaving, dyeing, printing and finishing in one Xiamen site &mdash; 15,000 m&sup2;, 200+ staff, 100,000 metres of daily output",
    "Elastic stretch, recovery, compression set and fatigue figures quoted with the test method stated, so the numbers can be compared",
    "We tell you when a non-stretch construction with a concealed elastic closure will outlast your programme",
    "20+ years supplying brand owners, retailers and converters in 50+ countries since 2004",
]

CLOSING_PARAGRAPH = (
    "Elastic ribbon is the one category in our business where the specification gap shows up as a customer complaint "
    "rather than as a rejected delivery, because the ribbon passes every conventional inspection and then fails "
    "quietly on a shelf. That is why the four numbers matter: stretch, recovery, compression set and fatigue. "
    "Write them down with their test conditions, test the converted piece rather than the roll, and build a few "
    "packs and leave them in the heat for a week before you approve. We have been weaving ribbon in Xiamen since "
    "2004, and in that time we have learned that the elastic programmes that run well are the ones where the "
    "buyer and the mill are talking about the same four figures."
)
CLOSING_CTA = (
    "If you are specifying an elastic ribbon programme and want the stretch, recovery, compression set and "
    "fatigue requirements written into your tech pack &mdash; together with a recent test record on the "
    "construction you are quoting &mdash; send us the width, the required stretch, the end use and the "
    "conditions it has to survive, and we will prepare it. Email xmmsd@126.com, or reach us on WhatsApp and "
    "phone at +86 137 7995 1780 &mdash; we reply within 24 hours."
)

cfg = {
    "url": URL,
    "title": TITLE,
    "desc": DESC,
    "keywords": KEYWORDS,
    "date_iso": DATE_ISO,
    "date_display": DATE_DISPLAY,
    "num": 315,
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
    "h2_title": "Specifying Elastic Ribbon With Smith Ribbon",
}

html = build_html(cfg)
with open(f"/workspace/ribbonbow123/blog-{SLUG}.html", "w", encoding="utf-8") as f:
    f.write(html)
print(f"Wrote blog-{SLUG}.html ({len(html):,} bytes)")
