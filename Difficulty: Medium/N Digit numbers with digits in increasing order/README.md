<h2><a href="https://www.geeksforgeeks.org/problems/n-digit-numbers-with-digits-in-increasing-order5903/1">N Digit numbers with digits in increasing order</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an integer <strong>n</strong>, print all the <strong>n</strong> digit numbers in increasing order, such that their digits are in strictly increasing order(from left to right).</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>n = 1</span>
<span style="font-size: 18px;"><strong>Output:
</strong>0 1 2 3 4 5 6 7 8 9</span>
<span style="font-size: 18px;"><strong>Explanation:
</strong>Single digit numbers are considered to be 
strictly increasing order.
</span></pre>
<p><strong><span style="font-size: 18px;">Example 2:</span></strong></p>
<pre><strong><span style="font-size: 18px;">Input:
</span></strong><span style="font-size: 18px;">n = 2</span>
<strong><span style="font-size: 18px;">Output:
</span></strong><span style="font-size: 18px;">12 13 14 15 16 17 18 19 23....79 89</span>
<strong><span style="font-size: 18px;">Explanation:
</span></strong><span style="font-size: 18px;">For n = 2, the correct sequence is
12 13 14 15 16 17 18 19 23 and so on 
up to 89.</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:&nbsp;&nbsp;</strong><br>You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>increasingNumbers</strong>() which takes an integer n as an input parameter and returns the list of numbers such that their digits are in strictly increasing order.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(9<sup>n</sup>)<br><strong>Expected Auxiliary Space:</strong> O(n)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= n &lt;= 9</span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>ABCO</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Recursion</code>&nbsp;<code>Algorithms</code>&nbsp;