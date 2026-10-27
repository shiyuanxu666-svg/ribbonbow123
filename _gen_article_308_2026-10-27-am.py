#!/usr/bin/env python3
"""Article #308 - 2026-10-27 AM slot.

Topic: OEM private-label packaging artwork-to-shelf readiness is covered in
#301/#302; this article focuses on the *cost-side* of a factory buying
decision that is not covered by the generic should-cost pieces: how to read
and defend a woven-ribbon quoted price line by line, and where the money
actually goes between the mill's quote and the price that lands on your
dock. Built as a practical cost-transparency playbook for procurement
managers who have to defend a number internally.
"""
import sys
sys.path.insert(0, "/workspace/ribbonbow123")

from tmpl_ribbon_article import build_html

SITE = "ribbonbow123.com"
SLUG = "ribbon-oem-quoted-price-line-by-line-where-the-money-goes-defending-a-factory-number-b2b-procurement-2026-10-27-am"
URL = f"https://{SITE}/blog-{SLUG}.html"
DATE_ISO = "2026-10-27T08:00:00+08:00"
DATE_DISPLAY = "October 27, 2026"

TITLE = ("Ribbon OEM Quoted Price, Line by Line &mdash; Where the Money Actually Goes and How to Defend a Factory Number (2026)")
DESC = (
    "A practical guide to reading a woven ribbon factory quotation. Breaks a mill price into fourteen "
    "cost lines - yarn, dyeing, weaving, finishing, sizing, tooling, QC, packing, overhead, margin, "
    "freight and duty - shows what each line should look like for a given width, material and print "
    "process, explains the five places where quotes quietly differ from each other without the buyer "
    "noticing, and gives a negotiation sequence that protects margin without pushing the mill into "
    "a quality corner. Written for procurement managers and brand owners sourcing private-label ribbon."
)
KEYWORDS = (
    "ribbon OEM quotation breakdown, ribbon factory price per meter, woven ribbon cost structure, "
    "ribbon OEM cost transparency, how to negotiate ribbon factory price, ribbon yarn weaving finishing cost, "
    "printed ribbon tooling cost, ribbon MOQ pricing tiers, private label ribbon quotation comparison, "
    "B2B ribbon procurement, ribbon cost per yard explained, satin ribbon wholesale price guide 2026"
)

