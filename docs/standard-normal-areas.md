# 16 Standard Normal Areas

Here is the code with the requested find/replace operations:

In this section we see how to find **left tail areas** , **right tail areas** and also **areas between** for the standard normal distribution by using the z-table. See Appendix A for the table.

## 16.1 Standard Normal Left Tail Areas

The first examples here are for **left tail areas**. We actually already saw how to do this in Standard Normal Table by looking up the z-value and reading off the left tail area directly in the table, but it is worth doing one more example since it is so important.

Here is a problem with the z-value is positive:

**Example 16.1 (Find left tail area when $z=1.52$)**

Find the left tail area when $z=1.52$.

**_Solution:_**

We have $z = 1.52$.

Here is the picture of the area we want.

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/standard-normal-areas_unnamed-chunk-19-1.png)

We want the shaded region to the left of $z=1.52$

If we look up the area in the standard normal z-table using $z=1.52$ we go to the row that has 1.5 and then to the column that contains .02 and we see this:

| .00| .01| .02| .03| .04| .05| .06| .07| .08| .09  
---|---|---|---|---|---|---|---|---|---|---  
1.4| .9192| .9207| .9222| .9236| .9251| .9265| .9279| .9292| .9306| .9319  
1.5| .9332| .9345| .9357| .9370| .9382| .9394| .9406| .9418| .9429| .9441  
1.6| .9452| .9463| .9474| .9484| .9495| .9505| .9515| .9525| .9535| .9545  
  
So that means:

$$\text{left tail area} =0.9357$$

Rounded to the nearest percent this is 94%. This means that the shaded area corresponds to 94% of the entire data.

$$\tag*{$\blacksquare$}$$

## 16.2 Standard Normal Right Tail Areas

Next lets take a look at finding a **right tail area**. Since our table only uses left tail areas we need a trick. This trick is sometimes called the **1 minus trick**.

It relies on this fact:

$$\text{right tail area} + \text{left tail area} = 1.0 \tag{16.1}$$

That is any right tail and its corresponding left tail add up to 100%.

So for example below the **right tail is 0.06** and the **left tail is 0.94** and these add up to **1.0**

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/standard-normal-areas_unnamed-chunk-3-1.png)

So when we want to find the right tail area for some situation we can just find the left tail area and then subtract. Here are some examples.

**Example 16.2 (Find right tail area when $z=-1.32$)**

Find the right tail area when $z=-1.32$.

**_Solution:_**

Here is the picture of the area we want. This area is called a “right tail area”:

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/standard-normal-areas_unnamed-chunk-38-1.png)

We want the shaded region to the right of $z=-1.32$ and underneath the standard normal curve.

Since the standard normal table only has “left tail” areas in it, we cannot look up the area we want directly. But if we look up the left tail area in the z-table for $z=-1.32$, we can then subtract that from 1.0 to get the area that we want.

Now to find the left tail area we need using standard normal z-table using $z=-1.32$ we go to the row that has -1.3 and then to the column that contains .02 and we see this:

| .00| .01| .02| .03| .04| .05| .06| .07| .08| .09  
---|---|---|---|---|---|---|---|---|---|---  
-1.4| .0808| .0793| .0778| .0764| .0749| .0735| .0721| .0708| .0694| .0681  
-1.3| .0968| .0951| .0934| .0918| .0901| .0885| .0869| .0853| .0838| .0823  
-1.2| .1151| .1131| .1112| .1093| .1075| .1056| .1038| .1020| .1003| .0985  
  
So the left tail area is 0.0934. We use this to find the right tail area now:

$$\text{right tail area}=1.0 - \text{left tail area} =1.0 - 0.0934 = 0.9066$$

Rounded to the nearest percent this right tail area is 91%.

This means that the shaded area corresponds to 91% of the entire data.

Another way to say it is that 91% of the data falls to the right of $z=-1.32$.

$$\tag*{$\blacksquare$}$$

Another example:

**Example 16.3 (Find right tail area when $z=0.52$)**

Find the right tail area when $z=0.52$.

**_Solution:_**

Here is the picture of the area we want. This area is called a “right tail area”:

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/standard-normal-areas_unnamed-chunk-57-1.png)

We want the shaded region to the right of $z=0.52$ and underneath the standard normal curve.

Since the standard normal table only has “left tail” areas in it, we cannot look up the area we want directly. But if we look up the left tail area in the z-table for $z=0.52$, we can then subtract that from 1.0 to get the area that we want.

Now to find the left tail area we need using standard normal z-table using $z=0.52$ we go to the row that has 0.5 and then to the column that contains .02 and we see this:

| .00| .01| .02| .03| .04| .05| .06| .07| .08| .09  
---|---|---|---|---|---|---|---|---|---|---  
0.4| .6554| .6591| .6628| .6664| .6700| .6736| .6772| .6808| .6844| .6879  
0.5| .6915| .6950| .6985| .7019| .7054| .7088| .7123| .7157| .7190| .7224  
0.6| .7257| .7291| .7324| .7357| .7389| .7422| .7454| .7486| .7517| .7549  
  
