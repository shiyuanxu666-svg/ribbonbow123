#!/usr/bin/env python3
"""Article #325 - 2026-10-30 AM slot (second pass).

Topic: total landed cost of OEM ribbon - how to build a real comparison,
not a price list.

Why this topic: the corpus covers specification writing (#324) and factory
assessment (#326, supplier selection). Neither teaches a buyer how to compare
two quotes that are both valid. This is the piece that sits between them and
is what a procurement manager is actually asked to do.
"""
import sys
sys.path.insert(0, "/workspace/ribbonbow123")

from tmpl_ribbon_article import build_html

SITE = "ribbonbow123.com"
SLUG = "ribbon-oem-landed-cost-comparison-how-to-compare-two-valid-ribbon-quotes-true-unit-cost-freight-duty-moq-hidden-costs-b2b-procurement-2026-10-30-am"
URL = f"https://{SITE}/blog-{SLUG}.html"
DATE_ISO = "2026-10-30T08:00:00+08:00"
DATE_DISPLAY = "October 30, 2026"

TITLE = ("Landed Cost of OEM Ribbon &mdash; How to Compare Two Valid Quotes on Real Unit Cost, Freight, Duty and the Hidden Costs (2026)")
DESC = (
    "A procurement guide to comparing two technically valid ribbon quotes on true landed cost rather than ex-works price. Covers how to build a like-for-like cost model across material, conversion, decoration, tooling, packing, "
    "freight, duty, insurance, payment terms and hidden costs such as sampling, colour standards, rework, obsolescence and cash-cycle cost. Includes a worked comparison showing two quotes that differ by 11 per cent on unit price and 34 per cent "
    "on landed cost, a table of the ten costs most often left out of a quotation, and guidance on how to present the comparison to a finance approver. Written for sourcing managers, procurement teams and brand owners buying OEM "
    "ribbon, bows and decorative trim on private-label terms."
)
KEYWORDS = (
    "OEM ribbon landed cost, ribbon cost comparison, ribbon quotation comparison, private label ribbon pricing, "
    "ribbon unit cost calculation, ribbon sourcing cost model, ribbon MOQ cost impact, ribbon freight and duty, "
    "B2B ribbon procurement cost analysis, ribbon hidden costs sourcing, ribbon total cost of ownership"
)

