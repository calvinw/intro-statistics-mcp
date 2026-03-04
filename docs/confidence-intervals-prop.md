# 20 Confidence Intervals For Proportions

In this section we look at a technique for estimating a population proportion $p$ when we do not know it.

The technique is called **calculating a confidence interval**.

We start by taking a sample and finding a sample proportion $\hat p$. Then we add and subtract a margin of error $E$ to the sample proportion to make an interval where we hope to find the population proportion. We will show how to calculate the margin of error $E$ below.

We can say using something called the **confidence level** how likely we are to “capture” the population proportion inside our interval if we do this repeatedly.

This is an example of inferential statistics since we are using information from a sample (the statistic $\hat p$) to infer information about the population (the parameter $p$)

## 20.1 Steps for Finding Confidence Intervals - Proportions

The steps involved to do this are as follows:

  * Take a sample and calculate the sample proportion $\hat p$
  * Calculate a margin of error $E$ using the formula below. (This tells us roughly how far off $\hat p$ is from $p$)
  * Find the interval by adding and subtracting $E$ to $\hat p$. (This interval tells where we hope to find $p$)



**Example 20.1 (A Confidence Interval and Margin of Error)**

Suppose we take a sample and collect some data. Then we compute a sample proportion:

$$\hat p = .41$$

Then using the formula for a confidence interval suppose we find that

$$E = .03$$

(We will show how to compute this later on. For now just pretend we did it and got $.03$.)

Subtract $E$ from $\hat p$ to get the **lower endpoint** of the confidence interval:

$$\hat p - E = .41 - .03 = .38$$

Add $E$ to $\hat p$ to get the **upper endpoint** of the confidence interval:

$$\hat p + E = .41 + .03 = .44$$

So the confidence interval goes from .38 up to .44. Sometimes we write this like this:

$$(\hat{p} - E,\ \hat{p} + E) = (.38,.44)$$

Roughly what this says is that we believe the population proportion is **between 38% and 44%**.

Exactly how confident and in what sense the above is true we will see below.

$$\tag*{$\blacksquare$}$$

Next we look at how we come up with $E$, the margin of error.

## 20.2 Margin of Error E for Confidence Intervals - Proportions

To find $E$ we have to first decide on a **confidence level.** This is a percentage (something like 90% or 95% or 99%).

The confidence level describes how confident we are that our confidence intervals will contain the population proportion:

  * A confidence level of 95% means that our confidence intervals ($\widehat{p} - E$, $\widehat{p} + E$) will contain the population proportion $p$ about 95% of the time.
  * A confidence level of 99% means that our confidence intervals ($\widehat{p} - E$, $\widehat{p} + E$) will contain the population proportion $p$ about 99% of the time.
  * and so on



Another way to put this:

For 95% confidence, this means that if we repeatedly take samples and find a sample proportion $\hat p$, we can expect to find the population proportion inside our confidence intervals roughly 95% of the time.

This notion of confidence level makes sense only in the context of repeatedly taking confidence intervals for a particular situation.

Of the different confidence levels, by far **the most commonly used confidence interval is one with confidence level 95%.**

Once we decide on the confidence level we want to use, we will use the following formula to calculate the margin of error $E$:

$$E=(z^\star)\sqrt{\frac{(1-\hat p)(\hat p)}{n}}$$

The $\hat p$ we have and the sample size $n$ we have as well. The $z^\star$ comes from the chosen confidence level. We show where to get it in the next section.

## 20.3 Critical Value $z^\star$

The formula for E has something called $z^\star$ in it. This is called the **critical value**. It comes directly from the confidence level. Once you know the confidence interval you are using you can look up the $z^\star$ that goes with that confidence level. Here are the most typical values:

Confidence Level | 80% | 90% | 95% | 99% | 99.9%  
---|---|---|---|---|---  
$z^\star$ | 1.282 | 1.645 | 1.960 | 2.576 | 3.291  
  
As an example, this table says:

  * use 1.645 for the $z^\star$ if you are computing a 90% confidence interval
  * use 1.960 for the $z^\star$ if you are computing a 95% confidence interval



If you ever need a confidence interval for some confidence level not shown in the table above you can compute it yourself using a spreadsheet as follows:

**= NORMSINV( (c+1.0)/2)**

where c = confidence level as a proportion. For example if the confidence level was 97% (which is not on the table above) then you could get it in a spreadsheet with

**=NORMSINV((.97+1.0)/2)**

As part of using the normal distribution to find the $z^\star$ we also have to check the technical conditions like in the Central Limit Theorem.

For the above to be valid must have $n(\hat p)>5$ and $n(1-\hat p)>5$.

