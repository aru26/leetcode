class Solution {
    public int[] prisonAfterNDays(int[] cells, int N) {
        Map<String, Integer> seen = new HashMap<>();
        while (N > 0) {
            int[] cells2 = new int[8];
            seen.put(Arrays.toString(cells), N);
            N--;
            for (int i = 1; i <= 6; i++) {
                if (cells[i - 1] == cells[i + 1]) {
                    cells2[i] = 1;
                }
            }
            cells = cells2;
            if (seen.containsKey(Arrays.toString(cells))) {
                N = N % (seen.get(Arrays.toString(cells)) - N);
            }
        }
        
        return cells;
    }
}
