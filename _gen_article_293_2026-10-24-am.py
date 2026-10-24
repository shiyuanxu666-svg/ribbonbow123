#!/usr/bin/env python3
"""Article 293 (ribbonbow123, 2026-10-24 AM cron slot) - OEM Custom Ribbon MOQ,
Order-Lot Economics and Small-Brand Scale-Up Guide.
Distinct topic from 292 (sample approval/PPAP), 291 (compliance documentation),
290 (print registration), 289 (should-cost TCO), 288 (supplier vetting).
"""
import json
import html as html_mod
from pathlib import Path

DIR = "/workspace/ribbonbow123"
SITE = "ribbonbow123.com"
DATE = "2026-10-24"

NUM = "293"
SLUG = ("oem-custom-ribbon-moq-order-lot-economics-small-brand-scale-up-guide-lower-case-foiling-"
        "colour-development-cost-tradeoffs-b2b-brand-owners-2026-10-24-am")
TITLE = ("OEM Custom Ribbon MOQ &amp; Order-Lot Economics: A Small-Brand Scale-Up Guide to Lowering "
         "Case Folding, Colour Development Cost and the Trade-offs That Decide Your Unit Price (2026)")
DESC = ("A 2026 OEM custom ribbon MOQ and order-lot economics guide for brand owners, category managers and "
        "procurement leads. Covers how minimum order quantity is actually calculated across setup, dye lot, "
        "print plate, colour development and finishing charges, the three variable-cost tiers that dominate "
        "the unit price at low volume, and how to structure a ramp from 500 metres to full programme volume "
        "without paying the development cost twice. Designed to cut first-order landed cost by 18-34 percent "
        "for brands scaling from a single test run to a multi-SKU programme.")
KEYWORDS = ("custom ribbon MOQ, OEM ribbon minimum order quantity, ribbon order lot economics, small brand "
            "ribbon sourcing, ribbon colour development cost, custom ribbon first order, ribbon case pack MOQ, "
            "B2B ribbon sourcing 2026, ribbon print plate cost, ribbon MOQ negotiation")
DATE_ISO = "2026-10-24T08:00:00+08:00"
DATE_DISPLAY = "October 24, 2026 (08:00 CST)"

AUTHOR_NAME = "Smith Ribbon Co., Ltd."
AUTHOR_URL = "https://ribbonbow123.com"
LOGO_URL = "https://ribbonbow123.com/img/banner.png"

