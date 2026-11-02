#!/usr/bin/env python3
"""Article #311 - 2026-10-28 PM slot.

Topic: sampling & pre-production approval strategy for private-label ribbon.
Distinct from #310 (decoration method selection), #308 (cost lines),
#309 (certificate scope). Focus: what each type of sample actually proves,
how many to request, sample cost rules, and how to make an approval record
that means something at inspection.
"""
import sys
sys.path.insert(0, "/workspace/ribbonbow123")

from tmpl_ribbon_article import build_html

SITE = "ribbonbow123.com"
SLUG = "ribbon-oem-sampling-and-pre-production-approval-what-each-sample-proves-avoiding-the-wrong-approval-b2b-brand-procurement-2026-10-28-pm"
URL = f"https://{SITE}/blog-{SLUG}.html"
DATE_ISO = "2026-10-28T13:00:00+08:00"
DATE_DISPLAY = "October 28, 2026"

TITLE = ("Ribbon OEM Sampling &amp; Pre-Production Approval &mdash; What Each Sample Actually Proves (2026)")
DESC = (
    "A practical guide to sampling in private-label ribbon programmes. Breaks the sample ladder down into "
    "the eight distinct things a ribbon sample can be - colour lab dip, greige, printed strike-off, "
    "production sample, construction sample, performance test sample, assembly sample and packing "
    "sample - explains what each one proves and what it does not, sets a sensible sampling budget, "
    "covers sample cost and timing rules, and shows how to write a pre-production approval record that "
    "still means something when the roll arrives. Written for brand owners, quality managers and "
    "procurement teams running private-label ribbon programmes."
)
KEYWORDS = (
    "ribbon OEM sampling strategy, pre-production sample approval ribbon, lab dip vs strike off ribbon, "
    "printed ribbon sample proof, ribbon production sample PPAP, private label sample cost, "
    "ribbon sample approval checklist, ribbon colour lab dip process, ribbon testing sample before bulk order, "
    "B2B ribbon quality sampling guide, ribbon sample rejection reasons, ribbon new product introduction sample"
)

