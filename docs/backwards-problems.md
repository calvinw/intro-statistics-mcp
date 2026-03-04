# 18 Backwards Problems

In this section we want to go in the opposite direction from previous chapters. That is we want to find an **_x-value that will give us a certain left tail or right tail area_**. These are called **backwards** problems since they start with the area and then find the x-value. This is backwards from what we have done before.

So in previous chapters we had this:

_**Find Area From an X-value**_

  1. Start with an x-value
  2. Compute its z-value
  3. Find the area using the z table (or use NORMSDIST)



Now we want to go in the other direction:

_**Find X-value From an Area**_

  1. Start with an area
  2. Find the z-value that gives that area
  3. Compute the x-value from the z-value



Before we do these full backwards problems from area to x-value, first lets solve an easier problem that involves finding the z-value that goes with a particular area.

Then once we can do that, we will see how to find the x-value from the z-value for backwards problems.

Okay so we are given an area (left or right tail) and we want to find the z-value.

**Example 18.1 (z-value for left tail $z=1.23$)**

Find the z-value that gives a left tail area of $25\%$.

**_Solution:_**

We want to find the z-value for a given left tail area of $25\%$.

This is an example of a **backwards** problem, since we are going from an **area to a z-value**.

Here is what the picture looks like:

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/backwards-problems_unnamed-chunk-16-1.png)

The shaded left tail area corresponds to **25%** of the data. We use the standard normal table to find the z-value that goes with this left tail.

We look through the table and **_look for the area that is closest_** to the value **25%** which we need.

We might not find this value exactly but we locate the closest value that we can:

| .00| .01| .02| .03| .04| .05| .06| .07| .08| .09  
---|---|---|---|---|---|---|---|---|---|---  
-0.7| .2420| .2389| .2358| .2327| .2296| .2266| .2236| .2206| .2177| .2148  
-0.6| .2743| .2709| .2676| .2643| .2611| .2578| .2546| .2514| .2483| .2451  
-0.5| .3085| .3050| .3015| .2981| .2946| .2912| .2877| .2843| .2810| .2776  
  
So that means we can take:

$$z =-0.67$$

as our solution. That is the z-value that we need.

Here is the picture then:

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/backwards-problems_unnamed-chunk-18-1.png)

$$\tag*{$\blacksquare$}$$

**Example 18.2 (z-value for right tail of $18\%$)**

Find the z-value that gives a right tail area of $18\%$.

**_Solution:_**

We want to find the z-value for a given right tail area of $18\%$.

This is an example of a **backwards** problem, since we are going from an **area to a z-value**.

Here is what the picture looks like:

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/backwards-problems_unnamed-chunk-35-1.png)

The shaded right tail area corresponds to **18%** of the data.

Now we can’t just look up the area in the z-table since **the table only has left tails** and we have a right tail.

But we have this:

$$\text{left tail} = 1.0 - \text{right tail}$$

So instead of looking for a right tail of size **0.18** , we can look for a left tail of size **0.82**.

We look through the table and **_look for the area that is closest_** to the value **82%** which we need.

We might not find this value exactly but lets locate the closest value that we can:

| .00| .01| .02| .03| .04| .05| .06| .07| .08| .09  
---|---|---|---|---|---|---|---|---|---|---  
0.8| .7881| .7910| .7939| .7967| .7995| .8023| .8051| .8078| .8106| .8133  
0.9| .8159| .8186| .8212| .8238| .8264| .8289| .8315| .8340| .8365| .8389  
1.0| .8413| .8438| .8461| .8485| .8508| .8531| .8554| .8577| .8599| .8621  
  
So that means we can take:

$$z =0.92$$

as our solution. That is the z-value that we need.

Here is the picture then:

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/backwards-problems_unnamed-chunk-37-1.png)

$$\tag*{$\blacksquare$}$$

## 18.1 Solve Backwards for X-value

Once you have the z-value that you need using one of the above you can solve backward for the x-value that you need. It works like this:

_**Find X-value by Solving Z-score Formula Backwards**_

  1. Find the z-value you need using technique above
  2. Plug the z-value into the z-score formula
  3. Plug in $\mu$ and $\sigma$ (these are known)
  4. Solve for the x-value



So basically you just plug your z-value, $\mu$ and $\sigma$ into this and solve for x:

$$z =\frac{x-\mu}{\sigma} \tag{18.1}$$

Here is an example where we want to find the **lower 25%** of the data. That means we want to find the x-value that has a left tail area of 25%.

**Example 18.3 (Find $x$ for bottom $25\%$ of data)**

Suppose that a normal distribution has mean $18$ and standard deviation $3$. Find the x-value that represents a left tail area of $25\%$.

**_Solution:_**