SECTIONS = [
    ("Why MOQ Is the First Number a Ribbon Buyer Should Question",
     "For most manufactured materials, minimum order quantity is a factory policy number: below it, the setup does not pay for itself. For custom woven and printed ribbon, that framing is wrong, because the ribbon MOQ is not one number at all &mdash; it is the sum of several independent quantities, each with its own logic, and a buyer who negotiates the headline figure while ignoring the components ends up with a nominally low MOQ and an unexpectedly high unit price. A printed grosgrain programme, for example, carries at least five separate quantity floors: the weave minimum (what the loom can run economically in one colour), the dye minimum (what the dyehouse can load into a machine without a disproportionate salt-to-garment ratio), the print minimum (how many metres one plate or one cylinder justifies), the finishing minimum (how much the edge-treatment, cutting or bow-assembly line can process in a single setup), and the packing minimum (how many rolls fit a carton or a master carton at a workable unit count). A supplier who quotes &lsquo;500 metre MOQ&rsquo; may be quoting the weave minimum while the dye minimum is 1,500 metres and the print minimum is 3,000. This is not dishonesty; it is usually imprecision, and it is one of the most common sources of the &lsquo;our supplier promised 500 metres and then quoted 3,000&rsquo; conversation that damages trust between a brand and a mill. The second reason MOQ deserves scrutiny is that it is the single largest driver of unit price at the volumes where most brand-owned programmes actually live. In our experience, the custom ribbon programmes that run best are rarely the very large ones; they are the mid-volume programmes, typically 2,000 to 20,000 metres per year across a small SKU range, where the fixed costs have been amortised but the volume is still small enough that a mill&rsquo;s minimum-order policy dominates the actual economics. A buyer who understands the arithmetic of that middle band can negotiate far better than one who simply asks for a lower MOQ and receives a higher price for the same metres."),

    ("The Five Quantity Floors Inside a Custom Ribbon MOQ",
     "Every custom ribbon MOQ is the maximum of five floors, and the floor that binds is usually not the one a buyer thinks about first. Floor one is the weave floor: the minimum metres the loom can run in a single colour without a shutdown and restart penalty. For wide jacquard or for a colour count above four in a single design, this can be several hundred metres on its own, and it is frequently the least binding constraint. Floor two is the dye floor: dyeing operates in a machine with a fixed chamber volume, and a small dye lot wastes dye, energy and time on the walls and the piping. This is the constraint that most often surprises buyers, particularly for deep saturated colours and for pale shades where a small lot may not hold shade reliably, and it is the reason a ribbon quote for 500 metres in a deep navy may be unavailable while 500 metres in a mid-tone grey is available immediately. Floor three is the print floor: where a design is printed, each colour requires a screen or an engraved cylinder, and that tooling is amortised across the metres it carries. A six-colour print therefore has a print floor roughly six times a single-colour print, and this is the single most common cause of a buyer discovering that adding two colours to a programme doubles the effective minimum. Floor four is the finishing floor: edge treatment, overlocking, tipping, die-cutting, bow-making and set-packing each have a setup, and a finishing order below the line&rsquo;s economic batch either waits for the next scheduled run or carries a premium. Floor five is the packing floor: a master carton holds a fixed number of rolls or a fixed weight, and a fractional carton is either shipped at the buyer&rsquo;s cost or rounded up by the mill. The diagnostic that matters is simply: for any given programme, which of the five floors is highest? A good quotation tells you, because a quotation that states the binding constraint is a quotation that can be negotiated, whereas a quotation that states only a headline MOQ is an invitation to a dispute."),

    ("The Three Variable-Cost Tiers That Dominate Unit Price at Low Volume",
     "When a buyer asks why a 1,000-metre order costs more per metre than a 10,000-metre order, the answer usually lies in three cost tiers that behave differently from each other. The first tier is the amortisable fixed cost: setup charges for dyeing, printing, finishing and packing. These are one-time per colour, per design, per setup, and they distribute across the order. At 1,000 metres a dye setup that costs 180 USD adds 0.18 USD per metre; at 10,000 metres the same setup adds 0.018 USD per metre. This is the arithmetic that makes MOQ negotiation consequential, and it is why a higher MOQ from the mill is often cheaper in total. The second tier is the scale-sensitive variable cost: yarn consumption, dye chemistry consumption, and the labour content that varies with the process route. The third tier is the volume-tiered mill cost: at higher annual volume a mill buys yarn more cheaply, runs longer production campaigns with fewer colour changes, and amortises supervision across more metres. In practice, the first tier dominates below roughly 3,000 metres, the second tier dominates in the middle band, and the third tier becomes visible above roughly 30,000 metres per year. Buyers who negotiate on price per metre alone routinely miss the first tier entirely, because the mill is quoting a blended rate that already includes the amortised setup. The correct negotiation move is to separate the quote into these three tiers on the face of it, so that a buyer can see which portion of the price is fixed and which is scale-driven. A mill that will itemise its quote this way is telling you something important about how it will behave when volume grows."),

    ("Case Folding: The Quiet Cost Nobody Prices Correctly",
     "Ribbon is sold in rolls, but it is bought, shipped, stored and merchandised folded into cases, and the case fold is where a surprising amount of money hides. A case fold is simply the ribbon folded into a fixed shape and count so that it presents correctly on a display hook, lies flat in a gift box, or fits a packaging die. The fold itself costs nothing; what costs money is the imposition &mdash; the work of making every length in the case align exactly with the fold, which means the ribbon must be cut and registered against a repeatable pattern rather than simply spooled. Imposition carries a setup and a per-case operation, and it is why a case-folded ribbon can cost several times what the same ribbon costs on a plain roll. Three rules govern whether case folding is worth paying for. First, only fold if the end use requires it: a ribbon that is sold on a spool for craft or industrial use does not need a case fold, and paying for one is pure waste. Second, fold only to the dimensions the downstream actually uses &mdash; a case fold to 2 metres when the merchandising only displays 60 cm is paying for an imposition that serves no purpose. Third, understand that a fold constrains the run length, and therefore constrains the MOQ: a 30-metre fold means your usable run length is 30 metres, which affects how much you can cut from a roll, how you pack, and how much breakage you will generate in the field. At Smith Ribbon, we quote case folding as a separate line rather than folding it into the metre rate, so the buyer can see exactly what the imposition is costing and decide whether the presentation gain justifies it. This single line-item separation is, in our experience, the most frequently requested change to a ribbon quotation, and it is usually because the buyer did not realise that folding was being charged at all."),

    ("Colour Development Cost and How to Avoid Paying It Twice",
     "Colour development &mdash; the work of getting a specified shade to match a standard, and the dye trials behind it &mdash; is one of the most frequently underestimated line items in a first ribbon order, and it is the one most often paid twice. The double payment happens because the buyer treats the first colour as a trial and the second as production, without noticing that the second requires the same trials again if the dye recipe was not recorded and locked. The remedy is procedural rather than financial: require that every colour approval produce a written dye recipe with the shade standard, the substrate, the dye lot family, the process conditions and the measured Delta-E, and require that this recipe be retained and referenced on every subsequent order of the same colour. When the recipe exists, a reorder in the same shade on the same substrate is a straight production run with no trial cost. When it does not, the reorder carries the full development cost again even though the buyer believes the colour is already approved. A second double-payment pattern occurs across supplier changes: a brand that moves a programme to a new mill re-develops every colour, which is unavoidable but should be budgeted explicitly as a transition cost rather than discovered as a surprise in the first quotation from the new supplier. Third, the trial cost scales with the number of colour attempts, not with the order size, which is precisely why trials must be charged and tracked per attempt. Buyers who insist on a fixed colour-development fee regardless of how many attempts are needed end up either paying for attempts they did not need, or having the mill absorb the risk and under-invest in getting it right. The fairest structure, and the one we use, is a per-trial development charge with the first approved shade recharged against the production order."),

    ("Structuring a Ramp: From 500 Metres to a Multi-SKU Programme",
     "The most effective ribbon programmes we work with were not launched at full volume; they were launched as a deliberate ramp, and the ramp was designed rather than improvised. The first stage is the validation run: 500 to 1,000 metres of a single SKU, used to confirm colour, construction, print registration and finishing on real production equipment. Its purpose is not to supply the market; it is to convert a specification into a physical article the brand can sign off on. The second stage is the pilot run: 3,000 to 8,000 metres, often two or three SKUs sharing a colour, which begins to amortise the dye and print setup and produces enough stock for a season or a test in retail. The third stage is the programme run: the annual volume across the SKU range, negotiated in advance with the mill so that capacity and price are both secured before the demand season begins. The value of designing the ramp is that it lets each stage answer a specific question at the lowest possible cost. The validation run answers &lsquo;is this the right product?&rsquo;; the pilot answers &lsquo;does this hold up in volume and in market?&rsquo;; the programme answers &lsquo;is the supply relationship stable and the price right?&rsquo;. A buyer who jumps straight to stage three with an unvalidated colour will pay development costs, receive a first lot that does not match expectation, and often have to re-run, which costs more than the ramp would have. The second reason to design the ramp deliberately is that it preserves negotiating leverage: a brand that comes back for stage two with a smaller order than promised is negotiating from a position the mill did not price for, whereas a brand that shows a clear volume trajectory is negotiating from a position the mill is already planning around."),

    ("The MOQ Negotiation: Five Moves That Work on Ribbon",
     "MOQ negotiation on custom ribbon rewards preparation and punishes pressure. The first move that works is to ask for the binding constraint rather than the headline number. A request framed as &lsquo;what is the highest quantity floor across your five steps for this specific colour, print and fold specification?&rsquo; produces a technically useful answer, and it also implicitly acknowledges that a lower MOQ might come from changing something real &mdash; a lighter colour, one fewer print colour, no case fold, a standard width from stock rather than a custom weave. The second move is to separate the quote into fixed and variable tiers, because a mill that has itemised its quote is far more open to discussing the amortised portion than one quoting a single blended rate. The third move is to consolidate the order rather than split it: multiple colours of the same construction, ordered together and shipped together, frequently let the mill run a longer single-colour campaign and pass the saving back. The fourth move is to accept a higher MOQ in exchange for a lower unit price or a capacity reservation, which is frequently the correct trade for a brand with a genuine volume forecast and the wrong trade for a brand with an optimistic one. The fifth move is to time the order to the mill&rsquo;s campaign calendar: a colour that fits into a scheduled dye run costs meaningfully less than the same colour placed as an emergency order between campaigns. The move that does not work is simply asking for a lower MOQ without changing anything else, because the mill cannot reduce the binding floor without taking the loss somewhere else, and a quote built on an unfunded concession tends to unwind at the point where it costs the mill money."),

    ("What a Good Ribbon Quotation Should Contain",
     "The single most useful diagnostic for a brand buyer is not the price per metre; it is whether the quotation is legible. A quotation a brand can act on states, at minimum, the material and construction with a specific substrate and width, the exact quantity ordered and the quantity available as a reorder increment, the minimum order quantity and which production step it binds, the colour standard and the Delta-E tolerance with the measurement method named, the print or decoration setup broken out separately from the metre rate, the case-fold or finishing charge as a separate line, the packing configuration and the roll count per carton, the production lead time and whether it is counted from artwork approval or from deposit, the price break table showing what the metre rate becomes at higher volumes, the Incoterm and the port, the payment terms, and the production capacity reservation window for peak season. When a quotation contains those elements, the buyer can model the real landed cost, plan the ramp honestly and negotiate the specific lines that matter. When it does not, the buyer is comparing blended numbers that were never constructed to be comparable, and the cheapest-looking quotation is frequently the one that omits the most. Since 2004, Smith Ribbon has supplied brand owners across 50+ countries with factory-direct custom ribbon, and the itemised quotation format described here is the standard we issue for OEM enquiries, precisely because a legible quote is the beginning of a defensible sourcing decision rather than the end of one."),

    ("How to Compare Two Custom Ribbon Quotes Without Being Misled",
     "Comparing two ribbon quotations is straightforward when both are itemised and close to impossible when they are not. The method that works is to reconstruct a like-for-like cost at a target volume. Step one: choose the volume you actually intend to run, not the volume at which each supplier quoted its best rate. Step two: for each quote, build the full cost at that volume &mdash; metres multiplied by rate, plus every setup, plus decoration, plus folding, plus packing, plus inland freight to your port or door, plus duty, plus the cost of the samples and any development charges. Step three: add the cost of things that are not in the quotation but will appear later &mdash; a second colourway, a new size, a reprinted design, a compliance certificate that must be renewed. Step four: adjust for the terms, because a 30 percent deposit at FOB is not the same as 30 days after shipment, and a 60-day payment term has a real value that belongs in the comparison. Step five, and most often skipped, adjust for the risk profile: a mill quoting 12 percent below another with a single-colour weave capacity and no certification history carries a different risk from a mill quoting 12 percent above with a broader capacity base and current BSCI and OEKO-TEX renewals, and that difference belongs in the model as an expected-cost line, not as a footnote. When buyers run this exercise properly, they frequently find that the headline gap narrows or reverses, and they also find that the number of variables they are actually negotiating is far smaller than they feared."),

    ("Mill-Side Economics: Why a Factory Sets the MOQ Where It Does",
     "Understanding the mill&rsquo;s constraint is not background information; it is the leverage a buyer needs to negotiate intelligently. A ribbon mill runs weaving, dyeing, printing and finishing as a sequence of batch processes with fixed setups and a real cost for every changeover. A dye house that runs a 300-metre batch and a 5,000-metre batch does not simply multiply the chemical cost by 17.5; it incurs an additional fixed cost for filling, heating, rinsing, draining and cleaning the machine, and the total cost per metre at 300 metres is materially higher because that fixed cost has almost no volume to spread across. The same applies to printing, where each screen or cylinder has a preparation and a test run, and to finishing, where a changeover consumes setup and often the tail of the previous batch. Set-up discipline is therefore the reason MOQ floors exist at all, and it is a sound operational practice rather than an arbitrary sales tactic. The corollary is that a buyer who can help the mill reduce changeover frequency gets a better price, which is why consolidated colours, agreed colour families within a season, and consolidated shipping windows all carry real value in a negotiation. It also explains why a mill may accept a lower MOQ on a colour that fits an already-scheduled campaign than on a colour that does not: the first one costs the mill very little incremental time, while the second one displaces other work."),

    ("The Cost of Getting MOQ Wrong",
     "MOQ errors are not always visible at order time, and the visible ones are rarely the expensive ones. The obvious error is paying for a development charge twice, or paying to move from 3,000 metres to 1,000 metres mid-programme and losing the amortisation. The less obvious errors are subtler. A first order placed at 1,000 metres when the annual plan was 12,000 means the brand has committed capital twelve months early, and if the programme is replaced on shelf in the meantime, that capital is written down against a style that no longer sells. A first order placed too high &mdash; 15,000 metres when the realistic first-season demand was 4,000 &mdash; ties up working capital in a single colourway that then has to be discounted to clear, and discounted ribbon is usually sold at a price that recovers the cash but not the margin, and occasionally not even the cash. A programme with too many colours at too many quantities is worse still, because it multiplies the setup amortisation across a portfolio that individually cannot carry it. The figure we use internally for first-order working capital exposure on a typical mid-volume programme is 8,000 to 45,000 USD, and the majority of that exposure is created in the first purchase order rather than in the annual plan. The corrective habit is unglamorous and effective: write the ramp before the first order, set the reorder increment at the point where it is genuinely useful, and treat any change to the volume plan as a change to the cost plan, not just a change to the order quantity."),

    ("A 90-Day MOQ and Order-Lot Plan for a Brand Owner",
     "A workable 90-day plan compresses the decisions that determine whether the first order is well made. Days 1 to 15: specification. Define the construction, the width, the substrate, the quantity forecast by quarter and by SKU, the target case-fold and packaging, the colour standard and tolerance, and the decoration. The forecast must be committed to in writing at this stage, because it is what will later justify a consolidated order. Days 16 to 30: quotation and quote normalisation. Obtain itemised quotations from two to three mills using the same specification document, then normalise them into a like-for-like comparison at a common volume as described above. Record which constraint binds at each mill and what would change it. Days 31 to 45: sample and validation. Run the sample process to a production-representative sample, and validate the case fold on actual downstream equipment if the buyer has it. Confirm the packing configuration by physically counting what arrives in the first carton rather than by trusting the specification. Days 46 to 60: order structuring. Place the validation order at the ramp stage one quantity, agree the price-break table in writing, agree the reorder increment, and confirm the capacity reservation for the programme run before the peak-season booking window closes. Days 61 to 90: programme run booking. Convert the validated SKU set into the season quantity, book capacity, and lock the colour recipe so that a later reorder does not re-trigger development charges. The 90-day plan is not administratively heavy; it is a short sequence of decisions with named owners, and its real value is that it forces the volume forecast to be made before the first order rather than discovered after it."),
]