SECTIONS = [
    (
        "Why Two Quotes for the Same Ribbon Differ by 30%",
        """Two suppliers quote the same specification &mdash; 15mm grosgrain, 100% polyester, matte, single-colour, 5,000 metres &mdash; and one comes back at $0.11 per metre and the other at $0.145. Both are quoted as FOB Xiamen. Both claim a 10,000 metre minimum. Neither is lying, and the buyer who treats the $0.035 gap as a bargaining opportunity rather than as information usually ends up with the more expensive supplier and the worse result.

The gap is not margin. It is definition. A mill price is not a number; it is a number attached to a set of assumptions about material, construction, tolerance, packaging, testing, and what happens when something goes wrong. The first job of a procurement manager is not to negotiate the number. It is to make the two quotes comparable so that the number means the same thing on both sides. Once the assumptions are written down, most of the apparent gap either closes or becomes an obvious, defensible reason to prefer one supplier over the other.

This guide walks through the cost lines that make up a ribbon quote, what each one should plausibly look like for a given specification, where quotes most often differ in ways that are invisible until goods arrive, and how to run a negotiation that does not damage the relationship or the quality of the output. It is written from the mill side of the industry: Xiamen Smith Ribbon &amp; Bow has been weaving and finishing ribbons since 2004, supplying brands, retailers and packaging converters in more than fifty countries.""",
    ),
    (
        "Line 1&ndash;3: Yarn, Dyeing and the Material Substitution You Were Never Told About",
        """The first three lines are the material, and material is usually 35&ndash;50% of a finished ribbon's mill cost. This is also where quotes diverge most deceptively, because the substitution is invisible in the paperwork.

<b>Yarn cost.</b> Polyester yarn is priced by denier and by the raw polymer market. A mill buying yarn at a different week gets a different price, and that volatility passes straight through. When a buyer asks two mills for a quote in the same week and gets different numbers, the honest explanation is often just that one mill contracted yarn in June and the other in September. A good quote should state the yarn denier, the supplier or grade, and whether the price is locked or index-linked. If it does not, ask. A mill that cannot tell you what yarn it is quoting is telling you something.

<b>Dyeing.</b> This is where a lot of the real cost sits. Piece dyeing on a ribbon line means the mill runs the fabric through dye, fixes the colour, rinses, dries, and then has to wash off the surface excess to hit a crocking specification. The cost of that sequence scales with the number of colour changeovers on the order and with the depth of the shade. A deep, saturated navy costs meaningfully more to hit reliably than a pale pastel. Deep, dark, high-saturation shades also carry higher reject rates, and mills price that risk in. When comparing quotes, confirm that both mills are dyeing to the same depth and the same crocking target, and check whether the quoted price assumes a full-width dye or a piece dye at finished width.

<b>The substitution.</b> Here is the one that catches experienced buyers. A mill quoted for a 65% polyester / 35% cotton ribbon and a mill quoted for 100% polyester ribbon may both arrive at the same per-metre price, because the fibre blend is set by what the mill has on the shelf that week. A 100/35 poly-cotton ribbon is a different product from a 100% polyester ribbon: it feels different, it takes dye differently, it shrinks differently, and it costs a different amount. Under a brand's private label, that difference shows up in your wash test results and your customer complaints, not in the invoice.

The practical defence is to require the fibre content to be stated on the quotation line, and to require the mill to confirm it against the incoming goods. A mill that cannot verify yarn composition on the goods receipt note is a mill that is not controlling its own inputs.

At Smith Ribbon, since 2004, we have quoted and documented yarn denier, fibre composition and dyeing route on every quotation we issue, because the buyers who stay in business for a decade are the ones who build their costing on facts rather than on a per-metre number.""",
    ),
    (
        "Lines 4&ndash;6: Weaving, Finishing and Sizing &mdash; Where Construction Choices Drive Cost More Than Volume Does",
        """If material is the first half of the cost, construction is the second, and it is the half that gets underestimated in early-season costing.

<b>Weaving and selvedge.</b> Woven ribbon is made on a loom, and loom productivity is not linear in width. A 6mm ribbon woven on a wide loom with many ends across takes a disproportionate amount of loom time relative to its sale price, because the setup and thread-count cost is spread over very few centimetres of product. A 38mm ribbon on the same loom uses that time to make far more saleable metres. This is the single biggest reason narrow trims cost more per metre than wide ones, and why a quote for a narrow decorative trim at a small volume should not be compared against a quote for a wide spool ribbon at a large volume. If the width on your programme has shifted, the price should shift with it.

<b>Finishing.</b> Finishing is what makes a woven ribbon feel like a ribbon rather than like fabric: heat-setting for width and curl stability, calendaring or brushing for surface, edge treatment for a clean cut, and the mechanical properties that come with them. Metallic yarn, wired edge, elastic recovery, and velvet pile are not finishes applied to a standard ribbon; each one is a different construction with a different cost base. Where a quote says "velvet" at the same price as "satin", ask what the pile base is, how it is cut and finished, and what the wear behaviour is after a wash.

<b>Sizing and slit width.</b> A 16mm ribbon is usually slit from a wider web. The web is made once and slit into several widths, which sounds like it should make the narrow width cheaper. It does not, because the slit edges are not selvedge edges, and the customer accepts a different edge quality. Where the edge quality matters &mdash; and it always does on a visible gift-bow edge &mdash; a selvedge construction costs more and behaves better. Say which one you need.

<b>Quality tolerance.</b> Ask what the mill will guarantee and at what tolerance. Width tolerance expressed as a percentage is common; expressed in absolute millimetres, it is better. Crocking, fastness to wash, light fastness, and the behaviour under tension each have a stated method. A quote that says "good quality" and a quote that says "crocking grade 4 per ISO 105-N02, wash fastness grade 4 per ISO 105-C06" are not comparable, and the second one is the one you can hold someone to.

Our own production standards at Smith Ribbon &mdash; OEKO-TEX, FSC, BSCI, SEDEX, ISO 9001 and SMETA &mdash; exist because the buyers who place repeat orders are the ones who need the mill's test reports to mean something specific on a Tuesday afternoon, not a vague assurance that quality is fine.""",
    ),
    (
        "Lines 7&ndash;9: Printing, Tooling and the Cost of Getting the Design Right",
        """Printing is where customisation most obviously changes the price, and where the largest avoidable costs live.

<b>The print process.</b> Woven ribbon printing is one of four things: screen printing, heat-transfer (also called digital or sublimation transfer), woven-in jacquard, or foil/emboss. Screen printing is cheapest per metre and cheapest on tooling, but it has a per-colour setup and a practical limit on how many colours and how much coverage it can hold. Heat transfer gives unlimited colours and photographic reproduction at a higher per-metre cost and a minimum order that is much higher. Jacquard is not printing at all; the design is in the weave, so it costs more in setup and in loom time but has no ink and no registration problem. Foil is a finish on top, applied to a printed or plain base.

A quotation that says "printed" without naming the process is not a quotation. Ask for the process, the number of colours, the coverage, and the repeat length. A repeat length is the distance over which the design tiles &mdash; a 10cm repeat on a 38mm ribbon means the design repeats about four times per metre of tape and every repeat has to be registered.

<b>Tooling and setup.</b> Screen printing carries a physical charge per screen. A six-colour design means six screens. Designs are reworked far more often than buyers expect, and every rework is a new set of screens. The correct commercial arrangement is to have the mill own the screens or plates and quote them as a reusable asset, then amortise that cost across the programme rather than charging it on every reorder &mdash; but only once the design has been signed off. Some mills will quote the tooling free and recover it in the unit price; others will charge it outright. Both are legitimate. What matters is knowing which one you are in, because a design that gets reworked after the screens are cut is a real and recurring cost that is easy to lose.

<b>Artwork readiness.</b> The most expensive version of a printing quote is the one where the artwork was not ready when the price was calculated. A design that arrives as a low-resolution image, in the wrong colour space, or with effects the mill cannot reproduce will either raise the price at the last moment or, worse, will be printed approximately. At Smith Ribbon, artwork is checked against a print-readiness standard before a price is confirmed, and the specification that follows &mdash; resolution, colour space, repeat length, and the acceptance criteria for the printed result &mdash; is written into the job folder. This is one of the cheapest cost controls available to a brand owner: most artwork problems are free to fix before the screens are cut and expensive afterwards.

<b>Sample cost.</b> Lab dips, pre-production samples and sealed samples are usually quoted as separate line items with separate charges. They should be. A buyer who asks for all three on every order and then reuses them will eventually approve goods that were never actually produced to the standard they assumed. The correct discipline is: a pre-production sample is approved against the specification, and a production sample is approved against the pre-production sample.""",
    ),
    (
        "Lines 10&ndash;14: Overhead, Margin, Packing, Freight and the Part That Never Appears on the Invoice",
        """The remaining lines are where a buyer loses the most money, because they are the lines most often treated as fixed or invisible.

<b>Conversion overhead.</b> Warping, sizing, setting, threading, and the machine time that is not the weaving itself. This is the mill's fixed cost recovery. It behaves in a familiar way: per-metre overhead falls as volume rises, which is why quantity breaks matter. But it also means that a small quantity carries a disproportionately high overhead load, and a mill quoting aggressively on small quantities is usually accepting a lower margin to get the slot. Ask what the quantity break actually is, and get it in writing.

<b>Margin.</b> A healthy, sustainable ribbon mill at volume earns a margin that lets it survive a bad year, fund a machine upgrade, and still quote competitively. An extraordinarily thin margin on a quote is a warning sign, not a bargain. It usually means the quote is built on assumptions that will not hold &mdash; cheaper yarn, less finishing time, a lighter QC regime &mdash; and the difference surfaces at the invoice or, worse, at the inspection.

<b>Packing.</b> How the ribbon is packaged has a real cost and a real effect on what arrives. Spools of a specified length, reels, flat-folded ribbon with a header card and a polybag, or bulk rolls. Flat-fold with a printed header card is more expensive per metre and is what a private-label retail programme needs; a bulk roll is cheaper and is what a converter needs. This is a frequent source of "identical" quotes differing materially, and it is a line buyers should specify rather than accept.

<b>Freight and insurance.</b> 5,000 metres of 15mm ribbon is not a large shipment, and the fixed cost per shipment is spread over a small volume. Air freight is fast and expensive; sea freight is economic above a volume threshold and takes three to four weeks door to door from Xiamen. Consolidation, which means shipping with other customers' goods in a shared container, reduces cost and adds unpacking and repacking at the destination.

<b>Duty and the landed cost beyond the mill price.</b> This is the part that never appears on the invoice and frequently decides whether the programme works. Classification, the duty rate that applies to that classification in your destination market, and the fact that a "same product" can be classified differently depending on material content and construction. A 100% polyester ribbon and a poly-cotton ribbon can attract different duty treatment. The importer's broker will tell you, but ask the mill for the technical data &mdash; fibre composition, construction, and material description &mdash; early, because that is the documentation the broker will need.

<b>Working capital and the cost of the money.</b> A buyer who pays 30% deposit, 70% against bill of lading, has tied up cash for roughly 45 to 60 days from order to delivery. That is a real cost that never shows in a per-metre price, and in a programme where the mill's margin is 8% and the buyer's cost of capital is 12%, the financing gap can erase the apparent saving from the cheaper quote entirely.

<b>Defect and rework cost.</b> A rejected lot costs more than the rejected metres. It costs the material, the machine time, the freight, the re-order, the delay to the shelf, and the retailer's chargeback for late delivery. This is the strongest argument for paying attention to the inspection and test lines in the quote, and the weakest argument for choosing on unit price alone.""",
    ),
    (
        "How to Compare Two Quotes Properly: A Five-Step Sequence",
        """The single most useful thing a procurement manager can do is refuse to compare two quotes until they are written on the same basis. This sequence takes about an hour per quote and removes most of the false differences.

<b>Step one &mdash; Make the specification identical.</b> One document, one version, both mills confirm receipt. Width, material and composition, construction (selvedge or slit), finish, print process, number of colours, repeat length, edge treatment, and any wire or elastic. If these are not identical, you are not comparing quotes, you are comparing two different products.

<b>Step two &mdash; Get the physical terms in writing.</b> Quantity per colour, total quantity, quantity breaks and what triggers them, minimum order per design, minimum order per colour, the tolerance on width, and the test standard for each performance property. Write the quantity break table directly into the quotation.

<b>Step three &mdash; Ask for the cost structure, not just the number.</b> Not the mill's internal costing, but the line items: material, conversion, finishing, printing and setup, tooling treatment, QC and testing, packing, and margin as a separate line. A factory that will break a quote down for you is a factory that is confident in its numbers, and you have somewhere to negotiate when a line moves.

<b>Step four &mdash; Separate the FOB price from the landed price.</b> Freight, duty, and insurance computed on the same basis for both mills, including the broker's estimate. Then add the working capital cost for the payment terms each mill offers. Two quotes that look four cents apart on FOB can be close to identical on a landed basis, and two that look close on FOB can differ materially once freight allocation and duty are applied.

<b>Step five &mdash; Test the price against the market.</b> Benchmark at least one finished, delivered, compliant price from a different supplier, so you know whether the number you are arguing about is in the right range or simply reflecting a specification difference you have not accounted for.

Then, and only then, negotiate. The sequence matters: negotiating before step five is a negotiation against an unknown, and it teaches the mill that you will argue about price without a basis. That is how quality gets quietly traded away.""",
    ),
    (
        "Negotiating Without Damaging the Mill or the Work",
        """There is a productive way to negotiate a ribbon price and a destructive way, and the difference shows up in the goods six months later.

<b>What works.</b> Negotiate the high-volume break explicitly: ask what quantity unlocks the next price, and commit to it in writing. Negotiate the amortisation of setup and tooling across a programme rather than per order. Negotiate the terms that have a real cost to the mill &mdash; payment terms, delivery window, forecast visibility, minimum reorder &mdash; and understand what they are worth, because they are often worth more to the mill than a price concession and cost you almost nothing. Negotiate the specification, not just the number: a slightly narrower width, a two-colour design instead of six, a standard size instead of a custom size, a standard finish instead of a special one. These changes are worth real money and cost the programme very little.

<b>What does not work.</b> Pushing a mill's margin below what lets it run a competent quality function, because you will not see the consequence until the goods fail. Accepting a quote that is only viable if the specification is quietly reduced. Using the threat of a future order to extract a discount on an order that has already been placed. And the pattern that damages a relationship fastest: arguing hard on price, then asking for an extra favour on the next order &mdash; a rush, a colour change, a shorter payment term &mdash; as though the price fight and the favour request are separate conversations. They are not.

<b>The question that usually settles the argument.</b> When a buyer and a mill disagree about price, ask what specifically would need to change in the job for the number to change, and by how much. This converts a positional argument about whether $0.13 is fair into an engineering conversation about what the job actually involves. It is remarkable how often the price question resolves once both sides are describing the same physical job.

<b>What we offer at Smith Ribbon.</b> Since 2004 we have worked on the basis that a buyer who can see the structure of a price will come back when the market improves, and a buyer who cannot will keep shopping on a spreadsheet. Our quotations itemise material, conversion, finishing, printing setup, QC, packing and freight separately, we quote quantity breaks with the trigger conditions stated, and our factory is open to buyers who want to visit. We have a 15,000 square metre plant, more than 200 staff, daily output of 100,000 metres, and we supply brands, retailers and converters in more than fifty countries with OEKO-TEX, FSC, BSCI, SEDEX, ISO 9001 and SMETA certification.""",
    ),
    (
        "The Cost Risks That Are Not in the Quotation at All",
        """Four costs sit entirely outside the mill's quotation, and they are the ones that turn a good-looking price into a bad programme.

<b>Rework from an unclear specification.</b> The single largest hidden cost in a custom ribbon programme is a specification that was ambiguous when it was approved and was resolved by the mill's interpretation. A width tolerance of "&plusmn;0.5mm" and a tolerance of "1mm" are both colloquial and both enforceable in a dispute. Acceptance criteria belong in the job folder, in writing, before production.

<b>The cost of a late colour change.</b> Once a dye lot is running, changing the colour means a new dye lot. This is why an early and correct colour approval is worth more than it looks, and why mill-side spectrophotometric measurement against an approved physical standard &mdash; not a screen, not a photograph &mdash; is the only process that reliably prevents it.

<b>The cost of a failed wash or performance test.</b> If the ribbon fails crocking, colour fastness, or abrasion after it has shipped and been decorated into finished goods, the loss is the ribbon, the decoration labour, the packaging, and the shelf space you cannot get back. Ask the mill what test evidence travels with the shipment.

<b>The cost of a supplier who cannot be audited.</b> When something goes wrong, the question that matters is whether anyone can look at the mill. Credentials that can be verified &mdash; against the issuing body, with a current scope and expiry date &mdash; are worth real risk reduction. Credentials that are a logo on a PDF are not. Smith Ribbon holds OEKO-TEX, FSC, BSCI, SEDEX, ISO 9001 and SMETA; each certificate has a scope, a certificate number and an expiry date, and we will give you the certificate number so you can verify it independently with the issuing body rather than taking our word for it.

<b>The cost of not having a second source.</b> Not immediately, and not expensively, but a documented second source for the highest-volume SKUs is what allows you to hold a price honest. Buyers who have never tested an alternative learn nothing about where their price actually sits, and they cannot tell a supplier that a change is necessary without bluffing.""",
    ),
]