SECTIONS = [
    (
        "Sampling Is Not a Step, It Is a Chain",
        """A buyer in a hurry treats sampling as one event: the factory sends something, the buyer looks at it, the buyer says yes or no. That model works occasionally and fails quietly the rest of the time, because the thing you are shown at any single moment is not the thing you will receive in a container four months later.

The reason is simple. A ribbon programme contains several kinds of uncertainty, and each kind of uncertainty needs its own piece of evidence. Will this construction be right? Is the colour right? Does the printed artwork sit correctly on this substrate? Will the decoration survive the use? Does the finish hold up? Does the whole thing work in the finished assembly? These are separate questions, and a single sample handed across a table answers at most one of them.

The consequence of skipping a step is rarely a catastrophic failure. It is a quiet drift: the production roll is slightly off in shade, the print sits a little wide of centre, the hand is a bit stiffer than the swatch, and the problem is discovered by your customer rather than by your inspector. That is the expensive version, because the cost of a rejected container is far higher than the cost of three extra sample rounds.

So the useful frame is not "how many samples do I need" but "what is each sample for". Once you can name the question a sample answers, the number of samples stops being a matter of preference and starts being a consequence of your programme. A simple solid-colour ribbon on a standard construction may need two samples and a signature. A new construction in a new print process, in a new decoration, going into a new assembly, needs the whole ladder.

The other thing to get right at the outset is that approval is a record, not a feeling. A sample that is liked in a meeting and never written down has not been approved, it has been admired. The approval record &mdash; who approved it, when, against which document, with what measurement or visual criterion &mdash; is what the mill builds the production run against and what an inspector refers to when the shipment is checked. Getting the discipline right early is far cheaper than reconstructing what was agreed after the goods have shipped.""",
    ),
    (
        "The Eight Samples That Do Different Jobs",
        """Not every programme needs all eight. But every sample a buyer requests should be doing a specific job, and these are the jobs that exist.

<b>1. The greige sample.</b> The undecorated ribbon in the specified construction &mdash; the weave, the width, the selvedge, the hand. This is the sample that answers the most fundamental question: is the base material right? Is the edge properly selvedged or is it a slit edge? Is the width within tolerance at three points along the ribbon? Is the hand soft or stiff? Does it drape the way the finished product needs it to drape? Get this wrong and everything downstream is built on a bad foundation. If your construction is new or unusual, this is the first sample to request and the one most often skipped.

<b>2. The colour lab dip.</b> A small swatch of the ribbon dyed to your colour, before decoration. This settles shade, and only shade. A lab dip does not prove the print will look right on that shade, does not prove the shade holds when the ribbon is printed, and does not prove the colour is even along the width or repeatable lot to lot. Its role is to let you approve a shade in isolation, cheaply and quickly, before any screen or plate is cut. Note that a lab dip for a metallic or a textured effect is of limited use, since the effect comes from the finishing, not the dye.

<b>3. The printed strike-off or swatch.</b> The decoration applied to a short length of the greige, showing the artwork as it will print. This is the sample that answers the artwork questions: is the artwork positioned correctly across the width, is the design repeat correct, are the colours where they should be, is any detail lost at this size, does the ink sit acceptably on this texture. A strike-off is the right place to catch a logo that is too small, a colour that does not read on the ground colour, or a design that needs to move. It is not the right place to judge wear or wash performance, because a metre of ribbon has not been through the process a finished product will.

<b>4. The production or pre-production sample.</b> Made on the production line, on the actual machine, using the actual production tooling, at close to production length and quantity. This is the sample that answers the production question: does the line produce this consistently, and does a production-made example match the strike-off. In many programmes the most valuable thing about this sample is not the ribbon in your hand but the discovery of what differs between the strike-off and the production run &mdash; typically print saturation, edge definition, or a shade that shifts slightly once the full heat-setting cycle has run.

<b>5. The construction and dimension sample.</b> A measured length used to verify the specification numerically rather than visually &mdash; width at three points and along the length, selvedge condition, thickness, the count or structure, and any dimensional characteristic that the finished assembly depends on. In practice this is often the same physical sample as the greige, but the purpose is different: you are not looking at it, you are measuring it, with a calibrated instrument, against a written tolerance. The habit of measuring rather than eyeballing is worth building early, because eyeballed width drifts across a programme faster than anyone expects.

<b>6. The performance test sample.</b> A quantity of ribbon reserved for destructive testing &mdash; crocking, wash fastness, rubbing, light fastness, colour fastness, and whatever specific test your end use implies. These are not samples you hold; they are samples you consume. The point is to test before the production run rather than after, and to test on ribbon made the way the production run will be made, because a test on a different construction proves nothing about your product. A programme that will be washed should have the wash test specified with a method and an acceptance grade, not with an adjective.

<b>7. The assembly sample.</b> The decorated ribbon built into the actual finished assembly &mdash; the bow, the gift box, the hair accessory, the garment, the pack. This is the sample that answers the question no ribbon sample can: does the ribbon work in the product. It exposes the mismatches that only appear at this stage: the width is wrong for the loop, the hand is too stiff to tie neatly, the decoration is at an awkward position once the bow is formed, the colour is wrong against the pack. Many programmes skip this step and then discover the problem in a photo of the finished product.

<b>8. The packing and presentation sample.</b> How the ribbon arrives: the spool or reel, the length per unit, the carton quantity, the labelling, the placement of the brand mark on the core, the inner bag, the master carton. A ribbon that is excellent in the hand and unusable on the shelf &mdash; the wrong core size, the wrong length per reel, no brand identification on the core &mdash; is a real and common failure, and it is only visible in this sample.

Eight questions, eight samples, each answering something the others cannot. The programme decides which ones you need, and a supplier who understands this will help you build the right set rather than sending a package of miscellaneous swatches.""",
    ),
    (
        "How Many Samples to Request, and What to Budget",
        """Buyers routinely over-sample and then rush the ones that mattered. A better approach is to request one sample per open question, and to be explicit about what each one is for.

<b>Count the questions, not the metres.</b> For a standard construction, an existing colour, in a new print, going into an existing assembly, the honest answer might be three rounds: a strike-off for the artwork, a production sample for the line, and an assembly sample for the finished product. A new construction in a new colour with a new decoration into a new assembly might need six or seven rounds. Adding rounds without adding questions costs time and money and teaches you nothing.

<b>Set a sample budget in time as well as money.</b> Money is the smaller cost. The real cost of sampling is calendar. Every round of a sample sits on the critical path of the launch, and samples travel, get reviewed internally, and often wait for a decision. A programme that needs four rounds should assume four to six weeks of sampling activity, not two. Building that into the launch plan at the start is much better than discovering it.

<b>Understand the sample cost rules.</b> Samples are normally not free, and it is entirely reasonable that they are not &mdash; the mill has set up a screen, used yarn and machine time, and shipped a parcel. The reasonable arrangements, and the ones you should expect from a serious supplier, are: sample cost is charged and then credited against the production order if the order is placed; sample charges are modest and stated upfront rather than discovered on the invoice; and a limited number of samples are included or free at the pre-production stage, usually against the eventual order value. What you should not accept is a sample cost that appears for the first time after approval, or a charge that is not credited.

<b>Specify the physical format and quantity of each sample.</b> "Send us a sample" is an instruction that produces a 20cm offcut, which is useless for testing and useless for judging hand. Specify what you need: a metre length for a strike-off, a five-metre length for an assembly sample, a specific number of reels in production packing for a packing sample, and the width you want to see it at. The mill will usually supply a sensible format if you ask for one; it just will not infer it reliably.

<b>Set the turnaround expectation in the request.</b> Sample lead time is not the same as production lead time, and it is often shorter, but it is not instant. State the date by which you need the sample and what the programme deadline is, and ask for a realistic commitment. A supplier who tells you the sample will take five working days is giving you information you can plan around.

<b>Send samples to more than one decision-maker.</b> If the approval depends on design, on quality and on merchandising, do not let one person hold the only physical sample. Either route the sample to each of them or take good photographs under controlled light with a colour reference in frame, which serves surprisingly well for colour approval and poorly for hand and drape.""",
    ),
    (
        "Approving a Sample in a Way That Survives Production",
        """The purpose of approval is not to record that you liked something. It is to give the mill a reference against which the production run will be built, and to give yourself a reference against which the shipment will be judged. Most quality disputes in ribbon programmes are not disagreements about quality; they are disagreements about what was approved.

<b>Approve against criteria, not impressions.</b> A sample approved as "looks right" cannot be defended. A sample approved against written criteria can. The criteria for a colour sample: the reference standard it was compared to, the measurement method, the tolerance, and the lighting condition under which the comparison was made. For a print: the artwork file or version, the position across the width, the repeat length, the colour list with references, and the acceptable tolerance for the print itself. For a construction: the dimensions with tolerances and the measurement method.

<b>Compare against the right standard.</b> A screen is not a reference. A photograph on a phone is not a reference, because every screen renders colour differently. Approved colour references should be physical: the retained lab dip, a production swatch cut from an approved lot, or a defined physical standard. If you approve colour on a screen, you have approved nothing reproducible, and you will get an argument at inspection that you cannot win.

<b>Control the viewing conditions.</b> Colour approval under a shop-floor fluorescent tube and approval under a daylight window can produce different decisions on the same ribbon. Agree one standard condition &mdash; typically D65 daylight or a standardised light box &mdash; and use it every time, including at incoming inspection. This single discipline removes a remarkable share of colour disputes.

<b>Record the approval formally and immediately.</b> Who approved it, on what date, which sample, against which document version, and any conditions attached. A formal approval record takes two minutes to write and is the difference between a defensible position and an argument. Where your organisation has a quality system, the approval record is a controlled document, not an email.

<b>Approve the right level of the assembly.</b> If the ribbon goes into a bow, approve the bow, not the ribbon. If it goes into a hair accessory, approve the accessory. The approval should be on the level at which the product will be judged by a customer, because that is the level at which failure will occur.

<b>Keep the approved sample.</b> A physical sample of the approved construction, printed or decorated, signed and dated, retained in the file, is the most useful single artefact in a dispute. It costs almost nothing and it is decisive. We ask clients to retain ours, and we send a signed, dated production sample back with the shipment so that the standard travels with the goods.

<b>State what happens if production does not match.</b> Put it in the purchase order or the job folder: production must match the approved sample and the written specification; where it does not, the lot is subject to rejection or to a defined remedy. A programme with that clause has a clear route out of a quality problem. A programme without it has a conversation.""",
    ),
    (
        "The Approval Record That Makes Production Unambiguous",
        """The written approval record is not paperwork for its own sake. It is the document the mill's production and quality teams work from, and if it is missing, they work from a verbal understanding and from their own interpretation of the specification. That is where most ribbon quality problems originate.

A workable approval record for a ribbon programme contains these fields.

<b>Programme and item identification.</b> The internal programme reference, the buyer-side item code, the mill's job number, and the article number. These need to be reconciled, because a mismatch here is how a good roll ends up attached to the wrong paperwork.

<b>The specification version.</b> The date and version number of the technical specification the sample was judged against. If the specification changes after the sample, the approval does not automatically carry over, and the record should say so.

<b>The sample identity.</b> Which sample, physically described: the length, the width, the colour reference, the construction, the decoration method, and the date it was made.

<b>The decision.</b> Approved, approved with the listed conditions, or rejected &mdash; and if rejected, what specifically failed. A rejection without a reason teaches nobody anything and guarantees the same conversation next time.

<b>The criteria applied.</b> The specific measurement or comparison: the colour standard and tolerance and the measurement method; the width and tolerance and where it was measured; the artwork version and position and repeat; the performance test results with their method and grade, if the test sample was part of this approval.

<b>The limitations and the open points.</b> What the approval does <em>not</em> cover. This is the field most often omitted and the one that prevents the worst disputes, because it tells the mill that a wear test, a wash test or a bulk comparison is still outstanding.

<b>The conditions.</b> The date by which the production run must be scheduled, the approval's validity period if the approval is time-limited, the delivery point for the retained sample, and any requirement for a pre-shipment inspection or a third-party check.

<b>The signatories.</b> Who approved, in what role, and the date.

<b>The retained artefact.</b> Where the physical approved sample is held, and the job folder reference.

Keep the record with the specification, the purchase order and the test reports, in one place, in a form your team can find. A document that exists but cannot be located is not evidence.

At Smith Ribbon, this record is generated with the job folder and travels with the production paperwork, so that the mill's production team, our quality team and your inspector are all working from the same reference. We send the signed approval sample with the shipment as well. It is a small administrative habit that removes an entire category of dispute, and we have kept it since 2004 for exactly that reason.""",
    ),
    (
        "Sampling Mistakes That Cost Buyers Real Money",
        """These are the failures that recur, and they are worth listing because each is avoidable.

<b>Approving on a screen.</b> Every laptop and phone renders colour differently, and none of them is a reference. Colour approval on a screen is not approval. It is a preference that will not survive contact with a warehouse.

<b>Approving the strike-off as if it were the production sample.</b> The strike-off is often hand-made or run at short length with different settings. The production run differs. Approving the strike-off and then treating a normal production difference as a defect produces a pointless dispute and, worse, teaches the mill that you will not accept normal variation.

<b>Testing ribbon that is not the ribbon you will ship.</b> If the test sample is a different construction, a different substrate, a different print process or a different finish, the result tells you about that sample and not about your product. Every test must be on production-equivalent material.

<b>Skipping the assembly sample.</b> The ribbon is approved, the production run is fine, and the product still does not work &mdash; because the width is wrong for the loop, or the colour is wrong against the pack, or the hand does not tie. The assembly sample is the cheapest insurance in the programme and it is the one most often dropped.

<b>Not specifying the physical format of the sample.</b> A 20cm offcut cannot be tested, cannot be assembled into a bow, and cannot be judged for hand. Say what you need in metres and at what width.

<b>Sampling everything and deciding nothing.</b> Sending a supplier eleven samples with no questions attached produces eleven samples and no information, and it delays production while the mill waits for direction. Every sample request should say which question it answers.

<b>Approving by email without recording what was approved.</b> "Looks good, go ahead" is approval by implication. It will not settle a later disagreement about what "good" meant, and it leaves the mill without a reference to build against.

<b>Treating a test failure as a sample problem.</b> If the wash test fails, that is a specification or process issue, not a sampling issue. The right response is to identify whether the substrate, the colour, the decoration process or the curing was the cause, and to fix that. A buyer who simply re-samples and hopes for a different result has learned nothing and has burned four weeks.

<b>Letting the schedule slip without telling anyone.</b> Sampling slips for good reasons. The damage comes from the launch date moving silently while the production plan was built on the old one. Say it early; the mill can often help with a shorter route to the same answer if they know the date is real.""",
    ),
]

