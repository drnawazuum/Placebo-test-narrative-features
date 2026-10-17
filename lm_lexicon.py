"""
Finance-domain sentiment lexicon, in the spirit of Loughran & McDonald (2011).

Why a hand-built list instead of pip-installing the official LM Master
Dictionary: this sandbox has no live internet access (confirmed — pypi.org,
GitHub raw, Kaggle, HuggingFace, FRED and federalreserve.gov all refused the
connection), so the official dictionary CSV cannot be fetched here. This list
reconstructs the most frequently-cited LM "Negative" and "Positive" categories
from memory, trimmed to terms that actually recur in central-bank
communication (press statements / FOMC statements), so it is usable but not
a byte-for-byte substitute for the real file.

>>> If you have the official Loughran-McDonald Master Dictionary CSV
>>> (sentiment-analysis word lists from https://sraf.nd.edu), upload it and
>>> this module will be swapped for the exact published list — call
>>> load_official_lm(path) instead of using NEGATIVE/POSITIVE below, so the
>>> ECB and FOMC scores are computed with an identical, citable dictionary.

Scoring convention (kept IDENTICAL to the existing ECB analysis in
ecb_sentiment_scores.csv, reverse-engineered from that file):
    net_sentiment = (negative_count - positive_count) / num_words
  i.e. higher net_sentiment = more negative/pessimistic tone.
"""
import re

NEGATIVE = {
    "adverse","adversely","against","against","aggravate","aggravated","anomaly",
    "anxiety","anxious","bad","bankrupt","bankruptcy","barrier","breach","burden",
    "burdensome","catastrophic","caution","cautious","cautiously","challenge",
    "challenges","challenging","collapse","complicate","complication","concern",
    "concerned","concerns","constrain","constrained","constraint","constraints",
    "contraction","contagion","crisis","critical","damage","danger","dangerous",
    "decline","declined","declines","declining","deficiency","deficient","deficit",
    "deflation","deflationary","delay","delayed","deteriorate","deteriorated",
    "deterioration","difficult","difficulties","difficulty","disappointing",
    "disrupt","disrupted","disruption","disruptions","distress","disturbance",
    "divergence","downgrade","downside","downturn","drag","drop","dropped",
    "erode","eroded","erosion","exposure","fail","failed","failure","fear",
    "fears","fragile","fragility","friction","frictions","hamper","hampered",
    "harm","harmful","hazard","headwind","headwinds","hesitant","imbalance",
    "imbalances","impair","impaired","impairment","inadequate","instability",
    "insufficient","interrupt","interruption","jeopardize","lack","limitation",
    "limitations","loss","losses","negative","negatively","obstacle","pandemic",
    "panic","penalty","pessimism","plunge","pressure","pressures","problem",
    "problems","recession","recessionary","reduce","reduced","reduction",
    "restrict","restricted","restriction","restrictive","risk","risks","risky",
    "severe","severely","shock","shocks","shortage","shortfall","slow","slowdown",
    "slower","slowing","sluggish","slump","strain","stress","stressed","struggle",
    "stumble","subdued","suffer","suspend","suspended","tension","tensions",
    "threat","threaten","threatening","tighten","tightening","trouble","turmoil",
    "uncertain","uncertainty","undermine","undermined","unemployment","unfavorable",
    "unprecedented","unsettled","unstable","unsustainable","vulnerability",
    "vulnerable","volatile","volatility","weak","weaken","weakened","weakening",
    "weakness","worsen","worsened","worsening","worry","worrying",
}

POSITIVE = {
    "accelerate","accelerated","accommodative","achieve","achieved","advance",
    "advances","advancing","benefit","benefits","boost","boosted","buoyant",
    "confidence","confident","durable","durably","ease","eased","easing",
    "effective","efficiency","efficient","encouraging","expand","expanded",
    "expansion","favorable","favourable","firm","firming","gain","gains",
    "good","growth","healthy","improve","improved","improvement","improving",
    "increase","increased","increasing","momentum","opportunity","optimism",
    "optimistic","outperform","positive","positively","progress","prosper",
    "prosperity","rebound","recover","recovered","recovery","resilience",
    "resilient","restore","restored","robust","solid","sound","stabilize",
    "stabilized","stabilizing","stability","stable","strength","strengthen",
    "strengthened","strengthening","strong","stronger","success","successful",
    "sufficient","supportive","sustain","sustainable","sustained","upbeat",
    "upside","upturn",
}

_WORD_RE = re.compile(r"[A-Za-z']+")


def score_text(text: str) -> dict:
    """Score raw document text. Returns counts in the same schema as
    ecb_sentiment_scores.csv: num_words, negative_count, positive_count,
    net_sentiment = (negative_count - positive_count) / num_words."""
    words = [w.lower() for w in _WORD_RE.findall(text)]
    n = len(words)
    neg = sum(1 for w in words if w in NEGATIVE)
    pos = sum(1 for w in words if w in POSITIVE)
    net = (neg - pos) / n if n else 0.0
    return {
        "num_words": n,
        "negative_count": neg,
        "positive_count": pos,
        "net_sentiment": round(net, 6),
    }


def load_official_lm(master_dict_csv_path: str):
    """If the user uploads the real Loughran-McDonald Master Dictionary CSV
    (columns include 'Word', 'Negative', 'Positive' as nonzero-year flags),
    call this to replace NEGATIVE/POSITIVE above with the exact published
    sets, so ECB and FOMC scores can be recomputed on an identical,
    citable dictionary instead of this reconstruction."""
    import csv
    negative, positive = set(), set()
    with open(master_dict_csv_path, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            word = row.get("Word", "").strip().lower()
            if not word:
                continue
            if int(row.get("Negative", 0) or 0) > 0:
                negative.add(word)
            if int(row.get("Positive", 0) or 0) > 0:
                positive.add(word)
    return negative, positive
