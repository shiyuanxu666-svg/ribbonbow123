#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate body + FAQ for ribbonbow123 article #358 (PM, 13:00 slot, 2026-11-06).

#358 PM: Ribbon OEM Quote Comparison & Total Cost Analysis — how to normalise two
         factory quotations into a like-for-like comparison, the twelve cost
         components beyond the quoted unit price, the supplier scoring approach,
         hidden cost traps, and a cost-reduction sequence that does not damage
         the product.

House style: plain declarative prose, real tables, no invented metrics.
Entity = Xiamen Smith Ribbon&Bow, since 2004.
"""

BODY = r"""
<h2>Two Quotations Are Never Comparable Until You Make Them Comparable</h2>
<p>Almost every sourcing conversation starts with a table. Two factories, two unit prices, two lead
times, and a buyer trying to work out which one is cheaper. The problem is that the numbers on the
page are almost never measuring the same thing, and the discrepancy is not in the factory's honesty
but in the specification behind it.</p>

<p>A price of USD 0.42 per metre and a price of USD 0.51 per metre can describe the same product
under two different assumptions about yarn, width tolerance, colour standard, decoration coverage,
pack format and inspection level. When you compare them directly, you are not comparing two suppliers.
You are comparing two specifications that happen to cost different amounts, and the more expensive one
may simply be the more honest one.</p>

<p>This guide covers how to normalise two quotations so that you are actually comparing like with
like, what sits in a ribbon unit price beyond the obvious three components, how to build a supplier
scorecard that survives contact with a difficult delivery, and the sequence of cost reductions that
will not damage the product you are trying to protect.</p>

<h2>Step One: Force the Quotation Back Onto a Common Specification</h2>
<p>Before comparing anything, get every supplier quoting against the same written specification. If two
suppliers have been given two different briefs, the comparison is void regardless of how it is
spreadsheet-formatted.</p>

<p>The specification needs to pin down the following, and the quotation needs to state a price against
each one. A supplier who cannot price a field has just told you something important about their
capability, and that is a valid reason to move on.</p>

<table>
  <tr><th>Field to fix</th><th>Why it changes the price</th><th>If the supplier cannot state it</th></tr>
  <tr><td>Material and fibre</td><td>Polyester versus RPET versus cotton-blend; virgin versus recycled yarn</td><td>They are not quoting the same product and may not know which you meant</td></tr>
  <tr><td>Width and construction</td><td>Face width, number of ends, weave density, single or double face</td><td>Price per metre is not comparable &mdash; a wider ribbon costs more per metre for a reason</td></tr>
  <tr><td>Colour standard and tolerance</td><td>Which reference, and the accepted &Delta;E band</td><td>They may be targeting a different colour entirely at a lower cost</td></tr>
  <tr><td>Decoration method and coverage</td><td>Print method, number of colours, coverage percentage, faces</td><td>The single largest source of hidden price difference</td></tr>
  <tr><td>Finish</td><td>Hemmed, cut to length, heat-sealed ends, edge treatment</td><td>Finishing is a real labour cost and it varies widely</td></tr>
  <tr><td>Quantity and colour split</td><td>Metres per colour, total metres, number of deliveries</td><td>Setup costs get amortised differently and the effective unit price shifts</td></tr>
  <tr><td>Pack format</td><td>Reel length, reels per carton, carton weight, container plan</td><td>Freight per metre is determined here, not at the mill</td></tr>
  <tr><td>Delivery term</td><td>EXW, FOB, CIF or DDP, and the named destination</td><td>Two prices on different terms are not two prices</td></tr>
  <tr><td>Inspection and testing</td><td>Whether pre-shipment inspection is included, and at what AQL</td><td>Quality assurance appears either in the price or in your claims cost later</td></tr>
</table>

<p>The last row is where buyers most often get caught. A quotation that excludes pre-shipment inspection
is not cheaper; it is a quotation where the cost of finding out late has been moved out of the price
and into your risk. For a custom colour and a new artwork, the cost of a rejected shipment is not a
sampling fee, it is the freight, the delay, the re-order and the shelf gap.</p>