We have $\mu=18$ and $\sigma = 3$.

We want an x-value whose **left tail area** is $0.25$ (or $25\%$).

Here is what the picture looks like:

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/backwards-problems_unnamed-chunk-54-1.png)

To do this we first find the z-value that goes with this same left tail area. It looks like this:

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/backwards-problems_unnamed-chunk-55-1.png)

We use the table backwards and look for the closest z-value to our area 0.25. We may not find it exactly so we look for the entry that is closest to 0.25.

| .00| .01| .02| .03| .04| .05| .06| .07| .08| .09  
---|---|---|---|---|---|---|---|---|---|---  
-0.7| .2420| .2389| .2358| .2327| .2296| .2266| .2236| .2206| .2177| .2148  
-0.6| .2743| .2709| .2676| .2643| .2611| .2578| .2546| .2514| .2483| .2451  
-0.5| .3085| .3050| .3015| .2981| .2946| .2912| .2877| .2843| .2810| .2776  
  
We get this z-value:

$$z = -0.67$$

Then we can find the x-value by plugging in the z-value and the $\mu=18$ and $\sigma = 3$ (which were given) and solving for x:

$$z &= \frac{x-\mu}{\sigma} \\\ -0.67 &= \frac{x-18}{3} \\\ 3(-0.67) &= x-18 \\\ -2.01+ 18 &= x \\\ 15.99 &= x$$

_**Steps to solve for x:**_

  1. Plug in $\mu=18$, $\sigma=3$ and $z=-0.67$
  2. Multiple by $3$ on both sides
  3. Add $18$ to both sides as well



This gives us the x-value that we need. Here is the graph:

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/backwards-problems_unnamed-chunk-57-1.png)

So $x=15.99$ is the x-value that has a left tail area of $25$%.

$$\tag*{$\blacksquare$}$$

Here is an example where we want to find the **upper 15%** of the data. That means we want to find the x-value that has a right tail area of 15%.

**Example 18.4 (Find $x$ for top $15\%$ of data)**

Suppose that a normal distribution has mean $23$ and standard deviation $4$. Find the x-value that represents a right tail area of $15\%$.

**_Solution:_**

We have $\mu=23$ and $\sigma = 4$.

We want an x-value whose **right tail area** is $0.15$ (or $15\%$).

Here is what the picture looks like:

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/backwards-problems_unnamed-chunk-75-1.png)

To do this we first find the z-value that goes with this same right tail area.

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/backwards-problems_unnamed-chunk-76-1.png)

Since the right tail is **0.15** , the left tail is **0.85** and so we just need to find the z-value that corresponds to a left tail area of **0.85**.

We use the table backwards and look for the closest z-value to our area 0.85. We may not find it exactly so we look for the entry that is closest to 0.85.

| .00| .01| .02| .03| .04| .05| .06| .07| .08| .09  
---|---|---|---|---|---|---|---|---|---|---  
0.9| .8159| .8186| .8212| .8238| .8264| .8289| .8315| .8340| .8365| .8389  
1.0| .8413| .8438| .8461| .8485| .8508| .8531| .8554| .8577| .8599| .8621  
1.1| .8643| .8665| .8686| .8708| .8729| .8749| .8770| .8790| .8810| .8830  
  
We get this z-value:

$$z = 1.04$$

Then we can find the x-value by plugging in the z-value and the $\mu=23$ and $\sigma = 4$ (which were given) and solving for x:

$$z &= \frac{x-\mu}{\sigma} \\\ 1.04 &= \frac{x-23}{4} \\\ 4(1.04) &= x-23 \\\ 4.16+ 23 &= x \\\ 27.16 &= x$$

_**Steps to solve for x:**_

  1. Plug in $\mu=23$, $\sigma=4$ and $z=1.04$
  2. Multiple by $4$ on both sides
  3. Add $23$ to both sides as well.



This gives us the x-value that we need. Here is the graph:

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/backwards-problems_unnamed-chunk-78-1.png)

So $x=27.16$ is the x-value that has a right tail area of $15$%.

$$\tag*{$\blacksquare$}$$

## 18.2 Applications of Backwards Problems

Here is an example where you want to find out when a demand value would be in the bottom 10% of your demand expectations for an item.

**Example 18.5 (Bottom $10\%$ of Demand Values)**

Suppose you have a retail item SKU with demand on average of 257 units per month with a standard deviation of 45. What demand would correspond to the bottom 10% of all demand values here?

**_Solution:_**

We have $\mu=257$ and $\sigma = 45$.

We want an x-value whose **left tail area** is $0.1$ (or $10\%$).

Here is what the picture looks like:

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/backwards-problems_unnamed-chunk-100-1.png)

To do this we first find the z-value that goes with this same left tail area. It looks like this:

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/backwards-problems_unnamed-chunk-101-1.png)

