# Brainstorm: Crescent Bakery Analytical Questions

## Prompt used

Role: Act as a senior data analyst helping me scope an analytical project for
a small fictional bakery client.

Task: Brainstorm analytical questions I should consider asking of the dataset
described below. I'm at the Define stage of the analytics lifecycle and need
a candidate list of questions before I start writing any code.

Context: The dataset is for Crescent Bakery, a fictional regional bakery.
50 rows, one row per customer. Columns:

- customer_id: string, unique identifier per customer (nominal)
- region: categorical, one of {Downtown, North Side, South Side, West End} (nominal)
- first_visit_year: integer year between 2018 and 2025 inclusive (interval)
- satisfaction: integer 1 to 5, customer satisfaction rating (ordinal)
- total_spent_usd: continuous, total dollars the customer has spent (ratio)
- visits_last_year: integer, number of visits in the last year (ratio)

The bakery is interested in understanding customer behavior to inform
marketing and product decisions.

Constraints:
1. Only suggest questions that can be answered from the columns listed above.
   Don't invent additional columns.
2. For each suggested question, identify which columns would be used and
   what statistical method would be appropriate.
3. Make sure the statistical methods you propose are appropriate for the
   data type of each column (mean for ratio, mode for nominal, etc.).

Output Format: A numbered list of 8 to 12 analytical questions. For each:
- The question (one sentence)
- The columns involved
- The recommended statistical or visualization method


## Tool 1: Claude output

Here's a candidate list of analytical questions for the Define stage, scoped strictly to the six columns available.

1. How does total spending differ across regions? Columns: region, total_spent_usd. Method: group by region and compare means/medians (bar chart of mean total_spent_usd by region); one-way ANOVA or Kruskal-Wallis if testing for statistically significant differences.

2. Is there a relationship between visit frequency and total spending? Columns: visits_last_year, total_spent_usd. Method: Pearson (or Spearman, if non-linear) correlation and a scatterplot with a fitted trend line.

3. Does customer satisfaction relate to how much a customer spends? Columns: satisfaction, total_spent_usd. Method: since satisfaction is ordinal, use Spearman rank correlation or compare median total_spent_usd across satisfaction levels with a boxplot.

4. Does satisfaction relate to visit frequency? Columns: satisfaction, visits_last_year. Method: Spearman rank correlation; boxplot of visits_last_year grouped by satisfaction score.

5. What is the distribution of customer satisfaction overall, and which rating is most common? Columns: satisfaction. Method: mode and frequency table (bar chart of counts per rating 1-5), since satisfaction is ordinal, not continuous.

6. Which region has the most customers, and how is the customer base distributed geographically? Columns: region. Method: mode and frequency count (bar chart or pie chart of customer counts by region).

7. Has customer acquisition grown or slowed over time? Columns: first_visit_year. Method: frequency count of customers by first_visit_year (line or bar chart showing new customers per year); note the data only captures first-visit year, not repeat acquisition trends.

8. Do customers acquired in earlier years spend more or visit more than recently acquired customers? Columns: first_visit_year, total_spent_usd, visits_last_year. Method: group by first_visit_year (or by cohort buckets, e.g., pre-2021 vs. post-2021) and compare mean total_spent_usd and mean visits_last_year; visualize with grouped bar charts or scatterplots.

9. Are certain regions associated with higher satisfaction? Columns: region, satisfaction. Method: cross-tabulation (contingency table) of region by satisfaction rating, or compare median satisfaction by region using a boxplot; chi-square test of independence to check for association between two categorical/ordinal variables.

10. What does the overall spread of customer spending look like, and are there high-value outliers? Columns: total_spent_usd. Method: descriptive statistics (mean, median, standard deviation, min/max, quartiles) and a histogram or boxplot to check distribution shape and outliers.

11. How does visit frequency vary by region? Columns: region, visits_last_year. Method: group by region and compare mean/median visits_last_year (boxplot or bar chart); ANOVA/Kruskal-Wallis for significance testing.

