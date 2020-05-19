module Test where
import Data.List
import Data.Ord

data ForestW a = ForestW [[a]] [(a, a, Int)]
    deriving (Show, Eq, Ord)

type Edge = (Int,Int,Int)

main = do
    line <- getLine
    contents <- getContents
    let [n,_] = map read $ words line :: [Int]
        edges = buildEdges (lines contents)

    print $ kruskal [1..n] edges

-- Sort the edges in ascending order of weight,
-- and initialise F to one list (of vertices) for each vertex:
kruskal vs es = kruskal' [[v] | v <- vs] [] (sortBy (comparing (\(_, _, w) -> w)) es)

-- When the edges are exhausted, we have our MST (or MSFs):
kruskal' _ acc [] = foldr (\(_,_,w) -> (+w)) 0 acc --ForestW forest acc

kruskal' forest   -- ^The initial forest F is one tree for each vertex of the graph
         acc      -- ^The minimum spanning forest
         (e : es) -- ^All the edges in the graph
         = kruskal' forest' acc' es
    where
        -- We always remove the minimum weight edge of the graph:
        edge @ (a, b, w) = e

        -- Expand the MST if the minimum weight edge connects two forests:
        acc' = if forest == forest' then acc else e:acc

        -- Rearrange the forest:
        --  Find the trees containing the vertices of `edge`,
        --  If they're disjoint, concatenate them:
        forest' = if fa /= fb then fab : ((forest \\ fa) \\ fb) else forest

        -- Note that fa and fb are guaranteed to contain a single element:
        fa = filter (\x -> a `elem` x) forest
        fb = filter (\x -> b `elem` x) forest
        fab = nub $ concat (fa ++ fb)

buildEdges :: [String] -> [Edge]
buildEdges [] = []
buildEdges (l:ls) = (formatTuple $ edge l) : buildEdges ls
    where 
        edge l = map read $ words l
        formatTuple [u,v,w] = (u,v,w)