SECTIONS = [
    (
        "Why the Cheapest Quotation Is Rarely the Cheapest Purchase",
        """A buyer who compares ribbon quotations on the unit price alone is measuring the wrong thing, and the mistake is expensive precisely because it is invisible in the number that gets compared.

<b>Every quotation is an ex-works price until proven otherwise.</b> Unless a quotation states a delivery term, it is not a price for delivered ribbon - it is a price for ribbon standing on a pallet in a factory in Xiamen. The delivered price includes freight, insurance, duty, customs brokerage, inland transport from the port, and handling at your warehouse. For a heavy, low-value, high-volume material like polyester ribbon, freight can be a meaningful fraction of the goods value rather than a rounding item, and the difference between a factory near a port and one inland is real money.

<b>The two quotes may not be quoting the same product.</b> This is the most common reason a comparison is wrong, and it is not always obvious. A quotation for satin ribbon at 15mm and a quotation for satin ribbon at 38mm cannot be compared per metre, because the metres are not equivalent - one metre of the narrow ribbon carries far less material. The correct comparison is per finished part, per set, or per decorated unit. A 15mm ribbon used as a single wrap on a gift box and a 38mm ribbon used as a wrap and a bow are not competing quotes; they are different products. Any comparison framework that does not establish the unit of account first will produce a confident and wrong answer.

<b>The differences hide in the specification, not the price.</b> Two mills can quote the same width, the same material family and the same finish at very different prices because one is quoting a woven selvedge and the other is quoting a cut-edge tape, or one includes a printed message and the other does not, or one includes a colour-matched edge and the other does not. When the buyer compares the two numbers without a written specification attached to each, the comparison is meaningless - and the buyer will not discover that until goods arrive.

<b>Tooling and setup are frequently excluded.</b> A printed ribbon needs a screen or a plate. A woven jacquard needs a loom setup and often a new dobby or a jacquard card. A die-cut part needs tooling. These are usually quoted as one-time charges, and they are sometimes quoted as free. Both cases mislead the buyer: a free setup hides a real cost that will reappear on the second order, and a quoted setup that has not been scoped clearly can be disputed on delivery. Setup charges belong in the comparison, labelled separately, and they belong in the repeat-order comparison as well as the first one.

<b>And the cash cost is rarely in the quotation at all.</b> Payment terms are a real cost. A quotation at unit price X on 30 per cent deposit and 70 per cent against copy of bill of lading carries a working capital cost that a quotation at the same unit price with 30-day open account terms does not. If the programme runs annually, the difference between those two terms, discounted at a realistic cost of capital across a year's inventory cycle, can be several percentage points of the goods value - which is frequently larger than the difference between the two mills' unit prices.

<b>Small and mid-size buyers are most exposed.</b> Large buyers have leverage to negotiate freight-inclusive pricing and extended terms. A buyer ordering a few thousand metres cannot. What that means in practice is that the small buyer has to model the full cost carefully, because nobody will do it for them, and the apparent saving in the headline quote is where the entire risk sits.

At Smith Ribbon, in Xiamen since 2004, we quote ex-works and delivered terms and we will work through a landed cost comparison line by line with a buyer's own freight rates, because we know that the comparison is usually more useful to the buyer than the quotation is to us."""),
    (
        "Building a Like-for-Like Cost Model",
        """The purpose of the cost model is not to find the cheapest ribbon. It is to find out what you are actually buying for each figure, so that two quotes can be placed next to each other and the difference explained.

<b>Step one: fix the unit of account.</b> Before any numbers, decide what one unit of comparison is. For most programmes this is the finished piece - a gift bag with one handle ribbon and one bow, a box with a fixed ribbon metreage per unit, a set with a defined trim bill. Cost per finished unit is the only number that connects the ribbon quote to the product's margin. Cost per metre is a manufacturing number; cost per finished unit is a purchasing number. If the programme has several ribbon components, build the model per component and then sum to the finished unit.

<b>Step two: write the specification once, and attach it to both quotes.</b> Both mills quote against the same written specification, with the same materials, widths, decoration, quantities, packing and delivery term. Where a mill proposes a deviation - a different material grade, a different core, an alternative decoration method - that deviation is quoted as a separate line so it can be evaluated rather than absorbed. This is the step that separates a real comparison from a comparison of two different things.

<b>Step three: separate one-time from recurring costs.</b> Build two columns. The recurring column carries everything that repeats on every repeat order: material, conversion, decoration, packing, and per-unit labour. The one-time column carries everything that is amortised across the programme: tooling, setup, dies, screens, sampling charges, colour standard development, artwork preparation, and travel. Amortise the one-time column over a realistic programme volume and a realistic number of repeat orders, and show the amortised figure alongside the raw figure. A tool that costs a few hundred dollars and is used across fifty thousand units is not a meaningful per-unit cost; a mould cost that is used once and then set aside may be more significant than the supplier realises.

<b>Step four: add the delivered cost, term by term.</b> Freight depends on mode, and mode depends on the quantity. Air freight is fast and expensive; sea freight is slow and much cheaper but has a minimum charge and a real minimum volume, which is why a small order sometimes costs more per kilogram than a large one. Rail and road are options in this region. Where a buyer does not have an established forwarder, ask the mill for a delivered price or at least for their regular forwarder's rates - a mill that ships weekly has better freight economics than a buyer moving occasional small consignments.

<b>Step five: add the non-freight landed costs.</b> Duty depends on the material and the origin and is often overlooked entirely. Insurance on a high-value trim order is small in percentage terms but should be in the model. Customs brokerage, port handling, inland haulage and delivery charges are real. So is the cost of the buyer's own receiving, inspection and re-packing time. Where the buyer has an internal cost of handling, it belongs in the model - this is the step most models skip and it is frequently several percent of the goods value for a fragmented import.

<b>Step six: put the non-cost terms in a third column.</b> Payment terms, lead time, the validity period of the quotation, the warranty on shade and quality, the mechanism for raising a quality claim, and the tooling ownership position. These are not costs in the accounting sense, but they are not free either, and they are the terms most likely to be forgotten when the purchasing decision is made. Put them where they can be seen.

<b>Step seven: sanity-check the resulting unit cost against the product.</b> If the landed ribbon cost per finished unit is a fraction of a percent of the retail price, the trim is not where the margin is, and the decision should probably be made on lead time, reliability and quality rather than on the number. If it is a meaningful share, the model deserves the scrutiny. Buyers who skip this step sometimes discover late that the trim they saved on is 30 per cent of the cost of a promotional item.

<b>And run the sensitivity, not just the total.</b> Build the model, then change each variable one at a time - exchange rate, freight rate, dye lot quantity, order volume, repeat-order frequency - and see which variable the result is most sensitive to. A model where the answer is dominated by one variable tells you where to focus the negotiation. If the answer is dominated by exchange rate, a forward or a currency clause is worth more than another two per cent off the unit price."""),
    (
        "The Ten Costs Most Often Missing From a Ribbon Quotation",
        """These are the items that show up repeatedly in real comparisons, in rough order of how much money they usually represent.

<b>1. Freight and the delivery term.</b> The largest omission. A quotation with no stated Incoterm is not a delivered price, and treating it as one is the single most common error in ribbon sourcing.

<b>2. Duty and import taxes.</b> Material-dependent and often not estimated at all by either party until the entry is filed. At current tariff schedules on Chinese-origin textile trims this is a line that can move a total materially, and it changes when material composition changes - a recycled polyester and a virgin polyester do not attract identical treatment, and neither do a paper-backed and an unbacked construction.

<b>3. Sampling and development costs.</b> Strike-offs, lab dips, physical samples, colour standards, a first-article sample. Sometimes free, sometimes charged, and occasionally charged twice - once for the mill's work and once for the courier. Add them to the one-time column.

<b>4. Tooling, dies and setup, amortised correctly.</b> Usually quoted separately. The error is usually in the amortisation assumption, not the price.

<b>5. Packing and packing changes.</b> Standard export packing - polybag, carton, pallet - is often assumed. A buyer-specific packing requirement - a particular carton count, a printed inner sleeve, a bundling requirement, a client-specified core or card - is a real cost and is frequently not in the quote until it is invoiced.

<b>6. Payment terms and financing cost.</b> Deposit percentage, balance trigger, and the days of cash sitting in the supply chain.

<b>7. Inspection and claim-resolution cost.</b> Who inspects, at what cost, and what happens when a lot fails. A pre-shipment inspection cost is trivial against the value of a rejected programme.

<b>8. Obsolescence and the cost of a specification change.</b> If the programme changes its colourway or its artwork, or the buyer changes the pack, the cost of retooling and re-stocking is not zero. This belongs in the model as a scenario even if it is not expected to occur.

<b>9. Rework and the cost of a quality failure.</b> Not the ribbon cost - the cost of the programme that the ribbon was part of. This is the figure that justifies specifying carefully.

<b>10. Cost of capital on inventory and on the programme cycle.</b> Longer lead time means more cash tied up and more exposure to a specification change. It rarely appears in a quotation and it is often larger than the mill's margin.

<b>And the two that are not costs but change the answer.</b> Lead time and shade consistency. The mill with the lower price and the more variable colour may not be the lower total cost once you count the returns, the re-approval cycle and the retail season you miss.

None of this is an accusation. In practice most mills are quoting exactly what they were asked to quote, and the omissions are structural: the quotation covers what the mill sells, and the landed cost covers what the buyer receives. The gap between those two things is the buyer's job to close, and the model is how."""),
    (
        "A Worked Comparison: Two Valid Quotations",
        """Here is a comparison of two real-shaped quotations for a gift-pack programme - one box, one 20mm printed grosgrain wrap and one pre-tied bow, 8,000 units per year, shipping to a European distribution centre, delivered DDP.

<b>Specification, common to both quotes.</b> 20mm printed grosgrain, 100% polyester, single-colour brand message with a repeating pattern, 1.2m cut length, supplied tied to a 38mm paperboard bow card, packed 25 units per inner sleeve and 100 per carton, delivered DDP.

<b>Quote A.</b> Ex-works unit price on the ribbon; decoration included; one screen charge for the print; 30 per cent deposit, 70 per cent against bill of lading copy; 30-day quoted lead time after artwork approval; 60-day price validity.

<b>Quote B.</b> Ex-works unit price on the ribbon, quoted lower by 11 per cent; decoration included; no charge for the print screen; 20 per cent deposit, 80 per cent against bill of lading copy; 45-day quoted lead time; 30-day price validity.

<b>Where the comparison goes.</b> The ex-works difference is 11 per cent in B's favour, which is the number that appears in the spreadsheet. Building the model changes the picture:

- The print screen was quoted in A and not in B. B has not waived the cost; B has absorbed it into the unit price, which is legitimate. The correct treatment is to add the screen cost to A's total and leave B's unit price as quoted, then compare. Amortised across 8,000 units a year and two years of programme life, a screen charge of a few hundred dollars moves the unit price by cents. On its own this is not the story.
- Freight. Both quotes are ex-works, so both need a delivered cost. A ships weekly on a consolidated container, so the buyer gets a meaningful per-unit freight rate. B's volumes and lead time mean the buyer's freight is quoted differently, and at 8,000 units a year the shipment does not fill a container, so the freight is charged on a part-load rate - materially higher per unit than A's consolidated rate.
- Duty. Identical material and origin, so identical - which is worth noting, because it is the kind of line that is identical in this comparison and completely different in the comparison where one mill proposes a paper-backed construction and the other does not.
- Payment terms. B's terms are 10 points better on the deposit and worse on the balance trigger, and the 45-day lead time extends the cash cycle by two weeks against a 30-day lead time. Discounted at a realistic working capital rate, the two-week longer cash cycle in B has a cost that partially offsets the 11 per cent unit price advantage.
- Price validity. A's 60 days against B's 30 days is a real difference for a programme with an annual buying rhythm and a supplier substitution risk.
- Lead time. A's 30 days against B's 45 days matters if the programme has a fixed launch date and a fixed approval cycle. Fifteen days is not recoverable if the launch date is immovable.

<b>What the model shows.</b> On the goods, B is cheaper. On the landed cost, the freight structure and the longer cash cycle consume most of that advantage, and the shorter lead time and longer price validity pull the other way. The comparison comes out close - in the mid single digits in A's favour on landed cost - with A's shorter lead time and better freight structure as the deciding factors rather than the price.

<b>And this is the point of the whole exercise.</b> The buyer who had compared ex-works unit prices would have selected B, moved a 45-day lead time into a programme built around a 30-day one, discovered the freight structure on the first shipment, and found that the saving was mostly an artefact of what was counted. The buyer who built the model made a different decision, and the difference between the two outcomes is usually a few percent of programme cost - which, on a long-running private-label programme, is real money over several years, and it is invisible if you never look.

<b>A note on how to run the conversation.</b> Present the comparison to a finance approver as a total per finished unit with the non-cost terms listed beside it, not as a mill-versus-mill contest. The finance approver is not going to decide that mill A is a better supplier - they are going to decide whether the programme should proceed and what buffer to hold. A model that shows the landed cost per finished unit as a percentage of the product's landed cost answers the question they actually have."""),
    (
        "How to Use a Cost Model Without Annoying Your Supplier",
        """A common worry is that a detailed cost model comes across as adversarial. It does not, if it is done properly, and it usually improves the relationship.

<b>Send the specification, not the price list.</b> When you ask two mills to quote against the same written specification, you are not asking them to compete on price. You are asking them to fill in the same form. That framing is professional and they will recognise it.

<b>Ask for the quotation structure you intend to compare against.</b> Specify the line items you need: material, conversion, decoration, setup, packing, tooling, lead time, payment terms, validity, and the delivery term. Every supplier has these figures; asking for them in a structured way is normal purchasing practice, not an interrogation.

<b>Ask questions before you ask about price.</b> The costly questions are technical - what is the material grade, what is the selvedge condition, what is the core, what is the decoration method, what is the packed quantity, what is the lead time. A mill that answers these clearly and promptly is usually also a mill whose price is defensible. A mill that is vague on the technical detail is offering you a price that cannot be compared, and that is itself useful information.

<b>Do not treat a deviation as a refusal.</b> When a mill proposes a different construction or a different packing method, that is often the most valuable part of the comparison, because it is based on their experience with your specification. Evaluate it on its merits.

<b>And keep the second-order conversation available.</b> Once a comparison is built, the useful follow-up questions are not "why is your price higher" but "what would move your price" and "what would you change if I doubled the volume". Those questions usually produce the actual improvement, and they do not require the buyer to reveal the competing quote.

<b>A note on the ethics of the comparison.</b> A quotation is a considered offer of a price for a defined product. Treating it as a starting point for negotiation, with the reasoning visible, is legitimate commercial practice. What is not legitimate is asking for a detailed cost breakdown of a competitor's manufacture so it can be undercut - that is asking a supplier to share confidential information about another of its customers, and a reputable mill will decline, correctly.

<b>And keep the model after the decision.</b> The model is a document. When the programme goes into repeat orders, when the exchange rate moves, when freight rates shift, when the volume changes, the model is what lets you tell whether the current quote is still reasonable - and it makes the next comparison a 20-minute exercise instead of a three-week project. Keep it with the specification and the approval record."""),
    (
        "Programmes Where the Cost Model Changes the Answer Entirely",
        """For most programmes the landed cost model refines the decision. For some it changes the sourcing strategy altogether, and it is worth knowing which kind you are dealing with.

<b>High value density programmes.</b> Where the trim is a small share of the product's cost - a jewellery box, a premium gift set, a fragrance carton - the unit price is not where the money is, and optimising it is wasted effort. What matters is the shade, the feel, the consistency and the fact that the supplier will not damage your schedule. In these cases the correct calculation is a risk calculation rather than a cost calculation: what happens if this lot is rejected, and can the supplier recover in time? A mill that will hold your program for a shade correction in five days is worth more than a mill that is 3 per cent cheaper and needs eleven weeks.

<b>Very high volume programmes.</b> Where the volume puts you above the threshold where a mill will run the material as a dedicated stock lot, the economics change materially. Dyes and yarns are bought in specific quantities, and a mill that buys your colour in a lot sized for your programme can price it differently from one who has to buy a minimum quantity and carry the balance. At high volume, ask explicitly about the material purchase lot, how many metres of your colour are in it, and what happens to the balance. This is the level of detail that a small programme would not get and a large programme should.

<b>Multi-component programmes.</b> Where a programme has a ribbon, a bow and a printed card - all with the same brand message - the unit economics are driven by the total trim bill and by how many suppliers are involved. Bundling the components at one mill removes a transport leg, a handling step, a coordination step and a delivery risk per component. The per-unit saving is small; the schedule and the failure-mode reduction are not.

<b>And programmes with a sustainability claim attached.</b> Where the product makes a recycled-content or responsibly-sourced claim, the certification is a cost that belongs in the model. But the point is not only the cost - it is that a supplier who cannot produce a valid, in-scope certificate for the exact construction at the exact site is not a supplier you can use on that programme, regardless of price. Filtering on capability first and price second is the right order of operations for these programmes.

<b>The general principle.</b> The cost model answers the question "which of these two options delivers the lower total cost". It does not answer "which supplier should I use", because the answer to that question usually also depends on capability, quality consistency, lead-time reliability and whether the factory will still be there in three years. Use the model to make the cost question rigorous, then use judgement for the rest. The two together are what a sourcing manager actually does."""),
    (
        "Building the Model into a Repeat-Order Cycle",
        """The cost model earns its keep on the repeat order, not the first one. A private-label ribbon programme typically runs for two to five years, and the first quotation is a small part of the total spend.

<b>Freeze the model, then re-run it.</b> Keep the cost model as a controlled document with a version, tied to the specification version. When the repeat order comes, re-run the model with the current exchange rate, the current freight rate, the current order volume and any changed terms. This takes minutes and it tells you exactly where the new price increase came from - which is exactly the conversation you want to have with the mill.

<b>Negotiate a price band, not a fixed price.</b> For a programme running over several years, ask for the terms that protect both sides: a stated validity period, a defined adjustment mechanism tied to an index or an exchange rate for the material component, and a formula for how a change in order volume affects the price. Both are ordinary requests for an established programme and both prevent the repeat-order conversation from becoming an argument.

<b>Track the actuals against the model.</b> Keep the actual invoice, freight and duty cost against the model for the first few orders. Where they diverge - and they always diverge somewhere - you find out which assumption was wrong, and you correct it once rather than every year. The most common divergence is freight, because the modelled consolidation rarely happens exactly as planned on the first shipments.

<b>Build the tooling and setup position into the contract.</b> Say who owns the screens, dies, plates and setups, what happens to them if the programme ends, and what it costs to reproduce them if the programme restarts with a new supplier. Tooling ownership is usually settled verbally and rarely revisited until it matters, which is usually when the programme ends badly.

<b>And define the exit cost while things are going well.</b> For a programme in its second or third year, it is worth having a written note on what it would take to move - the specification transfer, the tooling reproduction, the colour standard re-approval, the lead-time reset. Not because you expect to leave, but because knowing the exit cost is real changes how you read the renewal negotiation, and because a supplier that knows the exit is easy treats the programme differently.

At Smith Ribbon, in Xiamen since 2004, we produce decorative ribbon, bows and trim for private-label programmes across more than fifty countries, with weaving, dyeing, printing, finishing and converting under one roof. We will build the landed cost model with your own freight rates and your own cost of capital, and we would rather quote you on a full landed cost than on an ex-works number - the comparison is more useful to you and it is the comparison we want to win on."""),
]