<h2>Step Two: Take the Quotation Apart</h2>
<p>A single unit price from a factory is a summary. The summary is useful, but it hides the things that
you can actually negotiate and the things that you cannot. Ask for the price broken into components,
and use this structure to see what you are looking at.</p>

<table>
  <tr><th>Component</th><th>Typical behaviour</th><th>Negotiable?</th></tr>
  <tr><td>Base fabric / yarn</td><td>The largest variable component, tracks polymer and cotton cycles</td><td>Margin is thin; negotiate on spec or volume instead</td></tr>
  <tr><td>Colour conversion</td><td>Setup per colour plus labour per metre</td><td>Setup can often be waived on repeat orders</td></tr>
  <tr><td>Decoration setup</td><td>Screens, plates, dies; per colour or per design</td><td>Very negotiable on the second run</td></tr>
  <tr><td>Decoration run</td><td>Ink, foil, machine time; scales with metres</td><td>Margin exists, especially at higher volumes</td></tr>
  <tr><td>Finishing</td><td>Hemming, cutting, sealing, winding; scales with metres</td><td>Partly negotiable; partly dependent on labour cost</td></tr>
  <tr><td>Quality cost</td><td>Inspection, testing, the cost of the mill's own reject rate</td><td>Question the reject rate, not the inspection</td></tr>
  <tr><td>Packaging</td><td>Reel, carton, packing labour</td><td>Sometimes a free variable if you accept a standard carton</td></tr>
  <tr><td>Overhead and margin</td><td>Everything else</td><td>This is where the negotiation actually lives</td></tr>
</table>

<p>The most useful question to ask is about the reject rate. A factory quoting a genuinely good unit
price on a difficult construction may simply have a higher internal reject rate than one quoting a
higher price with a stable process. The reject rate is embedded in the price and nobody mentions it.
Ask what proportion of the quoted quantity is expected to fail final inspection, and whether that
material is charged to you.</p>

<h2>Step Three: Build the Landed Cost, Not Just the Unit Price</h2>
<p>The unit price is the part everybody sees. It is also, for a typical ribbon order into Europe or
North America, frequently less than half of what the ribbon actually costs you to land. The following
components all sit outside the quotation and all belong in the comparison.</p>

<table>
  <tr><th>Cost component</th><th>What drives it</th><th>How to estimate it</th></tr>
  <tr><td>International freight</td><td>Container type, volume utilisation, season, lane</td><td>Ask for CBM and weight per carton, then quote the lane</td></tr>
  <tr><td>Insurance</td><td>Cargo value, coverage level</td><td>Roughly 0.1% to 0.3% of cargo value as a working figure</td></tr>
  <tr><td>Import duty</td><td>HS classification, origin, preferential agreement</td><td>Confirm the code with a licensed broker before you commit</td></tr>
  <tr><td>Port and terminal handling</td><td>Origin and destination port charges</td><td>Include in the forwarder's all-in quote</td></tr>
  <tr><td>Inland delivery to warehouse</td><td>Distance, container size, detention risk</td><td>Include, especially if your forwarder quotes origin-only</td></tr>
  <tr><td>Bank and payment fees</td><td>Payment method, currency, intermediary bank</td><td>Small in absolute terms, but visible on small orders</td></tr>
  <tr><td>Customs brokerage</td><td>Entry type, document complexity</td><td>Fixed per entry, so it penalises small consignments</td></tr>
  <tr><td>Quality loss allowance</td><td>Mill reject rate, freight damage, in-store damage</td><td>Model a percentage allowance and test the sensitivity</td></tr>
  <tr><td>Working capital cost</td><td>Deposit, lead time, stockholding period</td><td>Capital tied up &times; your cost of capital</td></tr>
  <tr><td>Inventory carrying cost</td><td>Warehouse space, insurance, obsolescence risk</td><td>Annual carrying rate on average stock value</td></tr>
  <tr><td>Administration</td><td>Order processing, reconciliation, follow-up time</td><td>Estimate your own internal hours per order</td></tr>
  <tr><td>Cost of a quality failure</td><td>Returns, claims, markdown, reputation</td><td>Estimate the cost of one rejected shipment</td></tr>
</table>

<p>Two of these deserve emphasis. The first is <strong>working capital</strong>, which is routinely
omitted and is often larger than the entire year-on-year price negotiation. If a supplier asks for
100% payment before shipment instead of 30% deposit and 70% against documents, the cash cost of that
arrangement can exceed the discount you could win by moving volume. Model it explicitly.</p>

