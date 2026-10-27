#!/usr/bin/env python3
"""Article #312 - 2026-10-29 AM slot.

Topic: ribbon shrinkage, relaxation and dimensional stability for private-label
programmes - how to specify it, test it and stop shipped stock moving.

Distinct from every existing ribbonbow123 article:
  #308 quoted price line-by-line; #309 certificate scope; #310 decoration
  process selection; #311 sampling & pre-production approval; #307 compliance
  and claims substantiation; #306 inventory ownership / VMI.
Shrinkage and relaxation appear in the corpus only as fields inside a generic
spec-sheet decoder article, never as a dedicated buying topic.
"""
import sys
sys.path.insert(0, "/workspace/ribbonbow123")

from tmpl_ribbon_article import build_html

SITE = "ribbonbow123.com"
SLUG = "ribbon-oem-shrinkage-relaxation-dimensional-stability-specification-testing-private-label-buyers-guide-2026-10-29-am"
URL = f"https://{SITE}/blog-{SLUG}.html"
DATE_ISO = "2026-10-29T08:00:00+08:00"
DATE_DISPLAY = "October 29, 2026"

TITLE = ("Ribbon Shrinkage, Relaxation &amp; Dimensional Stability &mdash; How to Specify It, Test It and Stop Shipped Stock Moving (2026)")
DESC = (
    "A buyer's guide to ribbon shrinkage, relaxation and dimensional stability in private-label programmes. "
    "Explains why a ribbon that measures 38mm on the roll can measure 36mm in the finished pack, separates "
    "true shrinkage from roll relaxation and from the cutting and creasing that happen after the ribbon "
    "leaves the mill, covers the six causes - fibre relaxation, heat-setting, dyeing tension, printing "
    "heat, weaving tension and finishing - and sets out how to write a testable dimensional specification "
    "with the right conditioning protocol, measurement method and acceptance tolerance. Includes how to "
    "test before approval, how to re-order without the ribbon moving, and how to handle a batch that has "
    "moved. Written for brand owners, private-label managers and procurement teams."
)
KEYWORDS = (
    "ribbon shrinkage tolerance, ribbon relaxation specification, ribbon dimensional stability OEM, "
    "custom ribbon width tolerance after washing, ribbon shrinkage test method, private label ribbon spec, "
    "ribbon width change after cutting, ribbon heat setting shrinkage, satin ribbon shrinkage, grosgrain ribbon "
    "relaxation, ribbon conditioning protocol test, dimensional stability trim buying guide, "
    "ribbon batch to batch consistency, OEM ribbon quality control dimensions, B2B ribbon sourcing guide"
)