FAQ = [
    (
        "What is the difference between a lab dip and a printed strike-off in ribbon sampling?",
        "They answer different questions and are not interchangeable. A lab dip is a small swatch of the ribbon dyed to your colour before any decoration, so it settles shade only. It tells you nothing about how the print will look against that ground colour, nothing about the artwork, and nothing about wear performance. A printed strike-off is the decoration applied to a short length of the ribbon, so it settles artwork position, colour interaction with the ground, detail legibility and repeat. In practice you want both, in that order, because approving a print against a shade you have not yet approved means approving it twice if the shade changes. A third, separate artefact is the production sample, which is made on the production line and answers whether that result holds at production length and volume.",
    ),
    (
        "How many samples should a private-label ribbon programme require?",
        "One per open question, which for most programmes is between three and seven rounds rather than a fixed number. A standard construction in an existing colour with a new print going into an existing assembly typically needs three: a strike-off for the artwork, a production sample for line consistency, and an assembly sample for the finished product. A programme with a new construction, a new colour, a new decoration and a new assembly needs more, because each of those introduces a new variable that the previous sample could not have tested. The useful discipline is to name the question before requesting the sample. Buying a package of miscellaneous swatches produces information nobody can act on and delays the programme while the mill waits to be told which one matters.",
    ),
    (
        "Should samples be free?",
        "Not necessarily, but the commercial arrangement should be explicit and reasonable. A mill has set up a screen or plate, consumed yarn and machine time, and shipped a parcel, so charging for samples is legitimate. What you should expect is a stated sample charge that is credited against the production order if you proceed, a clear statement of what is included at the pre-production stage, and no surprise sample charges appearing after approval on the invoice. The arrangement worth agreeing at the outset is: sample cost quoted and credited against the first order, quantity and format of each sample specified in the request, and a stated turnaround per round. At Smith Ribbon we quote the sample cost and the credit against the order as a single line before you commit.",
    ),
    (
        "Can I approve ribbon colour from a photograph or a screen?",
        "No. Colour cannot be approved from a photograph or from a screen, because no display renders colour reliably and every device does it differently. A photograph is also affected by the lighting where the photo was taken, by the camera's white balance, and by compression. Approved colour references should be physical: a retained lab dip cut from the approved batch, a production swatch cut from an approved lot, or a defined physical standard held by both parties. If your organisation cannot retain physical references, the alternative is to specify the colour numerically with a stated measurement method and tolerance, and to confirm it on physical swatches at the point of production. What you should not do is approve a shade you cannot later reproduce in the inspection room.",
    ),
    (
        "How long should a ribbon sampling round take, and what should it be allowed to slip into?",
        "A typical round takes three to five working days for a greige or strike-off sample and five to ten for a production sample, because production samples wait for a slot on the line and for the relevant finishing step. A performance test sample takes longer again, since crocking and wash fastness are not instant. In practice you should budget four to six weeks of sampling activity across a full programme, and build that into the launch plan rather than treating sampling as a formality before the real timeline starts. When a round slips, tell the mill why, because a tightened commercial deadline often changes what can be run in parallel. The failure mode is not the slip itself but a launch date moving silently while the production plan was still built on the old one.",
    ),
    (
        "What should I do if the production roll does not match the approved sample?",
        "First establish what the difference actually is, because most production-versus-sample differences are normal variation rather than a defect. Screen-printed saturation, edge definition and shade can all shift slightly between a strike-off and a full production run, and the specification should state the tolerance that separates acceptable variation from a defect. If the difference is within the written tolerance, it is not a defect and should not be treated as one, however much it disappoints. If it falls outside the tolerance, then the approved sample and the written specification become the reference, and the mill's correction or replacement remedy applies under the purchase order. This is why the approval record needs the criteria and the tolerance written into it, and why it needs to be signed and dated on the day the decision was made rather than reconstructed after the dispute.",
    ),
    (
        "Is a pre-shipment inspection necessary if I have approved samples?",
        "Approved samples establish what you wanted; they say nothing about what was produced in your absence. The two most common findings in ribbon pre-shipment inspection are shade drift from the approved reference and decoration defects such as registration faults, incomplete curing, or foil adhesion failure in a batch, and both are invisible in a sample because they arise from the production run itself. For a first order, for a new decoration process, or for any order where a shade or construction has a history of drifting, a pre-shipment inspection before the container seals is inexpensive compared with the cost of a rejection after arrival. For a repeat order on a well-established programme running against a signed approval record, an inspection can often be scaled back to a documentation review plus a spot check.",
    ),
]