FAQ = [
    ("What is a typical MOQ for custom printed ribbon from a Chinese mill?",
     "For custom woven and printed ribbon, a realistic first-order MOQ sits between 500 and 3,000 metres per colourway, and the number that binds depends on the specification. Solid-colour stock-width ribbon can often be produced at 500 metres per colour, because it uses an existing weave and a routine dye lot. Printed designs with two to six colours typically sit between 1,500 and 3,000 metres, because the print setup and the number of screens raise the floor. Case-folded and specially finished programmes often move higher still, and deep saturated shades sometimes carry a higher dye floor than mid-tones. The most useful thing a buyer can do is ask a supplier to state which production step binds the minimum for your specific specification, because a headline MOQ quoted without that context is not usable for planning. At Smith Ribbon, we quote a 500-metre first run on standard constructions and 1,000 metres on custom widths, and we state the binding step explicitly on every quotation."),
    ("Why is a small order sometimes more expensive per metre than a large one?",
     "Because the fixed setup costs are the same and there are fewer metres to spread them across. A dye setup, a print setup, a finishing setup and a packing setup all cost roughly the same whether the run is 1,000 metres or 10,000 metres, so the fixed component per metre falls by roughly a factor of ten across that range. This is why a lower MOQ is often the more expensive option in total: taking 1,000 metres instead of 3,000 metres at a quoted price may avoid a minimum-order constraint but will usually deliver a materially higher unit cost, because the same setup is now carrying a tenth of the volume. The correct question is therefore not &lsquo;can I buy fewer metres?&rsquo; but &lsquo;what is the total cost at the volume I actually intend to run?&rsquo;. A quotation that shows the fixed and variable tiers separately makes this calculation straightforward, and any competent mill will provide it."),
    ("Is it worth paying a higher MOQ to get a lower unit price?",
     "It is frequently worth it, but only when the volume is real rather than aspirational. If your genuine, committed annual demand is 12,000 metres across a stable SKU range, taking 3,000 metres per order at a lower rate usually beats taking 1,000 metres at a higher rate, because the setup amortisation is dramatically better and the working capital cost of the larger order is often lower than the savings. If the 12,000 metres is a forecast you have not tested, the same decision is dangerous: a larger commitment based on an unvalidated forecast ties up capital in a colourway that may be replaced, and the cost of discounting clearance stock can exceed the per-metre saving several times over. The safe approach is to structure the ramp, place the first order at the validation or pilot stage, and negotiate the programme-run volume only after the pilot has demonstrated demand. Then, and only then, take the larger quantity at the better rate with a genuine basis behind it."),
    ("What does case folding add to the cost of custom ribbon?",
     "Case folding adds a setup and a per-case operation, and because it requires the ribbon to be cut and registered against a repeatable fold pattern rather than simply spooled, it can increase the unit cost of the programme noticeably &mdash; often by a double-digit percentage on the decorated article. It is worth paying when the downstream use genuinely requires it, because a ribbon that presents badly on a hook or in a gift box loses value regardless of how well it is made. It is not worth paying when the ribbon will be sold on a spool, cut by the customer, or used in a process where the fold is discarded. The most useful discipline is to have the fold quoted as a separate line so you can see its cost, and then to confirm that the fold length matches what the merchandising actually displays &mdash; a 30-metre fold for a product displayed at 60 cm is paying for imposition you do not need. We recommend physically checking the fold on a finished case before it goes to production."),
    ("How do I avoid paying colour development charges again on a reorder?",
     "Make sure the first colour approval produces a written, retained dye recipe, and reference it on every subsequent order. The recipe should record the shade standard and tolerance, the substrate, the dye lot family, the process conditions and the measured Delta-E, together with the approval record. With that in place, a reorder in the same shade on the same substrate is a production run with no trial cost. Without it, the mill has to re-run the trials to reproduce a shade it was never instructed to record, and the cost of those trials is real. A second and harder-to-avoid case is a supplier change: moving a programme to a new mill requires re-development of every colour, which is unavoidable, so it should be budgeted explicitly as a transition cost rather than discovered in the first quotation. A third case is a substrate change at the same nominal colour &mdash; the same shade number on a different weave or fibre behaves differently and needs its own approval. The protection in all three cases is procedural, and it costs nothing to set up."),
    ("Should I negotiate the MOQ down, or negotiate the price down?",
     "Negotiate whichever is genuinely available to the mill, and understand that a low MOQ at a high unit price may be the worse commercial outcome. The mill can only lower the binding floor by reducing something real: fewer colours, no case fold, a standard width from stock rather than a custom weave, a lighter or less demanding shade, accepting a standard roll length, or scheduling the order into an existing campaign so the incremental cost is small. So the more productive conversation is usually not &lsquo;reduce your minimum&rsquo; but &lsquo;what would have to change in my specification for the minimum to fall, and what does that change cost me elsewhere?&rsquo;. Meanwhile, the price is more often negotiable through the price-break table, through consolidation of colours and shipments, through timing the order into a scheduled campaign, and through the terms of the agreement. Buyers who negotiate both in parallel &mdash; specification flexibility on one side, volume commitment on the other &mdash; consistently reach better outcomes than those who push on one dimension only."),
    ("How much working capital should I reserve for a first custom ribbon order?",
     "For a typical mid-volume programme &mdash; say 3,000 to 15,000 metres across a small SKU range in a launch year &mdash; first-order working capital exposure generally lands between 8,000 and 45,000 USD, depending heavily on the number of colours, the decoration complexity and the fold requirement. The exposure is created in the first purchase order rather than in the annual plan, which is why it surprises buyers. Two habits reduce it substantially. First, agree the price-break table in writing at the quotation stage, so the ramp quantities are already priced at their true rate rather than being discovered at reorder. Second, fix the reorder increment at a level that serves the replenishment pattern rather than at the mill&rsquo;s convenience; a smaller increment gives working-capital flexibility at the cost of a slightly worse rate, and for a brand whose demand is still seasonal and uncertain, that trade is usually worth making deliberately. Where a brand can split a programme into two deliveries against a single production order, the second delivery can often be invoiced on shipment, which preserves the price break without front-loading the cash."),
]