FAQ = [
    (
        "What is a realistic price per metre for custom woven ribbon?",
        "For a mainstream polyester grosgrain or satin in a standard width at a mid-volume tier, a 2026 FOB Xiamen range for a plain or single-colour ribbon is broadly in the region of $0.09 to $0.16 per metre. Custom widths, woven jacquard, velvet, wired edge, elastic, metallic yarn and multi-colour printing all sit above that, and narrow trims below 15mm sit above it too because of the loom-time issue described in this guide. Treat any figure outside that band as a signal that the specification is not like-for-like, not as an opportunity. The only honest way to know a price is to put an identical specification in front of three mills and read the line items.",
    ),
    (
        "How do I get a mill to show me the cost breakdown behind the unit price?",
        "Ask for it directly and in writing before you negotiate anything: request the quote be itemised into material, conversion and weaving, finishing, printing setup and per-metre printing, QC and testing, packing, freight basis, and margin as a separate line. In our experience the reason a mill sometimes presents a single number is that the buyer's communication has been single-number. Specify the format you want in the request, list the lines you want, and give a deadline. Factories that have worked with sophisticated buyers for years will produce this as a matter of course because their buyers ask for it every time.",
    ),
    (
        "What should a quantity break look like on a ribbon quotation?",
        "A quantity break table should state the metric that triggers the tier and what changes when it is crossed: total metres, metres per colour, metres per design, or number of designs. The most common version has tiers at 1,000 / 5,000 / 10,000 / 30,000 metres with the price reducing at each step, and a separate minimum per colour and per design because a mill that weaves 10,000 metres across six colours is running six dye lots, not one. If the break table is not written into the quotation, the tier is not a commitment and you should treat it as an indication rather than a price.",
    ),
    (
        "Is it acceptable to negotiate hard on price with a ribbon factory?",
        "Yes, and most factories expect it. What damages the relationship is not the negotiation but negotiating without a basis and then treating the relationship as a source of free extras. The productive approach is to establish an identical specification, break the quote down, benchmark it, and then negotiate the things that genuinely have a cost to the mill: volume commitment, payment terms, delivery window, forecast visibility, tooling amortisation, and specification simplification. The approach that causes quality problems is pushing a margin down until the mill cannot fund a competent quality function, and then accepting the consequences six months later.",
    ),
    (
        "How do I avoid paying twice for setup and tooling on reorders?",
        "Decide who owns the asset and write it down. The two normal arrangements are that the mill creates and owns the screens or plates, quotes a one-time charge, and amortises it across the programme volume, with the screens retained for reorders; or that the buyer owns the physical tooling and the mill has rights to use it for your orders only. What causes a duplicate charge is ambiguity, and what causes a design that can never be reproduced is a mill that disposes of the tooling without your knowledge. Confirm in writing: who holds the tooling, how long it is retained, what the re-setup charge is if it is lost, and what happens to it if the programme ends.",
    ),
    (
        "How should I handle duty, freight and working capital so that I am comparing landed cost rather than mill cost?",
        "Build a landed cost sheet for each quote on the same basis: FOB value, freight and insurance by mode, estimated duty at the rate that applies to the product's actual classification in your destination market, customs and broker fees, and then the cost of carrying the money for the payment terms on offer. For a 5,000 metre order the fixed freight cost per metre is high, which sometimes makes an air-freighted small order cheaper in total than a sea-freighted one. Ask the mill for the fibre composition and construction description early, because that is what your broker needs to classify the goods, and classification differences between two mills' identical-looking product can be the largest single line in your landed cost comparison.",
    ),
    (
        "What should I check before signing a supply agreement with a ribbon factory?",
        "Five things. First, that the entity you are contracting with is the factory that will make the goods &mdash; verify the business licence and the address against the mill you visited. Second, the quality regime in writing: which tests are performed on which lots, at what tolerance, with what evidence on the shipment. Third, the capacity commitment, including what the mill commits to for your peak season specifically. Fourth, the remedy structure: what happens on a failed lot, on a late delivery, and on a specification dispute, and how claims are evidenced. Fifth, the credentials, verified independently against the issuing body with a current scope and expiry date rather than accepted on a PDF. Smith Ribbon &mdash; manufacturing in Xiamen since 2004 &mdash; will send certificate numbers for exactly this reason.",
    ),
]

