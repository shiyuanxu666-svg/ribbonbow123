#!/usr/bin/env python3
"""Article #326 - 2026-10-30 PM slot.

Topic: writing an RFQ / supplier enquiry package that gets comparable,
quotable answers - and how to read the answers you get back.

Why this topic: #324 covers the technical specification (what to buy),
#325 covers landed cost comparison (how to compare), and the supplier-selection
piece covers factory assessment. What is missing is the enquiry itself - the
first document a buyer sends, the one that determines whether the quotes you
receive back are comparable at all. And on the other side, how to read a quote
response for the signals that predict how the supplier will actually perform.
"""
import sys
sys.path.insert(0, "/workspace/ribbonbow123")

from tmpl_ribbon_article import build_html

SITE = "ribbonbow123.com"
SLUG = "ribbon-oem-rfq-guide-how-to-write-a-request-for-quotation-that-gets-comparable-answers-and-how-to-read-the-response-b2b-procurement-2026-10-30-pm"
URL = f"https://{SITE}/blog-{SLUG}.html"
DATE_ISO = "2026-10-30T13:00:00+08:00"
DATE_DISPLAY = "October 30, 2026"

TITLE = ("How to Write an RFQ for OEM Ribbon That Gets Comparable Answers &mdash; and How to Read the Quotations That Come Back (2026)")
DESC = (
    "A practical guide to writing a request for quotation for OEM decorative ribbon that produces comparable, quotable responses, and to reading those responses for what they predict about future performance. "
    "Covers the seven parts of a well-structured RFQ, the questions that force a mill to commit to a real number, the details buyers routinely omit that make quotes impossible to compare, how to read response speed and "
    "question quality as performance signals, the difference between a clarification question and a sales signal, how to score responses objectively, and what to do about the suppliers who reply with a question instead of "
    "a price. Written for procurement managers, sourcing teams and brand owners running private-label ribbon and decorative trim programmes."
)
KEYWORDS = (
    "ribbon RFQ template, OEM ribbon request for quotation, how to write an RFQ, "
    "private label ribbon sourcing enquiry, ribbon quotation request, B2B procurement RFQ guide, "
    "ribbon supplier enquiry, how to compare ribbon quotes, ribbon supplier evaluation, "
    "ribbon sourcing process, ribbon buyer guide, private label trim sourcing"
)

