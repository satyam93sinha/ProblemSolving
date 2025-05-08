<h2><a href="https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1">Longest Substring with K Uniques</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given a string <strong>s</strong>, you need to print the size of the longest possible substring&nbsp;<span style="box-sizing: border-box; margin: 0px; padding: 0px;">with exactly<strong>&nbsp;k unique</strong> characters. If no possible substring exists,</span>&nbsp;print -1.</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>s = "aabacbebebe</span><span style="font-size: 18px;">", k = 3
<strong>Output:</strong> 7
<strong>Explanation</strong>: "cbebebe" is the longest substring with 3 distinct characters.
</span></pre>
<pre><span style="font-size: 18px;"><strong>Input</strong>: s = "aaaa", k = 2
<strong>Output:</strong> -1
<strong>Explanation</strong>: There's no substring with 2 distinct characters.<br></span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>s = "aabaaab", k = 2
<strong>Output:</strong> 7
<strong>Explanation</strong>: </span><span style="font-size: 14pt;">"aabaaab" is the longest substring with 2 distinct characters.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ s.size() ≤ 10<sup>5</sup><br>1 ≤ k ≤ 26<br>All characters are lowercase letters</span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<code>Google</code>&nbsp;<code>SAP Labs</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>two-pointer-algorithm</code>&nbsp;<code>Hash</code>&nbsp;<code>Strings</code>&nbsp;<code>Map</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;