## 20.4 Confidence Interval Calculations - Proportions

**Example 20.2 (A $95\%$ Confidence Interval)**

Suppose we have a sample proportion of $210$ out of $250$. Find a $95\%$ confidence interval for this sample proportion.

**_Solution:_**

The sample proportion is $210$ out of $250$:

$$\hat p = \frac{count}{n} = \frac{210}{250} = 0.84$$

Before we start we check the conditions showing we can use z-values from a standard normal distribution here: $n(\hat p)=(250)(0.84)= 210$ and $n(1-\hat p)=(250)(0.16)= 40$

Since these are both at least $5$ we are in good shape.

Next we will calculate the $E$ involved, using the confidence level 95%.

For this confidence level we can look up that the appropriate critical value $z^\star$ to use. In this case it is $z^\star = 1.96$.

We plug the sample proportion $\hat p=0.84$ and the sample size $n=250$ and the $z^\star$ into our formula for $E$:

$$E=(z^\star)\sqrt{\frac{(1-\hat p)(\hat p)}{n}} =(1.96)\sqrt{\frac{(1-0.84)(0.84)}{250}} = 0.045$$

Then we find the two endpoints.

The left one is this:

$$\hat p - E = 0.84-0.045 = 0.795$$

The right one is this:

$$\hat p + E = 0.84+0.045 = 0.885$$

So the confidence interval for the sample proportion is

$$(0.795,0.885)$$

If we wanted this rounded to the nearest percent we would use:

$$(80 \% ,88 \%)$$

We could say the confidence interval is from $80 \%$ to $88 \%$.

$$\tag*{$\blacksquare$}$$

## 20.5 Effect of Changing Confidence Level

What is the effect of changing the confidence level?

The higher the confidence level, the more sure we are of “capturing” the actual population proportion. But at the same time, the more sure we are of “capturing” the actual population proportion the wider our confidence intervals become.

  * A 95% confidence interval will be wider than a 90% confidence interval.
  * A 99% confidence interval will be wider than a 95% confidence interval.
  * and so on



It is kind of like if we cast a larger net we will be sure to catch it in the net somewhere, but then we are less sure exactly where it is because the net is bigger.

Let’s see an example where we calculate the confidence interval twice, each time using a different confidence level.

  * First we compute it for 90% confidence level
  * Second we compute it for 99% confidence level



**Example 20.3 (First Version - 90% Confidence Level)** Suppose we have a sample proportion of $50$ out of $125$. Find a $90\%$ confidence interval for this sample proportion.

**_Solution:_**

The sample proportion is $50$ out of $125$:

$$\hat p = \frac{count}{n} = \frac{50}{125} = 0.4$$

Before we start we check the conditions showing we can use z-values from a standard normal distribution here: $n(\hat p)=(125)(0.4)= 50$ and $n(1-\hat p)=(125)(0.6)= 75$

Since these are both at least $5$ we are in good shape.

Next we will calculate the $E$ involved, using the confidence level 90%.

For this confidence level we can look up that the appropriate critical value $z^\star$ to use. In this case it is $z^\star = 1.645$.

We plug the sample proportion $\hat p=0.4$ and the sample size $n=125$ and the $z^\star$ into our formula for $E$:

$$E=(z^\star)\sqrt{\frac{(1-\hat p)(\hat p)}{n}} =(1.645)\sqrt{\frac{(1-0.4)(0.4)}{125}} = 0.072$$

Then we find the two endpoints.

The left one is this:

$$\hat p - E = 0.4-0.072 = 0.328$$

The right one is this:

$$\hat p + E = 0.4+0.072 = 0.472$$

So the confidence interval for the sample proportion is

$$(0.328,0.472)$$

If we wanted this rounded to the nearest percent we would use:

$$(33 \% ,47 \%)$$

We could say the confidence interval is from $33 \%$ to $47 \%$.

$$\tag*{$\blacksquare$}$$

Now let’s do that last one over with a 99% confidence level.

**Example 20.4 (Second Version - $99\%$ Confidence Level)**

Suppose we have a sample proportion of $50$ out of $125$. Find a $99\%$ confidence interval for this sample proportion.

**_Solution:_**

The sample proportion is $50$ out of $125$:

$$\hat p = \frac{count}{n} = \frac{50}{125} = 0.4$$

Before we start we check the conditions showing we can use z-values from a standard normal distribution here: $n(\hat p)=(125)(0.4)= 50$ and $n(1-\hat p)=(125)(0.6)= 75$

Since these are both at least $5$ we are in good shape.

Next we will calculate the $E$ involved, using the confidence level 99%.

For this confidence level we can look up that the appropriate critical value $z^\star$ to use. In this case it is $z^\star = 2.576$.

