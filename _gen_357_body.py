#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate body + FAQ for ribbonbow123 article #357 (AM, 08:00 slot, 2026-11-06).

#357 AM: OEM Custom Packaging & Private-Label Ribbon Programme Guide — what a
brand owner must define before a factory can quote, the 9-field development
brief, the sample ladder, artwork and colour ownership, decoration method
selection, MOQ and cost drivers, and the first-order readiness checklist.

House style: plain declarative prose, real tables, no "XXX-module" architecture
diagrams, no invented metrics. Entity = Xiamen Smith Ribbon&Bow, since 2004.
"""

BODY = r"""
<h2>What an OEM Packaging Programme Actually Is</h2>
<p>Private label is often described as "just putting my logo on their ribbon." That framing is the
single most expensive misconception in this category, and it is the reason so many brand owners
discover in month six that they cannot reorder what they launched, cannot prove they own the artwork,
and cannot get a second quote because the specification they gave was a photograph rather than a
document.</p>

<p>An OEM packaging programme is a manufacturing relationship in which you specify a physical product
precisely enough that two different factories would build materially the same thing, and precisely
enough that you can change factory without rebuilding your brand. That is the actual goal. Not
"find a cheap ribbon supplier." Not "find a factory that will put my logo on it." The goal is a
<strong>transferable specification</strong>.</p>

<p>Every section below exists to move you from the first position to the second. A specification that
only your current factory can interpret is a hostage negotiation. A specification that any competent
mill can quote against is an asset, and it is also what lets you renegotiate pricing later without
re-sourcing from scratch.</p>

<p>Smith Ribbon has been manufacturing ribbon, bows, tassels and decorative trim in Xiamen since 2004,
with an own factory of 15,000 m&sup2;, more than 200 employees, and daily output of 100,000 metres.
We have seen the failure modes below repeatedly, in both directions: brands who over-specified and
paid for unnecessary tooling, and brands who under-specified and paid for it in rejected shipments
instead.</p>

<h2>The Nine Fields a Factory Cannot Guess</h2>
<p>A factory will happily quote a one-line brief. It will also happily quote it wrong, because the
information missing from a one-line brief is not missing from the price. It is missing from the
<em>quality</em> of what you receive, and you pay for it at the receiving dock rather than in the
quotation.</p>

<p>Here are the nine fields we ask for before we put a number on anything. If your brief contains all
nine, you will receive comparable quotations. If it contains four, you will receive quotations that
look comparable and are not.</p>

<table>
  <tr><th>#</th><th>Field</th><th>What a usable answer looks like</th><th>What happens if it is missing</th></tr>
  <tr><td>1</td><td>Material and construction</td><td>Polyester satin (RPET or virgin), 2.5 cm width, 40mm roll face, double-faced weave</td><td>Supplier substitutes a cheaper base or a single-face construction; colour depth and hand change</td></tr>
  <tr><td>2</td><td>Width and tolerance</td><td>25 mm &plusmn;0.5 mm, verified across the roll, not at the core</td><td>Width drifts across the roll; trimming and spoilage absorb the difference</td></tr>
  <tr><td>3</td><td>Colour standard</td><td>Pantone 2945 C, target &Delta;E &le;1.5 against a signed physical lab dip</td><td>"Close enough to Pantone" becomes a recurring dispute about what Pantone even means on a woven textile</td></tr>
  <tr><td>4</td><td>Decoration method</td><td>Screen print, 4 spot colours, max 60% coverage per pass, on both faces</td><td>Wrong method selected; a heat-transfer or jacquard route may be technically possible but commercially wrong</td></tr>
  <tr><td>5</td><td>Finish</td><td>Hemmed, cut-to-length, cut ends heat-sealed</td><td>Raw-cut ends fray in transit and in the customer's assembly step</td></tr>
  <tr><td>6</td><td>Order profile and MOQ</td><td>3,000 metres per colour per style, single delivery, reorder cadence 8 weeks</td><td>MOQ set by what suits the mill's loom schedule rather than what suits your launch</td></tr>
  <tr><td>7</td><td>Pack format</td><td>50 m reels, 5 reels per carton, carton weight &le;15 kg, 40 cartons per 20 ft container</td><td>Freight cost per metre inflates because the reel format does not fit the carton or the container</td></tr>
  <tr><td>8</td><td>Delivery term and destination</td><td>FOB Xiamen, 40 HQ, deliver to Rotterdam, needed in warehouse by 2027-01-20</td><td>Lead time quoted is not lead time to your shelf; the difference lands entirely on your side</td></tr>
  <tr><td>9</td><td>Quality and compliance requirement</td><td>OEKO-TEX Standard 100 for the base fabric, ISO 9001 mill, colour fastness to ISO 105-B02 grade 4 minimum</td><td>CERTIFICATE GAPS DISCOVERED AT RETAILER ONBOARDING, WHEN REWORK IS NO LONGER AVAILABLE</td></tr>
