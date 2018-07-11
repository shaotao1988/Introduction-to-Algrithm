A common pattern in finding optimal substructure:
- You show that a solution to the problem consists of making a choice, such as choosing an initial cut in a rod. Making such choice leaves one or more sub-problems to be solved.(为了得到解决方案，需要作出选择，作出这一选择会产生一个或多个子问题)
- You suppose that for a given problem, you are given the choice that leads to an optimal solution. You don't concern yourself yet with how to determain this choice. You just assume that it has been given to you.（假设已经得到了最优解，暂时不必关心是如何得到的）
- Given the choice, you determine which subproblem ensue and how to best characterize the resulting space of subproblems.（在这种情况下，对子问题空间进行分析，哪一个或哪一些子问题发生，会导致得到这个最优解？）
- You show that the solution to the subproblems used within an optimal solution must themselves be optimal by using "cut and paste" technique.(证明这些子问题的解也必须是最优的，否则无法组合得到最优的父问题的解。方法是将一个子问题的非最优解替换到原问题中，从而获得比原问题的最优解更优的解，得到矛盾)

EG：
**1. Rod cutting problem**
*a.* 需要作出选择，在第i米长的位置是否需要切？作出这个选择后得到2个子问题：i米和(n-i)米的2段钢筋
*b.* 假设已经有了最优的切法
*c.* 切除的最后一段钢筋的长度为i，划分出子问题n-i
*d.* 剩下的n-i米长的钢筋切法也必须是最优的。假设n-i米的最优解为max_r，我们找到某个非最优解max_r-1，和i组合后得到原问题的最优解，由于(max_r-1)+r(i)小于max_r+r(i)，和最优解矛盾，所以n-i米长钢筋的解法必须是最优解
步骤c中i的长度未知，所以需要遍历

**2. 最长公共子序列问题**
X=(x~1~,x~2~,...,x~m~)和Y=(y~1~,y~2~,...,y~n~)为序列，令Z=(z~1~,z~2~,...,z~k~)为X和Y的最长公共子序列，那么：
(1) 如果x~m~=y~n~，那么z~k~=x~m~=y~n~，并且Z~(k-1)~为X~(m-1)~和Y~(n-1)~的最长公共子序列
(2) 如果x~m~!=y~n~，且z~k~!=x~m~，那么Z也是X~(m-1)~和Y的最长公共子序列
(3) 如果x~m~!=y~n~，且z~k~!=y~n~，那么Z也是X和Y~(n-1)~的最长公共子序列

**3. 最长公共子串问题**
X=(x~1~,x~2~,...,x~m~)和Y=(y~1~,y~2~,...,y~n~)为序列，令L[i,j]为以x~i~和y~j~结尾的最长公共子串，那么：
当x~i~!=y~j~时，L[i,j] = 0
当x~i~=y~j~时，L[i,j] = L[i-1, j-1]+1

### 能用动态规划求解的问题有如下2个性质
- 最优子结构
问题的最优解由其子问题的最优解组合而成
动态规划算法利用最优子结构性质，以自底向上的方式从子问题的最优解逐步构造出整个问题的最优解
- 重叠子问题
在用递归算法自顶向下求解问题时，每次产生的子问题并不总是新的子问题，有些子问题被反复计算多次。动态规划正是利用子问题的重复性质，对每个子问题只求解一次，后面再求解这个子问题时只是简单查表。

动态规划的解题过程往往是一个填表的过程，十分类似数学归纳法：
1.找边界（初始状态）
2.找状态递推式，将问题分解为子问题，最终通过初始状态推导出问题的解

**什么是状态？**
状态就是问题的最优解
如钢筋切分后获得的最大利润
**怎么寻找状态？**
根据子问题来描述状态
将钢筋切走i米长后，需要求解剩下的(n-i)米长的最优解法
因此，定义R(n)为长度为n的钢筋可以获得的最大利润
**什么是状态转移方程？**
将问题划分成子问题的划分方法
R(n)=max{P~i~+R(n-i)|i=1->n}
对于每个n，需要求解所有的n-1种子状态
有时候由于问题条件的限制，某些子状态没有意义，就不需要求解所有子状态了

求X最长单调非降序列，要求时间复杂度O(n^2^)
状态：L(i)为以x~i~结尾的最长单调非降序列
L(0)=1
L(1) = x~0~<=x~1~?(L(0)+1):1
L(2) = max[(x~0~<x~2~?(L(0)+1):1),(x~1~<x~2~?(L(0)+1):1)]
状态转移方程：
L(i) = max[x~j~<x~i~?:L(j)+1:1], j=0...i-1