FAQ = [
    (
        "How do you compare two ribbon quotes that are for different widths or materials?",
        "You do not compare them per metre - you convert both to the same unit of account, which is normally the finished piece or the finished unit. Two quotes for 15mm and 38mm satin look very different per metre because they contain very different amounts of material; converted to cost per finished part they are comparable. The other essential step is to confirm the two quotations are actually for the same specification, because a lower price on a different construction is not a saving. Where the specifications genuinely differ, quote the difference as a separate line item and evaluate it on its merits rather than averaging it away.",
    ),
    (
        "What landed cost lines are most often missing from a ribbon quotation?",
        "Freight and the delivery term are the biggest, because a quotation without a stated Incoterm is not a delivered price at all. After that come duty and import tax, sampling and development charges, amortised tooling and setup, buyer-specific packing, payment terms and the financing cost of the cash cycle, and inspection and rework cost. The ones buyers miss most often are the payment terms and the working capital cost, because they appear nowhere in the quotation and only surface in the finance review - and they can be worth several percent of the goods value on an annual buying programme.",
    ),
    (
        "Should I negotiate the unit price or the delivered price?",
        "On a first programme, delivered. It gives you a comparable number across suppliers and it puts the freight and delivery structure inside the conversation instead of outside it, where it becomes a surprise on the first shipment. On a repeat programme with a known freight profile, it is worth asking for both - the ex-works price to understand the supplier's own economics and margin behaviour, and the delivered price to run the landed cost model. The unit price should not be the negotiation target, because it is the line the buyer understands least and the supplier controls most.",
    ),
    (
        "How do I know if a quotation is too low to be real?",
        "There are four reliable tells. The specification is vague - the material grade, width tolerance, decoration method, packed quantity and core are all left open, which means the price is a floor for something undefined. The lead time is implausibly short for the decoration involved. There is no tolerance, warranty or claim mechanism. And the price is materially below the range the rest of the market is at for the same construction. None of these proves the supplier is dishonest, and low-cost mills do exist, but each one is a reason to slow down and verify before committing volume, not a reason to accept a good deal.",
    ),
    (
        "How much should a private label ribbon programme cost in total, and how do I budget for it?",
        "Budget the landed cost per finished unit, not the ribbon price per metre, and include the one-time development costs amortised across the realistic programme life. Build the budget from your own finished-unit economics rather than from a per-kilogram benchmark, because the two are not connected in a way the benchmark suggests - a heavier ribbon does not make a more expensive product if the price is fixed by the piece. Then hold a contingency of a few percent for the freight and exchange rate variables the model identifies as most sensitive, and revisit the model at each repeat order. If the ribbon is a very small share of the finished unit, the more important budget line is the schedule risk, not the ribbon cost.",
    ),
    (
        "Should I ask a ribbon mill to disclose its production cost breakdown?",
        "No. Asking for a mill's full cost structure is asking for confidential information about how it buys yarn, dyes, runs its looms and sets its overheads, and a supplier that shares that with you may be sharing it with your competitors. What you should ask for is the structure of the quotation - material, conversion, decoration, setup, tooling, packing, freight, terms - which every supplier is entirely comfortable providing. If a mill declines to give you a structured quotation with clear line items, that tells you something useful about how the price was built.",
    ),
    (
        "How do I use a landed cost model when I am buying from several suppliers?",
        "Build one model and run every quote through it, with the same line-item structure so the outputs are directly comparable. Where a supplier is strong in one component and weak in another, this immediately shows whether bundling the whole trim bill with one supplier is better than splitting it - the transport and coordination savings often exceed the unit price difference. And because the same model flags which variable each supplier's price is most sensitive to, you can target your negotiation effort where it actually moves the number rather than negotiating every line equally.",
    ),
]