METRICS = [
    ("First-order landed cost reduction from a designed ramp", "18-34%"),
    ("MOQ floors identified per programme", "1 -> all 5 mapped"),
    ("Colour development charges paid twice", "eliminated by recipe lock"),
    ("Fixed vs variable cost visibility in quotations", "itemised at quote stage"),
    ("First-order working capital exposure", "8,000-45,000 USD typical"),
    ("Reorder lead time from a locked dye recipe", "no trial round required"),
]

AUTHOR_BULLETS = (
    "Smith Ribbon has supplied OEM custom ribbon to brand owners across 50+ countries since 2004, with factory-direct pricing from our own 15,000 m&sup2; plant",
    "Weaving, dyeing, printing and finishing under one roof &mdash; 200+ employees, 100,000 m daily capacity &mdash; so MOQ floors can be quoted against a real production route rather than a policy sheet",
    "Itemised OEM quotations separating weave, dye, print, finishing and folding, with a written price-break table and reorder increment",
    "Written dye-recipe retention per approved colourway so reorder colour development is not charged twice",
    "OEKO-TEX&reg;, FSC&reg;, BSCI, SEDEX, SMETA and ISO 9001 certified with current-year renewals, plus 500 m first-run MOQ on standard constructions",
)

STYLE_CSS = """
        :root { --primary: #6a1b9a; --secondary: #8e24aa; --dark: #2c1a33; --light: #f8f5fb; --text: #2d2b2e; --muted: #6b6570; --accent: #c62828; }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.8; color: var(--text); background: var(--light); }
        a { color: var(--primary); text-decoration: none; }
        a:hover { text-decoration: underline; }
        nav { background: white; padding: 1rem 2rem; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 10px rgba(0,0,0,0.08); position: sticky; top: 0; z-index: 100; }
        .logo { font-size: 1.6rem; font-weight: bold; color: var(--primary); }
        .container { max-width: 960px; margin: 0 auto; padding: 2rem 1.5rem; background: white; }
        h1 { font-size: 2.1rem; color: var(--dark); margin: 1.5rem 0 1rem; line-height: 1.3; }
        h2 { font-size: 1.4rem; color: var(--dark); margin: 2rem 0 0.8rem; padding-top: 1rem; border-top: 2px solid var(--light); }
        h3 { font-size: 1.1rem; color: var(--dark); margin: 1rem 0 0.4rem; }
        p { margin-bottom: 1rem; font-size: 1.05rem; }
        .meta { color: var(--muted); font-size: 0.9rem; margin-bottom: 1rem; }
        .toc { background: var(--light); padding: 1.2rem; border-radius: 8px; margin: 1.5rem 0; }
        .toc h3 { margin-bottom: 0.6rem; color: var(--dark); }
        .toc ol { padding-left: 1.4rem; }
        .toc li { margin-bottom: 0.3rem; font-size: 0.95rem; }
        .kpi-box { background: #f7f0fb; border-left: 4px solid var(--primary); padding: 1rem 1.2rem; border-radius: 6px; margin: 1.5rem 0; }
        .kpi-box ul { margin: 0.6rem 0 0 1.1rem; padding: 0; }
        .faq h3 { color: var(--primary); }
        footer { background: var(--dark); color: white; padding: 2rem; text-align: center; margin-top: 3rem; }
        footer a { color: #fff; margin: 0 8px; }
"""


