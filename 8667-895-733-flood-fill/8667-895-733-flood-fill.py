class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initial_color = image[sr][sc]
        
        row = len(image)
        col = len(image[0])

        def dfs(r, c):
            if 0 <= r < row and 0 <= c < col and image[r][c] == initial_color and image[r][c] != color:
                image[r][c] = color

                dfs(r-1, c)
                dfs(r+1, c)
                dfs(r, c-1)
                dfs(r, c+1) 
        
        dfs(sr, sc)
        return image

            
                