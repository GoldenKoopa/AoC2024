# --- Part Two ---

Your analysis only confirmed what everyone feared: the two lists of location IDs are indeed very different.

Or are they?

The Historians can't agree on which group made the mistakes <b>or</b> how to read most of the Chief's handwriting, but in the commotion you notice an interesting detail: a lot[^1] of location IDs appear in both lists! Maybe the other numbers aren't location IDs at all but rather misinterpreted handwriting.

This time, you'll need to figure out exactly how often each number from the left list appears in the right list. Calculate a total <b>similarity score</b> by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

Here are the same example lists again:
<pre>3   4
4   3
2   5
1   3
3   9
3   3
</pre>

For these example lists, here is the process of finding the similarity score:
    - The first number in the left list is <pre>3</pre>. It appears in the right list three times, so the similarity score increases by <pre>3 * 3 = <b>9</b></pre>.
    - The second number in the left list is <pre>4</pre>. It appears in the right list once, so the similarity score increases by <pre>4 * 1 = <b>4</b></pre>.
    - The third number in the left list is <pre>2</pre>. It does not appear in the right list, so the similarity score does not increase (<pre>2 * 0 = 0</pre>).
    - The fourth number, <pre>1</pre>, also does not appear in the right list.
    - The fifth number, <pre>3</pre>, appears in the right list three times; the similarity score increases by <pre><b>9</b></pre>.
    - The last number, <pre>3</pre>, appears in the right list three times; the similarity score again increases by <pre><b>9</b></pre>.

So, for these example lists, the similarity score at the end of this process is <pre><b>31</b></pre> (<pre>9 + 4 + 0 + 0 + 9 + 9</pre>).

Once again consider your left and right lists. <b>What is their similarity score?</b>

[^1]: [a lot] We were THIS close to summoning the Alot of Location IDs!