We use the table backwards and look for the closest z-value to our area 0.1. We may not find it exactly so we look for the entry that is closest to 0.1.

| .00| .01| .02| .03| .04| .05| .06| .07| .08| .09  
---|---|---|---|---|---|---|---|---|---|---  
-1.3| .0968| .0951| .0934| .0918| .0901| .0885| .0869| .0853| .0838| .0823  
-1.2| .1151| .1131| .1112| .1093| .1075| .1056| .1038| .1020| .1003| .0985  
-1.1| .1357| .1335| .1314| .1292| .1271| .1251| .1230| .1210| .1190| .1170  
  
We get this z-value:

$$z = -1.28$$

Then we can find the x-value by plugging in the z-value and the $\mu=257$ and $\sigma = 45$ (which were given) and solving for x:

$$z &= \frac{x-\mu}{\sigma} \\\ -1.28 &= \frac{x-257}{45} \\\ 45(-1.28) &= x-257 \\\ -57.6+ 257 &= x \\\ 199.4 &= x$$

_**Steps to solve for x:**_

  1. Plug in $\mu=257$, $\sigma=45$ and $z=-1.28$
  2. Multiple by $45$ on both sides
  3. Add $257$ to both sides as well



This gives us the x-value that we need. Here is the graph:

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/backwards-problems_unnamed-chunk-103-1.png)

So $x=199.4$ is the x-value that has a left tail area of $10$%.

So any demand value below this would be in the bottom $10\%$ of the demand expectations for this SKU.

$$\tag*{$\blacksquare$}$$

Here is another application of backwards problems:

The **_service level_** in retail corresponds to the chance that a retailer would experience a lost sale (out of stock situation) for some period of interest.

  * A service level of 90% means that lost sales would happen 10% of the time.
  * A service level of 95% means that lost sales would happen be 5% of the time.
  * A service level of 99% means that lost sales would happen be 1% of the time.



Different items and categories can have different service levels as well, with some items being “high” service level items while others being “low” service level items.

The next example shows how to set inventory levels for an item to achieve a certain service level.

**Example 18.6 (Inventory For $95\%$ service level)**

Suppose you have a retail item SKU with demand on average of $340$ units per month with a standard deviation of $80$. What level inventory should you carry in the upcoming month to assure that you have $95\%$ service level on this item?

**_Solution:_**

We have $\mu=340$ and $\sigma = 80$.

We want an x-value whose **left tail area** is $0.95$ (or $95\%$).

Here is what the picture looks like:

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/backwards-problems_unnamed-chunk-126-1.png)

To do this we first find the z-value that goes with this same left tail area. It looks like this:

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/backwards-problems_unnamed-chunk-127-1.png)

We use the table backwards and look for the closest z-value to our area 0.95. We may not find it exactly so we look for the entry that is closest to 0.95.

| .00| .01| .02| .03| .04| .05| .06| .07| .08| .09  
---|---|---|---|---|---|---|---|---|---|---  
1.5| .9332| .9345| .9357| .9370| .9382| .9394| .9406| .9418| .9429| .9441  
1.6| .9452| .9463| .9474| .9484| .9495| .9505| .9515| .9525| .9535| .9545  
1.7| .9554| .9564| .9573| .9582| .9591| .9599| .9608| .9616| .9625| .9633  
  
We get this z-value:

$$z = 1.64$$

Then we can find the x-value by plugging in the z-value and the $\mu=340$ and $\sigma = 80$ (which were given) and solving for x:

$$z &= \frac{x-\mu}{\sigma} \\\ 1.64 &= \frac{x-340}{80} \\\ 80(1.64) &= x-340 \\\ 131.2+ 340 &= x \\\ 471.2 &= x$$

_**Steps to solve for x:**_

  1. Plug in $\mu=340$, $\sigma=80$ and $z=1.64$
  2. Multiple by $80$ on both sides
  3. Add $340$ to both sides as well



This gives us the x-value that we need. Here is the graph:

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/backwards-problems_unnamed-chunk-129-1.png)

So $x=471.2$ is the x-value that has a left tail area of $95$%.

So you should have at least $472$ for inventory to insure you have a $95\%$ service level.

$$\tag*{$\blacksquare$}$$

In this interpretation service level corresponds to a certain left tail area for the normal distribution:

  * A service level of 90% means you want a left tail area of 90%
  * A service level of 95% means you want a left tail area of 95%.
  * A service level of 99% means you want a left tail area of 99%.


Or you can say it this way as well:

  * A service level of 90% means you have lost sales 10% of the time.
  * A service level of 95% means you have lost sales 5% of the time.
  * A service level of 99% means you have lost sales 1% of the time.


