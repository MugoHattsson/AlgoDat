module Makingfriends where 
import Data.List (sortBy)
import Data.Function (on)
import Data.Sequence hiding (sortBy)

main = do 
    line <- getLine
    contents <- getContents
    let [n,_] = map read $ words line :: [Int]
        parent = [0..(n)]
        edges = sortBy (compare `on` (!!2)) $ buildEdges (lines contents)
    --print parent
    print edges
    --putStrLn "Running Kruskal..."
    result <- kruskal 0 edges (fromList parent)
    print result


kruskal :: Int -> [Edge] -> Seq Int -> IO (Int)
kruskal i   []      parent   = do 
    --print i
    return (i)
kruskal i ([u,v,w]:es) parent 
    | parentU /= parentV = do 
        --print (1,[u,v,w],debug)
        kruskal (i+w) es (union)
    | otherwise = do 
        --print (2,[u,v,w],debug)
        kruskal i es parent
    where 
        debug = (parent, i)
        (parentU,parent') = find u parent
        (parentV,newParent) = find v parent'
        union   = update parentV parentU newParent


type Edge = [Int]

buildEdges :: [String] -> [Edge]
buildEdges [] = []
buildEdges (l:ls) = edge l : buildEdges ls
    where 
        edge l = map read $ words l

find :: Int -> Seq Int -> (Int, Seq Int)
find n parent 
    | index parent n == n = (n, parent)
    | otherwise = (index (snd nextParent) p, update n (fst nextParent) (snd nextParent))
    where
        p = index parent n
        (nextParent) = find p parent

-- find :: [Int] -> [Int] -> Seq Int -> ([Int], Seq Int)
-- find [] res parent = (res,parent)
-- find (n:ns) res parent
--     | p == n = find (ns) (n:res) parent
--     | otherwise = find (p:ns) res parent
--     where
--         p = index parent n