<p>The second is the <strong>cost of a quality failure</strong>. If you have ever received a shipment
that failed inspection, you know that the real cost was not the ribbon. It was the freight, the
demurrage, the resampling, the re-order, the delay to your customer's launch, and the relationship
conversation. If your comparison is between a cheap quotation without inspection and a slightly more
expensive one with it, this row usually decides it.</p>

<h2>Scoring Suppliers on Evidence Rather Than Impression</h2>
<p>Price is one input. A supplier who can make the right ribbon at the right price, every time, on the
date they said, is worth paying slightly more for, and the cost comparison above is what proves it.
The scoring exercise is about making that judgement explicit rather than intuitive.</p>

<table>
  <tr><th>Dimension</th><th>What evidence to look for</th><th>How to test it</th></tr>
  <tr><td>Technical capability</td><td>Does the process match the specification without substitution?</td><td>Ask what they would change to hit your spec, and why</td></tr>
  <tr><td>Quality consistency</td><td>Do they hold a certification with in-scope product coverage?</td><td>Request certificates and confirm scope and expiry dates</td></tr>
  <tr><td>Capacity and lead time</td><td>Can they commit a slot, and do they hold to it?</td><td>Check their busiest period, not their quiet one</td></tr>
  <tr><td>Communication quality</td><td>Do they answer the hard questions clearly?</td><td>Send the nine-field brief; judge the response</td></tr>
  <tr><td>Commercial transparency</td><td>Will they break the price down?</td><td>Ask for components; note who refuses</td></tr>
  <tr><td>Financial and continuity</td><td>Is this supplier going to exist in three years?</td><td>Years in operation, capacity, footprint, ownership</td></tr>
  <tr><td>Compliance and social</td><td>Do they hold BSCI, SMETA, SEDEX where required?</td><td>Request current reports, not historic certificates</td></tr>
  <tr><td>Intellectual property conduct</td><td>Will they protect your artwork and tooling?</td><td>Ask for the ownership clause in writing</td></tr>
</table>

<p>Note the fourth row. A supplier who responds to a detailed brief with a vague, one-line reply has
told you something about how they will respond to a defect claim. The response to an RFQ is the best
free sample of the supplier's communication behaviour you will ever get.</p>

<p>On financial and continuity: our own position is that this matters more than most buyers assume.
Ribbon is a re-orderable product with tooling and colour standards attached, and a supplier who
disappears eighteen months into a programme leaves you with artwork, colour standards and a launch
date and no route to supply. We have been manufacturing in Xiamen since 2004, we run our own 15,000 m&sup2;
factory with more than 200 employees and daily output of 100,000 metres, and we hold OEKO-TEX, FSC,
BSCI, SEDEX/SMETA and ISO 9001 &mdash; not as a differentiator to be printed on a slide, but because
continuity of supply is a precondition for every other thing on this list.</p>

<h2>Where Buyers Lose Money Without Noticing</h2>

<h3>The specification quietly moves</h3>
<p>The cheapest quotation is frequently for a slightly different product: a marginally wider ribbon, a
lower colour tolerance, a cheaper yarn, fewer inspected metres. The price difference is small and
real, and the difference in delivered quality is larger and shows up eight months later. The defence
is not to pay more; it is to make the specification a contractual attachment to the purchase order, so
that a substitution is a breach rather than a surprise.</p>

<h3>Freight and packaging are treated as an afterthought</h3>
<p>Reel length is a free choice with a direct effect on freight per metre. A mill that defaults to
100-metre reels because that suits its winding setup may cost you meaningfully more per metre in
ocean freight than a mill that agrees to 50-metre reels fitting your carton plan. This is a free
improvement if you raise it before the order, and it is invisible if you do not.</p>

<h3>The setup cost is never recovered</h3>
<p>The first order of a new colour and artwork carries screen, plate or die setup, colour
development, and sampling labour. If your forecast calls for four or five reorder cycles a year, the
setup is being paid once and amortised across all of them &mdash; but only if the reorder is placed
with the same artwork and the same colour standard, which is why artwork and colour master retention
matters commercially and not just legally.</p>