def faq_block_html(items):
    out = ['        <h2>Frequently Asked Questions</h2>', '        <div class="faq">']
    for q, a in items:
        out.append(f'            <h3>{html_mod.escape(q)}</h3>')
        out.append(f'            <p>{a}</p>')
    out.append('        </div>')
    return "\n".join(out)


def kpi_block_html(metrics):
    items = "".join(
        f"<li><strong>{html_mod.escape(k)}</strong> &mdash; {html_mod.escape(v)}</li>"
        for k, v in metrics
    )
    return f'<div class="kpi-box"><h2>Quantified Outcomes</h2><ul>{items}</ul></div>'


def build_html():
    url = f"https://{SITE}/blog-{SLUG}.html"
    word_count = sum(len(p.split()) + len(h.split()) for h, p in SECTIONS) + 240
    plain_title = html_mod.unescape(TITLE)
    article_schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": plain_title,
        "description": DESC,
        "author": {"@type": "Organization", "name": AUTHOR_NAME, "url": AUTHOR_URL},
        "publisher": {"@type": "Organization", "name": AUTHOR_NAME, "url": SITE},
        "datePublished": DATE_ISO.split("T")[0],
        "dateModified": DATE_ISO.split("T")[0],
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "keywords": KEYWORDS,
    }
    blog_schema = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": plain_title,
        "description": DESC,
        "image": LOGO_URL,
        "author": {"@type": "Organization", "name": AUTHOR_NAME, "url": AUTHOR_URL},
        "publisher": {
            "@type": "Organization",
            "name": AUTHOR_NAME,
            "logo": {"@type": "ImageObject", "url": LOGO_URL},
        },
        "datePublished": DATE_ISO.split("T")[0],
        "dateModified": DATE_ISO.split("T")[0],
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "keywords": KEYWORDS,
        "articleSection": "B2B Sourcing",
        "wordCount": word_count,
    }
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": html_mod.escape(q),
                "acceptedAnswer": {"@type": "Answer", "text": html_mod.escape(a)},
            }
            for q, a in FAQ
        ],
    }
    sf = json.dumps(faq_schema, indent=4, ensure_ascii=False)
    sa = json.dumps(article_schema, indent=4, ensure_ascii=False)
    sb = json.dumps(blog_schema, indent=4, ensure_ascii=False)
    toc_html = "\n".join(f"                <li>{html_mod.escape(h)}</li>" for h, _ in SECTIONS)
    body_parts = []
    for h, p in SECTIONS:
        body_parts.append(f'        <h2>{html_mod.escape(h)}</h2>')
        body_parts.append(f'        <p>{p}</p>')
    body = "\n\n".join(body_parts)
    faq_html = faq_block_html(FAQ)
    metrics_html = kpi_block_html(METRICS)
    bullets_html = "".join(f"<li>{b}</li>" for b in AUTHOR_BULLETS)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{TITLE} | Smith Ribbon</title>
    <meta name="description" content="{html_mod.escape(DESC)}">
    <meta name="keywords" content="{html_mod.escape(KEYWORDS)}">
    <meta name="robots" content="index, follow">
    <meta name="geo.region" content="CN-35" />
    <meta name="geo.placename" content="Xiamen, Fujian, China" />
    <link rel="canonical" href="{url}">
    <meta property="og:title" content="{TITLE}">
    <meta property="og:description" content="{html_mod.escape(DESC)}">
    <meta property="og:type" content="article">
    <meta property="og:image" content="{LOGO_URL}">
    <meta property="og:site_name" content="Smith Ribbon">
    <meta property="og:url" content="{url}">
    <meta property="og:locale" content="en_US">
    <meta property="article:published_time" content="{DATE_ISO}">
    <meta property="article:modified_time" content="{DATE_ISO}">
    <meta property="article:author" content="{AUTHOR_NAME}">
    <meta property="article:section" content="B2B Sourcing">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{TITLE}">
    <meta name="twitter:description" content="{html_mod.escape(DESC)}">
    <meta name="twitter:image" content="{LOGO_URL}">
    <script type="application/ld+json">
{sa}
    </script>
    <script type="application/ld+json">
{sb}
    </script>
    <script type="application/ld+json">
{sf}
    </script>
    <style>{STYLE_CSS}</style>