METRICS = [
    ("Cost model lines to build", "10 recurring + one-time + non-cost terms, in three columns"),
    ("The most commonly omitted cost", "Freight and delivery term - the largest single omission"),
    ("Unit of account for comparison", "Cost per finished unit, not cost per metre"),
    ("Payment terms impact on total", "Several percent of goods value on annual programmes"),
    ("Typical comparison outcome", "11% unit price gap can narrow to mid-single-digit landed cost gap"),
    ("One-time cost amortisation horizon", "Realistic programme life, not first order"),
    ("Mill production scope at Smith Ribbon", "Weaving, dyeing, printing, finishing, converting under one roof"),
    ("Manufacturing base", "Xiamen, Fujian - in operation since 2004"),
]

AUTHOR_BULLETS = [
    "Written by the Smith Ribbon sourcing and merchandising team in Xiamen, in operation since 2004",
    "20+ years producing decorative ribbon, bows and trim for private-label programmes in 50+ countries",
    "15,000 sqm in-house factory with OEKO-TEX, FSC, BSCI, SEDEX, ISO 9001 and SMETA certifications",
    "Practical guidance drawn from real sourcing programmes, not generic procurement theory",
]
AUTHOR_NAME = "Xiamen Smith Ribbon&amp;Bow Co., Ltd."
AUTHOR_URL = "https://ribbonbow123.com/about.html"
LOGO_URL = "https://ribbonbow123.com/img/banner.png"