SECTIONS = [
    (
        "The Defect Nobody Notices Until the Pack Is Assembled",
        """There is a class of ribbon quality problem that does not show up on the mill floor, does not show up in the inspection report, and does not show up in the carton. It shows up in the finished pack, on the shelf, in front of a customer &mdash; and by then it is a line-down problem rather than a ribbon problem.

It is dimensional movement. The ribbon that left the mill at 38mm arrives at 36mm. The ribbon that was wound at 300 metres per roll now reads 292 metres on the roll. The bow that was assembled to a template no longer fits the gift box. The trim that was cut to length for a garment panel is now short by a few millimetres and the panel does not close. None of these are dramatic failures. The colour is right, the print is right, the hand feel is right, and the ribbon simply does not measure what the purchase order said it would.

The reason it is worth its own article is that dimensional movement is unusually easy to get wrong, for three specific reasons.

<b>It is invisible at the mill.</b> A roll of ribbon is inspected on the mill under tension, on the loom, immediately after finishing, often within hours of being wound. A ribbon that relaxes over several weeks of storage, or after a month in a hot warehouse, or after a night in a delivery van at 40&deg;C, will measure correctly at every one of those mill-side inspection points and still be wrong in your warehouse. The test that matters is the one taken under the conditions the ribbon will actually experience.

<b>It has three different causes that look identical.</b> A buyer who measures a short ribbon and assumes the mill made it to the wrong specification will often be wrong. The ribbon may be dimensionally correct and simply be relaxing after being wound under tension &mdash; a physical property of the fibre, not a fault. Or it may be correct at the roll and short after cutting, because cutting and creasing release the very tension that was holding the dimensions. Or it may genuinely be off-specification, in which case it is a defect and the mill should correct it. These three situations require three different responses, and confusing them wastes weeks.

<b>The tolerance is often written in a way that cannot be inspected.</b> "Shrinkage must be minimal." "Dimensional stability should be good." "No significant shrinkage." These sound like requirements and they are not requirements at all, because there is no measurement, no method and no number. An inspector reading them has nothing to test. The moment a dispute arises &mdash; and on a private-label programme disputes always arise eventually &mdash; the specification turns out to say nothing.

At Smith Ribbon, in Xiamen since 2004, we run weaving, dyeing, printing and finishing on one site and we test dimensional movement on every construction we quote, because a ribbon that moves is a ribbon the customer will blame on us regardless of whose fault it was. This guide sets out how to specify it properly, how to test it before approval, and how to make sure the re-order lands on the same numbers as the first order.""",
    ),
    (
        "Three Kinds of Movement That Are Not the Same Problem",
        """Before you can write a specification, you have to know what you are specifying against. Almost all dimensional confusion comes from treating three physically different phenomena as one.

<b>True shrinkage.</b> The ribbon genuinely changes dimension because the fibre itself changes length, usually because of heat, moisture or the removal of a processing aid. Polyester is the workhorse material in decoration ribbon and it is chemically stable, which is why polyester ribbon is comparatively forgiving. But polyester still relaxes: the fibres are held in a stressed state by the drawing and setting process, and over time, and under heat, that stress releases and the ribbon takes a slightly different set. This is the most common form of movement in polyester ribbon and it is not a defect; it is the material doing what the material does.

Where true shrinkage becomes a real problem is with other fibre families. Cotton and cotton-rich blends move significantly with moisture, and the movement is not one-way &mdash; the ribbon grows in humid conditions and shrinks in dry ones, so a cotton ribbon packed in a humid warehouse and opened in a dry retail environment will be measurably wider than the same ribbon measured in the warehouse. Viscose, modal and other regenerated cellulosics move with humidity in the same way, and more than cotton. Wool and wool blends move with both moisture and heat. Paper and metallised-paper ribbons behave completely differently, and are not covered by the tests discussed here.

<b>Roll relaxation.</b> This is the most commonly misdiagnosed phenomenon in the whole subject, and it is the reason experienced buyers insist on a conditioning step before measurement. Ribbon is wound onto a core under controlled tension. The winding tension holds the ribbon in a slightly stretched state. Once the roll is cut and the ribbon is free, the stored tension begins to release and the ribbon relaxes to its true length &mdash; and its true width may differ from the width it was at while it was being wound.

The practical consequence is straightforward and it surprises people: a ribbon measured directly off the mill roll can read differently from the same ribbon measured after it has been relaxed. That is why a specification that does not state a conditioning protocol before measurement is measuring two different things on two different days, and why two mills with identical looms can legitimately quote different numbers.

<b>Cutting, creasing and handling movement.</b> Once the ribbon leaves the roll, it is cut, folded, creased, twisted, tied and pulled. Each of those operations releases a little more of the stored tension. A ribbon cut to length for a garment panel and then folded will not measure the same as the same ribbon measured flat off the roll. This is not a fault, and it is not the mill's fault, but it is a real effect that has to be accounted for in the tolerance you set, because the customer will see the cut and folded version.

There is a fourth category that is genuinely a defect and should be handled as one: <b>batch-to-batch variation</b>. If the first delivery measures 38.0mm and the re-order measures 36.5mm, that is not relaxation &mdash; relaxation is deterministic and repeatable. That is the mill having produced a different product, and it is the failure mode that costs brands the most, because it is invisible until the second delivery lands and it silently invalidates every downstream cut dimension the brand has committed to.""",
    ),
    (
        "The Six Causes, and Where Each One Comes From",
        """Understanding the cause tells you where to look when a number moves, and more importantly it tells you what to ask the mill to control. There are six principal causes of dimensional movement in a ribbon programme, and each has a different owner.

<b>Fibre relaxation and residual tension.</b> The fibre arrives from the yarn supplier with a degree of internal tension set by the drawing and texturing process. When it is woven and then finished under tension, some of that tension is baked into the ribbon. Over time it releases. This is the baseline phenomenon that makes conditioning before measurement mandatory, and it is why the conditioning protocol is part of the specification rather than part of the mill's housekeeping.

<b>Heat setting and the tension under which it happens.</b> Almost every decorative ribbon is heat-set, because a ribbon that has not been heat-set will not hold its width, its edge or its finish. The heat-setting machine applies heat under tension, and the dimensional outcome depends on the temperature, the dwell time, the tension and the overfeed ratio. The overfeed &mdash; how much more ribbon is fed through the machine than the take-up pulls &mdash; is the primary dial: more overfeed means a more relaxed, more stable, slightly softer ribbon; less overfeed means a crisper, more stable-in-appearance ribbon that will move more later. This is a mill-side setting, and it is exactly the kind of variable a buyer should ask about when dimensions are not matching between suppliers.

<b>Dyeing tension and the effect of the dye bath.</b> Dyeing happens in a continuous process with the ribbon under tension, and dyeing itself applies heat, and the dye chemistry affects the fibre's behaviour. The dyeing tension and the overfeed used during dyeing contribute to the finished dimension in a way that is not obvious to a buyer. This matters most for heavy or elastic constructions, where the same setting has a much larger dimensional effect.

<b>Printing and decoration heat.</b> Printing adds heat, and heat adds movement. Screen printing with a cure oven, heat transfer with a heated platen, and sublimation all change the dimensional state of the ribbon. On a wide ribbon the effect across the width is small; on a narrow ribbon, where the web is under more tension relative to its width, the effect is proportionally larger. A printed narrow ribbon should therefore always be measured in its printed state, not in the greige state, because the two are different products dimensionally even when the mill considers them one job.

<b>Weaving tension, take-up and the width tolerance window.</b> The loom imposes a width tolerance as it weaves &mdash; typically something like plus or minus a small number of millimetres, and this window is set by the mill's own standard. Two things follow. First, a buyer's tolerance requirement interacts with the mill's tolerance window: a mill weaving to plus or minus 0.5mm cannot deliver a plus or minus 0.2mm requirement, so the requirement has to be realistic against the construction. Second, the position of a roll within the tolerance window matters. A roll that came off the loom at the narrow end of the window and a roll at the wide end can both be "in spec" and can still behave differently. This is one of the reasons a re-order can land at a different width even from the same mill.

<b>Finishing, and the surface that behaves differently to the core.</b> Satin finishing, calendering, brushing, crinkling, sand-washing, flocking and embossing all change the dimensional state of the web, in some cases substantially. A brushed or flocked ribbon has a surface that behaves differently to its core, and a flocked or brushed construction in particular can measure differently at the roll than it does in the finished assembly. Heat-laminated and metallised constructions add a layer that has its own behaviour.

There is a seventh, non-technical cause that belongs in the list because it is so common: <b>storage and transit.</b> A ribbon that has been stored in an unheated warehouse through a cold winter and then moved into a warm van is going to show different dimensions than the same ribbon measured in the warehouse, before any of the mill's processes are even considered. If your warehouse and your store are at different temperatures, you will measure two different products, and you need to know that before you raise a quality claim with a supplier.""",
    ),
    (
        "Writing a Specification That Can Actually Be Inspected",
        """A dimensional specification is only useful if three people can read it and agree on the answer: the mill's quality engineer, your inspector, and a dispute resolver. That requires five things to be present, and most purchase orders contain at most one of them.

<b>1. The property, named precisely.</b> Say whether you mean residual shrinkage after a defined heat treatment, residual shrinkage after a defined wash, width change after conditioning, length change after conditioning, or width change after a specified number of flexing cycles. These are different measurements and they do not substitute for each other. A mill that meets your wet-shrinkage requirement has not necessarily met your dry-heat requirement.

<b>2. The conditioning protocol.</b> This is the single most commonly omitted element, and omitting it is the reason two honest suppliers can quote two different numbers for the same ribbon. State the pre-conditioning state: the temperature and relative humidity the specimen is held at, and for how long, before measurement. A widely used convention is to condition at 20&deg;C and 65% relative humidity for at least 24 hours, but what matters commercially is that you and the mill use the same one. Specify it once, put it in the tech pack, and never negotiate it again.

<b>3. The test method, referenced by number where one exists.</b> For dimensional change there are established methods, and citing one removes argument. Common references include ISO 3758 for the determination of dimensional changes on washing and drying, ISO 5077 for the determination of dimensional changes on washing and drying of fabrics, and ISO 3758-derived methods used widely in the textile trade for residual shrinkage. For woven and decorated trims where no finished-article standard applies, the practice is to state the method in full: specimen size, the number of conditioning cycles, the wash or heat treatment, the measurement procedure and the number of specimens. A method stated in full is defensible; a method named vaguely is not.

<b>4. The measurement method and the equipment.</b> How the ribbon is measured changes the number. State the tension applied during measurement, whether the measurement is taken flat or under light tension, the gauge and the measurement points, and whether the specimen is measured before or after the treatment. This is not pedantry: measuring a ribbon at zero tension and measuring it under a defined light tension can produce different widths on the same ribbon, and a spec that does not say which is being used cannot be audited.

<b>5. The tolerance and the consequence of failure.</b> State the acceptance limit as a number with a unit and a direction &mdash; for example, a maximum width change of a stated percentage, or a maximum absolute deviation in millimetres from nominal. Then state what happens if the lot fails: held, re-worked, re-made, or accepted with a concession. A tolerance without a consequence is a preference, and it will be treated as one the moment the delivery is short and the launch is three weeks away.

One further point on tolerance direction. <b>Width tolerance and length tolerance behave differently in the market.</b> A ribbon that is 0.5mm narrow is normally a nuisance. A ribbon that is 0.5mm narrow across a 10-metre cut length for a garment panel is a shortage, and it converts into scrapped panels. Where a programme is cut to length, state the length tolerance in absolute terms per cut length rather than as a percentage, because a percentage of a long cut length is a very large absolute number.

At Smith Ribbon we write these five elements into the job folder before production is scheduled, so that the quote, the greige, the lab dip, the production sample and the final inspection all refer to the same document. We will also tell you when a tolerance you have asked for is tighter than the construction can hold &mdash; because a mill that quietly accepts an impossible tolerance and then misses it is far less useful to you than one that explains the achievable window at the quotation stage.""",
    ),
    (
        "Testing Before You Approve, and Testing the Re-order",
        """A dimensional specification that is only exercised at final inspection protects the mill, not the buyer. By the time the roll is on the truck, the cost of a dimensional problem is a freight bill, a delay and a credit note. The value is in testing earlier, in stages, and in a way that predicts what the ribbon will do in your own environment.

<b>Ask for the mill's own dimensional record on the actual lot, not a summary.</b> Any mill running a real quality system measures dimensional stability as part of its routine, on production lots, with dated records. Ask to see a recent one for the construction you have quoted. It is a reasonable request, and a mill that cannot produce it is telling you something about its process control. Ask what the conditioning protocol is and what the measurement method is, because a record without those two pieces of information cannot be compared to your own requirement.

<b>Test at the width and construction you will actually run.</b> Dimensional behaviour is not scale-invariant. A 38mm and a 15mm of the same construction do not behave the same way, and a 15mm narrow ribbon has a higher tension-to-width ratio and will generally show a larger proportional change. Approving a construction at 38mm and running it at 15mm without a test is a real and common mistake.

<b>Test the printed or decorated ribbon, not the greige.</b> This is the point most often missed. The greige and the finished ribbon are dimensionally different products, because printing adds heat and the finishing adds layers and tension. A test on the greige tells you about the greige.

<b>Do your own conditioning test before approving the sample.</b> Take the sample, measure it flat under light tension with a tape or caliper, record the ambient temperature and humidity, then leave it in your own warehouse conditions for a defined period &mdash; 24 to 72 hours is usually enough to reveal the relaxation &mdash; and measure it again. If it moves, you have found a problem while it was still cheap to fix. Repeat the measurement once more after a further interval to establish the rate of movement rather than a single delta. This single test is the highest-value thing a buyer can do in the whole approval process, and it takes five minutes and a tape measure.

<b>Re-measure on arrival of the re-order, against the retained standard.</b> Keep a physical length of the approved production ribbon, about 30cm, in a sealed envelope, and keep the measurement data with it. When the second delivery arrives, measure it against the standard under the same conditions. If it has moved, you need to know whether it moved because the ribbon is different or because your measuring conditions were different &mdash; and without a retained standard and a recorded protocol, you cannot tell, which means you cannot raise a defensible claim and you will probably not try.

<b>Measure in the conditions the product will experience.</b> If the ribbon ships into a warehouse and sells through a retail environment at a different temperature and humidity, test at both. A cellulosic ribbon that behaves perfectly in a 65% humidity warehouse can behave differently on a shop floor in July. If you are going to have a problem with dimensional movement, this is where it will appear.

<b>Watch the cutting operation specifically.</b> If your programme converts ribbon to cut lengths, bows or panels, run a small trial through your own conversion process and measure the finished piece, not the ribbon going in. The gap between the two is where your actual cost lives, and it is your process, not the mill's, so it is yours to measure.""",
    ),
    (
        "When a Batch Does Move: Handling It Without Escalating",
        """Even with a good specification and a good test, a batch will occasionally arrive with dimensions outside the agreed window. The question is how you handle it, and handling it well is worth real money.

<b>Establish first whether it is a fault at all.</b> Before contacting the mill, do three things: measure the ribbon under your own recorded protocol; measure it again after conditioning for 48 hours; and compare it with the retained standard from the approved sample under identical conditions. If the ribbon relaxes into the window after conditioning, the mill made it correctly and the measurement protocol differs from theirs &mdash; which is a specification gap on your side, and worth fixing in the tech pack rather than in a claim.

<b>If it is genuinely out of specification, quantify it in the terms that matter.</b> Not "the ribbon is short" but "the ribbon is 1.4% narrower than the approved standard, which reduces the usable panel width by 3mm and puts the programme 340 pieces short at our current cut plan". A claim framed in programme impact is a conversation about solutions. A claim framed as a percentage is a conversation about a credit note, and it will get you a credit note and a supplier who does not particularly want your next order.

<b>Ask for the root cause, specifically.</b> The mill should be able to tell you which of the six causes above is responsible, and what changed. If the answer is that the overfeed setting was changed, or a different yarn lot was used, or a different finishing route was run, then the problem is a process control issue that can be corrected. If the answer is that nothing changed, the problem is a measurement or specification issue and the fix belongs in your document.

<b>Agree a corrective action with a verification step.</b> Whatever the resolution &mdash; replacement, rework, concession, or re-run &mdash; it should be written down with the specific parameter that will be changed and the test that will demonstrate it worked on the next lot. A corrective action without a verification step is a promise.

<b>Protect the next delivery.</b> If you accept a concession lot, ask for the concession in writing with the actual measured value on it, and ask the mill to hold the same yarn lot and the same machine settings for the next production run if they can. A concession lot that is followed by a different lot that measures differently is a worse outcome than the original problem, because it removes the baseline you were comparing against.

<b>And close the loop in your own documentation.</b> Record the measured value, the protocol, the ambient conditions, the conclusion and the agreed action in the programme file. Programmes run for years, and the most valuable document in a stable OEM programme is not the purchase order but the running record of what was measured and accepted.""",
    ),
]

