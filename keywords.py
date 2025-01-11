class HnKeywords:
    startup_founder_issues = [
        "getting first customers",
        "go to market strategy",
        "idea validation",
        "startup pain points",
        "building an MVP",
        "launching a startup",
        "startup mistakes",
    ]

    specific_tools_methodologies = [
        "surveymonkey",
        "google forms",
        "Typeform",
        "qualitative analysis software",
        "Nvivo",
        "dovetail",
    ]

    critiques_of_market_research = [
        "problems with market research",
        "market research is broken",
        "useless customer interviews",
        "market research bias",
        "ineffective feedback",
        "bad user research",
        "biased user feedback",
        "flaws in market analysis",
        "time consuming research",
        "expensive market research",
        "outdated market research",
    ]

    jobs_to_be_done = [
        "Jobs to be done framework",
        "understanding the job",
        "what job does the customer hire your product for",
        "JTBD implementation",
        "job to be done case study",
        "JTBD examples",
    ]

    market_research_terms = [
        "market research",
        "market analysis",
        "competitive analysis",
        "customer segmentation",
        "market trends",
        "industry research",
        "target market analysis",
        "understanding market size",
        "market sizing",
        "market opportunity",
        "identifying market needs",
        "secondary research",
        "primary research",
        "market surveys",
        "focus groups",
        "competitive landscape",
        "analyzing the market",
        "understanding our target market",
        "identifying our competitors",
        "market trends and insights",
        "potential market size",
        "market research reports",
        "market data analysis",
        "industry analysis",
        "understanding user behavior",
        "understanding customer behavior",
        "market research findings",
        "market gaps",
        "identifying business opportunities",
        "market opportunity assessment",
        "analyzing competitor strengths and weaknesses",
        "market segmentation strategy",
        "customer demographics analysis",
        "understanding market dynamics",
        "investigating the competitive environment",
        "examining market data",
        "looking at market trends",
        "competitive benchmarking",
    ]

    overlapping_terms = [
        "user research",
        "customer feedback",
        "user feedback",
        "product feedback",
        "feedback analysis",
        "customer insights",
        "user insights",
        "needs assessment",
        "problem validation",
        "testing assumptions",
        "understanding customer problems",
        "understanding user problems",
        "iterative feedback process",
        "collecting user stories",
        "collecting customer stories",
        "validating our approach",
        "feedback on our idea",
        "validating the problem",
        "product discovery",
        "understanding the customer",
        "understanding the user",
        "pain points",
        "jobs to be done",
        "JTBD",
        "early feedback",
        "customer preferences",
        "user preferences",
    ]

    customer_interviews_terms = [
        "customer interview",
        "user interview",
        "customer feedback session",
        "user feedback session",
        "one-on-one interview",
        "1:1 interview",
        "talking to customers",
        "talking to users",
        "speaking with customers",
        "speaking with users",
        "customer conversations",
        "user conversations",
        "customer dialogue",
        "user dialogue",
        "interviewing potential customers",
        "interviewing potential users",
        "conducting customer interviews",
        "conducting user interviews",
        "gathering user feedback",
        "collecting customer feedback",
        "qualitative interviews",
        "customer discovery",
        "user discovery",
        "understanding user needs",
        "understanding customer needs",
        "voice of the customer",
        "VoC feedback",
        "in-person interviews",
        "remote interviews",
        "virtual interviews",
        "interview transcripts",
        "analyzing customer feedback",
        "analyzing user feedback",
        "customer interview analysis",
        "user interview analysis",
        "customer insight gathering",
        "user insight gathering",
        "what did customers say",
        "what did users say",
        "feedback from customers",
        "feedback from users",
        "customer pain points",
        "user pain points",
        "listening to customers",
        "listening to users",
        "interviewing process",
        "asking about user needs",
        "asking about customer needs",
        "customer experience research",
        "user experience research",
        "deep dive interview",
        "customer stories",
        "user research study",
        "customer research study",
        "exploring customer needs",
        "exploring user needs",
    ]

    product_validation_terms = [
        "product validation",
        "validating product idea",
        "testing product fit",
        "product market fit",
        "PMF",
        "validating assumptions",
        "hypothesis testing",
        "idea validation",
        "minimum viable product",
        "concept testing",
        "feature validation",
        "usability testing",
        "early product feedback",
        "initial product feedback",
        "iterating on product",
        "is this product viable",
        "validating market demand",
        "finding product-market fit",
        "early user testing",
        "testing assumptions about customers",
        "testing assumptions about users",
        "validating value proposition",
        "product feedback loop",
        "testing the hypothesis",
        "refining our product based on feedback",
        "customer feedback on product",
        "user feedback on product",
        "validating our solution",
        "testing product usability",
        "is this product useful",
        "user acceptance testing",
        "collecting feedback on the prototype",
        "evaluating product performance",
        "testing product market hypothesis",
    ]

    def as_dict():
        # convert to dictionary
        result = {}
        for name, val in HnKeywords.__dict__.items():
            if isinstance(val, list):
                result[name] = val
        return result