</table>

<p>Note field 9 in particular. A brand that has not named its compliance requirement often finds out
that the mill it has been using for two years does not hold the certificate your retailer's vendor
compliance team requires, and that the certificate it does hold does not cover the specific product
class you are shipping. That gap is typically discovered at onboarding, and it is expensive at that
point because you are committed.</p>

<h2>The Sample Ladder: Five Steps, Each Proving a Different Thing</h2>
<p>The single most common sourcing error is approving a sample that does not prove what you need it to
prove. A swatch on a business card is not a pre-production sample. A pre-production sample is not a
production sample. Approving the wrong one means discovering a problem at 10,000 metres instead of at
10 metres.</p>

<table>
  <tr><th>Step</th><th>What it is</th><th>What it proves</th><th>What it cannot prove</th></tr>
  <tr><td>1. Lab dip / colour chip</td><td>Woven swatch, undecorated, in the target colour</td><td>Whether the mill can hit your colour at all, in the material you specified</td><td>Anything about print, finish or width</td></tr>
  <tr><td>2. Printed swatch</td><td>Decorated sample on correct stock, nominal print settings</td><td>Registration, ink coverage, hand, colour interaction with decoration</td><td>How it looks at 5,000 metres on a running loom</td></tr>
  <tr><td>3. Pre-production sample</td><td>Full-width, full-length, produced on production equipment</td><td>Edge finish, selvedge, roll winding, dimensional consistency</td><td>Batch-to-batch colour continuity</td></tr>
  <tr><td>4. Production sample / first-off</td><td>Taken from the actual production run</td><td>How the real run behaves, including dye-lot effects</td><td>Nothing about consistency across the run</td></tr>
  <tr><td>5. Sealed golden sample</td><td>One signed, sealed reference unit retained by you</td><td>The benchmark every future shipment is measured against</td><td>Nothing &mdash; it is a reference, not a test</td></tr>
</table>

<p>Step 5 is the one most brands skip and most regret skipping. A signed and sealed golden sample, held by
you, is what makes a dispute about a shipment resolvable in a week instead of a quarter. Without it, a
colour objection becomes an argument about whose memory of the approved shade is more reliable, and
the mill has a stronger incentive to be certain about it than you do, because the mill has the
production records.</p>

<p>Two practical notes. First, approve each step against a written specification, not against a
photograph, and store the specification with the sample. Second, put a <strong>date and a name</strong> on
every approval. An unsigned approval in an email thread is worth very little when you are trying to
recover a price increase or a defect credit eighteen months later.</p>

<h2>Artwork and Ownership: Get This Right Before You Print</h2>
<p>Intellectual property in private label is usually discussed as a legal matter, and it is a legal
matter, but the practical failure is an operational one. The artwork file sits on the mill's server, the
mill's pre-press team has made edits nobody logged, and when you move to a second source for a price
improvement, the new factory cannot get the file because you never actually held it.</p>

<p>Three things to settle, in order:</p>