FAQ = [
    (
        "What is the difference between shrinkage and relaxation in ribbon?",
        "Shrinkage is a permanent change in dimension caused by the fibre itself changing length under heat, moisture or the removal of a processing aid. Relaxation is the release of tension that was built into the ribbon when it was wound onto a core, so that the ribbon settles to its true dimensions after it has been cut free. They look identical on the shelf and they behave differently in practice: relaxation is deterministic, repeatable and normally settles within a defined period, so it can be accounted for in the specification and in the packing; shrinkage caused by a genuinely off-specification ribbon is not, and it is a defect. This distinction is why a specification needs a conditioning protocol before measurement, and why a mill that quotes a shrinkage figure without stating the conditioning and measurement method has not really quoted anything you can use.",
    ),
    (
        "What shrinkage tolerance should I specify for custom ribbon?",
        "It depends on the fibre, the construction and the end use, and there is no single number that transfers. For polyester woven ribbon, which is the most common construction in decoration trim, a residual shrinkage limit in the region of 3% to 5% after a standard wash or heat treatment is generally achievable, and tighter limits are available for specific constructions. For cotton or cotton-rich blends, the figure is larger and the direction is not stable, because the ribbon moves with humidity as well as with wash. The specification should always state the property, the conditioning protocol, the test method, the measurement method and the tolerance together, because a bare percentage is not an inspectable requirement. At Smith Ribbon we state the achievable tolerance against your construction and your end use at quotation stage, and we will tell you if the figure you have in mind is tighter than the material can hold rather than agreeing to it and missing it later.",
    ),
    (
        "How do I test ribbon shrinkage before approving a sample?",
        "Measure the sample flat under light tension and record the ambient temperature and humidity. Then condition it for 24 to 72 hours in the conditions it will actually be stored in, and measure again. A ribbon that is dimensionally stable will move very little; a ribbon carrying significant residual tension will visibly change, and that change is visible within a day. Repeat once more after a further interval to establish the rate rather than a single reading. This test is worth doing before approval rather than after delivery, because at approval stage the cost of a dimensional problem is a conversation, and after delivery it is a freight bill and a launch delay. Always also measure the decorated ribbon rather than the greige, because the two are dimensionally different products.",
    ),
    (
        "Why did my re-order ribbon measure differently from the first delivery?",
        "There are three likely causes, and they should be separated in that order. First, the measurement conditions differed &mdash; different temperature, humidity, tension or measuring method between the two deliveries will produce different numbers on identical ribbon, which is why the protocol and a retained standard matter. Second, the ribbon is dimensionally different because something upstream changed: a different yarn lot, a different loom or setting, a change to the overfeed ratio, a different finishing route, or the roll was produced at a different point in the loom's tolerance window. Third, the programme itself has changed &mdash; a different width, a different construction or a different decoration route. The first is a documentation problem and the second is a mill process-control question, and the distinction matters because the two lead to very different conversations. Keeping a retained standard from the approved production lot and recording the measurement protocol each time is what makes the answer diagnosable rather than arguable.",
    ),
    (
        "Does ribbon width tolerance mean the same thing as shrinkage tolerance?",
        "No, and they behave very differently in the market. Width tolerance is the mill's own weaving window &mdash; how far the loom may deviate from nominal width while still producing an acceptable roll. It is a production-control property and it is fixed at the weaving stage. Shrinkage and relaxation tolerance is a post-production property describing how much the finished ribbon moves after it leaves the mill, and it is affected by everything that happens to the ribbon afterwards. The two also have different commercial consequences. A ribbon that is half a millimetre narrow at the roll is a nuisance. A ribbon that is half a millimetre narrow across a ten-metre cut length is a shortage, and it becomes scrapped panels. Where a programme cuts to length, specify the length tolerance in absolute millimetres per cut length rather than as a percentage, because the same percentage on a long cut length is a very large absolute number.",
    ),
    (
        "How much does conditioning affect the measurement of ribbon dimensions?",
        "More than most buyers expect, which is why conditioning is specified rather than assumed. A ribbon that is wound under tension on the mill and measured directly off the roll can read a different width from the same ribbon after it has been conditioned and allowed to relax, and the difference can be enough to fail a tolerance that the ribbon would comfortably meet once settled. For regenerated cellulose and cotton-rich blends the effect is larger and it is reversible, because those fibres respond to ambient humidity &mdash; the ribbon grows in humid conditions and shrinks in dry ones, so the same ribbon genuinely measures differently in a humid warehouse and a conditioned inspection room. For polyester the effect is smaller and one-directional, but it is still present. The practical rule is that every measurement in a programme &mdash; the mill's, the inspection agency's and yours &mdash; has to use the same conditioning protocol, and that protocol has to be written down.",
    ),
    (
        "Can ribbon be ordered with a pre-shrunk or relaxed finish to improve dimensional stability?",
        "Yes, and it is worth asking about, but the more useful question is what the mill's standard finishing route already does. Ribbon that is properly heat-set under a controlled overfeed ratio has already had the bulk of its relaxation taken out at the mill, which is why a competent mill's standard product is dimensionally better behaved than an unconditioned ribbon. Beyond that, there are two additional options. A dedicated relaxation or pre-shrink pass &mdash; a conditioning step that deliberately releases residual tension before the ribbon is wound &mdash; will reduce movement further, at a cost in production time and usually in a small amount of softness or fullness, because relaxed ribbon is a slightly fuller, slightly less crisp ribbon. For programmes where the ribbon is cut to length, tie into a garment or fitted panel, or used in a package with a tight dimensional fit, this can be worth the cost. For a decorative ribbon on a gift box, the standard route is normally sufficient. At Smith Ribbon we apply a controlled overfeed and heat-setting route as standard and will quote the additional relaxation pass where a programme needs it.",
    ),
]