12. Can customers be segmented into value tiers based on spending and visit behavior? Columns: total_spent_usd, visits_last_year. Method: scatterplot of total_spent_usd vs. visits_last_year, optionally with simple binning/quantile segmentation (e.g., high-spend/high-frequency vs. low-spend/low-frequency) to identify natural groupings — a lightweight, code-free precursor to later clustering work.

A few scoping notes worth flagging before you move to code: satisfaction is ordinal, so I've paired it with median/mode-based methods and rank correlation rather than means; first_visit_year captures only initial acquisition, not a full visit history, so cohort-based questions (8) are really proxies and should be labeled as such in your final report; and with only 50 rows, tests like ANOVA or chi-square may have limited power, so treat significance results as directional rather than conclusive.

## Tool 2: Chatgpt output

For the **Define stage**, I’d focus on questions that connect directly to Crescent Bakery’s goal of understanding customer behavior for **marketing and product decisions**, while keeping the analysis realistic for a small dataset of 50 customers.

1. **How does customer spending differ across regions?**
   **Columns:** `region`, `total_spent_usd`
   **Method:** Group customers by region and calculate mean and median `total_spent_usd`; visualize with a bar chart or boxplot. If testing whether differences are statistically significant, use one-way ANOVA if assumptions are reasonable or Kruskal–Wallis otherwise.

2. **Is visit frequency associated with how much a customer spends?**
   **Columns:** `visits_last_year`, `total_spent_usd`
   **Method:** Use a scatterplot to visualize the relationship. Calculate Pearson correlation for an approximately linear relationship without major outliers, or Spearman correlation if those assumptions are questionable.

3. **Is customer satisfaction associated with total spending?**
   **Columns:** `satisfaction`, `total_spent_usd`
   **Method:** Because `satisfaction` is ordinal, use Spearman rank correlation. A boxplot of `total_spent_usd` by satisfaction level can also show differences in spending distributions.

4. **Is customer satisfaction associated with visit frequency?**
   **Columns:** `satisfaction`, `visits_last_year`
   **Method:** Use Spearman rank correlation because satisfaction is ordinal. A boxplot of `visits_last_year` grouped by satisfaction rating can help visualize the relationship.

5. **What is the overall distribution of customer satisfaction?**
   **Columns:** `satisfaction`
   **Method:** Calculate frequencies, percentages, median, and mode. Use a bar chart showing the number or percentage of customers at each satisfaction level from 1–5. Avoid relying on the mean because satisfaction is ordinal.

6. **Which regions have the highest and lowest customer satisfaction levels?**
   **Columns:** `region`, `satisfaction`
   **Method:** Compare the median and distribution of satisfaction ratings across regions. Use a grouped/stacked bar chart or boxplot. For statistical testing, Kruskal–Wallis is appropriate for comparing an ordinal outcome across multiple nominal groups.

7. **Does visit frequency differ across regions?**
   **Columns:** `region`, `visits_last_year`
   **Method:** Calculate mean and median visits for each region and visualize them with a bar chart or boxplot. Use one-way ANOVA if its assumptions are reasonable; otherwise use Kruskal–Wallis.

8. **Are longer-standing customers spending more than newer customers?**
   **Columns:** `first_visit_year`, `total_spent_usd`
   **Method:** Use a scatterplot and correlation analysis. Pearson correlation can assess a linear relationship, while Spearman is a useful alternative if the relationship is monotonic or affected by outliers. Because a later `first_visit_year` represents a newer customer, a negative association would indicate that earlier customers tend to have higher total spending.

9. **Do longer-standing customers visit the bakery more frequently?**
   **Columns:** `first_visit_year`, `visits_last_year`
   **Method:** Use a scatterplot and Pearson or Spearman correlation, depending on the shape and assumptions of the relationship. This can indicate whether customers who first visited in earlier years remain more active.

10. **How does customer satisfaction vary by the year customers first visited the bakery?**
    **Columns:** `first_visit_year`, `satisfaction`
    **Method:** Because satisfaction is ordinal, use Spearman rank correlation to examine whether satisfaction tends to increase or decrease with `first_visit_year`. A grouped bar chart or boxplot can supplement the analysis.