SECTIONS = [
    (
        "The RFQ Is Not a Step Before Sourcing. It Is the Sourcing",
        """Most ribbon sourcing processes are drawn as a sequence: shortlist suppliers, send an RFQ, receive quotes, compare, select. In practice the RFQ is where the outcome is largely decided, because the RFQ determines what kind of answer you get back. A vague enquiry produces a vague price that cannot be compared and a supplier relationship that starts with a gap. A precise enquiry produces a number that is genuinely quotable and a supplier who has already started working through your problem.

<b>A quotation is an answer to the question you asked.</b> If you ask "what is your price for polyester grosgrain ribbon, 20mm", the honest answer is a range, because the material grade, the construction, the selvedge, the core, the quantity and the decoration are all open. The supplier who gives you a single confident number for that question is telling you something about their process - not necessarily that they are dishonest, but that their pricing is anchored rather than derived. The supplier who comes back and says "I can quote that between X and Y depending on the material grade and decoration, and here is what I need to firm it up" is doing the actual work.

<b>The cost of a bad RFQ is paid twice.</b> Once in the first round, where you spend two weeks chasing clarifications and comparing quotes that are not comparable. And again in the second round, when the clarifications arrive and the quotes have to be re-based, and you discover that the apparent cheapest option changed because it was quoted on an assumption that nobody checked. The single most valuable thing a buyer can do is spend forty minutes on the enquiry document.

<b>An RFQ is also the buyer's first substantive communication with the mill.</b> The quality of your specification, the clarity of your requirements and the professionalism of the enquiry are the things a factory will form its long-term opinion of you on. In an industry where capacity is genuinely finite and the good mills are busy, the mills that are pleasant to work with get the work. This is not a favouritism argument - it is a fact about how allocation works when several buyers are asking the same factory for the same month.

<b>And the RFQ determines your negotiating position later.</b> If you have a clear written requirement and a documented quotation, your position on the second order is strong, because any change to the specification is visibly a change from what was agreed. If you started with a vague enquiry, your second-order negotiation inherits the vagueness, and every open question becomes a fresh negotiation.

<b>One more practical point.</b> An RFQ is not a binding request and it does not oblige the supplier to quote. Say so plainly in the document. Buyers who write an RFQ that reads like a purchase order generate unnecessary friction, because the mill has to respond to the implied commitment rather than to the actual question. A clear, professional, non-binding enquiry is faster to answer and easier to act on.

At Smith Ribbon, in Xiamen since 2004, we answer roughly a steady stream of RFQs from brand owners and sourcing teams across more than fifty countries. The ones that produce a clean quotation within a day or two share a set of characteristics, and they are the subject of this guide."""),
    (
        "The Seven Parts of an RFQ That Produces Comparable Answers",
        """This is the structure we would send if we were buying. It is not long - a good RFQ is typically two pages - but each part exists because its absence produces a specific failure in the response.

<b>1. Identity and the programme.</b> Who you are, what you buy, what the programme is, and what the volumes look like over the next 12 to 24 months. The volume forecast matters more than the current order quantity, because it determines whether the mill prices your current order as a one-off or as a programme, and because it tells the mill whether to reserve capacity. State it as a forecast, clearly labelled as a forecast. Do not present a forecast as a firm commitment - it damages the relationship when the forecast is not met, and a good mill will remember it.

<b>2. The product specification.</b> Everything from the technical specification that makes the product identifiable and quotable: material family and grade, fibre content, width and width tolerance, construction, weave, thickness or weight, selvedge condition, finish, colour reference and tolerance, decoration method and artwork status, packaging format and packed quantity, and any performance or compliance requirement.

<b>This is the part buyers most often under-specify, and it is the part that most determines whether the quotes come back comparable.</b> A buyer who writes "20mm polyester grosgrain, printed with our logo" will receive quotes for printed grosgrain in a wide range of grades and constructions. The quotes will differ by a large percentage, none of the differences will be explained, and the buyer will conclude the market is opaque when in fact the enquiries were not comparable.

<b>3. Quantities.</b> The trial quantity, the first production quantity, the repeat quantity, and the annual forecast. Ask for pricing at each tier. The tier structure itself is informative - a mill that has no tier pricing has not thought about the programme, and a mill whose tiers are unreasonably steep at low volume is telling you something about how the setup amortises.

<b>4. Commercial terms.</b> The delivery term you want quoted, the destination, the target lead time, the packing standard, the payment terms you are looking for, and the expected validity period for the quotation. A supplier who quotes delivered and a supplier who quotes ex-works are answering different questions; both are fine, but you need to know which you have got before you compare them.

<b>5. Compliance and documentation.</b> The certifications you require with their scope, the test reports you need, the material declarations, the labelling and the country-of-origin documentation. This should be short at RFQ stage and specific. A request for 'OEKO-TEX Standard 100' is answerable; a request for 'all certifications' is not.

<b>6. Samples and the sample process.</b> Whether you need a physical swatch, a lab dip, a strike-off, a woven sample, or a first article, at what stage, and who bears the cost. Specify the approval process you expect - how many rounds of sample revision you will allow, what triggers a revision, and how approval is recorded.

<b>7. The question section.</b> This is the part that distinguishes a good RFQ from a good-enough one. Instead of a bare requirement, ask the questions whose answers you actually need in order to make the decision. See the next section.

<b>And the document mechanics.</b> One file, one version, with a date and a reference number. Name the file with the programme and the date so that a supplier quoting three weeks later is working from the same revision you sent. State that the document is an enquiry and not a purchase order. State the date by which you would like a response, and ask the supplier to quote against the specification reference rather than restating it - a restatement introduces drift.

<b>The rule of thumb for length.</b> If a competent supplier cannot read your RFQ in under five minutes and know exactly what to price, it is either too vague or too complicated. Too vague is more common. Almost every supplier will ask you two or three questions regardless, because no specification is ever complete. The point is to make sure those questions are about genuinely open decisions rather than about basic information you should have supplied."""),
    (
        "The Questions That Force a Mill to Commit to a Real Number",
        """A requirement produces a range. A question produces a number. These are the questions worth asking in an RFQ, and why each one matters.

<b>What is the price at our stated volume, and what changes it if we move to double?</b> The second half of this question is where the information is. A mill that prices tier structure in a way that reflects real setup amortisation tells you how the programme will behave at scale. A mill that quotes the same price at every volume has not done the arithmetic or does not want to signal that the price is soft.

<b>What is the setup or tooling charge, and what does it cover?</b> Ask for the components separately if you can - screen, plate, die, jacquard card, loom setup - because the total is often a round number that bundles several items. You need to know which items recur if you change the programme, and which ones are genuinely one-time.

<b>What is the lead time, and what is in it?</b> A lead time of 30 days and a lead time of 30 days are different things depending on whether the quote assumes artwork approval, colour matching or a strike-off is already complete. Ask which approvals are assumed to be in hand on day zero.

<b>What would cause you to change that price?</b> This is an unusually good question to ask and it gets unusually good answers. A mill that names its real sensitivities - exchange rate on yarn, the price of a specific dye, the decoration method, the packed quantity - is telling you how to manage the programme. A mill that says 'nothing' is not being honest, and a mill that says 'your volume' has told you the price is entirely volume-driven.

<b>What is your minimum order quantity, and is it a material quantity or a setup quantity?</b> These are different barriers. A material MOQ is about how the yarn or dye is purchased. A setup MOQ is about how many metres the loom can run before a changeover. They respond differently to a negotiation, and a buyer who knows which one is binding can negotiate the right thing.

<b>What is your colour approval process and what standard do you match against?</b> A mill that matches against a physical standard and seals a retained sample has a process. A mill that matches against a Pantone chip without a standard does not, and the first shade dispute will reveal it.

<b>What is your tolerance for the specification - what can you hold consistently, and where are you at the edge?</b> Mill owners know where their own process ends. A supplier who tells you honestly that your 38mm width specification is achievable but your 0.2mm tolerance is not is giving you information you can use. A supplier who says yes to everything will eventually be held to the most demanding clause in the document.

<b>What is your typical lead time for a repeat order of the same item, and does it shorten?</b> Repeat orders usually run shorter than the first, because the setup is known and the colour is approved. If it does not shorten at the supplier, ask why - it may indicate the setup was never properly frozen.

<b>And what information do you need from us that we have not provided?</b> This is the most efficient question in the document. It surfaces the buyer's own gaps directly, in the supplier's own words, before the quotation is built on top of those gaps. A supplier that answers this question thoroughly is a supplier who will not be surprised later.

<b>One caution.</b> Do not put all of these in the first RFQ to every supplier. The purpose of the RFQ is a comparable quotation, not an interrogation. Send the core document to the whole shortlist, and put the deeper questions in a follow-up once you have the quotes in front of you and a real reason to ask them. That sequence respects the supplier's time, and it also gives you a chance to see who answers a hard question well before you have committed to them."""),
    (
        "Reading the Quotations That Come Back",
        """Before you read the price, read the response. There is a great deal of information in how a supplier answers, and it is often more predictive than the price itself.

<b>Response speed is a signal, but read it carefully.</b> A fast, complete response usually means the enquiry reached someone who knows the product and the process. A slow response can mean a busy factory, a question that needed a technical opinion, or an enquiry that went into a general inbox. One slow response means little; a pattern across several suppliers tells you about your own enquiry, which may be unclear. Treat speed as a diagnostic of the whole set, not a verdict on one supplier.

<b>The quality of the clarification questions is highly informative.</b> A question about the selvedge condition, the core diameter, whether the printed repeat should align to the bow card, or whether the buyer wants a specific packed quantity tells you the supplier has handled this product type before and is thinking about the programme. A question about the width and the quantity and the delivery port tells you nothing much - those are the things you should have specified. A supplier whose questions are all technical is a supplier who has understood the job. A supplier whose questions are all commercial is a supplier who is treating it as a price request, which is fine but tells you what to expect.

<b>Read the deviations, not just the price.</b> If a supplier has proposed a different material grade, a different decoration method, a different packing format or a different lead time, that deviation is the most useful thing in the response. It is based on their experience, and it is often better than what you asked for. Evaluate it. Many buyers skip the deviations and compare only the headline price, which is how they end up with a specification nobody optimised.

<b>Look at the level of detail in the quote itself.</b> A quote that itemises material, conversion, decoration, setup, packing, terms and validity is a quote from someone who has costed the job. A quote that gives a single figure and a validity date is a quote from someone who has given you a number to see if you are still interested. Both are legitimate ways to open a conversation, but you should know which one you are looking at.

<b>Watch the validity period and the payment terms for what they say about the supplier's confidence in their own price.</b> A very short validity - a week - usually means the price was assembled quickly and may not hold. A long validity - ninety days or more - usually means the price was built carefully and the supplier is comfortable with it. Neither is a quality signal on its own, but the combination of a long validity with a detailed breakdown is a good one.

<b>And watch for the answers that were requested but not given.</b> If you asked for the tolerance the supplier can hold and they did not answer, that is more important than if they had answered it. Ask again, directly.

<b>One more thing worth reading.</b> Whether the supplier asked about your programme rather than just your product. A supplier who asks what the ribbon is used on, whether the programme is seasonal, how the approval works, who signs off on colour - that supplier is thinking about the relationship and the repeat order, not just the invoice. It is a good sign, and it is a sign that is visible before you have any performance data at all."""),
    (
        "The Suppliers Who Reply With a Question Instead of a Price",
        """This happens more often than buyers expect, and it is usually handled badly - either by dropping the supplier from the shortlist or by waiting indefinitely. Both responses lose information.

<b>First: understand why it happened.</b> The enquiry was under-specified in a way that genuinely prevented a price. This is the buyer's gap, not the supplier's failure, and the right response is to fix the document rather than to penalise the person who identified the problem.

<b>Second: answer the question properly, not briefly.</b> A supplier who asks about the packed quantity and receives "whatever is standard" will either quote a packing that does not work for you, or quote a range and note the assumption. Answering with a specific number - the carton quantity, the packed quantity, the destination, the freight terms - removes the ambiguity and gets you a real quotation.

<b>Third: notice whether the question is the same for every supplier.</b> If all five suppliers ask the same question, the RFQ has a gap and it should be fixed for the second round and for every future programme. If only one supplier asks it, that supplier may have understood something the others did not - which is worth investigating before you discount them.

<b>Fourth: distinguish a clarifying question from a qualifying question.</b> A qualifying question is a supplier testing whether the programme is worth their capacity - something like asking about the forecast, the payment terms, the qualification process, or whether you are already talking to other mills. These are not obstacles; they are a supplier deciding how much attention to give you. Answer them directly and you get a better supplier than one who was polite and vague.

<b>And a fifth observation, which is the one buyers get wrong.</b> Some suppliers will not quote at all for a programme they judge to be too small or too speculative. That is a reasonable commercial decision and it should not be read as a quality judgement on your programme. If your volumes are below a mill's minimum, the right response is to adjust the plan - consolidate the trim bill across components, order a longer horizon, or accept a programme structure that makes the order viable - not to conclude that the mill is uninterested in you.

<b>On the other side, from the supplier's perspective.</b> A good RFQ is a small kindness to the person answering it. It means the questioner has done the work, the information is complete enough to act on, and the answer will not need to be re-derived. A supplier who receives a clean RFQ can respond in an afternoon. A supplier who receives a vague one spends two days and still has to come back. Over a long relationship, buyers who send clean RFQs get served faster, and that is worth noticing when a programme is tight on time."""),
    (
        "Scoring Responses Objectively",
        """At the point where you have a set of quotations, something more disciplined than a spreadsheet and a preference is useful. A simple scoring scheme, applied consistently, prevents the two common failure modes: choosing the quote you expected to choose, and overweighting the lowest price without saying so.

<b>Weight by what your programme actually depends on.</b> There is no universal weighting. A programme with a fixed launch date and a hard approval deadline weights lead time heavily. A programme with a tight margin weights landed cost. A luxury packaging programme weights colour consistency and shade risk. A first-article programme from a new supplier weights responsiveness and technical engagement. Write down your weights before you look at the prices, because after you look at the prices you will not be able to claim you were objective.

<b>Score the categories that matter.</b> A workable set for ribbon sourcing: landed cost; technical fit of the proposal; colour and appearance risk; lead time and its reliability; the supplier's financial and capacity stability; the quality system and certification coverage; communication and responsiveness; the terms offered; and the exit cost - how hard would this be to move. Score each from a defined scale with a written reason for the score. The reason matters more than the number: it is the thing that survives when a colleague asks why the recommendation is what it is.

<b>Weight the response quality, not only the price.</b> On the categories of technical engagement and communication, the quotations themselves are the evidence. A supplier whose quotation demonstrates that they understood the specification, whose questions were specific, and whose deviations were thoughtful, has demonstrated something that is difficult to fake and easy to observe.

<b>Then check the arithmetic before you check the ranking.</b> A surprisingly large proportion of scoring errors are arithmetic - a quantity mis-transcribed between the RFQ and the comparison sheet, a freight figure applied to the wrong tier, a setup charge amortised over the wrong volume. The single most common error in ribbon sourcing comparisons is a quantity mismatch between the RFQ and the comparison table, and it is invisible because both numbers look reasonable.

<b>And involve the people who will live with the decision.</b> The quality team should score the technical and compliance categories. The logistics team should score the lead time and the freight. The person who will approve the artwork should score the approval process. If the decision is going to be made by people who were not in the scoring, you will get a different decision than the one you prepared, which is the most common way a well-run process produces an outcome nobody expected.

<b>Finally: write down the decision and the reason while it is fresh.</b> Six months later, when the programme has had a shade problem and a lead-time slip, the record of why the supplier was chosen is what stops the argument from becoming personal. At Smith Ribbon, in Xiamen since 2004, we have seen how much better the second and third orders go when the first order included a documented specification, a documented quotation and a documented approval - because nothing has to be re-negotiated, only re-ordered."""),
    (
        "A Short, Repeatable RFQ Process",
        """The RFQ is worth systematising, because most buyers run the same programme shape repeatedly and the same enquiry shape should therefore be reusable.

<b>Keep a master RFQ template with the programme-specific parts separated.</b> The boilerplate - the programme identity block, the commercial terms section, the compliance section, the questions section, the response instructions - should be written once and reused. The variable parts - the specification, the quantities, the artwork status, the target dates - should be the only things that change. A template that has been used five times is a template that has been corrected five times, and it produces consistent, comparable responses.

<b>Keep a library of your own specifications.</b> When you have specified a construction that worked, save it with the mill's reference and the actual performance. The second programme for the same product line should start from the last specification rather than from a blank page, and this is where the real efficiency lives - not in writing the enquiry faster, but in not having to rediscover the specification each time.

<b>Build a supplier response template.</b> Ask suppliers to quote against a table with the line items you need. Standardising the response format makes the comparison mechanical, removes the transcription errors that cause most comparison mistakes, and it also tells the supplier what you need before they start asking you for it.

<b>Run the RFQ to a deadline.</b> Ask for responses by a date, state that late responses will be considered if useful, and hold the date. A soft deadline produces a trickle of responses over a week; a real deadline produces a set you can work with.

<b>And do a short debrief after each programme.</b> Three questions: what did we omit that we should include next time, what did the supplier ask that we should have specified, and what did we learn that changes the specification. Feed the answers into the template. This is the only part of the process that compounds, and it is the part everyone skips.

<b>The measure of a good RFQ process.</b> The first-round response time drops, the number of clarification emails falls, and - the real measure - the quotes you receive back are actually comparable, so the comparison takes an afternoon rather than a fortnight. At Smith Ribbon, in Xiamen since 2004, we answer RFQs for decorative ribbon, bows and trim across more than fifty countries, and we will tell you honestly if an enquiry is under-specified rather than quoting a number we know will not hold. A clean RFQ gets a clean quotation, and it gets it faster."""),
]