METRICS = [
    ("Causes of dimensional movement identified", "6 (fibre relaxation, heat setting, dyeing tension, printing heat, weaving tension, finishing)"),
    ("Elements required in an inspectable dimensional specification", "5 (property, conditioning protocol, test method, measurement method, tolerance + consequence)"),
    ("Typical residual shrinkage limit for polyester woven ribbon", "3% to 5% after wash or heat treatment"),
    ("Conditioning protocol used before measurement", "20&deg;C / 65% RH / 24 hours minimum"),
    ("Years of ribbon manufacturing and quality control experience", "22 (since 2004)"),
    ("Countries supplied", "50+"),
]

AUTHOR_BULLETS = [
    "Weaving, dyeing, printing and finishing in one Xiamen site &mdash; 15,000 m&sup2;, 200+ staff, 100,000 metres of daily output",
    "Dimensional records available on request for production lots, with the conditioning protocol and measurement method stated on them",
    "We tell you when a tolerance you have asked for is tighter than the construction can hold, rather than agreeing to it and missing it later",
    "20+ years supplying brand owners, retailers and converters in 50+ countries since 2004",
]

CLOSING_PARAGRAPH = (
    "Dimensional stability is the least glamorous property in a ribbon specification and the one most likely to "
    "cost a brand a launch. It is decided in the finishing room and in the winding hall, long before anybody "
    "looks at the ribbon, and it is either specified as a number or it is not specified at all. The good news is "
    "that it is entirely manageable: write the conditioning protocol down once, keep a retained standard, test "
    "at the width you will run, and measure the decorated ribbon rather than the greige. That is a discipline we "
    "have applied since we began weaving ribbon in Xiamen in 2004, and it is why buyers who move a programme to "
    "us tend to stay for the life of the programme."
)
CLOSING_CTA = (
    "If you are specifying a custom ribbon programme and want the dimensional tolerance, the conditioning "
    "protocol and the test method written into your tech pack &mdash; plus a recent dimensional record from a "
    "production lot of the construction you are quoting &mdash; send us the width, the material and the end use, "
    "and we will prepare it. Email xmmsd@126.com, or reach us on WhatsApp and phone at +86 137 7995 1780 "
    "&mdash; we reply within 24 hours."
)

cfg = {
    "url": URL,
    "title": TITLE,
    "desc": DESC,
    "keywords": KEYWORDS,
    "date_iso": DATE_ISO,
    "date_display": DATE_DISPLAY,
    "num": 312,
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
    "h2_title": "Specifying Dimensional Stability With Smith Ribbon",
}

html = build_html(cfg)
with open(f"/workspace/ribbonbow123/blog-{SLUG}.html", "w", encoding="utf-8") as f:
    f.write(html)
print(f"Wrote blog-{SLUG}.html ({len(html):,} bytes)")