<h3>1. Who owns the artwork, in writing, and when does it transfer</h3>
<p>The brand owner should own the artwork outright from the moment of creation. The contract should say
so explicitly, and it should say what happens to the file when the programme ends: the mill returns
all print-ready files, dies, screens and colour standards, or destroys them and confirms in writing.
"Files are held for the duration of the programme" is not good enough if you may exit the relationship
at any point, because you would then have to re-create your own artwork from scratch.</p>

<h3>2. Do you hold a copy of the print-ready file</h3>
<p>You should receive a full print-ready package for every artwork you use: vector artwork with fonts
converted to outlines, a separated colour file per print colour, and a written specification of the
declaration the mill used. In practice this is the item brands most often do not request, and most
often need. A logo drawn on a photograph of a swatch is not a production file, and if your second
source needs a plate, you will be waiting a week for a file that should have existed already.</p>

<h3>3. Are custom dies, screens or plates treated as your property</h3>
<p>A metal die, a screen or a printing plate is tooling, and tooling has a physical existence somewhere.
The usual arrangement is that tooling is paid for by the brand and remains the brand's property,
physically located at the mill, and returned or destroyed on exit. What you want to avoid is a
termination that requires the mill to "dispose of tooling at its discretion" while your artwork still
depends on it.</p>

<h2>Choosing a Decoration Method You Can Actually Cost</h2>
<p>The decoration method drives unit cost more than the base fabric does, which surprises people who
assume ribbon is a textile purchase. It also determines which decorations are possible at which widths,
and it determines the tooling cost you pay before you sell a single metre.</p>

<table>
  <tr><th>Method</th><th>Best for</th><th>Tooling</th><th>Volume behaviour</th><th>Watch for</th></tr>
  <tr><td>Screen print</td><td>Solid spot colours, simple repeats, larger runs</td><td>One screen per colour</td><td>Cost per metre falls sharply with run length</td><td>Ink coverage limits on woven or elastic substrates</td></tr>
  <tr><td>Heat transfer</td><td>Fine detail, photographic, short runs</td><td>Plate or transfer film</td><td>Cost per metre relatively flat across volumes</td><td>Hand of the ribbon changes noticeably</td></tr>
  <tr><td>Foil / hot stamping</td><td>Metallic and premium finishes</td><td>Die per size</td><td>Metallic foil cost dominates unit price</td><td>On very narrow widths, foil stiffness</td></tr>
  <tr><td>Jacquard weave</td><td>Pattern built into the structure, no inks</td><td>Programmed loom setup</td><td>Higher base cost, no per-decoration consumable</td><td>Pattern repeat limits, longer lead time</td></tr>
  <tr><td>Woven edge / wired</td><td>Structural edge for shape retention</td><td>Special loom setup</td><td>Cost driven by base construction</td><td>Stiffness, and weight per metre</td></tr>
</table>

<p>The mistake we see most often is specifying a method by name without specifying the coverage, the
colour count and the substrate it will run on. "Screen printed" is not a specification. "Screen printed,
four spot colours, maximum 60% coverage per pass, both faces, on 40mm polyester satin face" is a
specification, and it is the difference between a quotation you can compare and one you cannot.</p>

<h2>MOQ and the Cost Drivers Behind Your Unit Price</h2>
<p>Ribbon pricing is not one number, it is a stack. Understanding the stack is what lets you argue about
the parts that are negotiable and accept the parts that are not. A typical ex-works unit price for
custom printed polyester satin contains:</p>

<ul>
  <li><strong>Base fabric</strong> &mdash; the yarn and weave, often the largest single component, and the part that moves most with polymer and cotton price cycles.</li>
  <li><strong>Colour conversion</strong> &mdash; dyeing to your standard, which carries a setup cost per colour and a labour component per metre. The setup is why a second colour on an existing order is cheaper than a first colour on a new order.</li>
  <li><strong>Decoration setup</strong> &mdash; screens, plates, dies. Amortised across the run, which is why small quantities are disproportionately expensive per metre.</li>
  <li><strong>Decoration run cost</strong> &mdash; inks, foil, machine time, which scale with metres.</li>
  <li><strong>Finishing</strong> &mdash; hemming, cutting, heat-sealing ends, winding, which scales with metres and with roll format.</li>
  <li><strong>Quality cost</strong> &mdash; the inspection, testing and rework that your specification implicitly demanded.</li>
  <li><strong>Overhead and margin</strong> &mdash; which is where the negotiation actually lives.</li>