So the left tail area is 0.6985. We use this to find the right tail area now:

$$\text{right tail area}=1.0 - \text{left tail area} =1.0 - 0.6985 = 0.3015$$

Rounded to the nearest percent this right tail area is 30%.

This means that the shaded area corresponds to 30% of the entire data.

Another way to say it is that 30% of the data falls to the right of $z=0.52$.

$$\tag*{$\blacksquare$}$$

## 16.3 Standard Normal Area Between Two Z Values

Finding the **area between** involves a trick as well.

_**Find Area Between Z Values**_

  1. You look up the **left tail area** to the “upper z” (the one farthest to the right).
  2. Then you look up the **left tail area** to the “lower z” (the one farthest to the left).
  3. Then you subtract those two areas to get the **area between**.



Be sure to subtract these the right way. If you subtract them backwards your answer will turn out negative. Since areas cannot be negative, you will know you made a mistake.

Okay here are some examples of finding the **area between** two z-values.

**Example 16.4 (Find area between $z_1=0.52$ and $z_2=1.65$)**

Find the area between $z_{1}=0.52$ and $z_{2}=1.65$.

**_Solution:_**

Here is the picture of the area we want.

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/standard-normal-areas_unnamed-chunk-77-1.png)

We want the shaded region to the left of $z_2=1.65$ and to the right of $z_1 = 0.52$

If we look up the areas in the standard normal z-table we find:

$$\text{left tail area for } z_2 =0.9505$$

$$\text{left tail area for } z_1 =0.6985$$

So the area between is:

$$\text{area between} =0.9505 - 0.6985 = 0.252$$

Rounded to the nearest percent this is 25%.

This means that the shaded area corresponds to 25% of the entire data.

$$\tag*{$\blacksquare$}$$

Another one

**Example 16.5 (Find area between $z_1=-1.53$ and $z_2=1.23$)**

Find the area between $z_{1}=-1.53$ and $z_{2}=1.23$.

**_Solution:_**

Here is the picture of the area we want.

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/standard-normal-areas_unnamed-chunk-94-1.png)

We want the shaded region to the left of $z_2=1.23$ and to the right of $z_1 = -1.53$

If we look up the areas in the standard normal z-table we find:

$$\text{left tail area for } z_2 =0.8907$$

$$\text{left tail area for } z_1 =0.063$$

So the area between is:

$$\text{area between} =0.8907 - 0.063 = 0.8277$$

Rounded to the nearest percent this is 83%.

This means that the shaded area corresponds to 83% of the entire data.

$$\tag*{$\blacksquare$}$$

## 16.4 Applications of Standard Normal Distributions

We will see later in the text that **_service level_** in retail corresponds to the chance that a retailer would experience a lost sale (out of stock situation) for some period of interest.

  * A service level of 90% means that lost sales would happen 10% of the time.
  * A service level of 95% means that lost sales would happen be 5% of the time.
  * A service level of 99% means that lost sales would happen be 1% of the time.



For demand that is distributed normally, the service level can be represented as a **left tail area**.

In addtion, the $z$-value that goes with a particular service level is called the **_service factor_**.

service level | left tail area  
---|---  
service factor | $z$-value for that left tail area  
  
  * If you know the service factor ($z$-value) you can find the service level (the left tail area). (this section)
  * If you know the service level (left tail area), you can find the service factor ($z$-value) (later in book)



**Example 16.6 (Service Level)**

Suppose that monthly demand in units for a retail product is given by a normal distribution. Find the service level for service factor of $z=1.28$.

**_Solution:_**

The service level can be found by finding the left tail area for the given service factor $z$-value.

We have $z = 1.28$.

Here is the picture of the area we want.

![](https://raw.githubusercontent.com/calvinw/intro-statistics-mcp/main/docs/standard-normal-areas_unnamed-chunk-114-1.png)

We want the shaded region to the left of $z=1.28$

If we look up the area in the standard normal z-table using $z=1.28$ we go to the row that has 1.2 and then to the column that contains .08 and we see this:

| .00| .01| .02| .03| .04| .05| .06| .07| .08| .09  
---|---|---|---|---|---|---|---|---|---|---  
1.1| .8643| .8665| .8686| .8708| .8729| .8749| .8770| .8790| .8810| .8830  
1.2| .8849| .8869| .8888| .8907| .8925| .8944| .8962| .8980| .8997| .9015  
1.3| .9032| .9049| .9066| .9082| .9099| .9115| .9131| .9147| .9162| .9177  
  
So that means:

$$\text{left tail area} =0.8997$$

Rounded to the nearest percent this is 90%. This means that the shaded area corresponds to 90% of the entire data.

This left tail area is the **service level**. A service level of $90\%$ means that there is just a $10\%$ chance of lost sales in given month.

$$\tag*{$\blacksquare$}$$
