# Brewbird Lifecycle Worksheet

**Analyst:** Paola Paguaga
**Date:** June 19, 2026
**Client:** Brewbird Coffee Roasters
**Stakeholder:** Carmen Ruiz-Santana

## 1. Define

The question: Why has customer count declined over the last six months, while other locations remain stable or are growing?

The decision will inform: whether the decline in customer count is driven by customer service quality, location accesability, prices, store aesthetics, or an increased competition from new coffee shops around the area.

What "done" looks like: Identifying the root cause of the decline and delivering a clear, actionable recommendation.

## 2. Collect

Datasets needed: monthly_sales, prices_items, sales_by_shop, daily_customer_count, number_of_coffeshops_in_the_area, reviews_on_social_media, customer_feedback, monthly_sales_items

Datasets that already exist: monthly_sales, prices_items, sales_by_shop, daily_customer_count

Datasets that don't exist or aren't accessible: number_of_coffeshops_in_the_area, reviews_on_social_media, customer_feedback, monthly_sales_items

## 3. Clean

- Integrating external data sources: Pulling insights from Google Reviews or social media may require building datasets from scratch or reconciling data across platforms. This introduces complexity.
- Incomplete data: Gaps caused by system errors or missing values can create blind spots that skew findings. Addressing these will require decisions around flagging records before analysis begins.
- Duplicate and irrelevant records: Redundant or off-topic entries inflate dataset volume and introduce ambiguity that can distort results. A cleaning protocol will be needed to deduplicate records and filter out noise before drawing any conclusions.

## 4. Analyze

- Do all locations offer the same menu items?
- Are raw materials sourced from the same vendors across all locations?
- Have new coffee shops opened in the area?
- Has there been a change in management or staff?
- How long does a customer typically stay per visit?
- How have prices changed month over month?
- Have any major schools or businesses in the area closed?

## 5. Visualize 
- Line chart showing customer count by location over time. We can verify if the decline is really unique to that specific location.
- Bar chart showing average rating or review by location. Compare customer satisfaction across locations to test if the service has experienced a declined. 
- Bar chart showing price changes by month. We can answer whether pricing trends aligns with customer drop.

## 6 Communicate 

The Brewbird Coffee Roaster customer count declined over the last six months and the timing aligns closely with two new competitors opening nearby in the same period. Customer satisfaction scores and pricing have stayed consisten across locations. We recommend reallocating x% of this location's marketing budget from abroad awareness campaings. 

## 7 Act

- A follow-up call with the stakeholders three weeks after the report
- An analysis at the end of the month to see whether the trend has reversed.
- A check on customer reviews trends to verify service quality has not dropped