METRICS = [
    ("Distinct jobs a ribbon sample can do", "8"),
    ("Typical sampling rounds for a standard programme", "3"),
    ("Sampling rounds for a new construction, colour, decoration and assembly", "6-7"),
    ("Recommended sampling calendar before production", "4-6 weeks"),
    ("Years of ribbon manufacturing and sampling practice", "22 (since 2004)"),
    ("Countries supplied", "50+"),
]

AUTHOR_BULLETS = [
    "Sampling plan and approval record generated with the job folder, so production and inspection share one reference",
    "Signed, dated production sample retained and returned with the shipment",
    "Greige, lab dip, strike-off and production samples available in-house &mdash; 15,000 m&sup2;, 200+ staff, 100,000 metres of daily output",
    "20+ years supplying brand owners, retailers and converters in 50+ countries since 2004",
]

CLOSING_PARAGRAPH = (
    "Sampling is the only mechanism a buyer has to find out what a factory can actually make before a "
    "container is on the water. Used well, it converts the programme's uncertainties into named questions and "
    "answers them in order, at a cost measured in weeks rather than in a rejected shipment. Used badly, it is a "
    "handful of swatches, a hurried approval and a discovery made by your customer. The difference is "
    "discipline: one sample per question, physical references for colour, written criteria, and a signed record "
    "that travels with the goods. It is how we have worked since 2004, and it is why the buyers who sample "
    "properly the first time rarely have to argue about quality later."
)
CLOSING_CTA = (
    "If you are building a private-label ribbon programme and want a sampling plan for your specific "
    "construction, decoration and end use, together with an approval record template your quality team can "
    "adopt, send us the requirement and we will send both. Email xmmsd@126.com, or reach us on WhatsApp and "
    "phone at +86 137 7995 1780 &mdash; we reply within 24 hours."
)

cfg = {
    "url": URL,
    "title": TITLE,
    "desc": DESC,
    "keywords": KEYWORDS,
    "date_iso": DATE_ISO,
    "date_display": DATE_DISPLAY,
    "num": 311,
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
    "h2_title": "Building a Sampling Plan With Smith Ribbon",
}

html = build_html(cfg)
with open(f"/workspace/ribbonbow123/blog-{SLUG}.html", "w", encoding="utf-8") as f:
    f.write(html)
print(f"Wrote blog-{SLUG}.html ({len(html):,} bytes)")