</ul>

<p>Two practical levers are usually overlooked. The first is <strong>colour consolidation</strong>: a
programme that uses four colours across 3,000 metres is far more expensive per metre than a programme
using two colours across 12,000 metres, even where the total decoration cost looks similar on paper.
The second is <strong>roll format</strong>: reel length is a free choice, and choosing a reel that fits
your carton plan and your container plan reduces freight per metre measurably, without touching the
mill's price at all.</p>

<p>Our standard terms for OEM customisation run from 1,000 metres per colour, with small-batch runs
available from 500 metres where the decoration is screen print and the artwork is simple. Those
thresholds are workable for a brand testing a product line, but they are not efficient, and a buyer
who plans around them will find the per-metre cost higher than it needs to be.</p>

<h2>Building the First Order: A Readiness Checklist</h2>
<p>The first order is where a packaging programme either becomes repeatable or becomes an anecdote.
The following checklist is what we work from internally before we release a first order, and we have
published it because buyers who use it get fewer surprises.</p>

<table>
  <tr><th>Ready</th><th>Item</th><th>Why it matters</th></tr>
  <tr><td>&#9744;</td><td>Development brief complete with all nine fields</td><td>Nothing should be quoted or ordered against a verbal brief</td></tr>
  <tr><td>&#9744;</td><td>Print-ready artwork received and confirmed in writing</td><td>Prevents the most common cause of production delay</td></tr>
  <tr><td>&#9744;</td><td>Lab dip approved against a signed physical reference</td><td>Colour is the single most expensive thing to get wrong</td></tr>
  <tr><td>&#9744;</td><td>Pre-production sample approved and sealed</td><td>Proves finish, width and winding</td></tr>
  <tr><td>&#9744;</td><td>Golden sample signed, dated, retained by the brand</td><td>Your reference for every future shipment</td></tr>
  <tr><td>&#9744;</td><td>Written specification with acceptance criteria attached</td><td>Defines what "good" means before production, not after</td></tr>
  <tr><td>&#9744;</td><td>Compliance evidence verified against the exact product class</td><td>Certificate scope, not certificate existence, is what gets audited</td></tr>
  <tr><td>&#9744;</td><td>Delivery term, container plan and in-store date confirmed in writing</td><td>Turns a lead time into a date</td></tr>
  <tr><td>&#9744;</td><td>Inspection level and pre-shipment photo evidence agreed</td><td>Protects you on the shipment that arrives, not the one you saw</td></tr>
  <tr><td>&#9744;</td><td>Tooling ownership and artwork return terms in the contract</td><td>Determines whether you can leave later</td></tr>
</table>

<h2>How to Structure the Agreement</h2>
<p>The commercial agreement should be short enough to be read and specific enough to be useful. The
clauses that earn their place in a first-order agreement are the ones that address the specific risks of
decorative trim: the specification attachment, the golden sample as the acceptance reference, the
defect remedy, the delivery window and the tooling and artwork ownership provisions.</p>

<p>Two of these deserve particular attention. The first is the <strong>defect remedy ladder</strong>: a
tiered structure that says what happens at a defect rate below the agreed AQL, what happens above it,
and at what point you require rework, at what point you require replacement, and at what point you
require a credit. A remedy that is not tiered is either too soft to be useful or too harsh to be
signed. The second is the <strong>price adjustment mechanism</strong>: an agreed index reference and an
agreed review cadence, so that a six-month-old price does not become either a windfall for the mill or
an open-ended exposure for you.</p>

<p>Longer relationships are usually better served by a separate supply agreement covering capacity
reservation, forecasting, lead-time commitments, quality escalation and review cadence, rather than
by overloading the first purchase order. Most of the friction in a packaging relationship comes from
not having agreed on those things before the first peak, not from the price.</p>