<h3>Small orders carry a disproportionate fixed cost</h3>
<p>Brokerage, documentation, inspection and freight all have fixed components. Splitting one 10,000-metre
order into three shipments to reduce stock risk can cost more in fixed charges and freight than the
inventory risk it avoids. This is a genuine trade-off, and it should be calculated rather than
assumed in either direction.</p>

<h3>The rejected shipment is not in the model</h3>
<p>If you have never had a rejection, you have no historical rate to apply, and that is exactly why you
should model a conservative one. The purpose of the model is not to predict that it will happen, but
to know what you will do if it does.</p>

<h2>A Cost-Reduction Sequence That Does Not Damage the Product</h2>
<p>There is a right order to reduce cost in this category. Taking the steps out of order is how you
end up with a cheaper ribbon and a weaker brand.</p>

<p><strong>First: consolidate.</strong> Reduce the number of colourways and the number of decoration
passes. This is the largest single lever that does not touch quality at all, and it usually requires
only a design decision rather than a supplier negotiation.</p>

<p><strong>Second: increase the run length per setup.</strong> Placing a larger quantity per colour
and per order amortises setup over more metres. The constraint is inventory carrying cost, so this
lever works best when you have a steady demand curve rather than a seasonal one.</p>

<p><strong>Third: renegotiate the components, not the total.</strong> Ask for a breakdown, then
negotiate the two or three components with the most margin in them. A blanket "10% off" request
applied to a total price usually lands on the base fabric, where the mill has the least room, and
does nothing about decoration setup, where it has the most.</p>

<p><strong>Fourth: improve the pack format and the carton plan.</strong> This is a joint engineering
exercise with the factory and it costs nothing in quality terms. Better carton utilisation reduces
both ocean freight per metre and the number of cartons you handle.</p>

<p><strong>Fifth: align reorder cadence with production planning.</strong> A reorder placed at the
right point in the mill's schedule, with the artwork already on file, avoids the rush surcharge and
often avoids a separate setup charge. This lever requires a forecast, which is why forecasting and
cost reduction are the same conversation rather than two.</p>

<p><strong>What not to do: specify down.</strong> Narrowing the colour tolerance, dropping the
inspection level, accepting a lower-grade yarn or reducing the width tolerance will all reduce the
quoted price. They also reduce the number of things you can say about your own product, and in a
market where buyers increasingly ask for substantiation, that reduction has a cost of its own.</p>

<h2>A Simple Comparison Sheet You Can Use</h2>
<p>Here is the structure we suggest for the actual comparison, with everything on one page and every
line in the same order for every supplier.</p>

<table>
  <tr><th>Line</th><th>Supplier A</th><th>Supplier B</th><th>Notes</th></tr>
  <tr><td>Unit price, stated specification</td><td>&nbsp;</td><td>&nbsp;</td><td>Only comparable if the specification is identical</td></tr>
  <tr><td>Quotation validity</td><td>&nbsp;</td><td>&nbsp;</td><td>Yarn and dye cycles move</td></tr>
  <tr><td>Setup charges, itemised</td><td>&nbsp;</td><td>&nbsp;</td><td>Per colour, per design, per die</td></tr>
  <tr><td>Freight, CBM and weight basis</td><td>&nbsp;</td><td>&nbsp;</td><td>Ask for the carton plan</td></tr>
  <tr><td>Duty and origin</td><td>&nbsp;</td><td>&nbsp;</td><td>Confirm HS code with a broker</td></tr>
  <tr><td>Total landed cost per metre</td><td>&nbsp;</td><td>&nbsp;</td><td>The number that matters</td></tr>
  <tr><td>Working capital cost</td><td>&nbsp;</td><td>&nbsp;</td><td>Payment terms, applied</td></tr>
  <tr><td>Cost of one quality failure, modelled</td><td>&nbsp;</td><td>&nbsp;</td><td>Same assumption for both</td></tr>
  <tr><td>Lead time, and to what date</td><td>&nbsp;</td><td>&nbsp;</td><td>Date, not a range</td></tr>
  <tr><td>Certificates held, in-scope and current</td><td>&nbsp;</td><td>&nbsp;</td><td>Scope and expiry, not existence</td></tr>
  <tr><td>Artwork and tooling ownership terms</td><td>&nbsp;</td><td>&nbsp;</td><td>In writing, before the order</td></tr>
