# --- Day 1: Historian Hysteria ---

The <b>Chief Historian</b> is always present for the big Christmas sleigh launch, but nobody has seen him in months! Last anyone heard, he was visiting locations that are historically significant to the North Pole; a group of Senior Historians has asked you to accompany them as they check the places they think he was most likely to visit.

As each location is checked, they will mark it on their list with a <b>star</b>. They figure the Chief Historian <b>must</b> be in one of the first fifty places they'll look, so in order to save Christmas, you need to help them get <b>fifty stars</b> on their list before Santa takes off on December 25th.

Collect stars by solving puzzles.  Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first.  Each puzzle grants <b>one star</b>. Good luck!

You haven't even left yet and the group of Elvish Senior Historians has already hit a problem: their list of locations to check is currently <b>empty</b>. Eventually, someone decides that the best place to check first would be the Chief Historian's office.

Upon pouring into the office, everyone confirms that the Chief Historian is indeed nowhere to be found. Instead, the Elves discover an assortment of notes and lists of historically significant locations! This seems to be the planning the Chief Historian was doing before he left. Perhaps these notes can be used to determine which locations to search?

Throughout the Chief's office, the historically significant locations are listed not by name but by a unique number called the <b>location ID</b>. To make sure they don't miss anything, The Historians split into two groups, each searching the office and trying to create their own complete list of location IDs.

There's just one problem: by holding the two lists up <b>side by side</b> (your puzzle input), it quickly becomes clear that the lists aren't very similar. Maybe you can help The Historians reconcile their lists?

For example:
<pre>3   4
4   3
2   5
1   3
3   9
3   3
</pre>

Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are. Pair up the <b>smallest number in the left list</b> with the <b>smallest number in the right list</b>, then the <b>second-smallest left number</b> with the <b>second-smallest right number</b>, and so on.

Within each pair, figure out <b>how far apart</b> the two numbers are; you'll need to <b>add up all of those distances</b>. For example, if you pair up a <pre>3</pre> from the left list with a <pre>7</pre> from the right list, the distance apart is <pre>4</pre>; if you pair up a <pre>9</pre> with a <pre>3</pre>, the distance apart is <pre>6</pre>.

In the example list above, the pairs and distances would be as follows:
    - The smallest number in the left list is <pre>1</pre>, and the smallest number in the right list is <pre>3</pre>. The distance between them is <pre><b>2</b></pre>.
    - The second-smallest number in the left list is <pre>2</pre>, and the second-smallest number in the right list is another <pre>3</pre>. The distance between them is <pre><b>1</b></pre>.
    - The third-smallest number in both lists is <pre>3</pre>, so the distance between them is <pre><b>0</b></pre>.
    - The next numbers to pair up are <pre>3</pre> and <pre>4</pre>, a distance of <pre><b>1</b></pre>.
    - The fifth-smallest numbers in each list are <pre>3</pre> and <pre>5</pre>, a distance of <pre><b>2</b></pre>.
    - Finally, the largest number in the left list is <pre>4</pre>, while the largest number in the right list is <pre>9</pre>; these are a distance <pre><b>5</b></pre> apart.

To find the <b>total distance</b> between the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is <pre>2 + 1 + 0 + 1 + 2 + 5</pre>, a total distance of <pre><b>11</b></pre>!

Your actual left and right lists contain many location IDs. <b>What is the total distance between your lists?</b>