FAQ = [
    (
        "How long should a ribbon RFQ be?",
        "Two pages is usually enough, and the length is a poor measure of quality. What matters is whether a supplier can read it and know exactly what to price without asking a basic question - material grade, width, construction, colour reference, decoration method, quantities, packing, delivery term and target date are the minimum viable set. A short RFQ with those fields in it beats a long one padded with general company information. If the answer to the question 'could this be quoted without a follow-up call' is no, the missing detail is usually the specification rather than the length of the document.",
    ),
    (
        "Should I send the same RFQ to every supplier, or tailor it?",
        "Send the same core document to everyone, because that is what makes the responses comparable. Tailoring the enquiry per supplier introduces differences the buyer cannot control, which means the comparison is no longer measuring the supplier. If you want to explore a supplier's alternative approach, do it in a second round after the comparable quotes are in, as a targeted follow-up on a specific deviation they proposed. The one exception worth making is genuinely programme-specific context - your brand position, the target retail window, the intended product - because it helps a good supplier propose intelligently, and it does not distort the numbers.",
    ),
    (
        "What should I do if a supplier asks for a volume forecast before quoting?",
        "Give it, and label it clearly as a forecast rather than a commitment. The forecast is genuinely useful to a mill because it determines whether they price the order as a one-off or as part of a programme, and a supplier who is willing to quote on a forecast is telling you they can work with a programme rather than only with transactional orders. What you should not do is present a forecast as firm and then reduce it - that damages the relationship at exactly the moment you will need the supplier's cooperation. If you genuinely cannot commit, say what the realistic range is and over what period, and note what is fixed and what is indicative.",
    ),
    (
        "How should I respond to a supplier who proposes a different construction than I specified?",
        "Treat it as the most useful part of the response, which it usually is. A mill suggesting a different material grade, decoration method, packing format or core is doing so from experience with the product rather than from a generic price list, and they can often see a problem with your specification that you cannot see from the outside. Ask them why, in writing, so the reasoning is on record. Then evaluate it as a separate line item against your specification rather than absorbing it silently. In our experience at Smith Ribbon, where our own production team is proposing an alternative to a buyer's specification, the proposal is usually right about the process and sometimes right about the product as well - which is why the buyer should never simply decline to look.",
    ),
    (
        "Is it a problem that quotes come back with different quantities or pack configurations?",
        "Usually it means the suppliers have made assumptions you did not specify, and it is worth resolving rather than accepting, because once quantities differ the unit prices are not comparable at all. Specify the packed quantity, the carton quantity, the carton dimensions if they matter for your warehouse, the core or spool, and the shipment configuration. Where a supplier has a genuinely better packing proposal - fewer cartons, a more robust carton, a size that fits your container better - evaluate it as a proposal with a small cost attached rather than as a discrepancy to be averaged out. The comparison should be built on one configuration that every supplier has priced.",
    ),
    (
        "How many suppliers should I send an RFQ to?",
        "Enough to have a real choice and enough to be a meaningful benchmark - in practice three to five is the useful range for decorative ribbon. Below three you have no comparison; above about five the quotation effort starts to exceed the value of the decision for all but the largest programmes, and the responses you get back become generic. Send the same core document to all of them. If you want a wider market read, an early market-sounding question to a larger list can tell you the price range without generating five full quotations, but do not treat a price range from a broad sound-out as a comparable quotation set.",
    ),
    (
        "How do I read a quote that is significantly below the others?",
        "Treat it as a question, not a bargain. Establish what is different - the specification, the material, the decoration method, the packed quantity, the terms, the lead time, the inclusion of setup - before you decide whether it is an opportunity. An unusually low quote usually means one of four things: a different or lower material grade, a scope difference, a price that will move when the scope is confirmed, or a supplier with a genuine cost advantage. The fourth is possible and welcome. The first three account for most cases, and the first three are all visible if the quote is itemised. Ask for the quote to be broken down, and ask what the price assumes. A supplier who cannot or will not explain a low price is telling you something important.",
    ),
]