<h2>Common Mistakes and How to Avoid Them</h2>

<h3>Mistake 1: Specifying by photograph</h3>
<p>A photograph of a ribbon establishes an impression, not a specification. It cannot be quoted against
reliably, it cannot be used to compare quotations, and it cannot be used to argue a quality claim. Every
field in the nine-field table above exists because someone, somewhere, learned what happens when it is
left out.</p>

<h3>Mistake 2: Treating the first price as a permanent one</h3>
<p>The first quotation carries setup cost recovery, learning curve and a relationship premium that will
not be there on the second order. If you do not expect the price to come down and you do not ask, it
will not come down. Plan a price review at a defined point, with the order history as your evidence.</p>

<h3>Mistake 3: Leaving artwork and tooling unaddressed</h3>
<p>It feels like a formality at the start of a friendly relationship. It is not. It is the clause that
determines whether you have a right to your own logo at the end of it.</p>

<h3>Mistake 4: Not naming the compliance requirement</h3>
<p>The mill will make whatever it is certified to make. If you want a product class outside that scope,
you have to ask for it explicitly, and you have to ask early, because certification takes time.</p>

<h3>Mistake 5: Skipping the golden sample</h3>
<p>It costs one unit and a signature, and it is the only artefact that survives a dispute with a
supplier six months later.</p>

<h3>Mistake 6: Accepting a lead time instead of a date</h3>
<p>"Four to six weeks" means two different things in November and in March. Ask for the date the material
has to be on the floor to hit your in-store date, and confirm it in writing.</p>

<h2>What a Good First Conversation Looks Like</h2>
<p>If you are starting from zero, the fastest route to a usable quotation is a thirty-minute call with the
factory's own technical and merchandising staff in the room, not just a salesperson. Bring the brief,
bring the artwork, and be explicit about the field you are unsure about. A factory that asks you hard
questions about coverage and width and colour tolerance is telling you something about how the
relationship will go. A factory that quotes immediately from a photograph is telling you something else.</p>

