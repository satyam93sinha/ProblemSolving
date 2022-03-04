class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        rows = [poured]
        for row in range(query_row):
            glasses = [0 for _ in range(len(rows)+1)]
            for glass in range(len(rows)):
                pour = (rows[glass] - 1) / 2
                if pour > 0:
                    glasses[glass] += pour
                    glasses[glass+1] += pour
            rows = glasses.copy()
        return min(1, rows[query_glass])
    