METRICS = [
    ("Cost lines to decode", "14"),
    ("Comparison steps before negotiating", "5"),
    ("Cost lines that never appear on the invoice", "5"),
    ("Certificates verifiable against the issuing body", "6 (OEKO-TEX, FSC, BSCI, SEDEX, ISO 9001, SMETA)"),
    ("Years of ribbon manufacturing experience", "22 (since 2004)"),
]

AUTHOR_BULLETS = [
    "Factory-direct pricing from our own 15,000 m&sup2; plant in Xiamen &mdash; no trading-company margin in the quote",
    "Itemised quotations with quantity breaks and their trigger conditions stated in writing",
    "20+ years producing ribbons, bows, trims and decorative packaging accessories for brands and retailers in 50+ countries",
    "OEKO-TEX, FSC, BSCI, SEDEX, ISO 9001 and SMETA &mdash; certificate numbers supplied so you can verify them independently",
]

CLOSING_PARAGRAPH = (
    "The price is the last conversation in a ribbon sourcing process, not the first. Buyers who treat the quotation "
    "as a single number either chase a saving that is not there, or accept a specification that is not what they "
    "thought. Buyers who treat the quotation as a structured document &mdash; material, construction, process, "
    "tolerance, testing, packing, and the terms around it &mdash; end up with a supplier relationship that is easier "
    "to manage and a landed cost they can actually predict. That is the whole argument, and it has been our position "
    "since we started weaving ribbon in Xiamen in 2004."
)
CLOSING_CTA = (
    "If you are pricing a custom ribbon programme and want an itemised quotation against your own specification, "
    "send us the width, material, construction, finish, print process and volume, and we will return the quote with "
    "the cost lines separated so you can see exactly what you are buying. Email xmmsd@126.com, or reach us on "
    "WhatsApp and phone at +86 137 7995 1780 &mdash; we answer messages within 24 hours, and sample requests are "
    "welcome whether or not the order follows."
)

cfg = {
    "url": URL,
    "title": TITLE,
    "desc": DESC,
    "keywords": KEYWORDS,
    "date_iso": DATE_ISO,
    "date_display": DATE_DISPLAY,
    "num": 308,
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
    "h2_title": "Working With Smith Ribbon &mdash; A Factory That Shows Its Work",
}

html = build_html(cfg)
with open(f"/workspace/ribbonbow123/blog-{SLUG}.html", "w", encoding="utf-8") as f:
    f.write(html)
print(f"Wrote blog-{SLUG}.html ({len(html):,} bytes)")