<p>Bring the deliverable date, not just the quantity. Bring the compliance list, not just the product.
And if the answer is that something you want is not possible at your volume, that is useful information
to receive in week one rather than after you have committed to a launch date.</p>
"""

FAQ = [
    [
        "How long does it take to launch an OEM custom ribbon programme from first brief to shipment?",
        "For a standard custom printed polyester satin programme with a new colour and new artwork, a "
        "typical path from complete development brief to shipment is 45 to 70 days: colour development "
        "and lab dip approval in 7 to 12 days, printed swatch and pre-production sample in a further 7 "
        "to 10 days, then 25 to 40 days of production and 7 to 15 days in transit depending on "
        "destination and delivery term. Programmes with jacquard woven patterns, wired edges or "
        "multi-colour lamination run longer because setup is a loom programme rather than a print run. "
        "The single largest avoidable delay is artwork arriving late or in a non-print-ready format, "
        "which can add two to three weeks on its own.",
    ],
    [
        "What is the minimum order quantity for custom printed ribbon, and does it apply per colour?",
        "Our standard OEM customisation starts at 1,000 metres per colour per style, and we accept "
        "small-batch runs from 500 metres where the decoration is screen print and the artwork is simple "
        "enough not to require a separate plate. In practice the MOQ applies per colourway, not per "
        "order, which is the point that surprises first-time buyers: 1,000 metres split across four "
        "colours means 1,000 metres of each of four colours, and four dye-lot setups, not 4,000 metres "
        "of mixed stock. If your launch plan needs more colours at less depth per colour, that is a "
        "conversation worth having before the brief is written, because the alternative is usually to "
        "reduce the colour count or to raise the volume per colourway.",
    ],
    [
        "Do I own the artwork and the custom tooling if I work with your factory?",
        "Yes. The brand owner owns the artwork. We ask for a signed acknowledgement that the artwork, "
        "the print-ready files, the colour standards and any custom dies, screens or plates are paid "
        "for by the brand and remain the brand's property. On termination of the programme, those items "
        "are either returned to you or destroyed on your written instruction, and we confirm either "
        "outcome in writing. We also recommend, and practise as standard, that you receive a complete "
        "print-ready file package for every artwork you use, so that your brand is never dependent on "
        "our pre-press team to reproduce your own logo if you move to another source.",
    ],
    [
        "What is the difference between a lab dip, a pre-production sample and a golden sample?",
        "A lab dip is an undecorated woven swatch in your target colour, and it proves only whether we "
        "can hit the colour in the material you specified. A pre-production sample is a full-width, "
        "full-length decorated sample produced on production equipment, and it proves edge finish, "
        "selvedge quality, roll winding and dimensional consistency. A golden sample is a signed, sealed "
        "reference unit that you retain and use as the benchmark for every subsequent shipment. They "
        "each prove a different thing, and approving one does not substitute for approving the others. "
        "Most disputes we see come from a buyer approving a printed swatch and assuming production "
        "behaviour has been verified when it has not.",
    ],
    [
        "How do I make sure two factories quote the same thing so I can compare them?",
        "Send the same nine-field development brief to every factory: material and construction, width "
        "and tolerance, colour standard, decoration method with coverage and colour count, finish, "
        "order profile and MOQ, pack format, delivery term and destination with in-store date, and "
        "compliance requirement. Ask each factory to quote against each field separately rather than "
        "returning a single unit price, so you can see where the quotations actually differ. In our "
        "experience, quotations that look comparable on price are frequently not comparable on "
        "specification, and the differences usually surface as claims and rework after the first "
        "shipment rather than as a clear advantage at the point of comparison.",
    ],
    [
        "Which certifications do I need, and can you supply them?",
        "It depends on your end market and your retailer's vendor compliance requirements, so the "
        "honest answer is that it depends and you should specify it in the brief. In practice the most "
        "commonly required are OEKO-TEX Standard 100 for the base fabric, FSC where paper or "
        "board elements are involved, BSCI and SEDEX/SMETA for social compliance, and ISO 9001 for "
        "quality management. We hold these and can supply current certificates and test reports. The "
        "important point for a buyer is that you need to confirm the <em>scope</em> of each certificate "
        "covers your specific product class, not merely that the certificate exists. Certificate scope, "
        "expiry and covered product categories are what an auditor actually reads.",
    ],
    [
        "How do you handle colour matching, and what happens if the delivered colour is off?",
        "We work against a Pantone reference and an agreed physical lab dip, and we measure with "
        "spectrophotometer against the approved sample, with a target of &Delta;E within 1.5 for most "
        "programmes. Where a brand has no physical reference, we produce a lab dip first and get that "
        "approved before any print sample, because a Pantone chip read through a woven textile is not a "
        "reliable target on its own. If a delivered lot falls outside the agreed tolerance, the remedy "
        "is set out in the agreement: rework, replacement or credit depending on the defect rate and "
        "the timing. This is why the golden sample matters, and why we would rather resolve a colour "
        "question against a sealed reference in week one than against a recollection in month nine.",
    ],
    [
        "Can you produce from recycled or sustainable materials under my own brand label?",
        "Yes. We work with RPET recycled polyester and with certified sustainable material pathways, and "
        "we can support the documentation a brand needs to make an environmental claim. The requirement "
        "on your side is to be specific about the claim you intend to make, because recycled content "
        "claims are regulated and a claim you cannot substantiate is a liability rather than an "
        "asset. Tell us the claim you want to make and the market you will make it in, and we will tell "
        "you which evidence we can produce and which we cannot. It is better to design the supply route "
        "around the claim at the start than to add certification to a finished programme later.",
    ],
]

if __name__ == "__main__":
    import json
    from pathlib import Path
    Path("/tmp/rb357_body.html").write_text(BODY, encoding="utf-8")
    Path("/tmp/rb357_faq.json").write_text(json.dumps(FAQ, ensure_ascii=False, indent=1), encoding="utf-8")
    import re
    words = len(re.sub(r"<[^>]+>", " ", BODY).split())
    print(f"[OK] body words={words} faq={len(FAQ)}")
