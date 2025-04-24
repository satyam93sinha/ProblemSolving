<h2><a href="https://www.geeksforgeeks.org/problems/permutation-with-spaces3627/1">Permutation with Spaces</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given a string <strong>s</strong>, you need to print <strong>all possible strings</strong> that can be made by placing spaces (zero or one) in between them. The output should be printed in <strong>sorted</strong> <strong>increasing</strong> order of strings.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input</strong>:
s = "ABC"
<strong>Output: </strong>(A B C)(A BC)(AB C)(ABC)
<strong>Explanation</strong>:
ABC
AB C
A BC
A B C
These are the possible combination of "ABC".</span></pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong>
s = "BBR"
<strong>Output: </strong>(B B R)(B BR)(BB R)(BBR)
</span></pre>
<p><br><span style="font-size: 18px;"><strong>Your Task:&nbsp;&nbsp;</strong><br>You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>permutation()</strong> which takes the string <strong>s</strong> as input parameters and returns the <strong>sorted array&nbsp;</strong>of the string denoting the different permutations <strong>(DON'T ADD '(' and ')' it will be handled by the driver code only)</strong>.<br><br><strong>Expected Time Complexity:</strong> O(2<sup>s</sup>)<br><strong>Expected Auxiliary Space:</strong> O(1)</span></p>
<p>&nbsp;</p>
<p><span style="font-size: 18px;"><strong>CONSTRAINTS:</strong><br>1 &lt;= |s| &lt; 10<br>s only contains <strong>lowercase and Uppercase English</strong> letters.</span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Recursion</code>&nbsp;<code>Backtracking</code>&nbsp;<code>Algorithms</code>&nbsp;