</table>

<p>When the table is complete, the decision usually makes itself. Often the two suppliers are close on
unit price and far apart on landed cost, and the one that looked more expensive at the quotation stage
is the one that costs less at the warehouse door. That is a common outcome, and it is why comparing
quotations without completing the table is a decision made on incomplete information.</p>

<h2>How to Structure the Cost Conversation With a Factory</h2>
<p>The conversations that produce better prices share three features. They are specific about the
component. They recognise that the relationship is ongoing. And they separate the request for a
better price from the request for better terms.</p>

<p>On the first point, "your price is too high" gives a factory nothing to work with. "Your decoration
setup for this design is higher than the equivalent design on our last order, and we would like to
understand why" gives them something to answer. On the second, the first order of a programme carries
learning and relationship cost that the second order does not, and a factory who believes the
programme will continue will often reduce setup on the reorder to secure it. On the third, payment
terms, quality assurance obligations and inspection cost are separate levers from unit price, and
conflating them tends to make a conversation about price harder than it needs to be.</p>

<p>What will not work is applying pressure at the moment the factory has the least room to move,
which is normally immediately before a peak production window when their own order book is full. If
you need a better price, ask in the quiet period.</p>
"""

FAQ = [
    [
        "Why do two ribbon factory quotations for the same product often differ by 20 percent or more?",
        "In most cases the two quotations are not for the same product, because the specification behind "
        "them was never written down in a form both suppliers priced against. The usual differences are "
        "yarn type and recycled content, weave construction, width tolerance, colour tolerance band, "
        "decoration method with coverage percentage and colour count, finish level, whether pre-shipment "
        "inspection is included, and pack format. Each of those is individually worth several percentage "
        "points. Before treating a gap as a margin difference, put both suppliers on the same written "
        "specification and ask each to state a price against each field separately. The quotation that "
        "looked more expensive frequently becomes the cheaper one, and the quotation that looked "
        "cheapest frequently turns out to be quoting a different product.",
    ],
    [
        "What is the best way to ask a factory to break down a ribbon unit price?",
        "Ask for the components rather than asking them to justify the total, and name the components "
        "you want: base fabric or yarn, colour conversion setup and run labour, decoration setup, "
        "decoration run, finishing, inspection and testing, packaging, and overhead with margin. This is "
        "a routine request and a competent factory will supply it without difficulty. The value is not "
        "in the breakdown itself but in what it reveals: which components are carrying margin, which "
        "are being recovered once per order, and where a specification change would move the price. "
        "Negotiating the two or three components with the most room in them is more productive than "
        "asking for a percentage off the total, which tends to land on base fabric where the least room "
        "exists.",
    ],
    [
        "How do I calculate the true landed cost of imported ribbon?",
        "Start from the quoted unit price and add, per metre or per order as appropriate: international "
        "freight based on the container type and the actual carton dimensions and weights the factory "
        "gives you; cargo insurance at roughly 0.1 to 0.3 percent of cargo value; import duty at the "
        "rate for the confirmed HS classification and origin; origin and destination port and terminal "
        "handling; inland delivery from the destination port to your warehouse; bank and payment fees; "
        "customs brokerage, which is a fixed per-entry cost and therefore penalises small consignments; "
        "an allowance for quality loss based on the mill's own reject rate and freight damage; the "
        "working capital cost of the deposit and the lead time; the carrying cost of the stock; your own "
        "administrative time; and the modelled cost of a single quality failure. The last two are the "
        "ones most often left out, and they are frequently large enough to change which supplier you "
        "choose.",
    ],
    [
        "Should I pay a higher unit price for a supplier that includes pre-shipment inspection?",
        "Almost always yes, particularly for a new colour and new artwork. Pre-shipment inspection is a "
        "small line item relative to the cost of discovering a problem after the container has sailed. "
        "That cost is not the ribbon: it is the freight you have already paid, any demurrage, the "
        "resampling and re-order cycle, the delay to your customer's launch, and the claims conversation "
        "with your customer. There are two reasons the comparison can still favour the quotation "
        "without inspection. The first is a genuinely small or routine reorder where the risk is low. "
        "The second is that the inspection is being offered by a factory whose internal process is "
        "weak, in which case the inspection only catches the defect at the last moment rather than "
        "preventing it. Ask about the mill's internal process and its own reject rate before deciding "
        "that inspection is the answer.",
    ],
    [
        "What is a reasonable reject rate to assume in a cost model for custom ribbon?",
        "It depends far more on the construction and the decoration method than on the factory, so a "
        "single industry figure will mislead you. Screen-printed polyester on a stable construction is "
        "generally predictable; a jacquard woven pattern, a wired edge or a very narrow width with a "
        "large decoration count is not. Model a conservative allowance and test the sensitivity of your "
        "total landed cost against it, so you know how much the number matters. More usefully, ask each "
        "supplier what proportion of the quoted quantity they expect to fail final inspection and "
        "whether that material is charged to you. A factory that answers this question directly and "
        "gives you a figure is telling you it manages its own reject rate, which is a materially "
        "different situation from one that has never been asked.",
    ],
    [
        "How do I decide between reducing order quantity to lower inventory risk and accepting a higher "
        "unit cost?",
        "Calculate the fixed cost per shipment before deciding. Brokerage, documentation, inspection "
        "booking and the inward handling at destination are largely fixed regardless of whether the "
        "consignment is 8,000 or 24,000 metres, and they are penalised by splitting one order into "
        "three. Then calculate the carrying cost of the extra stock you would hold if you consolidated: "
        "warehouse space, insurance, capital at your cost of funds, and obsolescence exposure on a "
        "colourway that may not sell through. Whichever of the two is larger decides it, and in many "
        "programmes the fixed cost of fragmentation is larger than the carrying cost of consolidation. "
        "The other option worth pricing is a staggered schedule of two medium shipments rather than one "
        "large one followed by a small top-up, because it captures most of the inventory benefit without "
        "paying the full fixed cost twice.",
    ],
    [
        "How should a buyer handle a factory that will not provide a price breakdown?",
        "Treat the refusal as data rather than as an obstacle. It may mean the mill resells rather than "
        "manufactures, in which case the quoted price is really a purchasing decision made elsewhere and you have "
        "less direct access to the process than you assumed. It may mean the factory's commercial model "
        "is a single blended rate, which is common among smaller mills. Or it may simply be that the "
        "salesperson is not the person who can answer it. In each of those cases the practical response "
        "is the same: ask for the information you actually need in a different form. Ask for the carton "
        "plan and weights so you can price freight yourself, ask for the certificate scope and expiry, "
        "ask for the production lead time as a date rather than a range, and ask for the artwork and "
        "tooling ownership terms in writing. A supplier who answers those is materially more useful to "
        "you than one who answers the price breakdown question and nothing else.",
    ],
    [
        "What negotiating levers actually work with ribbon factories on price?",
        "Three, reliably. The first is the specification: agreeing a different construction, a "
        "consolidated colour count, or a smaller decoration coverage changes the cost of the product "
        "rather than the margin on it, and both sides usually prefer that to a discount. The second is "
        "timing and predictability: a stable, rolling forecast with defined reorder points and artwork "
        "already on file lets the mill plan production more efficiently, and a meaningful part of that "
        "efficiency is normally shared rather than retained. The third is scope and duration: agreeing "
        "a multi-year arrangement with a defined volume profile in exchange for a firmer price is the "
        "one lever that genuinely changes the mill's commercial position, and it is the one most buyers "
        "never pull because they assume the factory will not move. What does not work is applying "
        "pressure during a peak production window, when the factory's own order book is full and it has "
        "no reason to move, and what does not work is asking for a percentage reduction without "
        "showing the components you believe are carrying margin.",
    ],
]

if __name__ == "__main__":
    import json
    from pathlib import Path
    Path("/tmp/rb358_body.html").write_text(BODY, encoding="utf-8")
    Path("/tmp/rb358_faq.json").write_text(json.dumps(FAQ, ensure_ascii=False, indent=1), encoding="utf-8")
    import re
    words = len(re.sub(r"<[^>]+>", " ", BODY).split())
    print(f"[OK] body words={words} faq={len(FAQ)}")