11. **Which customers appear to be the bakery’s most engaged customers based on spending and recent visits?**
    **Columns:** `customer_id`, `total_spent_usd`, `visits_last_year`
    **Method:** Rank customers separately by spending and visit frequency, or standardize the two ratio variables before constructing a simple combined engagement score. Use a scatterplot of spending versus visits and label notable high-value/high-frequency customers by `customer_id`.

12. **What customer behavior patterns emerge when spending, visit frequency, satisfaction, and customer tenure are considered together?**
    **Columns:** `first_visit_year`, `satisfaction`, `total_spent_usd`, `visits_last_year`
    **Method:** Start with a correlation matrix using Pearson for the ratio/interval relationships and Spearman where the ordinal satisfaction variable is involved. A scatterplot matrix can help identify relationships worth investigating further. With only 50 observations, keep this exploratory rather than fitting an unnecessarily complex model.

One important **Define-stage distinction**: `customer_id` should generally be treated as an **identifier**, not a quantitative variable. Likewise, `region` is nominal, so calculating a mean for it would not be meaningful, while `satisfaction` is ordinal, making median, mode, frequencies, and rank-based methods especially appropriate.

These 12 questions also give you a good progression for the project: **describe the customers → compare groups → investigate relationships → identify potentially valuable customer patterns**.


## Verification

Here's just the Verification section (Step 5) to copy into your `.md` file:

```markdown
## Verification

### Combined question list

| # | Question | Source | Columns used | Column check | Method check | Business context check | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | How does total spending differ across regions? | Both | region, total_spent_usd | Pass — both real columns | Pass — group means/median on ratio data, ANOVA/Kruskal-Wallis for a nominal grouping variable | Pass — directly informs regional marketing spend | ✓ Verified |
| 2 | Is visit frequency associated with total spending? | Both | visits_last_year, total_spent_usd | Pass | Pass — Pearson/Spearman correlation, both ratio variables | Pass — core loyalty/upsell question | ✓ Verified |
| 3 | Is satisfaction associated with total spending? | Both | satisfaction, total_spent_usd | Pass | Pass — Spearman used because satisfaction is ordinal (not Pearson) | Pass — links happiness to revenue | ✓ Verified |
| 4 | Is satisfaction associated with visit frequency? | Both | satisfaction, visits_last_year | Pass | Pass — Spearman correctly used for ordinal variable | Pass — retention-relevant | ✓ Verified |
| 5 | What is the distribution of customer satisfaction? | Both | satisfaction | Pass | Pass — mode/median/frequency for ordinal data; both tools explicitly avoid the mean | Pass — baseline CX metric | ✓ Verified |
| 6 | Which region has the most customers / how are customers distributed geographically? | Claude only | region | Pass | Pass — mode/frequency count, correct for nominal data | Pass — needed context for interpreting other regional comparisons (uneven group sizes) | ✓ Verified |
| 7 | Has customer acquisition grown or slowed over time? | Claude only | first_visit_year | Pass | Pass — frequency count by year is valid | Pass, with caveat — only measures *first*-visit year, not repeat acquisition or churn; flagged as a proxy, not discarded | ✓ Verified (caveat noted) |
| 8 | Do longer-standing customers (by first-visit cohort) spend/visit more? | Claude only | first_visit_year, total_spent_usd, visits_last_year | Pass | Pass — grouped means by cohort bucket is a reasonable ratio-on-interval comparison | Pass, with caveat — same tenure-proxy limitation as #7 | ✓ Verified (caveat noted) |
| 9 | Is satisfaction associated with region? | Both (converging, different methods) | region, satisfaction | Pass | Claude proposed a chi-square test of independence; ChatGPT proposed Kruskal-Wallis. With 4 regions × 5 satisfaction levels and only 50 rows, several contingency-table cells would have expected counts under 5, which violates chi-square's sample-size assumption. Kruskal-Wallis (ordinal outcome across nominal groups) avoids this and is the more defensible choice here. | Pass | ✓ Verified |
| 10 | What is the distribution/spread of total spending, and are there outliers? | Claude only | total_spent_usd | Pass | Pass — descriptive stats + histogram/boxplot, correct for ratio data | Pass — needed before trusting any mean-based comparison elsewhere in the list | ✓ Verified |
| 11 | Does visit frequency differ by region? | Both | region, visits_last_year | Pass | Pass — group means, ANOVA/Kruskal-Wallis | Pass | ✓ Verified |
| 12 | Which customers are most engaged (spend + visits)? | Both (converging) | customer_id, total_spent_usd, visits_last_year | Pass — 'customer_id' is used only as a label, never averaged or ranked numerically itself | Pass — ranking/standardizing two ratio variables into a simple composite score is a reasonable exploratory technique | Pass — realistic for identifying loyalty-program or outreach targets | ✓ Verified |
| 13 | Are longer-standing customers spending more? | ChatGPT only | first_visit_year, total_spent_usd | Pass | Pass — scatterplot + Pearson/Spearman | Pass, with caveat — 'first_visit_year' has only 8 distinct values, limiting correlation power; same tenure-proxy issue as #7/#8 | ✓ Verified (caveat noted) |
| 14 | Do longer-standing customers visit more frequently? | ChatGPT only | first_visit_year, visits_last_year | Pass | Pass — same method logic as #13 | Pass, with caveat — same tenure-proxy issue | ✓ Verified (caveat noted) |
| 15 | How does satisfaction vary by first-visit year? | ChatGPT only | first_visit_year, satisfaction | Pass | Pass — Spearman is correct since satisfaction is ordinal | Pass, with caveat — same tenure-proxy issue | ✓ Verified (caveat noted) |
| 16 | What patterns emerge when spending, visits, satisfaction, and tenure are considered together? | ChatGPT only | first_visit_year, satisfaction, total_spent_usd, visits_last_year | Pass | Pass — correlation matrix mixing Pearson (ratio-ratio pairs) and Spearman (pairs involving ordinal satisfaction) is the right way to handle mixed scales | Pass, with caveat — with n=50, this should stay exploratory, not a fitted model | ✓ Verified (caveat noted) |

**Column check summary:** zero hallucinated columns from either tool. Every question above references only 'customer_id', 'region', 'first_visit_year', 'satisfaction', 'total_spent_usd', or 'visits_last_year'.

**Method check summary:** no mean of nominal errors (region was always handled with mode/frequency), and satisfaction was consistently treated as ordinal (Spearman, median, mode) rather than averaged outright. The one real finding from cross-checking the two tools against each other was #9

**Business context check summary:** all 16 questions are answerable from customer behavior data a small bakery would track, and all map to a marketing or product decision

## Verified question list

16 of 16 questions passed verification.

### Segmentation
1. Which customers are most engaged, based on total spending and visits in the last year? (`customer_id`, `total_spent_usd`, `visits_last_year` — composite rank/score, labeled scatterplot)

### Behavior (spending & visit relationships)
2. Is visit frequency associated with total spending? 
3. What is the distribution and spread of total spending, and are there outliers?

### Satisfaction
4. What is the overall distribution of customer satisfaction? 
5. Is satisfaction associated with total spending? 
6. Is satisfaction associated with visit frequency?

### Regional patterns
7. How does total spending differ across regions? 
8. Which region has the most customers, and how are customers distributed geographically?
9. Is satisfaction associated with region? 
10. Does visit frequency differ by region? 

### Time trends (tenure, based on first_visit_year as a proxy)
11. Has customer acquisition grown or slowed over time? 
12. Do longer-standing customers spend and visit more, by acquisition cohort? 
13. Are longer-standing customers spending more? 
14. Do longer-standing customers visit more frequently? 
15. How does satisfaction vary by first-visit year? 
16. What patterns emerge when spending, visits, satisfaction, and tenure are considered together?

**Shrinkage note:** raw combined output was 24 questions (12 per tool); after collapsing exact duplicates the distinct list was 16, and all 16 survived verification