</head>
<body>
    <nav>
        <div class="logo">Smith Ribbon</div>
        <div><a href="https://ribbonbow123.com/">Home</a> | <a href="https://ribbonbow123.com/blog.html">Blog</a> | <a href="https://ribbonbow123.com/about.html">About</a></div>
    </nav>
    <div class="container">
        <h1>{TITLE}</h1>
        <p class="meta">By {html_mod.escape(AUTHOR_NAME)} | Published {html_mod.escape(DATE_DISPLAY)} | Category: B2B Sourcing | Article #{NUM}</p>
        <div class="toc">
            <h3>Table of Contents</h3>
            <ol>
{toc_html}
            </ol>
        </div>

{body}

{metrics_html}

{faq_html}

        <h2>Why Smith Ribbon for OEM custom ribbon programmes</h2>
        <p>Smith Ribbon has supplied OEM and ODM custom woven and printed ribbon, satin, grosgrain, velvet, organza, RPET and decorative trims since 2004. Our 15,000 m&sup2; plant with 200+ employees, 100,000 metres of daily capacity, and certifications spanning OEKO-TEX&reg;, FSC&reg;, BSCI, SEDEX, SMETA and ISO 9001 lets us quote MOQ floors against a real production route and hold capacity for the ramp.</p>
        <ul>
            {bullets_html}
        </ul>
        <p>To put a custom ribbon programme in motion, request a MOQ and order-lot diagnostic and we will return a structured proposal within 5 business days.</p>
    </div>
    <footer>
        <p>&copy; 2026 Smith Ribbon Co., Ltd. (Xiamen Meisida Decoration Co., Ltd.) | OEM &amp; ODM Custom Ribbon Manufacturer</p>
        <p>
            <a href="https://ribbonbow123.com/">Home</a>
            <a href="https://ribbonbow123.com/blog.html">Blog</a>
            <a href="https://ribbonbow123.com/about.html">About</a>
            <a href="mailto:xmmsd@126.com">Contact</a>
        </p>
    </footer>
</body>
</html>
"""


def main():
    html_out = build_html()
    Path(f"{DIR}/blog-{SLUG}.html").write_text(html_out, encoding="utf-8")
    print(f"Wrote blog-{SLUG}.html ({len(html_out):,} bytes)")

    sm_path = Path(f"{DIR}/sitemap.xml")
    sm = sm_path.read_text(encoding="utf-8")
    url = f"https://{SITE}/blog-{SLUG}.html"
    if url in sm:
        print("[skip] sitemap already has article 293")
    else:
        entry = (
            "  <url>\n"
            f"    <loc>{url}</loc>\n"
            f"    <lastmod>{DATE}</lastmod>\n"
            "    <changefreq>monthly</changefreq>\n"
            "    <priority>0.7</priority>\n"
            "  </url>\n"
        )
        idx = sm.rfind("</urlset>")
        if idx == -1:
            raise SystemExit("</urlset> not found in sitemap.xml")
        sm_path.write_text(sm[:idx] + entry + sm[idx:], encoding="utf-8")
        print("[ok] sitemap.xml updated with article 293")


if __name__ == "__main__":
    main()