METRICS = [
    ("Parts of a well-structured RFQ", "7 - programme, spec, quantities, terms, compliance, samples, questions"),
    ("Target RFQ length", "2 pages - enough to be quoted without a clarification call"),
    ("Questions that force a real number", "8, including volume tiering, setup scope and lead-time assumptions"),
    ("Question quality as a performance signal", "Technical questions predict better programme handling"),
    ("Typical RFQ clarifications to eliminate", "Material grade, packed quantity, colour reference, delivery term"),
    ("Supplier response quality measures", "9 categories - cost, fit, colour risk, lead time, stability, compliance, communication, terms, exit cost"),
    ("Smith Ribbon production scope", "Weaving, dyeing, printing, finishing, converting under one roof"),
    ("Manufacturing base", "Xiamen, Fujian - in operation since 2004"),
]

AUTHOR_BULLETS = [
    "Written by the Smith Ribbon sourcing team in Xiamen, in operation since 2004",
    "20+ years producing decorative ribbon, bows and trim for private-label programmes in 50+ countries",
    "15,000 sqm in-house factory with OEKO-TEX, FSC, BSCI, SEDEX, ISO 9001 and SMETA certifications",
    "Practical process guidance from real quotation cycles, not generic procurement templates",
]
AUTHOR_NAME = "Xiamen Smith Ribbon&amp;Bow Co., Ltd."
AUTHOR_URL = "https://ribbonbow123.com/about.html"
LOGO_URL = "https://ribbonbow123.com/img/banner.png"