We plug the sample proportion $\hat p=0.4$ and the sample size $n=125$ and the $z^\star$ into our formula for $E$:

$$E=(z^\star)\sqrt{\frac{(1-\hat p)(\hat p)}{n}} =(2.576)\sqrt{\frac{(1-0.4)(0.4)}{125}} = 0.113$$

Then we find the two endpoints.

The left one is this:

$$\hat p - E = 0.4-0.113 = 0.287$$

The right one is this:

$$\hat p + E = 0.4+0.113 = 0.513$$

So the confidence interval for the sample proportion is

$$(0.287,0.513)$$

If we wanted this rounded to the nearest percent we would use:

$$(29 \% ,51 \%)$$

We could say the confidence interval is from $29 \%$ to $51 \%$.

$$\tag*{$\blacksquare$}$$

Which confidence interval was wider in the above?

The 99% confidence level one.

To be more confident that your confidence interval contains the population proportion it must be wider.

Of course this means your estimate is less accurate and that is reflected in the range of the interval being larger.

## 20.6 Applications of Confidence Intervals

**Example 20.5 (Shopping App Usage)**

A department store thinks that $40\%$ of their customers would use a shopping app while in-store. They poll $300$ users one day and find out that $78$ of them would use such an app. Find a $90\%$ confidence interval for this sample proportion.

**_Solution:_**

The sample proportion is $78$ out of $300$:

$$\hat p = \frac{count}{n} = \frac{78}{300} = 0.26$$

Before we start we check the conditions showing we can use z-values from a standard normal distribution here: $n(\hat p)=(300)(0.26)= 78$ and $n(1-\hat p)=(300)(0.74)= 222$

Since these are both at least $5$ we are in good shape.

Next we will calculate the $E$ involved, using the confidence level 90%.

For this confidence level we can look up that the appropriate critical value $z^\star$ to use. In this case it is $z^\star = 1.645$.

We plug the sample proportion $\hat p=0.26$ and the sample size $n=300$ and the $z^\star$ into our formula for $E$:

$$E=(z^\star)\sqrt{\frac{(1-\hat p)(\hat p)}{n}} =(1.645)\sqrt{\frac{(1-0.26)(0.26)}{300}} = 0.042$$

Then we find the two endpoints.

The left one is this:

$$\hat p - E = 0.26-0.042 = 0.218$$

The right one is this:

$$\hat p + E = 0.26+0.042 = 0.302$$

So the confidence interval for the sample proportion is

$$(0.218,0.302)$$

If we wanted this rounded to the nearest percent we would use:

$$(22 \% ,30 \%)$$

We could say the confidence interval is from $22 \%$ to $30 \%$.

The confidence interval does not contain $40\%$ and so probably the store is overestimating what proportion of their customers would use such an app. It appears to be somewhat less than $40\%$.

$$\tag*{$\blacksquare$}$$

In the next example we estimate the chance of being out of stock for some item we are selling.

**Example 20.6 (Estimating Out Of Stock)**

A store had some item out of stock in $26$ of the past $208$ weeks (the last 4 years). Calculate a $90\%$ confidence interval estimate for the proportion of weeks this item is out of stock.

**_Solution:_**

The sample proportion is $26$ out of $208$:

$$\hat p = \frac{count}{n} = \frac{26}{208} = 0.125$$

Before we start we check the conditions showing we can use z-values from a standard normal distribution here: $n(\hat p)=(208)(0.125)= 26$ and $n(1-\hat p)=(208)(0.875)= 182$

Since these are both at least $5$ we are in good shape.

Next we will calculate the $E$ involved, using the confidence level 90%.

For this confidence level we can look up that the appropriate critical value $z^\star$ to use. In this case it is $z^\star = 1.645$.

We plug the sample proportion $\hat p=0.125$ and the sample size $n=208$ and the $z^\star$ into our formula for $E$:

$$E=(z^\star)\sqrt{\frac{(1-\hat p)(\hat p)}{n}} =(1.645)\sqrt{\frac{(1-0.125)(0.125)}{208}} = 0.038$$

Then we find the two endpoints.

The left one is this:

$$\hat p - E = 0.125-0.038 = 0.087$$

The right one is this:

$$\hat p + E = 0.125+0.038 = 0.163$$

So the confidence interval for the sample proportion is

$$(0.087,0.163)$$

If we wanted this rounded to the nearest percent we would use:

$$(9 \% ,16 \%)$$

We could say the confidence interval is from $9 \%$ to $16 \%$.

Our estimate is between $9 \%$ and $16 \%$

$$\tag*{$\blacksquare$}$$