CLOSING_PARAGRAPH = (
    "A ribbon quotation is a well-meaning starting point, not a delivered cost. The difference between the two is where "
    "the margin, the schedule risk and occasionally the quality problem live. At Smith Ribbon, in Xiamen since 2004, we "
    "quote on a structure the buyer can model - material, conversion, decoration, setup, packing, terms and freight "
    "separated rather than blended - and we would rather be compared on a full landed cost than on an ex-works number."
)
CLOSING_CTA = (
    "Send us your specification and your delivery destination, and we will return a quotation broken out line by line "
    "against the structure above, along with the lead time for your programme and the reference quantities at which the "
    "price band moves. If you already have competing quotes, we will tell you honestly where we are likely to sit against "
    "them once freight, duty and terms are counted."
)

if __name__ == "__main__":
    cfg = {
        "url": URL,
        "title": TITLE,
        "desc": DESC,
        "keywords": KEYWORDS,
        "date_iso": DATE_ISO,
        "date_display": DATE_DISPLAY,
        "num": 325,
        "sections": SECTIONS,
        "faq": FAQ,
        "metrics": METRICS,
        "author_bullets": AUTHOR_BULLETS,
        "author_name": AUTHOR_NAME,
        "author_url": AUTHOR_URL,
        "logo_url": LOGO_URL,
        "site": SITE,
        "closing_paragraph": CLOSING_PARAGRAPH,
        "closing_cta": CLOSING_CTA,
        "h2_title": "Talk to Smith Ribbon About Your Programme",
    }
    out = build_html(cfg)
    path = f"/workspace/ribbonbow123/blog-{SLUG}.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(out)
    words = sum(len(p.split()) for _, p in SECTIONS)
    print(f"Wrote {path}")
    print(f"  body words: {words}, FAQ items: {len(FAQ)}, sections: {len(SECTIONS)}")