CLOSING_PARAGRAPH = (
    "The RFQ decides the quality of the comparison you will spend a fortnight doing. A clear enquiry produces a quotable "
    "number, a specific set of technical questions, and a supplier who has already begun thinking about your programme. "
    "A vague one produces a range, a follow-up call, and a price comparison that is quietly meaningless. At Smith Ribbon, "
    "in Xiamen since 2004, we would rather answer one complete enquiry than resolve a scattered one - it is faster for us "
    "too, and it is the only way the quotation we give you is a number you can actually plan around."
)
CLOSING_CTA = (
    "Send us your programme details - product, specification, quantities, delivery destination and target dates - and we "
    "will tell you what information is still missing before you go to a full quotation round, and what our lead time "
    "would be for your volumes. If your RFQ is already drafted, send it as it stands; we will mark up anything that would "
    "prevent a comparable quotation from your other suppliers as well."
)

if __name__ == "__main__":
    cfg = {
        "url": URL,
        "title": TITLE,
        "desc": DESC,
        "keywords": KEYWORDS,
        "date_iso": DATE_ISO,
        "date_display": DATE_DISPLAY,
        "num": 326,
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
        "h2_title": "Send Us Your RFQ",
    }
    out = build_html(cfg)
    path = f"/workspace/ribbonbow123/blog-{SLUG}.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(out)
    words = sum(len(p.split()) for _, p in SECTIONS)
    print(f"Wrote {path}")
    print(f"  body words: {words}, FAQ items: {len(FAQ)}, sections: {len(SECTIONS)}")
